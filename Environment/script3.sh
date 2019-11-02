echo "######### INIT ORB_SLAM ###########"
echo "---------  ORB_SlAM  --------------"
sleep 5
echo "<--------------------Install Dependencies------------------------->"
sudo apt-get -y install libblas-dev liblapack-dev libeigen3-dev
echo "***********************************"

echo "<-------------------- CLONE ORB-SLAM ------------------------->"
cd ~
git clone https://github.com/raulmur/ORB_SLAM.git ORB_SLAM
echo "<---------------- Export path ------------------------>"
export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:~

echo "<******************** ENDED CLONING **************************>"

echo "############ THIRDPART INSTALLATION #############"
sleep 5

echo "<----------------------- INSTALL G2O ----------------------------->"
cd ~/ORB_SLAM/Thirdparty/g2o/
mkdir build
cd build/
echo "-------- CMAKE --------"
cmake .. -DCMAKE_BUILD_TYPE=Release
echo "-------- Make  --------"
make -j4
echo "***********************************"
sleep 5


echo "<----------------------- INSTALL DBoW2 ---------------------------->"
cd ~/ORB_SLAM/Thirdparty/DBoW2/
mkdir build
echo "-------- CMAKE --------"
cd build/
echo "-------- Make  --------"
make -j4
echo "***********************************"

echo "#############################################################################"
echo "# If you use ROS Indigo, remove the depency of opencv2 in the manifest.xml. #"
echo "# If you use ROS Indigo, remove the depency of opencv2 in the manifest.xml. #"
echo "#############################################################################"


