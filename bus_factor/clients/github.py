import requests
import asyncio
from urllib.parse import urljoin

from models.project import Project

class GitHubClient:
    BASE_URL = "https://api.github.com"
    PER_PAGE = 100
    CONTRIBUTOR_LIMIT = 25

    GET_PROJECTS_ENDPOINT = "/search/repositories"

    def __init__(self, github_key):
        self.github_key = github_key

    def format_project_params(self, params, page):
        params["page"] = page
        return params
    
    async def get_projects(self, language, project_count):
        pages = project_count // self.PER_PAGE + (1 if project_count % self.PER_PAGE != 0 else 0)
        params = {
            "q": "language:{}".format(language),
            "sort": "stars",
            "per_page": self.PER_PAGE,
        }

        
        for page in range(pages):
            partial = await self._make_call(
                self.GET_PROJECTS_ENDPOINT, 
                self.format_project_params(params.copy(), page)
            )
            for project in partial["items"]:
                yield project

    async def get_contributors(self, contributor_url: Project):
        params = {
            "per_page" : self.CONTRIBUTOR_LIMIT,
            "anon": "true"
        }

        return await self._make_call(contributor_url, params)

    async def _make_call(self, endpoint, params):
        r = requests.get(
            urljoin(self.BASE_URL, endpoint), 
            headers={
                "Authorization": "token {}".format(self.github_key),
                "Accept": "application/vnd.github.v3+json"
            },
            params=params
        )
        return r.json()
