from bus_factor.models.contributor import Contributor


class Project:
    def __init__(self, name, owner, contributor_url):
        self.name = name
        self.owner = owner
        self.contributor_url = contributor_url

    def high_bus_factor(self, contributors):
        top_contribution = sum([contributor.contribution for contributor in contributors[1:25]])
        if contributors[0].contribution >= 3 * top_contribution:
            return contributors[0]
        else:
            return None

    def add_contributors(self, contributors):
        self.contributors = contributors