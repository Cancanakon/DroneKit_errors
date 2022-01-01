from PyQt5.QtWidgets import *
from pymavlink import mavutil
from dronekit import *
import time


drone=connect('tcp:192.168.1.117:5762',wait_ready=True)
print("Bağlantı Sağlandı")
time.sleep(1)


class classDrone():
    if drone.battery.level<5:
        print("Drone bataryası yetersiz...")
        time.sleep(1)
        quit()

    def Takeoff():
      while True:
        if drone.location.global_relative_frame.alt < 1:
            irtifa = int(input("Kalkış yüksekliği girin: "))

            print(*"IHA CONTROL CENTER")

            while drone.is_armable is not True:
                print("Drone ARM edilemiyor.")
                time.sleep(1)
            print("Drone ARM için Hazır!")

            drone.mode = VehicleMode("GUIDED")

            drone.armed = True

            while drone.armed is not True:
                print("Drone ARM deneniyor.")
                time.sleep(1)
            print("Drone ARM edildi.")

            drone.simple_takeoff(irtifa)

            while drone.location.global_relative_frame.alt < irtifa * 0.9:
                print("Drone yüksekliği: ", drone.location.global_relative_frame.alt)
                time.sleep(1)
            print("Yükseklik ", irtifa, "sabitlendi.")


        else:
            batlevel = drone.battery.level
            batvoltage = drone.battery.voltage
            altitude = drone.location.global_relative_frame.alt
            speed = drone.groundspeed

            print("Batarya durumu: ", batlevel)
            print("Batarya voltaj: ", batvoltage)
            print("Yükseklik: ", altitude)
            print("Hız: ", speed)
            print("----------------------------------------------")
            print(*"BLACKNIGHT")
            print("----------------------------------------------")
            time.sleep(2)














    Takeoff()