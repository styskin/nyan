#!/bin/bash

mkdir -p models
cd models
curl -L -O https://github.com/NyanNyanovich/nyan/releases/download/v0.1/nyan_models.tar.gz --output nyan_models.tar.gz
tar -xzvf nyan_models.tar.gz && rm nyan_models.tar.gz
