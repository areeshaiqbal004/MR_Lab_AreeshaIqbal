# Week 5: TurtleBot3 Simulation, RViz, SLAM, and Custom Nodes

## Aim

This lab used TurtleBot3 in Gazebo and RViz to study robot simulation, sensor visualization, odometry, rosbag recording, and SLAM mapping. I also created `my_lab5_slam`, which includes a `/cmd_vel` publisher and an `/odom` subscriber.

## Setup

```bash
cd "/home/bilal41/mr labs/MR_Lab"
source /opt/ros/humble/setup.bash
source /usr/share/gazebo/setup.sh
export TURTLEBOT3_MODEL=burger
colcon build --packages-select my_lab5_slam
source install/setup.bash
```

## Gazebo

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

## Teleoperation

```bash
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
s: stop
```

## SLAM and RViz

```bash
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=true
```

In RViz, useful displays include `TF`, `LaserScan`, `Odometry`, `Map`, and `Path`.

## Record Bag

```bash
mkdir -p src/week5/rosbag_recordings
ros2 bag record -a -o src/week5/rosbag_recordings/week5_motion_bag
```

## Save Map

```bash
mkdir -p src/week5/maps
ros2 run nav2_map_server map_saver_cli -f src/week5/maps/my_map
```

## Custom Nodes

Publisher:

```bash
ros2 run my_lab5_slam cmd_pub
```

Subscriber:

```bash
ros2 run my_lab5_slam odom_sub
```

## Result

The robot was simulated in Gazebo, visualized in RViz, and used to generate a SLAM map. The custom publisher and subscriber demonstrated direct topic communication with `/cmd_vel` and `/odom`.
