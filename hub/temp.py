import time
import machine
import onewire, ds18x20
import json

with open("config.json", "r") as file:
    pin = file[Pin]
    RR = file["interval"] # RR = Refresh Rate

#dat = machine.Pin(16) #placeholder, to be changed to read from config file
dat = machine.Pin(pin)

# create the onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))


# scan for devices on the bus
roms = ds.scan()
print('found devices:', roms)

# gets sensor and device id's and translates them into hex
sensor_id = hex(int.from_bytes(b'(\xabG8N \x01\x0c', 'little'))
device_id = hex(int.from_bytes(b'(\xe6ad\x08C% &)', 'little'))



#placeholder if json doesn't work
#while True:
#    ds.convert_temp()
#    time.sleep_ms(750)
#    for rom in roms:
#        print( device_id, sensor_id, ds.read_temp(rom), end='\n') # Needs some testing


#prints while powered
while True:
    ds.convert_temp()
    time.sleep_ms(RR) 
    for rom in roms:
       print( device_id, sensor_id, ds.read_temp(rom), end='\n') 