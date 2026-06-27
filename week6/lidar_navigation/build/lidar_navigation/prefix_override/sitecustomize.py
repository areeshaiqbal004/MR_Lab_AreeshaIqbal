import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/areesha/ros2_ws_areesha/src/lidar_navigation/install/lidar_navigation'
