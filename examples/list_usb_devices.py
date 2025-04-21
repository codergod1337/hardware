import os
import sys

# DLL-Pfad setzen, bevor 'hid' geladen wird
dll_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_files", "hidapi-win", "x64"))
os.add_dll_directory(dll_path)

# Pfad für usb_devices-Modul
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from usb_devices.usb_helper import list_hid_devices

def main():
    devices = list_hid_devices()
    print("Gefundene HID-Geräte:\n")

    for dev in devices:
        print(f"- {dev['manufacturer']} | {dev['product']} "
              f"(VID: {dev['vendor_id']}, PID: {dev['product_id']})")

if __name__ == "__main__":
    main()