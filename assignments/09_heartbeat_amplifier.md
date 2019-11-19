# Sketch #9: Heartbeat Amplifier

* Assemble an Arduino Nano microcontroller and pulse sensor
    * Plug Arduino into breadboard straddling the gap
    * Put clear sticker on flat side of pulse sensor
    * Put electrical tape on component side of pulse sensor
    * Connect ground, 5V, and A0 leads from pulse sensor to Arduino

* Program the Arduino
    * Download the [Arduino IDE](https://www.arduino.cc/en/main/software), unzip it, and copy the application to your Applications folder
    * Open the the Arduino IDE (On a mac, if you receive the note "Apple cannot check it for malicious software," try holding down the control-key and trying again)
    * Install any libraries suggested by the application
    * Under Tools, set the board to "Arduino Nano Every", and Registers Emulation to "None"
    * Write code and see data in Serial Plotter:
```c
int value;

void setup() {
  Serial.begin(9600);
}

void loop() {

  value = analogRead(0);
  Serial.println(value);

  delay(40);

}
```

* Add an LED
    * Connect a 220 ohm resistor from D12 to a new breadboard row
    * Connect an LED from the resistor to the ground rail
    * Connect the ground rail to ground
    * Modify code:

In `setup`:
```c
  pinMode(12, OUTPUT);
```

In `loop`:
```c
  if (value > 530) {
    digitalWrite(12, HIGH);
  } else {
    digitalWrite(12, LOW);
  }
 ```

* Communicate with P5
    * Download the [p5.serialcontrol](https://github.com/p5-serial/p5.serialcontrol/releases) app (make sure Serial Plotter is closed in the Arduino IDE)
    * Download this [p5 template](09_heartbeat_amplifier.zip)
    * Modify the serial port
    * Customize your heartbeat input

