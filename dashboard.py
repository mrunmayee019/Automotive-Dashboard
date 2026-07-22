from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QProgressBar, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt, QTimer, QTime
from speedometer import Speedometer

print("Dashboard file is running!")
print(__file__)

class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Automotive Dashboard")
        self.resize(1000,700)

        self.current_speed = 0
        self.startup = True
        self.startup_speed = 0
        self.current_fuel = 100
        self.current_temp = 25
        self.odometer = 0.0
        self.trip = 0.0
        self.speed_direction = 1 
        self.headlight_on = False
        self.current_battery = 100
        self.left_on = False
        self.right_on = False
        self.hazard_on = False

        self.title = QLabel("AUTOMOTIVE DASHBOARD")
        self.warning = QLabel("")
        self.clock = QLabel()

        self.clock.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
            color:white;
        """)

        self.clock.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.battery = QLabel("🔋")

        self.battery.setStyleSheet("""
        font-size:24px;
        color:#00ff00;
        """)

        self.warning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.warning.setStyleSheet("""
            color:red;
            font-size:20px;
            font-weight:bold;
        """)
        self.speedometer = Speedometer()
        self.rpm = QLabel("RPM : 0")
        self.gear = QLabel("Gear : D")
        self.odo = QLabel("ODO : 0.0 km")
        self.trip_label = QLabel("TRIP : 0.0 km")
        self.fuel_label = QLabel("Fuel")
        self.temp_label = QLabel("Temperature")
        self.fuel = QProgressBar()
        self.fuel.setRange(0, 100)
        self.fuel.setValue(100)
        self.temp = QProgressBar()
        self.temp.setRange(0,90)
        self.temp.setValue(25)

                # Turn indicators
        self.left_indicator = QPushButton("⬅")
        self.right_indicator = QPushButton("➡")

        self.left_indicator.setCheckable(True)
        self.right_indicator.setCheckable(True)

        for btn in [self.left_indicator, self.right_indicator]:
            btn.setFixedSize(60, 40)
            btn.setStyleSheet("""
                QPushButton{
                    background:#444;
                    color:white;
                    font-size:22px;
                    border-radius:8px;
                }

                QPushButton:checked{
                    background:#00ff00;
                    color:black;
                }
            """)
            self.headlight = QLabel("●")
            self.engine = QLabel("⚠")

            for label in [self.headlight, self.battery, self.engine]:
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setStyleSheet("""
                    font-size:24px;
                    color:gray;
                """)


        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
        """)

        for label in [self.rpm, self.gear, self.fuel_label, self.temp_label, self.odo, self.trip_label]:
            label.setStyleSheet("""
                                font-size: 18px;
                                color: white;
                                """)
        self.fuel.setStyleSheet("""
        QProgressBar{
            border:2px solid gray;
            border-radius:5px;
            text-align:center;
            color:white;
        }

        QProgressBar::chunk{
            background-color:#00ff66;
        }
        """)

        self.temp.setStyleSheet("""
        QProgressBar{
            border:2px solid gray;
            border-radius:5px;
            text-align:center;
            color:white;
        }

        QProgressBar::chunk{
            background-color:#ff6600;
        }
    """)

        
        self.setStyleSheet("""
                           QWidget{background: #1f1f1f;
                           }
                           """)

        main_layout = QVBoxLayout()

        main_layout.addStretch()
        main_layout.addWidget(self.clock, alignment=Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.warning)
        main_layout.addSpacing(50)       

        indicator_layout = QHBoxLayout()

        indicator_layout.addWidget(self.left_indicator)

        indicator_layout.addStretch()

        indicator_layout.addWidget(self.headlight)

        indicator_layout.addSpacing(25)

        indicator_layout.addWidget(self.battery)

        indicator_layout.addSpacing(25)

        indicator_layout.addWidget(self.engine)

        indicator_layout.addSpacing(25)

        indicator_layout.addWidget(self.warning)

        indicator_layout.addStretch()

        indicator_layout.addWidget(self.right_indicator)
       
        main_layout.addLayout(indicator_layout)

        main_layout.addWidget(self.speedometer, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addSpacing(70)

        grid = QGridLayout()

        grid.setHorizontalSpacing(250)
        grid.setVerticalSpacing(60)

        grid.addWidget(self.rpm,0,0,alignment=Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.gear,0,1,alignment=Qt.AlignmentFlag.AlignCenter)

        grid.addWidget(self.odo,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.trip_label,1,1,alignment=Qt.AlignmentFlag.AlignCenter)

        grid.addWidget(self.fuel,2,0,alignment=Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.temp,2,1,alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addLayout(grid)

        self.setLayout(main_layout)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFocus()


        self.timer = QTimer()
        self.timer.timeout.connect(self.update_dashboard)
        self.timer.start(100) 
        self.indicator_timer = QTimer()
        self.indicator_timer.timeout.connect(self.blinkIndicators)
        self.indicator_timer.start(500)
        self.startup_timer = QTimer()
        self.startup_timer.timeout.connect(self.startupAnimation)
        self.startup_timer.start(20)

    def update_dashboard(self):
        if self.startup:
            return
        current_time = QTime.currentTime()
        self.clock.setText(current_time.toString("hh:mm:ss"))
        self.speedometer.setSpeed(self.current_speed)        
        distance = self.current_speed / 36000

        self.odometer += distance
        self.trip += distance

        self.odo.setText(f"ODO : {self.odometer:.2f} km")
        self.trip_label.setText(f"TRIP : {self.trip:.2f} km")
        rpm = self.current_speed * 40
        self.rpm.setText(f"RPM : {rpm}")
         # Automatic Gear Selection
        if self.current_speed == 0:
            gear = "P"
        elif self.current_speed < 20:
            gear = "1"
        elif self.current_speed < 40:
            gear = "2"
        elif self.current_speed < 60:
            gear = "3"
        elif self.current_speed < 100:
            gear = "4"
        elif self.current_speed < 160:
            gear = "5"
        else:
            gear = "6"

        self.gear.setText(f"Gear : {gear}")

        if self.current_fuel > 0:
            self.current_fuel -= 0.05

        self.fuel.setValue(int(self.current_fuel))
        if self.current_fuel <= 20:
            self.warning.setText("⚠ LOW FUEL")
        else:
            self.warning.setText("")

        if self.current_fuel > 50:
            color = "#00ff66"      # Green
        elif self.current_fuel > 20:
            color = "#FFD700"      # Yellow
        else:
            color = "#ff3333"      # Red

        self.fuel.setStyleSheet(f"""
        QProgressBar {{
            border:2px solid gray;
            border-radius:5px;
            text-align:center;
            color:white;
        }}

        QProgressBar::chunk {{
            background-color:{color};
        }}
        """)
        if self.current_temp < 90:
            self.current_temp += 1

        self.temp.setValue(self.current_temp)


                # Battery discharge
        if self.current_battery > 0:
            self.current_battery -= 0.05

        if self.current_battery > 50:
            self.battery.setStyleSheet("""
                font-size:24px;
                color:#00ff66;
            """)
        elif self.current_battery > 20:
            self.battery.setStyleSheet("""
                font-size:24px;
                color:yellow;
            """)
        else:
            self.battery.setStyleSheet("""
                font-size:24px;
                color:red;
            """)

        # Engine warning
        if self.current_temp >= 80:
            self.engine.setStyleSheet("""
                font-size:24px;
                color:red;
            """)
        else:
            self.engine.setStyleSheet("""
                font-size:24px;
                color:gray;
            """)

    def startupAnimation(self):

        if not self.startup:
            return

        self.startup_speed += 6

        self.speedometer.setSpeed(self.startup_speed)

        self.rpm.setText(f"RPM : {self.startup_speed * 40}")

        if self.startup_speed <= 120:
            self.battery.setStyleSheet("""
                font-size:24px;
                color:#00ff66;
            """)

            self.headlight.setStyleSheet("""
                font-size:24px;
                color:#00BFFF;
            """)

        if self.startup_speed >= 240:

            self.startup_timer.stop()
            self.left_indicator.setChecked(True)
            self.right_indicator.setChecked(True)

            self.speedometer.setSpeed(0)
            self.left_indicator.setChecked(False)
            self.right_indicator.setChecked(False)

            self.current_speed = 0

            self.startup = False

            self.headlight.setStyleSheet("""
                font-size:24px;
                color:gray;
            """)
    def blinkIndicators(self):

        if self.hazard_on:

            self.left_indicator.setChecked(
                not self.left_indicator.isChecked()
            )

            self.right_indicator.setChecked(
                self.left_indicator.isChecked()
            )

            return

        if self.left_on:
            self.left_indicator.setChecked(
                not self.left_indicator.isChecked()
            )
        else:
            self.left_indicator.setChecked(False)

        if self.right_on:
            self.right_indicator.setChecked(
                not self.right_indicator.isChecked()
            )
        else:
            self.right_indicator.setChecked(False)

    def keyPressEvent(self, event):
        print(event.key())
        if event.key() == Qt.Key.Key_Up:
            self.current_speed = min(240, self.current_speed + 5)

        elif event.key() == Qt.Key.Key_Down:
            self.current_speed = max(0, self.current_speed - 5)

        elif event.key() == Qt.Key.Key_Left:
            self.left_on = not self.left_on
            self.right_on = False

        elif event.key() == Qt.Key.Key_Right:
            self.right_on = not self.right_on
            self.left_on = False

        elif event.key() == Qt.Key.Key_H:
            self.headlight_on = not self.headlight_on

            if self.headlight_on:
                self.headlight.setStyleSheet("""
                    font-size:26px;
                    color:#00BFFF;
                """)
            else:
                self.headlight.setStyleSheet("""
                    font-size:26px;
                    color:gray;
                """)
        elif event.key() == Qt.Key.Key_Space:

                self.hazard_on = not self.hazard_on

                if self.hazard_on:
                    self.left_on = True
                    self.right_on = True
                else:
                    self.left_on = False
                    self.right_on = False  