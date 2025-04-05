# Description/Overview
Uses [IR Positioning camera](https://evelta.com/gravity-ir-positioning-camera-for-arduino/?srsltid=AfmBOooNiAx0S3C0ovRrFRF-nSRxPkPTq1QWmGUFn1qSm-HRJ7FWbIFC) to create a wiimote style mouse that can be used to control the mouse without needing to rely on an accelorometer which will drift

#Setup
Step 1: Find the receiver mac address, and put it in the sender microPython code
Step 2: Update the python mouse listener with the com port for the receiver device
Step 3: 🤷🏽‍♂️🤷🏽‍♂️🤷🏽‍♂️ Havent gotten here yet... probably some calibration steps or simething 

# Hardware Requirements 
(Dont actually use these links they were just the first ones I found. All of this hardware can be found for much cheaper elsewhere):
- [esp32 mini s2](https://electropeak.com/esp32-s2fn4r2-s2-mini-v1-0-wifi-development-board?srsltid=AfmBOoprF23pO9AllEyRGTtK3-14SjYbZwIYpXnKzNadF5Cy1n_I1n3kOKA) x 2
- [IR Positioning camera](https://evelta.com/gravity-ir-positioning-camera-for-arduino/?srsltid=AfmBOooNiAx0S3C0ovRrFRF-nSRxPkPTq1QWmGUFn1qSm-HRJ7FWbIFC)
- [IR LEDs](https://www.amazon.com/Electronics123-com-Inc-LED-Infrared-950nm/dp/B07PXLZGBP?gQT=1)
