import sys  #for system start and close
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QGridLayout #import classes
# from PyQt6.QtCore import Qt, QTimer #import Qt ennumeration and constants

from PyQt6.QtWidgets import QApplication 

from dashboard import Dashboard #import Dashboard class from dashboard.py

app = QApplication(sys.argv) #manage window clicks, keyboard i/p etc

window = Dashboard() #create an instance of the Dashboard class

# current_speed = 0
# speed_direction = 1 #1 for increasing speed and -1 for decreasing speed

# current_fuel = 100
# current_temp = 25

# title = QLabel("AUTOMOTIVE DASHBOARD") #create  widget
# title.setStyleSheet(""" 
#                     font-size: 20px;
#                     font-weight: bold;
#                     color: white;
#                     """)
# speed = QLabel("0km/h")
# speed.setStyleSheet(""" 
#                     font-size: 42px;
#                     font-weight: bold;
#                     color: cyan;
#                     """)
# rpm = QLabel("RPM: 0")
# rpm.setStyleSheet(""""
#                   font-size: 20px;
#                   color: white;
#                   """)
# gear = QLabel("Gear: D")
# gear.setStyleSheet(""""
#                   font-size: 20px;
#                   color: white;
#                   """)
# fuel = QLabel("Fuel: 100%")
# fuel.setStyleSheet(""""
#                    font-size: 20px;
#                    color: white;
#                    """)
# temp = QLabel("Temp: 90°C")
# temp.setStyleSheet(""""
#                   font-size: 20px;
#                   color: white;
#                   """)
# button = QPushButton("Increase Speed")
# timer = QTimer() #create a timer oject


# def increase_speed(): #create a function
#     global current_speed  #specify current sppeed to be used for reference  
#     global speed_direction 
#     if current_speed < 240:  
#         current_speed += speed_direction * 10 #current speed = current speed*speed direction+ 10
#         if current_speed>=240:
#             speed_direction = -1
#         if current_speed<=0:
#             speed_direction = 1
        

#     speed.setText(f"{current_speed} km/h") #set speed to the label
    
#     current_rpm = current_speed * 40
#     rpm.setText(f"RPM: {current_rpm}")

#     global current_fuel
#     if current_fuel >0:
#         current_fuel -= 1
#         fuel.setText(f"fuel: {current_fuel}%")

#     global current_temp
#     if current_temp < 90:
#         current_temp += 1
#         temp.setText(f"Temp: {current_temp}°C")

# title.setAlignment(Qt.AlignmentFlag.AlignCenter) #Set Alignment
# speed.setAlignment(Qt.AlignmentFlag.AlignCenter)

# layout = QVBoxLayout()
# layout.addWidget(title)
# layout.addWidget(speed)

# grid = QGridLayout()
# grid.addWidget(rpm,0,0)
# grid.addWidget(gear,0,1)
# grid.addWidget(fuel,1,0)
# grid.addWidget(temp,1,1)

# layout.addLayout(grid)

# #layout.addWidget(button)

# timer.timeout.connect(increase_speed)
# timer.start(1000)
# #button.clicked.connect(increase_speed) #connect teh button clickto the function

# window.setLayout(layout)

window.show()
sys.exit(app.exec())

