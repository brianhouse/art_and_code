# Sketch #9: Heartbeat Amplifier

1. Assemble an Arduino Nano microcontroller and pulse sensor
    1. Plug Arduino into breadboard straddling the gap
    1. Put clear sticker on flat side of pulse sensor
    1. Put electrical tape on component side of pulse sensor
    1. Connect ground, 5V, and A0 leads from pulse sensor to Arduino

1. Program the Arduino
    1. Download the [Arduino IDE](https://www.arduino.cc/en/main/software), unzip it, and copy the application to your Applications folder
    1. Open the the Arduino IDE (On a mac, if you receive the note "Apple cannot check it for malicious software," try holding down the control-key and trying again)
    1. Install any libraries suggested by the application
    1. Under Tools, set the board to "Arduino Nano Every", and Registers Emulation to "None"
    1. Write code and see data in Serial Plotter:
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

1. Add an LED
    1. Connect a 221.ohm resistor from D12 to a new breadboard row
    1. Connect an LED from the resistor to the ground rail
    1. Connect the ground rail to ground
    1. Modify code:

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

1. Communicate with P5
    1. Download the [p5.serialcontrol](https://github.com/p5-serial/p5.serialcontrol/releases) app (make sure Serial Plotter is closed in the Arduino IDE)
    1. Download this [p5 template](1._heartbeat_amplifer.zip)
    1. Modify the serial port
    1. Customize your heartbeat input

