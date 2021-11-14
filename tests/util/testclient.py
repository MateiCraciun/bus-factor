class TestClient:
    def load_results(self, results):
        self.results = results

    async def get_projects(self, language, project_count):
        return self.results["projects"][language][project_count]

    async def get_contributors(self, contributor_url):
        return self.results["contributors"][contributor_url]