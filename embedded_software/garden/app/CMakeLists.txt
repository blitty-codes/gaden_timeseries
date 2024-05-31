set(PROJECT_NAME "GARDEEN")
set(VERSION_NUMBER "1.0.0")
set(BUILD_NUMBER "1")

add_compile_definitions(APP_NAME="${PROJECT_NAME}")
add_compile_definitions(APP_VERSION="${VERSION_NUMBER}")
add_compile_definitions(BUILD_NUM=${BUILD_NUMBER})

add_executable(${PROJECT_NAME}
    main.c
)

target_link_libraries(${PROJECT_NAME}
    pico_stdlib
    freertos
)

pico_enable_stdio_usb(${PROJECT_NAME} 1)
pico_enable_stdio_uart(${PROJECT_NAME} 0)

pico_add_extra_outputs(${PROJECT_NAME})
