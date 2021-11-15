from bus_factor.models.contributor import Contributor


class Project:
    def __init__(self, name, owner, contributor_url):
        self.name = name
        self.owner = owner
        self.contributor_url = contributor_url

    def high_bus_factor(self):
        max_contributors = len(self.contributors) if len(self.contributors) < 25 else 25

        top_contribution = self.contributors[0].contributions
        other_contribution = sum([contributor.contributions for contributor in self.contributors[1:max_contributors]])
        contribution_percentage = top_contribution / (top_contribution + other_contribution)
        if contribution_percentage >= 0.75:
            return contribution_percentage
        else:
            return None

    def add_contributors(self, contributors):
        with open("contributors.txt", "a+") as f:
            f.write(self.contributor_url + ": " + str(contributors) + ",\n")
        self.contributors = [Contributor(
            contributor["login"],
            int(contributor["contributions"])
        ) if "login" in contributor else Contributor(
            "anonymous",
            int(contributor["contributions"])
        ) 
            for contributor in contributors 
        ]