from clients.github import GitHubClient


class Executor:
    def __init__(self, github_client: GitHubClient):
        self.github_client = github_client

    def execute(self, query_parameters):
        # retrieve and aggregate github pages
        projects = self.github_client.query(
            query_parameters["language"],
            int(query_parameters["project_count"])
        )
        print(len(projects))
        # filter pages by criteria

        # print out results
        pass
