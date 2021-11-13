import asyncio

from clients.github import GitHubClient
from models.project import Project

class Executor:
    def __init__(self, github_client: GitHubClient):
        self.event_loop = asyncio.get_event_loop()
        self.github_client = github_client

    def execute(self, query_parameters):
        # retrieve and aggregate github projects
        projects = [Project(
                project["name"],
                project["owner"]["login"],
                project["contributors_url"]
            ) 
            for project in self.github_client.get_projects(
                query_parameters["language"],
                int(query_parameters["project_count"])
            )
        ]

        contributor_queries = asyncio.gather(*[self.get_contributors(
            project
        ) for project in projects])
        results = self.event_loop.run_until_complete(contributor_queries)
        # filter projects by criteria

        # print out results
        pass

    async def get_contributors(self, project: Project):
        contributors = await self.github_client.get_contributors(project.contributor_url)
        project.add_contributors(contributors)
        return project
