# 🧩 Maze Generator & Solver

A Python-based interactive web application for generating and solving mazes using multiple pathfinding algorithms. The application is built with **Python** and **Streamlit** and provides a simple visual interface to understand how different algorithms find a path through a maze.

## 🚀 Live Demo

**Maze Generator & Solver:**
https://your-app-name.streamlit.app/

> Replace the URL above with your actual Streamlit deployment URL.

## 📌 Project Overview

Maze Generator & Solver is an interactive application that allows users to:

* Generate random mazes.
* Select different maze sizes.
* Choose a pathfinding algorithm.
* Solve the generated maze.
* Visualize the explored cells and final path.
* Compare different pathfinding approaches.

The project demonstrates important concepts from **Data Structures, Algorithms, Graph Traversal, and Artificial Intelligence**.

## ✨ Features

### 🔐 User Interface

* Simple and interactive Streamlit interface.
* Clean dashboard for maze generation and solving.
* Easy-to-use controls.
* Adjustable maze size.
* Algorithm selection.

### 🧱 Maze Generation

The application generates random mazes dynamically and displays them visually.

### 🧠 Maze Solving Algorithms

The following algorithms are implemented:

| Algorithm | Type             | Main Idea                                       |
| --------- | ---------------- | ----------------------------------------------- |
| BFS       | Graph Traversal  | Explores nodes level by level                   |
| DFS       | Graph Traversal  | Explores as deeply as possible                  |
| Dijkstra  | Shortest Path    | Finds the minimum-cost path                     |
| A*        | Heuristic Search | Uses cost + heuristic to find an efficient path |

## 🔍 Algorithms Explained

### 1. Breadth-First Search (BFS)

BFS explores the maze level by level.

**Advantages:**

* Finds the shortest path in an unweighted maze.
* Simple and reliable.

**Time Complexity:**

`O(V + E)`

---

### 2. Depth-First Search (DFS)

DFS explores one path as deeply as possible before backtracking.

**Advantages:**

* Simple to implement.
* Uses backtracking naturally.

**Limitation:**

DFS does not necessarily find the shortest path.

**Time Complexity:**

`O(V + E)`

---

### 3. Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path by continuously selecting the node with the smallest known distance.

**Advantages:**

* Guarantees the shortest path when edge weights are non-negative.

**Time Complexity:**

`O((V + E) log V)`

---

### 4. A* Algorithm

A* combines the actual cost of reaching a node with an estimated cost to the destination.

The evaluation function is:

`f(n) = g(n) + h(n)`

where:

* `g(n)` = cost from the start node to the current node.
* `h(n)` = estimated cost from the current node to the goal.
* `f(n)` = total estimated cost.

A* can be significantly faster than uninformed search when an appropriate heuristic is used.

## 🛠️ Technologies Used

* **Python 3**
* **Streamlit**
* **NumPy**
* **Matplotlib**
* **Pandas**
* **Git**
* **GitHub**

## 📂 Project Structure

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

> Update the structure if your actual filenames are different.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/MazeGeneratorSolver.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Open the project

```bash
cd MazeGeneratorSolver
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Git Bash:

```bash
source venv/Scripts/activate
```

Windows Command Prompt:

```cmd
venv\Scripts\activate
```

PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

## ☁️ Deployment

This project can be deployed using **Streamlit Community Cloud**.

### Deployment steps

1. Push the project to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in with GitHub.
4. Select the `MazeGeneratorSolver` repository.
5. Select the `main` branch.
6. Set the main file to:

```text
app.py
```

7. Click **Deploy**.

After deployment, Streamlit provides a public URL that can be shared with others.

## 🧪 How to Use

1. Open the application.
2. Select the desired number of rows and columns.
3. Generate a maze.
4. Select a pathfinding algorithm.
5. Click **Solve**.
6. Observe the explored cells and final path.
7. Try another algorithm and compare the results.
8. Use **Reset** to start again.

## 📊 Algorithm Comparison

| Algorithm | Shortest Path | Uses Heuristic | Search Style |
| --------- | ------------- | -------------- | ------------ |
| BFS       | ✅ Yes*        | ❌ No           | Uninformed   |
| DFS       | ❌ No          | ❌ No           | Uninformed   |
| Dijkstra  | ✅ Yes         | ❌ No           | Cost-based   |
| A*        | ✅ Yes*        | ✅ Yes          | Informed     |

`*` Assumes an unweighted maze and an appropriate movement model.

## 🎯 Learning Objectives

This project helps demonstrate:

* Graph representation.
* Graph traversal.
* Pathfinding algorithms.
* Queue and stack concepts.
* Priority queues.
* Heuristic search.
* Shortest-path algorithms.
* Algorithm comparison.
* Python modular programming.
* Streamlit application development.
* Git and GitHub workflow.
* Web application deployment.

## 🔮 Future Enhancements

Possible future improvements include:

* Animation of algorithm execution.
* Adjustable solving speed.
* Step-by-step algorithm visualization.
* Maze difficulty levels.
* Different maze-generation algorithms.
* Weighted mazes.
* Algorithm performance statistics.
* Path length comparison.
* Execution-time comparison.
* Dark/light theme customization.
* Downloadable maze results.

## 👩‍💻 Author

**Sruthi**

B.Tech Computer Science and Engineering

### GitHub

https://github.com/YOUR_USERNAME

> Replace `YOUR_USERNAME` with your actual GitHub username.

## 📄 License

This project is intended for educational and academic purposes.

You are free to modify and improve the project for learning and development.

---

## ⭐ Project Highlights

**Maze Generator & Solver** combines:

`Python` + `Streamlit` + `Graph Algorithms` + `Pathfinding` + `Visualization`

It provides an interactive way to understand and compare different maze-solving algorithms.
