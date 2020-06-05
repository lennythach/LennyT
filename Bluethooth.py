#Class Libraries for the bluetooth application

import time #<--Class library is a 1st party module

from bluetooth.ble import BeaconService #<--beacon service is a third party module

#obstantiating the object
service = BeaconService() #<--Creating an instance object of the class library

service.start_advertising("11111111-2222-3333-4444-5555555555555",1,1,1, 200)#<--adding a uuid < advertise the uuid and different ports for spoofing device
#everytime 15 sec you want to spoof a device
time.sleep(15)
service.stop_advertise()

print("Done.")

















