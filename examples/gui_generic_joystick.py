# file: examples/gui_generic_joystick.py
import os
import sys
# Projektverzeichnis zu sys.path hinzufügen (eine Ebene hoch)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from usb_devices.generic_joystick import GenericJoystick
import tkinter as tk
from tkinter import ttk
import threading
import time



class JoystickMonitorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🕹️ Universelle Joystick-GUI")
        self.joystick = GenericJoystick()

        self.num_axes = 4  # Platzhalter, dynamisch erweiterbar
        self.num_buttons = 16  # Standardmäßige Obergrenze

        # Achsenanzeige
        self.axes_labels = []
        axes_frame = ttk.LabelFrame(master, text="Achsen")
        axes_frame.pack(padx=10, pady=5, fill="x")
        for i in range(self.num_axes):
            row = ttk.Frame(axes_frame)
            row.pack(anchor="w", padx=5, pady=2)
            ttk.Label(row, text=f"Achse {i+1}:").pack(side="left")
            lbl = ttk.Label(row, text="0")
            lbl.pack(side="left")
            self.axes_labels.append(lbl)

        # Buttonanzeige
        self.button_indicators = []
        buttons_frame = ttk.LabelFrame(master, text="Buttons")
        buttons_frame.pack(padx=10, pady=5, fill="x")
        for i in range(self.num_buttons):
            btn = tk.Label(buttons_frame, text=str(i+1), width=3, relief="ridge", bg="lightgray")
            btn.grid(row=i//8, column=i%8, padx=2, pady=2)
            self.button_indicators.append(btn)

        # Hintergrundthread starten
        self.running = True
        threading.Thread(target=self.read_loop, daemon=True).start()

        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def read_loop(self):
        while self.running:
            data = self.joystick.read_raw_input()
            if data:
                self.update_axes(data[:self.num_axes])
                if len(data) >= 6:
                    self.update_buttons(data[4], data[5])
            time.sleep(0.05)

    def update_axes(self, axis_values):
        for i, val in enumerate(axis_values):
            if i < len(self.axes_labels):
                self.axes_labels[i].config(text=str(val))

    def update_buttons(self, byte_low, byte_high):
        for i in range(8):
            pressed = byte_low & (1 << i)
            color = "limegreen" if pressed else "lightgray"
            self.button_indicators[i].config(bg=color)
        for i in range(8):
            pressed = byte_high & (1 << i)
            color = "limegreen" if pressed else "lightgray"
            if i + 8 < len(self.button_indicators):
                self.button_indicators[i + 8].config(bg=color)

    def on_close(self):
        self.running = False
        self.joystick.close()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = JoystickMonitorGUI(root)
    root.mainloop()
