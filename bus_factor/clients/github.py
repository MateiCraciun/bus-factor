import requests
import asyncio
from urllib.parse import urljoin

class GitHubClient:
    BASE_URL = "https://api.github.com"
    PER_PAGE = 100

    def __init__(self, github_key):
        self.event_loop = asyncio.get_event_loop()
        self.github_key = github_key

    def format_params(self, params, page):
        params["page"] = page
        return params
    
    def query(self, language, project_count):
        pages = project_count // self.PER_PAGE + (1 if project_count % self.PER_PAGE != 0 else 0)
        params = {
            "q": "language:{}".format(language),
            "sort": "stars",
            "per_page": self.PER_PAGE,
        }

        queries = asyncio.gather(*[self._query_page(self.format_params(params.copy(), page)) for page in range(pages)])
        results = self.event_loop.run_until_complete(queries)

        print(results)
        print(len(results[0]["items"]))
        print(results[0]["items"][0])

    async def _query_page(self, params):
        r = requests.get(
            urljoin(self.BASE_URL, "/search/repositories"), 
            headers={
                "Authorization": "access_token {}".format(self.github_key),
                "Accept": "application/vnd.github.v3+json"
            },
            params=params
        )
        return r.json()
