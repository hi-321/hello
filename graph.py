from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.n = 0
        self.adj = {} 
        self.weight = {}

    def add_node(self, node):
        if node not in self.adj:
            self.n += 1
            self.adj[node] = []
            self.weight[node] = {}
        self.sort_graph()
    
    def add_edge(self, node1, node2, cost):
        if node1 in self.adj and node2 in self.adj:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
            self.weight[node1][node2] = cost
            self.weight[node2][node1] = cost
        self.sort_graph()
    
    def del_node(self, node):
        if node in self.adj:
            del self.adj[node]
            del self.weight[node]
            for key in self.adj.keys():
                if node in self.adj[key]:
                    self.adj[key].remove(node)
            for key in self.weight.keys():
                if node in self.weight[key]:
                    del self.weight[key][node]
        self.sort_graph()
    
    def del_edge(self, node1, node2):
        if node1 in self.adj and node2 in self.adj:
            self.adj[node1].remove(node2)
            self.adj[node2].remove(node1)
            del self.weight[node1][node2]
            del self.weight[node2][node1]
        self.sort_graph()
    
    def sort_graph(self, reverse=False):
        for key in self.adj.keys():
            if reverse:
                self.adj[key].sort(reverse=True)
            else:
                self.adj[key].sort()

    def print_adj_list(self):
        print(self.adj)
        print(self.weight)
        print("\nUnweighted Graph:")
        for key in self.adj.keys():
            print("node", key, ": ", self.adj[key])
        print("\nWeighted Graph")
        for key in self.weight.keys():
            print("node", key, ": ", self.weight[key])

    def print_path(self, x):
        print("\nPath:", end=" ")
        print(" -> ".join(x))
    
    def bfs(self, source, goal):
        bfslist=[]
        visited=[source] 
        queue=[source] 
        while queue:
            s = queue.pop(0)
            bfslist.append(s) 
            self.print_path(bfslist)
            if(s==goal):
                print("\nReached goal state!")
                return 
            for neighbour in self.adj[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        print("\nGoal not found!")

    def dfs(self, source, goal):
        self.sort_graph(True)
        dfslist=[]
        visited=[source] 
        stack=[source] 
        while stack:
            s = stack.pop()
            dfslist.append(s) 
            self.print_path(dfslist)
            if(s==goal):
                print("\nReached goal state!")
                self.sort_graph()
                return 
            for neighbour in self.adj[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    stack.append(neighbour)
        print("\nGoal not found!")
        self.sort_graph()

    def ucs(self, source, goal):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, source, []))
        all_paths = []

        while not queue.empty():
            cost, current_node, path = queue.get()
            if current_node == goal:
                all_paths.append((path + [current_node], cost))
                continue

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbour in self.adj[current_node]:
                new_cost = cost + self.weight[current_node][neighbour]
                new_path = path + [current_node]

                if neighbour not in visited:
                    queue.put((new_cost, neighbour, new_path))

        if not all_paths:
            print("\nGoal not found!")
            return

        print("\nAll possible paths:")
        for path, path_cost in all_paths:
            self.print_path(path)
            print("Cost:", path_cost)

        optimal_path = min(all_paths, key=lambda x: x[1])
        print("\nMost optimal path:")
        self.print_path(optimal_path[0])
        print("Minimum Path Cost:", optimal_path[1])

        return all_paths

graph = Graph()
graph.add_node('S')
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('G')

graph.add_edge('S', 'A' ,1)
graph.add_edge('S', 'B' ,5)
graph.add_edge('S', 'C' ,8)
graph.add_edge('A', 'D' ,3)
graph.add_edge('A', 'E' ,7)
graph.add_edge('A', 'G' ,9)
graph.add_edge('B', 'G' ,4)
graph.add_edge('C', 'G' ,5)

while(True):
    print("\n===========MENU===========")
    print("1 -> Add Node")
    print("2 -> Add Edge")
    print("3 -> Remove Node")
    print("4 -> Remove Edge")
    print("5 -> Print adjacency list")
    print("6 -> BFS of Graph")
    print("7 -> DFS of Graph")
    print("8 -> UCS of Graph")
    print("9 -> Exit")
    print("==========================\n")
    choice = int(input("Enter choice: "))

    if(choice==1):
        node=input("Enter node: ")
        graph.add_node(node)

    elif(choice==2):
        node1=input("Enter node 1: ")
        node2=input("Enter node 2: ")
        cost=int(input("Enter cost: "))
        graph.add_edge(node1, node2, cost)

    elif(choice==3):
        node=input("Enter node: ")
        graph.del_node(node)

    elif(choice==4):
        node1=input("Enter node 1: ")
        node2=input("Enter node 2: ")
        graph.del_edge(node1, node2)

    elif(choice==5):
        graph.print_adj_list()

    elif(choice==6):
        source = input("Enter source: ")
        goal = input("Enter goal: ")
        graph.bfs(source, goal)

    elif(choice==7):
        source = input("Enter source: ")
        goal = input("Enter goal: ")
        graph.dfs(source, goal)

    elif(choice==8):
        source = input("Enter source: ")
        goal = input("Enter goal: ")
        graph.ucs(source, goal)

    elif(choice==9):
        break

    else:
        print("Enter a valid choice!")
