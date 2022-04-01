# Lab 2/1
# Programm, das in 10°-Schritten zwischen 0 und 180° den jeweiligen Cosinus-Wert berechnet und ausgibt

import math

winkel_grad=0

while winkel_grad <= 180:
    winkel_rad = winkel_grad * math.pi /180
    cosinus = math.cos(winkel_rad)
    print("Winkel: ", winkel_grad, "-> cosinus: ", cosinus)
    winkel_grad +=10
    