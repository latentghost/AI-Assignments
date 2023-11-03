import heapq
import pandas as pd
import numpy as np


class Graph:
    def __init__(self):
        self.graph = {}


    def add_edge(self, start, end, cost):
        if(start==end):
            if start not in self.graph.keys():
                self.graph[start] = []
            self.graph[start].append((end,0))

            return

        if start not in self.graph.keys():
            self.graph[start] = []
        self.graph[start].append((end,int(cost)))
        
        if end not in self.graph.keys():
            self.graph[end] = []
        self.graph[end].append((start,int(cost)))


    def  ucs(self, start, goal):
        assert start in self.graph.keys(), "Invalid city entered as start"
        assert goal in self.graph.keys(), "Invalid city entered as goal"

        queue = []
        visited = {}
        path = {}

        queue.append([0,start])
        visited[start] = 0
        path[start] = None

        while len(queue)>0:
            queue = sorted(queue)

            top = queue[0]
            del queue[0]

            cur_cost = top[0]
            cur = top[1]

            for i in range(len(self.graph[cur])):
                city,next_cost = self.graph[cur][i]
                
                if (city not in visited) or ((city in visited) and (cur_cost+next_cost<visited[city])):
                    visited[city] = cur_cost + next_cost
                    queue.append([visited[city],city])

                    path[city] = cur
                
        if goal in visited.keys():
            return (visited[goal],self.reconstruct_path(path,start,goal))
        else:
            print(f"No path found from {start} to {goal}")


    def reconstruct_path(self, path, start, goal):
        if goal not in path:
            return None
        
        node = goal
        path_list = [node]

        while node != start:
            node = path[node]
            path_list.insert(0, node)
        
        return path_list


if __name__ == '__main__':
    df = pd.read_csv("Road_Distance.csv")

    graph = Graph()
    
    for i in range(df.shape[0]):
        cur = df.iloc[i][0]
        for j in range(1,df.shape[1]):
            graph.add_edge(cur,df.columns[j],df.iloc[i][j])

    start = input("Enter start city: ")
    goal = input("Enter goal city: ")
    ucs = graph.ucs(start,goal)

    path = ""
    for city in ucs[1]:
        if city != ucs[1][-1]:
            path = path + f"{city}-->"
        else:
            path = path + f"{city}"

    print(f"\nCost = {ucs[0]}\nPath taken: {path}")