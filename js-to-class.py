import json

class stop_area:
    def __init__(self, name, stop_id):
        self.name = name
        self.stop_id = stop_id
       # self.physical_mode = physical_mode
    #def update_time_table(self, time_table):
    #   self.time_table = time_table

class route:
    def __init__(self, route_id, nodes):
        self.route_id = route_id
        self.nodes = nodes

with open("./tmp_semi_parsed_stop_points.json") as json_file:
    json_data = json.load(json_file)
print("List of all routes")

stops = []
routes = []
for line in json_data:
    stops = []
    for stop in json_data[str(line)]:
        new_stop = stop_area(stop["label"], stop["id"])
        stops.append(new_stop)
    routes.append(route(str(line), stops.copy()))

#print(routes);
#print(routes[0].nodes[0].name);
