Title: "Chromatic Explorer: Graph Coloring a Constraint Satisfaction Problem Solver"

Introduction
    The primary goal of this Python program is to demonstrate graph coloring, which is a fundamental concept in Constraint Satisfaction Problems (CSPs) frequently encountered in our course curriculum. To achieve this objective, the program utilizes various functionalities and leverages specific libraries.

    The program's core functionality revolves around the manipulation and analysis of graphs, facilitated by the NetworkX library, a powerful tool for working with complex network structures. By employing NetworkX, the program enables users to create graphs from files, traverse them using Depth-First Search (DFS), apply graph coloring algorithms, and visualize the results through image exportation.

    Through its comprehensive set of features and integration with NetworkX, this program serves as an invaluable educational tool, aiding in the exploration and understanding of graph theory concepts, particularly in the context of CSPs.

Requirements
    - Python 3.x
    - NetworkX
    - Matplotlib

Deployment
    Step 1: make sure you have latest python3 version and pip upgrade to latest version
    Step 2: pip3 install networkx
    Step 3: pip3 install matplotlib
    Step 4: Run the script by executing command
                - python3 gc_dfs.py.py
    Step 5: Generate or Use Graph:
            - Choose one of the following options:
                - Generate a new graph. [Scroll down to read more on this]
                - Use an existing sample graph.
                - Use a custom graph file. [Scroll down on how to create the custom graph]
    Step 6: DFS Traversal and Coloring:
            - The script performs DFS traversal on the graph and colors the nodes using the graph coloring algorithm.
    Step 7: Export Graph:
            - The colored graph is exported as a PNG image file.

Classes and Functions:
    - Graph:
        Represents an undirected graph with methods for adding edges, nodes, scanning from a file, performing DFS traversal, coloring the graph, and exporting the graph.
    - generate_new_graph():
        Generates a new graph based on user input for the number of nodes and edges.
    - use_existing_sample():
        Allows the user to choose an existing sample graph file.
    - generate_or_use_graph():
        Prompts the user to choose between generating a new graph, using an existing sample, or providing a custom graph file.

Samples
    - The program includes examples of generating or using a graph file and performing DFS traversal and coloring.
    - Example graph files are provided in the repository (example_graph_1.txt to example_graph_7.txt).

Create Custom Graphs
    To create a custom graph to be used in the provided Python program, follow these steps:
    - The Graph Representation:
        The script uses an adjacency list representation to store the graph's nodes and edges.
    - Create a Graph File:
        Create a text file (.txt) that represents your custom graph. Each line in the file represents an edge between two nodes.
        The format should be:
            node1,node2
    - Replace node1 and node2 with the names or identifiers of the nodes connected by the edge. Repeat this format for each edge in the graph.
    - Save the Graph File:
        Save the text file with a descriptive name, such as [yourLastName_]custom_graph.txt.
    - Enter the filename of the custom graph file you created ([yourLastName_]custom_graph.txt) when prompted.


Developed by Sushant Regmi
Feel free to customize and extend the script as needed for your own projects. If you have any questions or feedback, please contact sregmi@nmsu.edu.