#include <stdio.h>

#include <FreeRTOS.h>
#include <task.h>
#include <queue.h>

#include "pico/stdlib.h"

#define RED_LED 2

static QueueHandle_t xQueue = NULL;

void task1(void *param)
{   
    while (true) {
        printf("Task 1 is currently running\n");
        for (int i = 0; i < 20000000; i++);
    }
}

void task2(void *param)
{   
    while (true) {
        printf("Task 2 is currently running\n");
        // for (int i = 0; i < 20000000; i++);
        vTaskDelay(1000);
    }
}

int main()
{
    stdio_init_all();

    xQueue = xQueueCreate(1, sizeof(uint));

    xTaskCreate(task1, "task1", 256, NULL, 1, NULL);
    xTaskCreate(task2, "task2", 256, NULL, 2, NULL);
    vTaskStartScheduler();

    while(1){};
}