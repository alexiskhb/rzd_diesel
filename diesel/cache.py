from django.db import connection
from .analyse import get_analyzer, BaseAnalyzer
from typing import List


class DataGetter:
    def __init__(self):
        print("Loading database...", flush=True)

        with connection.cursor() as cursor:
            cursor.execute("""select * from dbloko.full_sql_locodataseconds limit 10000""")
            self.locodataseconds_data = list(cursor.fetchall())

        with connection.cursor() as cursor:
            cursor.execute("""select * from dbloko.full_sql_loco limit 10000""")
            self.loco_data = list(cursor.fetchall())

        self.num2id = {}
        for i, dt in enumerate(self.locodataseconds_data):
            self.num2id[dt[0]] = dt[0]

        with connection.cursor() as cursor:
            cursor.execute("""select * from dbloko.full_sql_locotype limit 10000""")
            self.locotype_data = list(cursor.fetchall())

        print("Cache initialized", flush=True)

    def get(self, request):
        # train: 1,
        # from_time: 10000000,
        # to_time: 100000000,
        response = {
            "points": [],  # list of dicts {x: x, y: y, p: p, id: id}
        }
        for i, dt in enumerate(self.locodataseconds_data):
            # dt[1] === timestamp
            # print(dt, request, flush=True)
            if request["from_time"] <= dt[1] <= request["to_time"] and dt[16] == request["train"]:
                response["points"].append({
                    "x": dt[3],  # rpm_diesel
                    "y": dt[5],  # power_generator
                    "p": dt[13],  # poz_kont_sec
                    "id": dt[16],  # loco_id
                })

        # dict {method: [(state, id)]}
        response["section_state"] = self.get_stats(request, response["points"])
        return response

    def get_stats(self, request, points):
        analyzers: List[BaseAnalyzer] = get_analyzer(request.get("method", ["naive"]))
        section_state = {}
        for method, A in analyzers:
            analyzer: BaseAnalyzer = A()
            section_state[method] = analyzer.analyze(points)
        return section_state


DG = DataGetter()
