import json

class stop_area:
    def __init__(self, name, stop_id):
        self.name = name
        self.stop_id = stop_id

class route:
    def __init__(self, route_id, nodes):
        self.route_id = route_id
        self.nodes = nodes

def get_list_classes_routes(path):
    with open(path) as json_file:
        json_data = json.load(json_file)

    stops = []
    routes = []
    for line in json_data:
        stops = []
        for stop in json_data[str(line)]:
            new_stop = stop_area(stop["label"], stop["id"])
            stops.append(new_stop)
        routes.append(route(str(line), stops.copy()))
    return (routes)

def get_single_class(path):
    with open(path) as json_file:
        json_data = json.load(json_file)

    for stop in json_data:
        new_stop = stop_area(stop["label"], stop["id"])
    return (new_stop)

#print(get_list_classes_routes("./tmp_semi_parsed_stop_points.json"));
#print(get_list_classes_routes("./tmp_semi_parsed_stop_points.json")[0].nodes[0].name);
#print(get_single_class("./tmp_start.json").stop_id);
