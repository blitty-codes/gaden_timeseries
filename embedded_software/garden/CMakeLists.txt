cmake_minimum_required(VERSION 3.25)

include(pico_sdk_import.cmake)

project(GARDEEN)

pico_sdk_init()

add_subdirectory(app)
add_subdirectory(freertos)
