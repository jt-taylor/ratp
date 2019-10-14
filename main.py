# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    routing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smaddox <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 11:23:03 by smaddox           #+#    #+#              #
#    Updated: 2019/10/13 16:42:30 by smaddox          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from data_structures import *
#import path_finder
from parsing import *

class app():
    def __init__(self):
        self.parse = parser()
#        self.pathfinder = path_finder.path_finder()

        self.routes = self.parse.get_routes("./tmp_semi_parsed_stop_points.json")
        self.startpoint = self.parse.get_startpoint("./tmp_final.json")
        self.endpoint = self.parse.get_endpoint("./tmp_start.json")

        print (self.startpoint.name)
        print (self.endpoint.stop_id)

#        self.pathfinder.solve(self.routes, self.startpoint, self.endpoint)
#        self.pathfinder.print_solution()

def main():
    new_application = app()

if __name__ == "__main__":
    main()