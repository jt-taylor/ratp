# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    routing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smaddox <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 11:23:03 by smaddox           #+#    #+#              #
#    Updated: 2019/10/13 14:37:03 by smaddox          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# list of routes
#   -> where each element of the list is a route object with:
#       -> route_id
#       -> list of stop_area objects
# list of stop_areas
#   -> where each element of the list is a stop_area object with:
#       -> a name
#       -> an id
#       -> a physical_mode (use if api queries didn't filter by physical_mode)
#
# ignore time_table for now 


# parsing template
# I haven't look at the json but this should be very close to the right idea
import json

def parsing():
    all_routes = []
    with open("./tmp_semi_parsed_stop_points.json") as json_file:
        json_data = json.load(json_file)
    for temp_route in json_data['route']:
        all_stops = []
        for stop in temp_route['stops']:
            stop_obj = stop_area(stop['name'], stop['id'], stop['physical_mode'])
            all_stops.append(stop_obj)
        route_obj = route(temp_route['id'], all_stops)
        all_routes.append(route_obj)
    return(all_routes)

class stop_area:
    def __init__(self, name, stop_id, physical_mode):
        self.name = name
        self.stop_id = stop_id
        self.physical_mode = physical_mode 

    def __eq__(self, other):
        return self.name == other.name and \
                self.stop_id == other.stop_id and \
                self.physical_mode == other.physical_mode

    def __hash__(self):
        return (hash((self.name, self.stop_id, self.physical_mode)))

    def update_time_table(self, time_table):
        self.time_table = time_table

class route:
    def __init__(self, route_id, nodes):
        self.route_id = route_id
        self.nodes = nodes

    def get_index(self, stop_area):
        try:
            index = self.nodes.index(stop_area)
            return(index)
        except:
            return(False)

class path_finder:
    def __init__(self, Ps, Pt, all_routes):
        self.path_profiles = [ ]


class app():
    def __init__(self):
        pass
        # do nothing for now
        # parse json that has start point info (Ps for Point source)
        #   -> self.Ps = get_startpoint()       
        # parse json that has end point info (Pt for point target)
        #   -> self.Pt = get_endpoint()
        # parse for all the available roots
        #   -> self.routes = get_routes()
        # find path / consecutive stop areas from source point to target point
        #   -> pathfinder = path_finder(self.Ps, self.Pt, self.routes)
        #   -> pathfinder.print_solution()

def main():
    new_application = app()

if __name__ == "__main__":
    main()
main()
