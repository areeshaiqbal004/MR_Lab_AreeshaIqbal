from setuptools import setup

package_name = 'week3_turtle_package_circular'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='areesha',
    maintainer_email='areesha.iqbal004@gmail.com',
    description='Week 3 turtle package circular task',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'circle_turtle = week3_turtle_package_circular.circle_turtle:main',
        'triangle_turtle = week3_turtle_package_circular.triangle_turtle:main',
    ],
},
)
