Team, Topic, and Preliminary Source Document 
Team Name: Puzzled 
Team Members: Sylvester Reyes, Steven Brashear, Jacob Guerra, Prince Baral

Problem statement 
Many logic puzzles require satisfying strict mathematical and spatial rules across an entire grid. This project aims to implement a generalized constraint satisfaction solver to automatically solve complex grid-based logic puzzles – specifically Sudoku (9x9 and 15x15 variants) and Nonograms (pain-by-numbers grids) – by treating empty cells as variables, domain numbers/marks as values, and row/column/region rules as hard constraints. As practical applications we considered puzzle enthusiasts, mobile gaming automated-solvers, and educators teaching algorithmic search logic who would use this solver to analyze, generate, and instantly crack complex constraint-based girds. This project’s scope and boundaries are limited to deterministic grid puzzles (specifically standard Sudoku and Nonograms up to 15x15). Dynamic puzzle generation based on human difficulty ratings and continuous puzzle video streaming inputs are explicitly left out to ensure completion within the semester time frame.
State representation 
	The type of state representation and candidate models that will be implemented into this project fall between Factored and Structured State Representation. Unlike atomic states (which treat states as black boxes), a puzzle state is factored into a defined set of variables X={S_1,1,S_1,2,…} representing each open grid square, where each variable has a discrete domain (e.g., D={1,2,…,9} for Sudoku). Constraints specify 9-way all-difference rules across rows, columns, and sub-grids. Candidate model variants include 3 paradigms Naïve Backtracking Search, Backtracking with Variable/Value Ordering, and Backtracking with Constraint Propagation (AC – 3) which we explain respectively. 
Naïve Backtracking Search uses basic Depth-First Search with variable assignment and simple constraint checking on violation. Backtracking with Variable/Value Ordering incorporates Minimum Remaining Values (MRV), Degree Heuristic, and Least Constraining Value heuristics. Backtracking with Constraining Propagation integrates forward checking and full arc-consistency pre-processing and maintenance to prune dead-end domains early.  To properly evaluate our candidate models, our experiments will measure performance across three core axes: Nodes Explored, Execution Time (milliseconds), and Failure Detection Point. 
The mechanism used for naïve backtracking (without propagation) explores the search tree depth-first, assigning variables one by one and checking constraints only after an assignment is made (an incremental goal test). The experimental behavior on our puzzles when applied to a hard 9x9 Sudoku or a dense Nonogram naïve backtracking is expected to wonder deep into invalid subtrees before hitting a wall. As it lacks foresight, it will happily assign conflicting numbers to multiple unassigned squares down the line until a hard constraining violation forces a heavy backtrack. This of course will be tested and refined as we build on top of our models. The performance profile will yield high node exploration counts O(d^n) as worst case, making it scale poorly as gris sizes or difficulty levels increase. 
The mechanism for Backtracking with forward checking/arc consistency will provide variable assignments which propagate algorithms immediately filtering the domains of all unassigned neighboring variables and cross off illegal options instantly. If any neighboring variable’s domain shrinks to an empty set, the algorithm detects the dead end immediately and backtracks before wasting time assigning downstream variables. The behavior of this mechanism on puzzles like Sudoku will act if a cell’s domain is reduced to zero legal options, the algorithm prunes that branch instantly. This performance profile will dramatically lower node exploration counts and faster overall solve times on medium-to-hard puzzles, though it introduces a small computation overhead per step to maintain arc consistency tables. 

Preliminary Paper List
Team Member Name: Sylvester Reyes
Paper: Artificial intelligence: A modern Approach (CSP Chapters)
Full Citation: Russel, S., & Norvig, P. (2020). Constraint Satisfaction Problems. A modern Approach (4th ed.). Pearson. 
Venue: Pearson Education, Indexed in Google Scholar and ACM Digital Library. 
Serves as the foundational theoretical text outlining backtracking, MRV, and arc Consistency (AC – 3) algorithms specifically evaluated on Sudoku and map-coloring CSPs. 

Team Member Name: 
Paper: An Efficient Algorithm for Solving Sudoku Puzzles via Constraint Propagation
Full Citation: Takakan, Y., & Sterling, L. (2012). Declarative pearls: Sudoku as a constraint satisfaction problem. Journal of Functional Programming. 22(1), 1-15.
Venue: Cambridge University Press, Indexed in Scopus and Web of Science. 
Details specific constraint graph mappings for 9x9 Sudoku grids and evaluates the performance delta between pure backtracking and constraint propagation.

Team Member Name: 
Paper: Solving Nonograms through Constraint Satisfaction Techniques
Full Citation: Ueda, H., & Nagao, M. (1996). NP-completeness of the nonogram puzzle and efficient creation of quality puzzles. IPSJ SIG Notes, 96(91), 59-66.
Venue: Information Processing Society of Japan (IPSJ), Indexed in DBLP.
Provides the structural formulation for translating line-segment run-length constraints into line-consistency filtering algorithms for Nonograms. 

Team Member Name: 
Paper: Solving Nonograms by Combining Relaxations
Full Citation: Batenburg, K. J., & Kosters, W. A. (2009). Solving Nonograms by combining relaxations. Discrete Applied Mathematics, 157(6), 1157-1170.
Venue: Elsevier, Indexed in Scopus, ScienceDirect, and Web of Science.
Explores advanced constraint propagation frameworks combining discrete tomography relaxations with arc-consistency methods specifically for pixel-based Nonogram grids. 

Data and environment/hardware 
	No external training datasets or machine learning corpus is required for this project. Our solutions are produced entirely algorithmically via search and propagation over benchmark puzzle strings and files. Standard benchmark puzzle test suites (ranging from “easy to “evil” difficulty Sudokus and 5x5 to 15x15 Nonograms) will be curated from public puzzle repositories by Sylvester Reyes by November 1. Local Hardware and environments will be personal development laptops, desktops and/or other devices and limited to device hardware (e.g., Intel Core i5 processors and 16GB RAM). Software Stack includes Python 3.14, Jupyter Notebooks, and custom-built CSP solver classes utilizing Git for version control. 
