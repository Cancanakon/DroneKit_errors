from PyQt5.QtWidgets import *
from Design import Ui_MainWindow
import time
from pymavlink import mavutil
from dronekit import *

drone = connect('tcp:192.168.1.117:5762', wait_ready=True)

class DesignTry(QMainWindow):



    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



        print("Bağlantı Sağlandı")
        self.ui.DsgnInfo.setText("Bağlantı Sağlandı!")

        # self.ui.DsgnInfo.setText("IHA CONTROL CENTER")

        # self.ui.DsgnInfo.setText("Bildirim yok")

        if drone.battery.level < 5:
            print("Drone bataryası yetersiz...")
            self.ui.DsgnInfo.setText("Drone bataryası yetersiz")
            time.sleep(2)
        # self.ui.btnTakeoff.clicked.connect(self.Takeoff)


    def Takeoff(self):
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
                batlevel = str(drone.battery.level)
                batvoltage = str(drone.battery.voltage)
                altitude = str(drone.location.global_relative_frame.alt)
                speed = str(drone.groundspeed)

                print("Batarya durumu: ", batlevel)
                print("Batarya voltaj: ", batvoltage)
                print("Yükseklik: ", altitude)
                print("Hız: ", speed)
                print("----------------------------------------------")
                print(*"BLACKNIGHT")
                print("----------------------------------------------")
                self.ui.DsgnBattery.setText(batlevel)
                self.ui.DsgnSpeed.setText(speed)
                # self.ui.DsgnYaw.setText(0)
                self.ui.DsgnAltitude.setText(altitude)
                time.sleep(2)
    Takeoff()

app = QApplication([])
window = DesignTry()
window.show()
app.exec()








        