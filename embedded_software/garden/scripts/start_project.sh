sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi libstdc++-arm-none-eabi-newlib

# raspberry pi pico C/C++ SDK
git clone https://github.com/raspberrypi/pico-sdk.git
cd pico-sdk && git submodule update --init && cd ..

# Free RTOS Kernel
mkdir freertos && cd freertos
git clone https://github.com/FreeRTOS/FreeRTOS-Kernel.git
cd ..

mkdir -p app
cp pico-sdk/external/pico_sdk_import.cmake .
