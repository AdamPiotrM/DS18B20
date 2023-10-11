# Simple Temperature reader        

BOM-list can be found under [hub](https://github.com/AdamPiotrM/Simple-Temperature-reader/blob/main/hub/requirements.txt).

You can change settings like changing refresh rate or the output PIN used by making changes in config file.

Before you upload the code to the device there's few things you have to do:
1. Connect the sensor's voltage input to 3.3V output on your Pico
2. Connect the signal output from sensor to resistor and then to signal input on your device
3. Ground the circuit (by connecting ground on device to ground on sensor)

After that you have to connect your Pico to your PC via microUSB-to-USB cable. In device manager check which COM port is being used by PICO.

Then you have to flash your device by using ```mpremote reset``` command in CMD and they you are free to put the code into your device by using your choice of IDE, I personally used Thonny IDE.

Double check if you are choosing right COM port before you send the code to PICO. After that you just run the file (either by using "Run" option on your IDE or using ```import main.py``` in command prompt) and you are done.
