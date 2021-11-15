class TestClient:
    def load_results(self, results):
        self.results = results

    async def get_projects(self, language, project_count):
        for project in self.results["projects"]:
            yield project

    async def get_contributors(self, contributor_url):
        return self.results["contributors"][contributor_url]