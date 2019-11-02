version="2.4"
echo "Installing OpenCV" $version

echo "Removing any pre-installed ffmpeg and x264"
echo "sudo apt-get remove x264 libx264-dev"

echo "***********************************"
echo "Installing Dependenices"

sudo apt-get -y install libopencv-dev

echo "************Build Tools***********************"
echo "<----------------------------------------------------Build Tools------------------------------------------------->"
sudo apt-get -y install build-essential pkg-config git checkinstall 
echo "*_*_*_*_*_*_*_*_*_*_*_*_*_*"

echo "<------------------------------------------------------Image I/O----------------------------------------------------->"
sudo apt-get -y install libtiff5-dev libjpeg-dev libjasper-dev libpng12-dev zliblg-dev libwebp-dev libopenexr-dev libgdal-dev  libdc1394-22-dev
echo "***********************************"

echo "<--------------------------------------------------------Video I/O--------------------------------------------------->"
sudo apt-get -y install libavcodec-dev libavformat-dev libmp3lame-dev libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev
sudo apt-get -y install libv4l-dev v4l-utils libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev x264 yasm
echo "***********************************"

echo "Parallelism and linear algebra libraries"
sudo apt-get -y install libtbb-dev libeigen3-dev libtbb2
echo "***********************************"

echo "<------------------------------------------------for GUI------------------------------------------------->"
sudo apt-get -y install libqt4-dev libgtk2.0-dev qt5-default libvtk6-dev
echo "*************************************************************************************************************"

echo "<--------------For JAVA-------------------->"
sudo apt-get -y install ant default-jdk

echo "<-------********------For Python------********-------->"
sudo apt-get -y install python-dev python-tk python-numpy python3-dev python3-tk python3-numpy python-matplotlib python-opencv
echo "%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%_%"


echo "Downloading OpenCV" $version
sleep 10
git clone -b 2.4 --single-branch https://github.com/Itseez/opencv.git
sleep 10

cd opencv/
mkdir build
cd build
echo "*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_"
cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D WITH_TBB=ON \
	-D BUILD_NEW_PYTHON_SUPPORT=ON \
	-D WITH_V4L=ON \
  	-D BUILD_opencv_java=ON \
	-D INSTALL_C_EXAMPLES=ON \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D BUILD_DOCS=ON \
	-D BUILD_EXAMPLES=ON \
	-D WITH_QT=ON \
	-D WITH_OPENGL=ON \
	-D WITH_EIGEN=ON ..


echo "************  CMAKE  **************"
make -j4 
echo "************make end**************"
sleep 10	

echo "***********************************"
sudo make install
echo "***********************************"

sudo sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
echo "***********************************"

sudo ldconfig
echo "OpenCV" $version "ready to be used"