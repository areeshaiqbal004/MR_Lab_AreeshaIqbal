# Week 5 Commands: TurtleBot3 SLAM, RViz, Rosbag, and Custom Nodes

## Setup

Run in every new terminal:

```bash
source /opt/ros/humble/setup.bash
source /usr/share/gazebo/setup.sh
export TURTLEBOT3_MODEL=burger
```

From the workspace:

```bash
cd "/home/bilal41/mr labs/MR_Lab"
colcon build
source install/setup.bash
```

## Launch TurtleBot3 in Gazebo

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

## Teleoperate the Robot

Open a new terminal:

```bash
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 run turtlebot3_teleop teleop_keyboard
```

Useful keys:

```text
w: forward
x: backward
a: turn left
d: turn right
q: increase speed
z: decrease speed
s: stop forcefully
```

## Launch Cartographer SLAM and RViz

Open a new terminal:

```bash
source /opt/ros/humble/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=true
```

In RViz, enable or add these displays:

```text
TF
Odometry
LaserScan
Map
Path
```

Useful topics:

```text
/scan
/odom
/map
/tf
/tf_static
/cmd_vel
```

## Check Topic and Message Types

```bash
ros2 topic list
ros2 topic info /odom
ros2 interface show nav_msgs/msg/Odometry
ros2 topic echo /odom
```

The `/odom` topic uses:

```text
nav_msgs/msg/Odometry
```

## Record All Topics with Rosbag

Create a folder and record all active topics:

```bash
mkdir -p src/week5/rosbag_recordings
ros2 bag record -a -o src/week5/rosbag_recordings/week5_motion_bag
```

Stop recording:

```text
Ctrl + C
```

Replay the bag:

```bash
ros2 bag play src/week5/rosbag_recordings/week5_motion_bag
```

Check bag information:

```bash
ros2 bag info src/week5/rosbag_recordings/week5_motion_bag
```

## Save the SLAM Map

After moving the robot and building a map:

```bash
mkdir -p src/week5/maps
ros2 run nav2_map_server map_saver_cli -f src/week5/maps/my_map
```

Expected output files:

```text
src/week5/maps/my_map.pgm
src/week5/maps/my_map.yaml
```

## Run rqt_graph

```bash
rqt_graph
```

If RQT crashes because of NumPy/Matplotlib:

```bash
PYTHONNOUSERSITE=1 rqt_graph
```

## Run Custom Velocity Publisher

This node publishes forward velocity and zero velocity every 2 seconds to `/cmd_vel`.

```bash
ros2 run my_lab5_slam cmd_pub
```

Expected behavior:

```text
Moving Forward
Stopping
Moving Forward
Stopping
```

## Run Custom Odometry Subscriber

This node subscribes to `/odom` and prints the robot position.

```bash
ros2 run my_lab5_slam odom_sub
```

Expected output:

```text
[INFO] [odom_subscriber]: X: ..., Y: ...
```

## Return Robot Near Origin

Use teleop to drive the robot back close to:

```text
x = 0
y = 0
theta = 0
```

Monitor with:

```bash
ros2 topic echo /odom
```

