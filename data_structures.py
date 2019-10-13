# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_structures.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: smaddox <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/13 15:22:23 by smaddox           #+#    #+#              #
#    Updated: 2019/10/13 16:01:53 by smaddox          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class stop_area:
    def __init__(self,name,stop_id):
        self.name=name
        self.stop_id=stop_id

    def __eq__(self,other):
        return self.name==other.name and \
        self.stop_id == other.stop_id and \
        self.physical_mode == other.physical_mode

    def __hash__(self):
        return(hash((self.name,self.stop_id,self.physical_mode)))

    def update_time_table(self,time_table):
        self.time_table = time_table

class route:
    def __init__(self,route_id,nodes):
        self.route_id=route_id
        self.nodes=nodes

    def get_index(self,stop_area):
        try:
            index=self.nodes.index(stop_area)
            return(index)
        except:
            return(False)
