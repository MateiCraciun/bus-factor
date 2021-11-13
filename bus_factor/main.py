import sys
import os
from argparse import ArgumentParser

from clients.github import GitHubClient
from executor.executor import Executor

ENV_VAR_GITHUB_KEY = "GITHUB_KEY"

def main():
    if ENV_VAR_GITHUB_KEY not in os.environ:
        print("Please define {} environment variable to initialize github access.".format(ENV_VAR_GITHUB_KEY))
        return -1
    github_key = os.environ[ENV_VAR_GITHUB_KEY]

    parser = ArgumentParser()
    parser.add_argument("--language", dest="language", help="programming language used in projects to query")
    parser.add_argument("--project_count", dest="project_count", help="number of projects to retrieve")

    query_parameters = vars(parser.parse_args())

    github_client = GitHubClient(github_key)

    executor = Executor(github_client)
    executor.execute(query_parameters)

if __name__ == "__main__":
    sys.exit(main())