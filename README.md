# dexhand_description
ROS 2 URDF and Visualization for DexHand V2

<img width="800" alt="Screenshot 2024-05-29 at 4 10 20 PM" src="https://github.com/iotdesignshop/dexhandv2_description/assets/2821763/858f8d88-bcbe-4b03-9915-61f791f2611a">


## Overview
The DexHand V2 is a dexterous humanoid robot hand that is designed for research and development activity
involving dexterous manipulation in the physical world. THe project homepage can be found at http://www.dexhand.com.

This package provides:
- URDF for the DexHand V2 robot hand
- RVIZ2 configuration for visualizing the hand with support for the ROS 2 Joint State Publisher GUI
- Launch files to make it easy to visualize the DexHand V2 in RVIZ2

### Models Provided

The package currently provides two variants of URDF/XACRO files for the DexHand V2:

- __dexhand_right.urdf__ - Just the palm and finger joints for the DexHand. Suitable for grafting onto other models.
- __dexhand_cobot_right.urdf__ - The V2 DexHand with Cobot Forearm (This is the default model used in RVIZ, etc. in the package)

## Setup

### Assumptions
Use of this package assumes that you have a functional ROS 2 installation, and are familiar with the procedures for setting up workspaces, building packages, and running the ROS 2 command line tools. If not, there are [excellent tutorials available on the ROS 2 distribution pages](https://docs.ros.org/en/humble/Tutorials.html). We used [ROS 2 Humble Hawksbill](https://docs.ros.org/en/humble/index.html) for developing and testing this package, but it's generic enough that it should run fine with whatever version of ROS 2 you have installed.

### Setup Process
Setting up the package is like any other ROS 2 package you would build from source:

1) __Clone the GitHub Project__ into a ROS 2 workspace.

   (From the src folder of your workspace - for example: /dexhand_ws/src)

   `git clone https://github.com/iotdesignshop/dexhandv2_description.git`

2) __Run rosdep__ to make sure you have all the dependencies.

   (From the root of your workspace - for example: /dexhand_ws)

   `rosdep install -i --from-path src --rosdistro humble -y`

   **Note: If you are using a distribution other than humble, change the parameter accordingly**

3) __Run colcon__ to build the package

   (From the root of your workspace - for example: /dexhand_ws)

   `colcon build`

4) __Source the environment__ for the workspace

   (Usually a good idea to do this in a fresh terminal window, and from the root of your workspace)

   `source install/setup.bash`
   
     
## Usage

Once you have the package built, you can use the included ROS 2 launchfile to start RVIZ2 and show the Joint State Publisher GUI:

`ros2 launch dexhandv2_description display.launch.py`

This should open the RVIZ2 window and display the hand along with the GUI which you can use to test the motion of all the joints


