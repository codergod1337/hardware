# file: usb_devices/communication_thrustmaster.py

import hid
import time

class ThrustmasterJoystick:
    def __init__(self, vendor_id=0x044f, product_id=0xb10a):
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.device = hid.device()
        self.device.open(self.vendor_id, self.product_id)
        self.device.set_nonblocking(True)
        print(f"✅ Thrustmaster-Gerät geöffnet (VID: {hex(self.vendor_id)}, PID: {hex(self.product_id)})")

    def read_raw_input(self):
        """
        Liest rohe HID-Daten vom Joystick. Gibt Liste von Byte-Werten zurück oder None.
        """
        data = self.device.read(64)
        return data if data else None

    def parse_axes(self, data):
        return {
            "x": data[0],
            "y": data[1],
            "z": data[2],
            "throttle": data[3]
        }

    def parse_buttons(self, data):
        buttons = []
        low = data[4]
        high = data[5]
        for i in range(8):
            buttons.append(bool(low & (1 << i)))
        for i in range(8):
            buttons.append(bool(high & (1 << i)))
        return buttons

    def read_state(self):
        """
        Gibt dekodierte Achsen- und Button-Daten zurück.
        """
        data = self.read_raw_input()
        if not data:
            return None

        axes = self.parse_axes(data)
        buttons = self.parse_buttons(data)
        return {"axes": axes, "buttons": buttons}

    def read_loop(self, delay=0.2):
        """
        Endlosschleife zum Auslesen und Anzeigen der Joystickdaten.
        """
        print("🎮 Starte Lese-Schleife. Drücke Strg+C zum Beenden.")
        try:
            while True:
                state = self.read_state()
                if state:
                    print(f"🎯 X={state['axes']['x']}, Y={state['axes']['y']}, Z={state['axes']['z']}, Throttle={state['axes']['throttle']}\n",
                          f"🔘 Buttons: {state['buttons']}")
                time.sleep(delay)
        except KeyboardInterrupt:
            print("👋 Beendet durch Benutzer.")
            self.device.close()

if __name__ == "__main__":
    joy = ThrustmasterJoystick()
    joy.read_loop()