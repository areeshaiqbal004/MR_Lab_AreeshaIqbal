                                     Week 1 – ROS 2 Lab

1. Brief Description of Week 1 Lab

In this lab, I learned the basic workflow of ROS 2 and how to set up a development environment. The main objective was to create a ROS 2 workspace, build it using colcon, and develop a simple Python package containing a ROS node. The node was implemented to print a log message when executed. I also learned basic Linux terminal commands required for ROS development. Finally, I successfully ran the node using the ros2 run command and verified that the package was correctly detected by ROS 2.

2. Commands Used

The following commands were used during the lab:

ros2 --version
source /opt/ros/humble/setup.bash

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source install/setup.bash

cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python my_first_pkg

cd ~/ros2_ws
colcon build
source install/setup.bash

ros2 pkg list | grep my_first_pkg

chmod +x ~/ros2_ws/src/my_first_pkg/my_first_pkg/simple_node.py

ros2 run my_first_pkg simple_node

3. Problems Faced and Solutions

Problem 1: ros2: command not found
Solution: The ROS 2 environment was not sourced. I fixed it by running:
              source /opt/ros/humble/setup.bash

Problem 2: Package my_first_pkg not found.
Solution: The workspace was not sourced after building. I rebuilt the workspace and sourced it again:
              colcon build
              source install/setup.bash
              
Problem 3: Executable not found when running the node.
Solution: I checked the entry_points section in setup.py and rebuilt the workspace.

4. Reflection

This lab helped me understand the basic workflow of ROS 2 development. I learned how to create and organize a ROS workspace and how packages are structured. Writing and running my first ROS node helped me understand how ROS executes programs using packages and executables. I also practiced several Linux terminal commands that are important for working with ROS. Troubleshooting issues such as environment sourcing and build errors improved my debugging skills. Overall, this lab provided foundation for future ROS development and robotics programming.
