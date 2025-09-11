#define LED_ESP32_BUILTIN 2

// Lab 2: Experiment 1

int param1 = 1000;
int param2 = 2000;
int param3 = 3000;

// the setup function runs once when you press reset or power the board
void setup()
{
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_ESP32_BUILTIN, OUTPUT);
  // initialize serial communication at 115200 bits per second:
  Serial.begin(115200);

  Serial.print("Setup: Executing on core ");
  Serial.println(xPortGetCoreID());

  xTaskCreate(
      genericTask,     /* Task function. */
      "genericTask",   /* String with name of task. */
      10000,           /* Stack size in words. */
      (void *)&param1, /* Parameter passed as input of the task */
      2,               /* Priority of the task. */
      NULL);           /* Task handle. */
  delay(2000);

  xTaskCreatePinnedToCore(
      genericTask,     /* Task function. */
      "Task_on_core0", /* String with name of task. */
      10000,           /* Stack size in words. */
      (void *)&param2, /* Parameter passed as input of the task */
      2,               /* Priority of the task. */
      NULL,            /* Task handle. */
      0);              /* Core ID = 1*/
  delay(2000);

  xTaskCreatePinnedToCore(
      genericTask,     /* Task function. */
      "Task_on_core1", /* String with name of task. */
      10000,           /* Stack size in words. */
      (void *)&param3, /* Parameter passed as input of the task */
      2,               /* Priority of the task. */
      NULL,            /* Task handle. */
      1);              /* Core ID = 1*/
  delay(2000);
}

// the loop function runs over and over again forever
void loop()
{
  Serial.printf("This loop() function is running on the core ID: %d\n", xPortGetCoreID());

  digitalWrite(LED_ESP32_BUILTIN, HIGH); // turn the LED on (HIGH is the voltage level)
  delay(2000);                           // wait for millisecond
  digitalWrite(LED_ESP32_BUILTIN, LOW);  // turn the LED off by making the voltage LOW
  delay(2000);                           // wait for 500 millisecond
}

void genericTask(void *parameter)
{
  const char *taskName = pcTaskGetName(NULL);

  Serial.printf("Created the task: Executing genericTask() on the core %d\n", xPortGetCoreID());

  while (1)
  {
    delay(2000);
    Serial.printf("Task Name: %s\n", taskName);
    Serial.printf("This task genericTask() is running on the core %d\n", xPortGetCoreID());
    Serial.printf("Parameter passed to it on creation was %d\n", *(int *)parameter);
  }

  Serial.println("If the control comes here ... This task is going to be deleted now!!! ... Bye Bye ...");
  vTaskDelete(NULL);
}
