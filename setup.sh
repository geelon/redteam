#!/bin/bash

CURR_PATH=$(pwd)
# download boost
if [ ! -d boost_1_69_0 ]; then
    wget https://dl.bintray.com/boostorg/release/1.69.0/source/boost_1_69_0.tar.bz2
    tar --bzip2 -xf boost_1_69_0.tar.bz2
fi
BOOST_PATH=$CURR_PATH/boost_1_69_0

# install he-transformer
if [ ! -d "he-transformer"]; then
    git clone https://github.com/NervanaSystems/he-transformer.git
fi

cd he-transformer
export HE_TRANSFORMER=$(pwd)
mkdir build
cd $HE_TRANSFORMER/build
cmake .. -DBOOST_ROOT=$BOOST_PATH
make install
source external/venv-tf-py3/bin/activate

cd $CURR_PATH


