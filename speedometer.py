from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QColor, QFont
from PyQt6.QtCore import Qt, QPoint
import math


class Speedometer(QWidget):

    def __init__(self):
        super().__init__()

        self.speed = 0
        self.setMinimumSize(350, 350)

    def setSpeed(self, speed):
        self.speed = speed
        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.fillRect(self.rect(), QColor("#1f1f1f"))

        center_x = 175
        center_y = 175
        radius = 150

        # ===============================
        # Colored Speed Arc
        # ===============================

        pen = QPen(QColor("#00ff66"))
        pen.setWidth(8)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)

        # Green
        painter.drawArc(
            center_x-radius,
            center_y-radius,
            radius*2,
            radius*2,
            210*16,
            -120*16
        )

        # Yellow
        pen.setColor(QColor("#FFD700"))
        painter.setPen(pen)

        painter.drawArc(
            center_x-radius,
            center_y-radius,
            radius*2,
            radius*2,
            90*16,
            -50*16
        )

        # Red
        pen.setColor(QColor("#ff3333"))
        painter.setPen(pen)

        painter.drawArc(
            center_x-radius,
            center_y-radius,
            radius*2,
            radius*2,
            40*16,
            -40*16
        )

        # ===============================
        # Tick Marks
        # ===============================

        pen = QPen(QColor("white"))
        painter.setPen(pen)

        for value in range(0, 241, 10):

            angle = math.radians(-120 + value)

            if value % 20 == 0:
                inner = radius - 20
                pen.setWidth(3)
            else:
                inner = radius - 12
                pen.setWidth(1)

            painter.setPen(pen)

            outer_x = center_x + radius * math.sin(angle)
            outer_y = center_y - radius * math.cos(angle)

            inner_x = center_x + inner * math.sin(angle)
            inner_y = center_y - inner * math.cos(angle)

            painter.drawLine(
                QPoint(int(inner_x), int(inner_y)),
                QPoint(int(outer_x), int(outer_y))
            )

        # ===============================
        # Speed Numbers
        # ===============================

        painter.setPen(QColor("white"))

        font = QFont("Arial", 10)
        font.setBold(True)
        painter.setFont(font)

        for value in range(0, 241, 20):

            angle = math.radians(-120 + value)

            text_radius = radius - 40

            x = center_x + text_radius * math.sin(angle)
            y = center_y - text_radius * math.cos(angle)

            painter.drawText(
                int(x) - 12,
                int(y) + 6,
                24,
                20,
                Qt.AlignmentFlag.AlignCenter,
                str(value)
            )

        # ===============================
        # Needle
        # ===============================

        angle = math.radians(-120 + self.speed)

        needle_length = radius - 30

        end_x = center_x + needle_length * math.sin(angle)
        end_y = center_y - needle_length * math.cos(angle)

        pen = QPen(QColor("#ff2222"))
        pen.setWidth(5)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)

        painter.drawLine(
            QPoint(center_x, center_y),
            QPoint(int(end_x), int(end_y))
        )

        # ===============================
        # Center Hub
        # ===============================

        painter.setBrush(QColor("white"))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(center_x-7, center_y-7, 14, 14)

        # ===============================
        # Digital Speed
        # ===============================

        painter.setPen(QColor("#00F5FF"))

        font = QFont("Arial", 18)
        font.setBold(True)
        painter.setFont(font)

        painter.drawText(
            self.rect(),
            Qt.AlignmentFlag.AlignCenter,
            f"{self.speed}\nkm/h"
        )