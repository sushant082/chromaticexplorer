import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
import generate_graph
import datetime

class Graph:
    def __init__(self):
        self.m_nodes = set()  
        self.m_adjList = defaultdict(list)  
        self.pre_visit = {}
        self.post_visit = {}
        self.clock = 1  

    def add_edge(self, a, b):
        self.m_adjList[a].append(b)
        self.m_adjList[b].append(a)
    
    def add_node(self, node):
        self.m_nodes.add(node)

    def get_adj_nodes(self, a):
        return self.m_adjList[a]

    def num_nodes(self):
        return len(self.m_nodes)

    def scan(self, file):
        with open(file, 'r') as f:
            for line in f:
                a, b = line.strip().split(',')
                self.add_edge(a, b)
                self.add_node(a)
                self.add_node(b)

    def dfs(self, start_node):
        self._dfs_visit(start_node)

    def _dfs_visit(self, node):
        self.pre_visit[node] = self.clock  
        self.clock += 1

        for neighbor in self.m_adjList[node]:
            if neighbor not in self.pre_visit:  
                self._dfs_visit(neighbor)

        self.post_visit[node] = self.clock  
        self.clock += 1

    def color_graph(self):
        colors = {}  # Dictionary to store the color assigned to each node
        for node in self.m_nodes:
            if node not in colors:
                neighbor_colors = set(colors.get(neighbor, None) for neighbor in self.m_adjList[node])
                color = 1
                while color in neighbor_colors:
                    color += 1
                colors[node] = color
        return colors

    def export_graph(self, file):
        G = nx.Graph()
        for node, adj_list in self.m_adjList.items():
            for neighbor in adj_list:
                G.add_edge(node, neighbor)
        colors = self.color_graph()
        node_colors = [colors[node] for node in G.nodes]
        pos = nx.spring_layout(G)  # You can use different layout algorithms
        nx.draw(G, pos, with_labels=True, node_color=node_colors, cmap=plt.cm.Set1)
        plt.savefig(file)
        plt.show()

def generate_new_graph():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    num_nodes = int(input("Enter the number of nodes for the new graph: "))
    num_edges = int(input("Enter the number of edges for the new graph: "))
    generate_graph.generate_large_graph_file(f"./user_generated_graphs/user_generated_graph_{timestamp}.txt", num_nodes, num_edges)
    print(f"New graph generated successfully. filename:user_generated_graph_{timestamp}.txt")
    return f"user_generated_graph_{timestamp}.txt"

def use_existing_sample():
    sample_number = input("We have seven sample files. Enter the sample number (1 to 7) of the existing graph you want to use: ")
    if sample_number.isdigit() and 1 <= int(sample_number) <= 7:
        sample_file = f"example_graph_{sample_number}.txt"
        print(f"Using existing sample graph: {sample_file}")
    else:
        print("Invalid sample number. Please enter a number between 1 and 7.")
    return sample_file


def generate_or_use_graph():
    while True:
        choice = input("Do you want to\n\t[1]:generate a new graph? or\n\t[2]:use an existing sample graph? or\n\t[3]:use custom graph?\n\tEnter your choice [1 or 2 or 3]:")
        if choice == '1':
            filename = "./user_generated_graphs/"+generate_new_graph()
            break
        elif choice == '2':
            filename = "./samples/"+use_existing_sample()
            break
        elif choice == '3':
            filename = "./custom_graphs/"+input("Provide your filename [Please make sure the file is in the custom_graph folder]:")
            break
        else:
            print("Invalid choice. Please enter '1' to generate a new graph or '2' to use an existing sample.")
    return filename

if __name__ == "__main__":
    x = generate_or_use_graph()

    graphs = [x]
    for graph_file in graphs:
        graph = Graph()

        graph.scan(graph_file)
        print("\nNumber of nodes:", graph.num_nodes())
        for node in graph.m_nodes:
            if node not in graph.pre_visit:
                graph.dfs(node)

        print(f"Traversing to color the undirected graph for {graph_file}")
        print("\tAdjacency list:")
        for node, adj_list in graph.m_adjList.items():
            print(f"\t\t{node}: {adj_list}")

        colors = graph.color_graph()
        print("\tNode colors:", colors)

        # print(graph_file)
        # graph_file.replace('.txt','').replace('./user_generated_graphs/','').replace('./samples/','').replace('./custom_graphs/','')
        # print(graph_file)

        print(f"Please check for the output file: {graph_file.replace('.txt','')}_output_graph.png")

        graph.export_graph(f"{graph_file.replace('.txt','')}_output_graph.png")
