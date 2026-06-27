# Week 5 Short Report

## Steps Performed

1. Launched TurtleBot3 in Gazebo.
2. Controlled the robot using keyboard teleoperation.
3. Opened Cartographer SLAM in RViz.
4. Observed LiDAR, odometry, map, TF, and path data.
5. Recorded all topics with `ros2 bag record -a`.
6. Saved a generated map using `map_saver_cli`.
7. Ran a custom velocity publisher.
8. Ran a custom odometry subscriber.

## Custom Publisher

The publisher alternates between forward motion and stopping every two seconds.

```python
self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
self.timer = self.create_timer(2.0, self.timer_callback)
```

Expected output:

```text
Moving Forward
Stopping
```

## Custom Subscriber

The subscriber listens to `/odom`, which uses:

```text
nav_msgs/msg/Odometry
```

It prints the robot's current x and y position from the odometry message.

## Observations

- LiDAR data updated continuously in RViz.
- Odometry values changed as the robot moved.
- The generated map improved as the robot explored more of the environment.
- Small drift and motion delay were visible, which is expected in simulation.

## Conclusion

This lab gave practical experience with Gazebo, RViz, SLAM, rosbag, and custom ROS 2 nodes. It also showed how simulation data can be recorded and reused for analysis.
