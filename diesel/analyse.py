class BaseAnalyzer:
    def analyze(self, points):
        pass

    def learn(self, data):
        pass


class NaiveAnalyzer(BaseAnalyzer):
    tolerances_min = {
        "x": [350, 350, 386, 421, 457, 493, 528, 564, 600, 636, 671, 707, 743, 778, 814, 850],
        "y": [0, 60, 100, 180, 262, 407, 527, 660, 790, 945, 1095, 1250, 1405, 1560, 1707, 1850],
    }

    tolerances_max = {
        "x": [350, 350, 386, 421, 457, 493, 528, 564, 600, 636, 671, 707, 743, 778, 814, 850],
        "y": [0, 70, 120, 198, 300, 445, 575, 720, 860, 1038, 1190, 1370, 1524, 1682, 1791, 1880],
    }

    def analyze(self, points):
        pass


class SuperAnalyzer(BaseAnalyzer):
    def learn(self, data):
        # here we go
        pass


def get_analyzer(methods):
    result = []
    for method in methods:
        if method == "naive":
            result.append(("naive", NaiveAnalyzer))
        if method == "super":
            result.append(("super", SuperAnalyzer))
    return result
