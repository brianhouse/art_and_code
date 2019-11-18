# Sketch #9: Heartbeat Amplifier

* Assemble an Arduino Nano microcontroller and pulse sensor
    0. Plug Arduino into breadboard straddling the gap
    0. Put clear sticker on flat side of pulse sensor
    0. Put electrical tape on component side of pulse sensor
    0. Connect ground, 5V, and A0 leads from pulsesensor to Arduino

* Program the Arduino
	0. Download the [Arduino IDE](https://www.arduino.cc/en/main/software), unzip it, and copy the application to your Applications folder
	0. Open the the Arduino IDE (On a mac, if you receive the note "Apple cannot check it for malicious software," try holding down the control-key and trying again)
	0. Install any libraries suggested by the application
	0. Under Tools, set the board to "Arduino Nano Every", and Registers Emulation to "None"
	0. Write code and see data in Serial Plotter:
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
	0. Connect a 220 ohm resistor from D12 to a new breadboard row
	0. Connect an LED from the resistor to the ground rail
	0. Connect the ground rail to ground
	0. Modify code:

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

	0. Download the [p5.serialcontrol](https://github.com/p5-serial/p5.serialcontrol/releases) app (make sure Serial Plotter is closed in the Arduino IDE)
	0. Download this [p5 template](09_heartbeat_amplifer.zip)
	0. Modify the serial port
	0. Customize your heartbeat input

