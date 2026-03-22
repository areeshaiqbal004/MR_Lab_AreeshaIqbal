import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/areesha/ros2_ws_areesha/src/install/my_first_pkg'
