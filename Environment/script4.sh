echo "------------ MAKE ORB_SLAM ------------"
sleep 5
echo "------------ Install ORB_SLAM ------------"
cd ~/ORB_SLAM/
mkdir build
cd build
cmake .. -DROS_BUILD_TYPE=Release
make -j4
echo "*****************************************************"
sleep 5