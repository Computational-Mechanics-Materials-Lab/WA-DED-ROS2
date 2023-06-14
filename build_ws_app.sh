#!/bin/bash

# Build Workspace
cd ..
mkdir WA-DED-ROS2-ws
cd WA-DED-ROS2-ws
mkdir src
cd src

# Clone github Repositories into src
git clone https://github.com/evocortex/optris_drivers2.git
git clone https://github.com/PickNikRobotics/abb_ros2.git

# Copy Optris Calibration and ABB End Effector to src


# Build Apptainer
cd ../..
mkdir ros2_container
cd ros2_container
pwd
module load apptainer/1.0.2
sudo apptainer build --sandbox ros2_container.image ../WA-DED-ROS2/ros2-container.def
pwd
# Build ROS2 Packages
apptainer exec --nv -B /run ../ros2_container/ros2_container.image ../WA-DED-ROS2/build_ros2.sh