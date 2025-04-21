# file: usb_devices/generic_joystick.py
import os
# DLL-Verzeichnis relativ zur Datei
dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_files", "hidapi-win", "x64"))

if os.path.isdir(dll_path):
    os.add_dll_directory(dll_path)

import hid
import time




class GenericJoystick:
    def __init__(self, vendor_id=None, product_id=None):
        self.device_info = self.find_first_joystick(vendor_id, product_id)
        if not self.device_info:
            raise IOError("Kein geeignetes HID-Joystick-Gerät gefunden.")

        # Gerät über eindeutigen HID-Pfad öffnen
        self.device = hid.Device(path=self.device_info['path'])
        self.device.nonblocking = True

#✅
        print(f" Verbunden mit {self.device_info['product_string']} "
              f"({hex(self.device_info['vendor_id'])}:{hex(self.device_info['product_id'])})")


    def find_first_joystick(self, vendor_id=None, product_id=None):
        for dev in hid.enumerate():
            if vendor_id and product_id:
                if dev['vendor_id'] == vendor_id and dev['product_id'] == product_id:
                    return dev
            elif dev['usage_page'] == 0x01 and dev['usage'] in (0x04, 0x05):
                return dev
        return None

    def read_raw_input(self):
        data = self.device.read(64)
        return data if data else None

    def close(self):
        self.device.close()

    def read_loop(self, delay=0.2):
        print("🎮 Starte generische Lese-Schleife. Strg+C zum Beenden.")
        try:
            while True:
                data = self.read_raw_input()
                if data:
                    print("📥 Daten:", data)
                time.sleep(delay)
        except KeyboardInterrupt:
            print("👋 Beendet durch Benutzer.")
            self.close()