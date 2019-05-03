#!/bin/bash

git clone https://github.com/NervanaSystems/he-transformer.git

cd he-transformer
export HE_TRANSFORMER=$(pwd)
mkdir build
cd $HE_TRANSFORMER/build
cmake .. [-DCMAKE_CXX_COMPILER=g++-7 -DCMAKE_C_COMPILER=gcc-7]
make install
source external/venv-tf-py3/bin/activate
