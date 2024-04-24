import random

# Generate a random large example graph file
def generate_large_graph_file(file_name, num_nodes, num_edges):
    with open(file_name, 'w') as f:
        for _ in range(num_edges):
            node_a = random.randint(1, num_nodes)
            node_b = random.randint(1, num_nodes)
            while node_b == node_a:  # Ensure different nodes
                node_b = random.randint(1, num_nodes)
            f.write(f"{node_a},{node_b}\n")

if __name__ == "__main__":
    num_nodes = input("Number of nodes : ")
    num_edges = input("Number of edges : ")
    file_name = "./user_generated_graphs/user_generated_graph.txt"
    generate_large_graph_file(file_name, int(num_nodes), int(num_edges))
    print(f"Graph '{file_name}' generated with {num_nodes} nodes and {num_edges} edges.")