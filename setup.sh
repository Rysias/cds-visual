#!/usr/bin/env bash

pip install --upgrade pip

# Copy notebook
python copy_notebook.py
pip install opencv-python scikit-learn tensorflow tensorboard pydot
sudo apt-get -y install graphviz
