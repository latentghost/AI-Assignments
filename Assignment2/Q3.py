import pandas as pd
import numpy as np
import networkx as nx


class Graph:
    def __init__(self):
        self.graph = {}
        
        self.a_star_visited = {}
        self.a_star_path = {}
        self.a_star_est = {}

        self.mst = {}

        self.nodes_a = 0
        self.nodes_i = 0


    def add_edge(self, start, end, cost):
        if(start==end):
            if start not in self.graph.keys():
                self.graph[start] = []
            self.graph[start].append([end,0])

            return

        if start not in self.graph.keys():
            self.graph[start] = []
            self.graph[start].append([end,int(cost)])
        else:
            for i in range(len(self.graph[start])):
                if(self.graph[start][i][0]==end):
                    self.graph[start][i][1] = min(self.graph[start][i][1],int(cost))
                    break
                elif i==len(self.graph[start])-1:
                    self.graph[start].append([end,int(cost)])
        
        if end not in self.graph.keys():
            self.graph[end] = []
            self.graph[end].append([start,int(cost)])
        else:
            for i in range(len(self.graph[end])):
                if(self.graph[end][i][0]==start):
                    self.graph[end][i][1] = min(self.graph[end][i][1],int(cost))
                    break
                elif i==len(self.graph[end])-1:
                    self.graph[end].append([start,int(cost)])


    def search(self,start,goal):
        print(f"\nUsing Uniform Cost Search:\n{self.ucs(start,goal)}")
        
        print("\nUsing A* search:")

        self.a_star_est = {}
        self.a_star_path = {}
        self.a_star_visited = {}
        self.nodes_a = 0

        print(f"Using Admissible Heuristic: {self.a_star(start,goal,[[0,start]],self.admissible_h,0)}")

        self.a_star_est = {}
        self.a_star_path = {}
        self.a_star_visited = {}
        self.nodes_i = 0
        
        print(f"Using Inadmissible Heuristic: {self.a_star(start,goal,[[0,start]],self.inadmissible_h,1)}\n")

        print(f"""Number of nodes expanded in A* search:
        Using Admissible Heuristic: {self.nodes_a}
        Using Inadmissible Heuristic: {self.nodes_i}""")


    def ucs(self, start, goal):
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

    
    def a_star(self, start, goal, queue, h, flag):
        assert start in self.graph.keys(), "Invalid city entered as start"
        assert goal in self.graph.keys(), "Invalid city entered as goal"

        self.a_star_visited[start] = 0
        if len(queue)==0:
            if goal in self.a_star_visited:
                return (self.a_star_visited[goal],self.reconstruct_path(self.a_star_path,start,goal))
            else:
                return (np.inf,None)

        queue = sorted(queue)
        
        top = queue[0]
        del queue[0]

        cur = top[1]

        for i in range(len(self.graph[cur])):
            city,next_cost = self.graph[cur][i]

            f_cost = self.a_star_visited[cur] + next_cost + h(city,goal)

            if (city not in self.a_star_visited) or ((city in self.a_star_visited) and (self.a_star_visited[cur]+next_cost<self.a_star_visited[city])):
                self.a_star_visited[city] = self.a_star_visited[cur]+next_cost
                self.a_star_path[city] = cur

            if ((goal not in self.a_star_visited) or (f_cost<self.a_star_visited[goal])) and (city not in self.a_star_est or f_cost<self.a_star_est[city]):
                queue.append([f_cost,city])
                self.a_star_est[city] = f_cost

        if flag==0:
            self.nodes_a+=1
        elif flag==1:
            self.nodes_i+=1

        return self.a_star(start,goal,queue,h,flag)
    

    def build_mst(self):
        def find(parent, node):
            if parent[node] == node:
                return node
            return find(parent, parent[node])

        def union(parent, rank, node1, node2):
            root1 = find(parent, node1)
            root2 = find(parent, node2)

            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1] += 1

        edges = [(u, v, w) for u, neighbors in self.graph.items() for v, w in neighbors]
        edges.sort(key=lambda edge: edge[2])

        mst = {}
        parent = {}
        rank = {}

        for node in self.graph:
            parent[node] = node
            rank[node] = 0

        for u, v, w in edges:
            root1 = find(parent, u)
            root2 = find(parent, v)

            if root1 != root2:
                if u not in mst:
                    mst[u] = []
                if v not in mst:
                    mst[v] = []

                mst[u].append((v, w))
                mst[v].append((u, w))

                union(parent, rank, root1, root2)

        return mst
    

    def admissible_h(self,n1,goal):
        assert n1 in self.graph, f"Invalid city, {n1} not in graph"
        assert goal in self.graph, f"Invalid city, {goal} not in graph"

        self.mst = self.build_mst()
        
        if n1==goal:
            return 0
        
        mn = 1e8
        for i in range(len(self.mst[n1])):
            mn = min(self.mst[n1][i][1],mn)

        return mn


    def inadmissible_h(self,n1,goal):
        assert n1 in self.graph, f"Invalid city, {n1} not in graph"
        assert goal in self.graph, f"Invalid city, {goal} not in graph"

        if(n1==goal):
            return 0

        for i in range(len(self.graph[n1])):
            if self.graph[n1][i][0]==goal:
                return self.graph[n1][i][1]
            
        return 1e8


    def reconstruct_path(self, path, start, goal):
        if goal not in path:
            return None
        
        node = goal
        path_list = [node]

        while node != start:
            node = path[node]
            path_list.insert(0, node)
        
        path = ""
        for city in path_list:
            if city != path_list[-1]:
                path = path + f"{city}-->"
            else:
                path = path + f"{city}"

        return path


if __name__ == '__main__':
    df = pd.read_csv("Road_Distance.csv")

    graph = Graph()
    
    for i in range(df.shape[0]):
        cur = df.iloc[i][0]
        for j in range(1,df.shape[1]):
            graph.add_edge(cur,df.columns[j],df.iloc[i][j])

    start = input("Enter start city: ")
    goal = input("Enter goal city: ")

    ucs = graph.search(start,goal)