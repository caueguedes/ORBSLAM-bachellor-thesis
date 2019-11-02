echo "Install CMake3"
sudo apt-get -y install cmake3

echo "sudo apt update"
sudo apt update
sudo apt-get update

echo "Install libboost-all-dev"
sudo apt-get -y install libboost-all-dev

echo "##### Start ROS Indigo installation #####"
sleep 5

echo "Setup Source List"
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'


echo "Setup Keys"
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

echo "Update and install apt-get and dkpg"
sudo apt-get update && sudo apt-get -y install dpkg

echo "#### install ros ####"
sleep 3
sudo apt-get -y install ros-indigo-desktop-full

echo "### Init Rosdep ###"
sudo rosdep init
rosdep update

echo "Enviroment Setup"
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
source ~/.bashrc

echo "Install python rosdep"
sudo apt-get -y install python-rosinstall

echo "###### ENDED INSTALLATION ROS ######"
sleep 8