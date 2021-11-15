from bus_factor.models.project import Project

class TestFormatter:
    def __init__(self):
        self.got = dict()

    def format(self, project: Project, top_contribution):
        self.got[self._result_to_string(
            project.name,
            project.contributors[0].username,
            top_contribution
        )] = True

    def load_expected(self, expected):
        self.expected = dict()
        for expected_result in expected:
            self.expected[self._result_to_string(
                expected_result["name"],
                expected_result["user"],
                expected_result["contribution"],
            )] = True

    def _result_to_string(self, project_name, user_name, contribution):
        return ".".join([project_name, user_name, str(contribution)])
    
    def evaluate(self):
        for expected in self.expected:
            assert expected in self.got

        for got in self.got:
            assert got in self.expected