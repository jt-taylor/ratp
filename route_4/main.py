# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    routing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smaddox <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 11:23:03 by smaddox           #+#    #+#              #
#    Updated: 2019/10/13 22:12:19 by smaddox          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from data_structures import *
from path_finder import *
from parsing import *
import os
import sys

class app():
    def __init__(self):
        self.parse = parser()
        self.pathfinder = path_finder()
        self.routes = self.parse.get_routes("./tmp_semi_parsed_stop_points.json")
        self.startpoint = self.parse.get_startpoint("./tmp_final.json")
        self.endpoint = self.parse.get_endpoint("./tmp_start.json")
        self.pathfinder.solve(self.routes, self.startpoint, self.endpoint)

def main(argv):
    querie = "php run_me.php " + "'"+argv[1] + "' '" + argv[2]+ "'"
    output = os.system(querie + " 1>/dev/null")
    new_application = app()
    

if __name__ == "__main__":
    main(sys.argv)
