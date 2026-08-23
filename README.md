# 🧩 Maze Generator & Solver

An interactive **Python-based Maze Generator and Solver** that allows users to generate random mazes and solve them using different pathfinding algorithms.

The application is developed using **Python and Streamlit** and provides a visual way to understand how popular graph traversal and shortest-path algorithms work.

---

## 🚀 Project Links

### 📂 GitHub Repository

https://github.com/Pokkuluri-Sruthi/MazeGeneratorSolver

### 🌐 Live Demo

> The live demo link will be added after deploying the application on Streamlit Community Cloud.

---

## 📌 Project Overview

**Maze Generator & Solver** is an interactive web application designed to demonstrate maze generation and pathfinding algorithms.

Users can:

* Generate random mazes.
* Select the maze size.
* Choose a pathfinding algorithm.
* Solve the maze.
* Visualize the explored cells.
* Visualize the final path.
* Compare different algorithms.

The project combines **Data Structures, Algorithms, Graph Traversal, Shortest Path Algorithms, and Web Application Development**.

---

## ✨ Features

### 🧱 Maze Generation

* Random maze generation.
* Customizable number of rows and columns.
* Visual representation of the generated maze.
* Ability to generate a new maze at any time.

### 🧠 Multiple Solving Algorithms

The application supports:

* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Dijkstra's Algorithm
* A* Search Algorithm

### 🎨 Interactive Visualization

The application visually displays:

* Maze walls.
* Start position.
* Goal position.
* Visited cells.
* Final solution path.

### ⚡ Interactive Controls

Users can:

* Generate a maze.
* Select an algorithm.
* Solve the maze.
* Reset the application.
* Adjust maze parameters.

---

# 🧠 Algorithms Used

## 1. Breadth-First Search — BFS

BFS explores the maze level by level using a queue.

It guarantees the shortest path in an unweighted maze.

### Advantages

* Simple to understand.
* Finds the shortest path in an unweighted graph.
* Complete search algorithm.

### Time Complexity

```text
O(V + E)
```

where:

* `V` = number of vertices/cells.
* `E` = number of edges/connections.

---

## 2. Depth-First Search — DFS

DFS explores one path as deeply as possible before backtracking.

### Advantages

* Simple implementation.
* Uses stack/backtracking concepts.
* Useful for exploring maze structures.

### Limitation

DFS does not necessarily find the shortest path.

### Time Complexity

```text
O(V + E)
```

---

## 3. Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path by repeatedly selecting the node with the smallest known distance.

### Advantages

* Finds the shortest path.
* Works with weighted graphs.
* Does not require a heuristic.

### Time Complexity

```text
O((V + E) log V)
```

when implemented using a priority queue.

---

## 4. A* Algorithm

A* is an informed search algorithm that combines the actual cost with an estimated cost to the goal.

The evaluation function is:

```text
f(n) = g(n) + h(n)
```

where:

* `g(n)` = cost from the start node to the current node.
* `h(n)` = estimated cost from the current node to the goal.
* `f(n)` = estimated total cost.

### Advantages

* Efficient pathfinding.
* Uses heuristic information.
* Can explore fewer nodes than uninformed algorithms.

---

# 📊 Algorithm Comparison

| Algorithm | Shortest Path    | Heuristic | Search Type |
| --------- | ---------------- | --------- | ----------- |
| BFS       | ✅ Yes*           | ❌ No      | Uninformed  |
| DFS       | ❌ Not guaranteed | ❌ No      | Uninformed  |
| Dijkstra  | ✅ Yes            | ❌ No      | Cost-based  |
| A*        | ✅ Yes*           | ✅ Yes     | Informed    |

`*` For an unweighted maze with uniform movement cost.

---

# 🛠️ Technologies Used

* **Python 3**
* **Streamlit**
* **NumPy**
* **Matplotlib**
* **Pandas**
* **Git**
* **GitHub**

