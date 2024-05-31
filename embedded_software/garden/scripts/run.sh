#!/bin/bash

set -e

BIN_NAME="GARDEEN.uf2"

export PICO_SDK_PATH="$PWD/pico-sdk"
export FREERTOS_KERNEL_PATH="$PWD/FreeRTOS-Kernel"

mkdir -p build
cd build && cmake ..
make -j4
cd ..

# List the contents of /dev/ and filter for "sda"
if ls /dev/ | grep -q sda; then
    # mount pico
    sudo mkdir -p /mnt/pico
    sudo mount /dev/sda1 /mnt/pico
    ls /mnt/pico

    # copy binary to pico
    sudo cp "build/app/$BIN_NAME" /mnt/pico
    sudo sync

    ls /mnt/pico
    sudo umount /mnt/pico
    
    printf "Enter minicom? [S/n] : "
    read x

    if [[ "${x,,}" == "s" ]]; then
        sudo minicom -b 115200 -o -D /dev/ttyACM0
    fi
else
    echo "Device sda not found."
fi
