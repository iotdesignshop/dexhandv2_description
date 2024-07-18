from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'dexhandv2_description'

setup(
    name=package_name,
    version='0.0.2',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*')),
        (os.path.join('share', package_name, 'meshes/right'), glob('meshes/right/*')),
        (os.path.join('share', package_name, 'meshes/cobot_right'), glob('meshes/cobot_right/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Trent Shumay',
    maintainer_email='trent@iotdesignshop.com',
    description='ROS 2 description package for DexHand v2',
    license='CC BY-NC-SA 4.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
