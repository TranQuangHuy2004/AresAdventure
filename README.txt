**PROJECT NAME**
	Project 1. Search - Ares’s adventure

**Description**
	This project is a Python-based maze-solving tool that demonstrates the implementation of several search algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), Uniform Cost Search (UCS), and A* Search. Each algorithm navigates a grid-based maze, where an agent named "Ares" pushes stones of varying weights onto switches to solve the maze. The maze is generated from input files, allowing users to specify custom maze layouts, stone weights, and other parameters.

**Prerequisites**
	Ensure you have the following installed:
		+ Python (version 3.x or higher)
		+ pip for managing packages
		+ Required Python packages are listed in requirements.txt

**Install required packages**
	> pip install -r requirements.txt or
	> py -m pip install -r requirements.txt

**How to Run**
	*Navigate to the main project directory*
		Open a terminal or command prompt in the project folder.

	*Run the main Python file*
		> python main.py or
		> py main.py
	
	*Create new inputs for testing*
		+ open the folder AresAdventure\input and create new text file with naming convention input-xx.txt (eg. input-01.txt)
		+ the folder AresAdventure\output stores the output-xx.txt files which save the results of input-xx.txt
		+ the folder AresAdventure\solution stores files which only save the solution paths of each algorithms for each input to be used for visualization

	*Visualiztion*
		+ after creating new input files, remember to generate the results of each using *run algorithm* option in the main menu of the GUI
		+ then you can choose *visualization* option and start running each algorithm of each input