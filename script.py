import ctypes
import keyboard
import pythoncom
import wmi

def set_brightness(brightness):
    pythoncom.CoInitialize()
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)
    pythoncom.CoUninitialize()

def on_key_press(event):
    if event.name == 'q' and keyboard.is_pressed('ctrl'):
        set_brightness(8)

    if event.name == 'ñ' and keyboard.is_pressed('ctrl'):
        set_brightness(100)

keyboard.on_press(on_key_press)
keyboard.wait('esc')  # Espera hasta que se presione la tecla 'Esc'