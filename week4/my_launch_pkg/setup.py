from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_launch_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Improved path joining and globbing for launch files 
        (os.path.join('share', package_name, 'launch'), 
            glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='areesha',
    maintainer_email='areesha.iqbal004@gmail.com',
    description='Launch package for turtlesim',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Matches the command: ros2 run my_launch_pkg follower_node
            'follower_node = my_launch_pkg.turtle_follower:main',
        ],
    },
)
