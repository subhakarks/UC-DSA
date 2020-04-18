#!/usr/bin/env python3


import math


class Node:
    def __init__(self, nid, parent=None):
        self.f_val = 0
        self.g_val = 0
        self.h_val = 0
        self.nid = nid
        self.parent = parent


class MapSpace:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = dict((idx, conns) for idx, conns in enumerate(edges))

    def get_astar_path(self, src, dst):
        # few validations on the inputs
        if src not in self.nodes:
            raise Exception('A-STAR: Invalid source')
        if dst not in self.nodes:
            raise Exception('A-STAR: Invalid destination')
        if not len(self.edges.get(src, [])):
            raise Exception('A-STAR: Isolated source cannot be reached')
        if not len(self.edges.get(dst, [])):
            raise Exception('A-STAR: Isolated destination cannot be reached')

        explored = set()
        frontiers = list()
        frontiers.append(Node(nid=src))
        while len(frontiers) > 0:
            current_index = 0
            current_node = frontiers[current_index]
            for idx, node in enumerate(frontiers):
                # check if there are any other better nodes towards destination
                if node.f_val < current_node.f_val:
                    current_node = node
                    current_index = idx
            # found a node, which we want to explore, so adjust frontiers and explored.
            # we just need to keep track of intersection-ids
            frontiers.pop(current_index)
            explored.add(current_node.nid)
            if dst == current_node.nid:
                return self._return_astar_path(current_node)

            # reached a best possible intermediate node towards destination.
            # explore all possible next moves from current node by reaching out
            # connected nodes of current node.
            for node_id in self.edges.get(current_node.nid, []):
                # ignore if node is aready explored.
                if node_id in explored:
                    continue

                # before actually considering this node, first check if this node can be
                # reached with shorter distance.
                # for that, first get g_val for this node from current node.
                g_val = current_node.g_val + self._get_cost_between_nodes(current_node.nid, node_id)
                # now, check if this node is already in frontiers with better cost
                can_reach_better = False
                for existing_node in frontiers:
                    if existing_node.nid == node_id:
                        if existing_node.g_val < g_val:
                            can_reach_better = True
                if can_reach_better:
                    continue

                # cannot reach this node in better way, so add it as possible node towards dest
                next_node = Node(nid=node_id, parent=current_node)
                # g_val is absolute value
                next_node.g_val = g_val
                # h_val is heuristic value
                next_node.h_val = self._get_cost_between_nodes(next_node.nid, dst)
                next_node.f_val = next_node.g_val + next_node.h_val
                frontiers.append(next_node)
        return []

    def _return_astar_path(self, path_end_node):
        ret_path = list()
        while path_end_node:
            ret_path.append(path_end_node.nid)
            path_end_node = path_end_node.parent
        ret_path.reverse()
        return ret_path

    def _get_cost_between_nodes(self, s_nid, d_nid):
        s_node = self.nodes[s_nid]
        d_node = self.nodes[d_nid]
        # euclidean cost between two co-ordinates (x1, y1) & (x2, y2) is
        # ref: https://en.wikipedia.org/wiki/Euclidean_distance
        # sqrt((|x2-x1|)^2 + (|y2-y1|)^2))
        return math.sqrt((d_node[0] - s_node[0]) ** 2 + (d_node[1] - s_node[1]) ** 2)




def shortest_path(M,start,goal):
    print("shortest path called")
    astar = MapSpace(M.intersections, M.roads)
    return astar.get_astar_path(start, goal)
    