# file: usb_devices/usb_helper.py
import os
# Absoluten Pfad zur DLL berechnen – relativ zur aktuellen Datei
dll_relative_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "_files", "hidapi-win", "x64")
)
os.add_dll_directory(dll_relative_path)
import hid

def list_hid_devices():
    """
    Gibt eine Liste aller angeschlossenen HID-Geräte mit Hersteller-, Produkt- und ID-Informationen zurück.
    """
    devices = []

    for dev in hid.enumerate():
        devices.append({
            "vendor_id": hex(dev['vendor_id']),
            "product_id": hex(dev['product_id']),
            "manufacturer": dev.get('manufacturer_string', 'Unbekannt'),
            "product": dev.get('product_string', 'Unbekannt')
        })

    return devices