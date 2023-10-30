from queue import PriorityQueue

class Node:
    def __init__(self, data, heuristic):
        self.data = data
        self.neighbors = []
        self.heuristic = heuristic
        self.g_cost = float('inf')

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node, heuristic):
        self.nodes[node] = Node(node, heuristic)

    def add_edge(self, start, end, cost):
        self.nodes[start].neighbors.append((end, cost))
        self.nodes[end].neighbors.append((start, cost))
    
    def astar_search(self, start, goal):
        visited = set()
        pq = PriorityQueue()
        pq.put((0 + self.nodes[start].heuristic, 0, [start]))

        while not pq.empty():
            current_cost, g_cost, current_path = pq.get()
            print(f"Chosen path: {' -> '.join(current_path)} \t Cost: {current_cost}")
            current_vertex = current_path[-1]

            if current_vertex == goal:
                return current_cost, current_path

            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            current_node = self.nodes[current_vertex]

            intermediate_paths = []

            for neighbor, cost in current_node.neighbors:
                new_g_cost = g_cost + cost
                if neighbor in visited:
                    self.nodes[neighbor].g_cost = min(self.nodes[neighbor].g_cost, new_g_cost)

                else:
                    new_cost = new_g_cost + self.nodes[neighbor].heuristic
                    new_path = current_path + [neighbor]
                    pq.put((new_cost, new_g_cost, new_path))
                    intermediate_paths.append((new_cost, new_path))

            print(f"Possible paths from {current_vertex}:")
            for cost, path in intermediate_paths:
                print(f"{' -> '.join(path)} \t Cost: {cost}")
        return float('inf'), None
    
graph = Graph()
''''
graph.add_node('L', 244)
graph.add_node('M', 241)
graph.add_node('D', 242)
graph.add_node('C', 160)
graph.add_node('R', 193)
graph.add_node('P', 100)
graph.add_node('B', 0)
graph.add_node('S', 253)
graph.add_node('F', 176)

graph.add_edge('L', 'M' ,50)
graph.add_edge('M', 'D' ,55)
graph.add_edge('D', 'C' ,90)
graph.add_edge('C', 'R' ,40)
graph.add_edge('C', 'P' ,138)
graph.add_edge('R', 'P' ,97)
graph.add_edge('R', 'B' ,30)
graph.add_edge('P', 'B' ,101)
graph.add_edge('B', 'S' ,80)
graph.add_edge('B', 'F' ,211)
graph.add_edge('S', 'F' ,99)
'''
graph.add_node('S', 7)
graph.add_node('A', 9)
graph.add_node('B', 4)
graph.add_node('C', 2)
graph.add_node('D', 5)
graph.add_node('E', 3)
graph.add_node('G', 0)

graph.add_edge('S', 'A' ,3)
graph.add_edge('S', 'D' ,2)
graph.add_edge('A', 'B' ,5)
graph.add_edge('A', 'C' ,10)
graph.add_edge('B', 'C' ,2)
graph.add_edge('B', 'E' ,1)
graph.add_edge('C', 'G' ,4)
graph.add_edge('D', 'B' ,1)
graph.add_edge('D', 'E' ,4)
graph.add_edge('E', 'G' ,3)

while(True):
    print("\n=======MENU=======")
    print("1 > Add Node")
    print("2 > Add Edge")
    print("3 > A-Star Search")
    print("4 > Exit")
    print("==================\n")
    choice = int(input("Enter choice: "))

    if(choice==1):
        node=input("Enter node: ")
        heuristic=int(input("Enter heuristic: "))
        graph.add_node(node, heuristic)

    elif(choice==2):
        node1=input("Enter node 1: ")
        node2=input("Enter node 2: ")
        cost=int(input("Enter cost: "))
        graph.add_edge(node1, node2, cost)
    
    elif(choice==3):
        source = input("Enter source node: ")
        goal = input("Enter goal node: ")
        cost, path = graph.astar_search(source, goal)
        if path is not None:
            print(f"\nOptimal path: {' -> '.join(path)}")
            print(f"Optimal cost: {cost}")
        else:
            print("No path found to goal node.")

    elif(choice==4):
        break

    else:
        print("Enter a valid choice!")
