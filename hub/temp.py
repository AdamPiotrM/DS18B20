import time
import machine
import onewire, ds18x20

# the device is on GPIO16
dat = machine.Pin(16) #placeholder, to be changed to read from config file

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))


# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

sensor_id = hex(int.from_bytes(b'(\xabG8N \x01\x0c', 'little'))


# loop 10 times and print all temperatures
for i in range(10):
    ds.convert_temp()
    time.sleep_ms(750) #placeholder, to be changed to read from config file
    for rom in roms:
        print(sensor_id, ds.read_temp(rom * 1000), end=' ') # Needs some testing
    print()