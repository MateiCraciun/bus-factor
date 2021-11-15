from bus_factor.models.project import Project

class Formatter:
    def format(self, project: Project, top_contribution):
        print("project: {project} \t\t user: {user} \t\t percentage: {percentage:.2f}".format(
            project=project.name.ljust(30),
            user=project.contributors[0].username.ljust(30),
            percentage=top_contribution
        ))