import asyncio

from clients.github import GitHubClient
from models.project import Project

class Executor:
    def __init__(self, github_client: GitHubClient):
        self.event_loop = asyncio.get_event_loop()
        self.github_client = github_client

    def execute(self, query_parameters):
        self.event_loop.run_until_complete(self._execute(query_parameters))

    async def _execute(self, query_parameters):
        # retrieve and aggregate github projects
        projects = [Project(
                project["name"],
                project["owner"]["login"],
                project["contributors_url"]
            ) 
            async for project in self.github_client.get_projects(
                query_parameters["language"],
                int(query_parameters["project_count"])
            )
        ]

        for project in projects:
            project = await self.get_contributors(project)
            top_contribution = project.high_bus_factor()
            if top_contribution:
                print("project: {project} \t user: {user} \t percentage: {percentage}".format(
                    project=project.name,
                    user=project.contributors[0].username,
                    percentage=top_contribution
                ))
        pass

    async def get_contributors(self, project: Project):
        contributors = await self.github_client.get_contributors(project.contributor_url)
        project.add_contributors(contributors)
        return project
