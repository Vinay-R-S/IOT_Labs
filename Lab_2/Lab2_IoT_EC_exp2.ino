// Lab 2: Exp 2: Three tasks each of them are running once in 1, 2 and 3 seconds respectively
// and prints incremented values

// #include "freertos/task.h"

#define LED_ESP32_BUILTIN 2

int task1Param = 0x1111;
int task2Param = 0x2222;
int task3Param = 0x3333;

void task1(void *task1Param)
{
  int task1Cnt = 1;

  Serial.printf("Entered task1 with the parameter %X\n", *(int *)task1Param);

  while (1)
  {
    delay(1000); // sleep for 1 second
    Serial.printf("Task1: task1Cnt = %d\n", task1Cnt);
    task1Cnt++;
  }
}

void task2(void *task2Param)
{
  int task2Cnt = 1;

  Serial.printf("Entered task2 with the parameter %X\n", *(int *)task2Param);

  while (1)
  {
    delay(2000); // sleep for 2 seconds
    Serial.printf("Task2: task2Cnt = %d\n", task2Cnt);
    task2Cnt++;
  }
}

void task3(void *task3Param)
{
  int task3Cnt = 1;

  Serial.printf("Entered task3 with the parameter %X\n", *(int *)task3Param);

  while (1)
  {
    delay(3000); // sleep for 3 seconds
    Serial.printf("Task3: task3Cnt = %d\n", task3Cnt);
    task3Cnt++;
  }
}

TaskHandle_t task1Handle;
TaskHandle_t task2Handle;
TaskHandle_t task3Handle;

eTaskState task1State;

void setup()
{
  // put your setup code here, to run once:
  static int cpuID_0 = 0;

  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_ESP32_BUILTIN, OUTPUT);
  // initialize serial communication at 115200 bits per second:
  Serial.begin(115200);

  // This task1 is created while this is code is running on Core 1 and the created task runs on Core 0
  xTaskCreate(
      task1,               /* Task function which runs on Core 0*/
      "Task1",             /* String with name of task. */
      10000,               /* Stack size in words. */
      (void *)&task1Param, /* Parameter passed as input of the task */
      2,                   /* Priority of the task. */
      &task1Handle);       /* Task handle. */

  // This task2 is created while this is code is running on Core 1 and the created task runs on Core 0
  xTaskCreate(
      task2,               /* Task function which runs on Core 0*/
      "Task2",             /* String with name of task. */
      10000,               /* Stack size in words. */
      (void *)&task2Param, /* Parameter passed as input of the task */
      2,                   /* Priority of the task. */
      &task2Handle);       /* Task handle. */

  // This task3 is created while this is code is running on Core 1 and the created task runs on Core 0
  xTaskCreate(
      task3,               /* Task function which runs on Core 0*/
      "Task3",             /* String with name of task. */
      10000,               /* Stack size in words. */
      (void *)&task3Param, /* Parameter passed as input of the task */
      2,                   /* Priority of the task. */
      &task3Handle);       /* Task handle. */
}

void loop()
{
  // put your main code here, to run repeatedly:

  digitalWrite(LED_ESP32_BUILTIN, HIGH); // turn the LED on (HIGH is the voltage level)
  delay(1000);                           // wait for 2 Secs
  digitalWrite(LED_ESP32_BUILTIN, LOW);  // turn the LED off by making the voltage LOW
  delay(1000);

  Serial.printf("Number of tasks in the system: %d\n", uxTaskGetNumberOfTasks());
  task1State = eTaskGetState(task1Handle);
  Serial.printf("State of task1: %d\n", task1State);

  Serial.println("Printing the task names ...");
  Serial.printf("Name of the task1 is %s\n", pcTaskGetTaskName(task1Handle));
  Serial.printf("Name of the task2 is %s\n", pcTaskGetTaskName(task2Handle));
  Serial.printf("Name of the task3 is %s\n", pcTaskGetTaskName(task3Handle));
}
