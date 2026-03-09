                                      Post Lab Questions
                                      
Q#1:Define: node, topic, package, workspace. Provide one sentence each.

A#1:Node:A node is a program in ROS2 that performs a specific task such as publishing or subscribing to data.
   Topic:A topic is a communication channel used by ROS2 nodes to send and receive messages.
   Package:A package is a directory that contains ROS2 nodes, libraries, configuration files, and other resources.
   Workspace:A workspace is a directory where multiple ROS2 packages are developed, built, and managed together.

Q#2:Explain why sourcing is required. What happens if you do not source a workspace?

A#2:Sourcing a workspace sets up environment variables so the system can find ROS2 packages and executables.  
If you do not source a workspace, ROS2 will not recognize your packages and commands like `ros2 run` will fail.

Q#3:What is the purpose of colcon build? What folders does it generate?

A#3:`colcon build` compiles and builds all packages inside a ROS2 workspace.  
It generates the following folders:

- **build/** – contains build files
- **install/** – contains installed packages and executables
- **log/** – contains build logs

Q#4:In your own words, explain what the entry_points console script does in setup.py.

A#4:The `entry_points` console script in `setup.py` creates a command that allows ROS2 to run a Python node using `ros2 run` instead of executing the Python file manually.

Q#5:Draw (by hand or ASCII) a diagram showing one publisher and one subscriber connected
by a topic.

A#5:The diagram for Question 5 is provided as a JPEG image file (Diagram.jpeg) located in this folder

