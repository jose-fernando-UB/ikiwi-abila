Industrial Cleaning Robot Prototype

Dependencies:

Ubuntu 18.04 ROS Melodic: http://wiki.ros.org/melodic/Installation/Ubuntu Gazebo (Tested on 9): http://gazebosim.org/tutorials?tut=install_ubuntu

ROS Dependencies: Gmapping, TEB Local Planner, Navigation, Python rospkg, Realsense

 $ sudo apt install ros-melodic-gmapping
 $ sudo apt-get install ros-melodic-teb-local-planner
 $ sudo apt-get install ros-melodic-navigation
 $ sudo apt-get install ros-melodic-rtabmap-ros
 $ sudo apt-get install ros-melodic-realsense2-camera
 $ pip3 install rospkg
Installation Instructions:

Once dependencies have been installed,

 $ cd catkin_ws/src
 $ git clone https://github.com/jose-fernando-UB/ikiwi-abila-ws
 $ cd ..
 $ rosdep install --from-paths src --ignore-src -r -y
 $ catkin_make
Simulation Instructions:

From different terminals:

For Teleoperation Simulation (with keyboard)

   $ roslaunch ikiwi_abila_gazebo ikiwi_abila_42.launch  (opens Gazebo and turtlebot3 house world and sets up robot state publisher)
   $ roslaunch ikiwi_abila_slam ikiwi_abila_slam.launch        (optional, starts slam node)
   $ roslaunch ikwiwi_abila_teleop_key                         (for keyboard navigation)
To create a map using slam:

   $ roslaunch ikiwi_abila_bringup ikiwi_abila_core.launch
   $ roslaunch ikiwi_abila_gmapping.launch
   $ roslaunch ikiwi_abila_mapping.launch
To run the navigation scripts (with a pgm file of a map):

   $ python nodeSelection.py                                          (to select points on the pgm map file in the desired order)
   $ python waypointCreation.py                                       (to generate the intermediate points, and all of the poses)
   $ roslaunch ikiwi_abila_gazebo ikiwi_abila_42_house.launch         (or similar gazebo launch file)
   $ roslaunch ikiwi_abila_navigation ikiwi_abila_navigation.launch   (or similar navigation launch file with reference to pgm map)
   $ python navigateToGoals.py                                        (sends goals to TEB local planner)
