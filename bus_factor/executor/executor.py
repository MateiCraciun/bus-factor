from clients.github import GitHubClient

from models.project import Project

class Executor:
    def __init__(self, github_client: GitHubClient):
        self.github_client = github_client

    def execute(self, query_parameters):
        # retrieve and aggregate github pages
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
        
        contributors = self.github_client.get_contributors(
            projects
        )
        # filter pages by criteria

        # print out results
        pass
