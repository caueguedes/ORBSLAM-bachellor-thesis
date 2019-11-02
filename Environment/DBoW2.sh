echo "###################################################"
echo "----------------INSTALLING DBoW2------------------"
sleep 4

echo "---------------Clonning from git -----------------"
cd ~
git clone https://github.com/dorian3d/DBoW2.git
cd DBoW2/
echo "**************************************************"

echo "--------------------CMAKE -----------------------"
mkdir build
cd build 
cmake .. -DCMAKE_BUILD_TYPE=Release

echo "---------------------MAKE-------------------------"
make -j 4
echo "***************Installation concluded*************"
