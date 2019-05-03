#!/bin/bash

git clone https://github.com/NervanaSystems/he-transformer.git

cd he-transformer
export HE_TRANSFORMER=$(pwd)
mkdir build
cd $HE_TRANSFORMER/build
cmake .. 
make install
source external/venv-tf-py3/bin/activate
