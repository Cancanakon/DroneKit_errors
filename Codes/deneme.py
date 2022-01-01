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
        self.ui.btnTakeoff.clicked.connect(self.deneme)

    def deneme(self):

        while True:
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















app = QApplication([])
window = DesignTry()
window.show()
app.exec()
