# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    routing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smaddox <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 11:23:03 by smaddox           #+#    #+#              #
#    Updated: 2019/10/13 12:47:05 by smaddox          ###   ########.fr        #
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

class stop_area:
    def __init__(self, name, stop_id, physical_mode):
        self.name = name
        self.stop_id = stop_id
        self.physical_mode = physical_mode 
    def update_time_table(self, time_table):
        self.time_table = time_table

class route:
    def __init__(self, route_id, nodes):
        self.route_id = route_id
        self.nodes = nodes
