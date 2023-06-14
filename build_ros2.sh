#!/bin/bash
pwd
cd ../WA-DED-ROS2-ws
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
