#!/bin/bash

mkdir -p models
curl -L -O https://github.com/NyanNyanovich/nyan/releases/download/v0.1/nyan_models.tar.gz --output models/nyan_models.tar.gz
cd models && tar -xzvf nyan_models.tar.gz && rm nyan_models.tar.gz
