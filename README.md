🧩 Maze Generator & Solver

An interactive Python-based Maze Generator and Solver that allows users to generate random mazes and solve them using different pathfinding algorithms.

The application is developed using Python and Streamlit and provides a visual way to understand how popular graph traversal and shortest-path algorithms work.

🚀 Project Links
📂 GitHub Repository

https://github.com/Pokkuluri-Sruthi/MazeGeneratorSolver

🌐 Live Demo

The live demo link will be added after deploying the application on Streamlit Community Cloud.

📌 Project Overview

Maze Generator & Solver is an interactive web application designed to demonstrate maze generation and pathfinding algorithms.

Users can:

Generate random mazes.
Select the maze size.
Choose a pathfinding algorithm.
Solve the maze.
Visualize the explored cells.
Visualize the final path.
Compare different algorithms.

The project combines Data Structures, Algorithms, Graph Traversal, Shortest Path Algorithms, and Web Application Development.

✨ Features
🧱 Maze Generation
Random maze generation.
Customizable number of rows and columns.
Visual representation of the generated maze.
Ability to generate a new maze at any time.
🧠 Multiple Solving Algorithms

The application supports:

Breadth-First Search (BFS)
Depth-First Search (DFS)
Dijkstra's Algorithm
A* Search Algorithm
🎨 Interactive Visualization

The application visually displays:

Maze walls.
Start position.
Goal position.
Visited cells.
Final solution path.
⚡ Interactive Controls

Users can:

Generate a maze.
Select an algorithm.
Solve the maze.
Reset the application.
Adjust maze parameters.
🧠 Algorithms Used
1. Breadth-First Search — BFS

BFS explores the maze level by level using a queue.

It guarantees the shortest path in an unweighted maze.

Advantages
Simple to understand.
Finds the shortest path in an unweighted graph.
Complete search algorithm.
Time Complexity
O(V + E)

where:

V = number of vertices/cells.
E = number of edges/connections.
2. Depth-First Search — DFS

DFS explores one path as deeply as possible before backtracking.

Advantages
Simple implementation.
Uses stack/backtracking concepts.
Useful for exploring maze structures.
Limitation

DFS does not necessarily find the shortest path.

Time Complexity
O(V + E)
3. Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path by repeatedly selecting the node with the smallest known distance.

Advantages
Finds the shortest path.
Works with weighted graphs.
Does not require a heuristic.
Time Complexity
O((V + E) log V)

when implemented using a priority queue.

4. A* Algorithm

A* is an informed search algorithm that combines the actual cost with an estimated cost to the goal.

The evaluation function is:

f(n) = g(n) + h(n)

where:

g(n) = cost from the start node to the current node.
h(n) = estimated cost from the current node to the goal.
f(n) = estimated total cost.
Advantages
Efficient pathfinding.
Uses heuristic information.
Can explore fewer nodes than uninformed algorithms.
📊 Algorithm Comparison
Algorithm	Shortest Path	Heuristic	Search Type
BFS	✅ Yes*	❌ No	Uninformed
DFS	❌ Not guaranteed	❌ No	Uninformed
Dijkstra	✅ Yes	❌ No	Cost-based
A*	✅ Yes*	✅ Yes	Informed

* For an unweighted maze with uniform movement cost.

🛠️ Technologies Used
Python 3
Streamlit
NumPy
Matplotlib
Pandas
Git
GitHub
📂 Project Structure
MazeGeneratorSolver/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── dijkstra.py
│   └── astar.py
│
├── components/
│   ├── header.py
│   └── sidebar.py
│
├── maze/
│   ├── grid.py
│   └── generator.py
│
└── utils/
    └── draw.py

Update the structure if your actual project contains additional files.
