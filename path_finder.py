# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    path_finder.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smaddox <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 17:25:37 by smaddox           #+#    #+#              #
#    Updated: 2019/10/13 21:28:23 by smaddox          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from data_structures import *
import math

class path_finder:

    def __init__(self):
        self.pathprofile = [ ]
        self.connections = [ ] 

    def solve(self, routes, startpoint, endpoint):
        self.connections.append(startpoint)
        start_route = self.get_route(routes, startpoint)
        end_route = self.get_route(routes, endpoint)
        stop1 = self.four_connection(routes[3], start_route, startpoint)
        stop2 = self.four_connection(routes[3], end_route, endpoint)
        self.get_path(start_route, startpoint, stop1)
        self.get_path(routes[3], stop1, stop2)
        self.get_path(end_route, stop2, endpoint)
        self.connections.append(endpoint)
        self.print_connections()
          
          
    def print_connections(self):
        self.connections.reverse()
        for connection in self.connections:
            print(connection.name)
        print("net trip length: ~" +  str(math.trunc((len(self.connections) * 110/60))) + " minutes")

    def get_path(self, route, start, end):
        for i in range(route.get_index(start), route.get_index(end)):
            self.connections.append(route.nodes[i])

    def get_route(self, routes, point):
        for route in routes:
            index = route.get_index(point)
            if (index):
                return(route)

    def four_connection(self, the_way,  route, point):
        for node in route.nodes:
            index = the_way.get_index(node)
            if (index):
                return(the_way.nodes[index])
