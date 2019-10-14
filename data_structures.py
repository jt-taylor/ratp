# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_structures.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smaddox <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 15:22:23 by smaddox           #+#    #+#              #
#    Updated: 2019/10/13 18:09:11 by smaddox          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class stop_area:
    def __init__(self,name,stop_id):
        self.name=name
        self.stop_id=stop_id

    def __eq__(self,other):
        return self.name==other.name and \
        self.stop_id == other.stop_id

    def __hash__(self):
        return(hash((self.name,self.stop_id)))

    def update_time_table(self,time_table):
        self.time_table = time_table

class route:
    def __init__(self,route_id,nodes):
        self.route_id=route_id
        self.nodes=nodes

    def get_index(self,stop_area):
        for node in self.nodes:
            if (node.name == stop_area.name):
                return (self.nodes.index(node))
        return(False)