---

# 📂 Project Structure

```text
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
```

> Update the structure if your actual project contains additional files.

---

# ⚙️ Installation

## 1. Clone the Repository

Open Git Bash or a terminal and run:

```bash
git clone https://github.com/Pokkuluri-Sruthi/MazeGeneratorSolver.git
```

---

## 2. Navigate to the Project

```bash
cd MazeGeneratorSolver
```

---

## 3. Create a Virtual Environment

```bash
python -m venv venv
```

---

## 4. Activate the Virtual Environment

### Git Bash

```bash
source venv/Scripts/activate
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

---

## 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 🎮 How to Use

### Step 1

Open the application.

### Step 2

Select the required maze dimensions.

### Step 3

Click **Generate Maze**.

### Step 4

Select a solving algorithm:

```text
BFS
DFS
Dijkstra
A*
```

### Step 5

Click **Solve**.

### Step 6

Observe the algorithm exploring the maze and finding the solution path.

### Step 7

Use **Reset** to create or solve another maze.

---

# ☁️ Deployment

This project can be deployed using **Streamlit Community Cloud**.

### Deployment Process

```text
Python Project
      ↓
Git
      ↓
GitHub
      ↓
Streamlit Community Cloud
      ↓
Public Web Application
```

### Deployment Steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in using GitHub.
4. Select the repository:

```text
Pokkuluri-Sruthi/MazeGeneratorSolver
```

5. Select the `main` branch.
6. Set the main file to:

```text
app.py
```

7. Click **Deploy**.

After successful deployment, Streamlit provides a public HTTPS URL.

---

# 🎯 Learning Objectives

This project demonstrates:

* Graph representation.
* Graph traversal.
* Breadth-First Search.
* Depth-First Search.
* Dijkstra's shortest-path algorithm.
* A* search.
* Queue and stack concepts.
* Priority queues.
* Heuristic search.
* Pathfinding.
* Python modular programming.
* Streamlit application development.
* Git version control.
* GitHub repository management.
* Cloud deployment.

---

# 📈 Future Enhancements

The project can be extended with:

* Animated algorithm execution.
* Adjustable solving speed.
* Step-by-step visualization.
* Maze difficulty levels.
* Multiple maze-generation algorithms.
* Weighted mazes.
* Algorithm performance comparison.
* Execution-time statistics.
* Path-length comparison.
* Number of visited cells.
* Downloadable maze results.
* Improved user interface.
* Dark/light theme.
* More pathfinding algorithms.

---

# 🧪 Example Workflow

```text
Start
  ↓
Generate Maze
  ↓
Select Algorithm
  ↓
Start Solving
  ↓
Explore Maze
  ↓
Find Goal
  ↓
Display Shortest/Found Path
  ↓
Reset / Generate New Maze
```

---

# 📚 Concepts Covered

This project applies concepts from:

### Data Structures

* Arrays
* Lists
* Queues
* Stacks
* Priority Queues
* Graphs

### Algorithms

* BFS
* DFS
* Dijkstra
* A*
* Maze Generation
* Pathfinding

### Software Development

* Python Modules
* Object-Oriented Programming
* Streamlit
* Git
* GitHub
* Cloud Deployment

---

# 👩‍💻 Author

## Sruthi

**B.Tech Computer Science and Engineering**

### GitHub Repository

https://github.com/Pokkuluri-Sruthi/MazeGeneratorSolver

---

# 📄 License

This project is developed for **educational and academic purposes**.

You are free to use, modify, and improve the project for learning and development.

---

# ⭐ Project Highlights

**Maze Generator & Solver** combines:

```text
Python
   +
Streamlit
   +
Graph Algorithms
   +
Pathfinding
   +
Visualization
   +
GitHub
   +
Cloud Deployment
```

The goal of this project is to provide an interactive and visual understanding of how different pathfinding algorithms explore and solve a maze.
