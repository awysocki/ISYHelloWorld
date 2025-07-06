#!/bin/bash
# Install script for Hello World NodeServer

echo "Installing Hello World NodeServer..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "Installation completed successfully!"
else
    echo "Installation failed"
    exit 1
fi
