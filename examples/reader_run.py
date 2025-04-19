#examples/reader_run.py
import sys
import os

# Pfad zum Projekt-Hauptverzeichnis hinzufügen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from thrustmaster.joystick_reader import JoystickReader
import time

def main() -> None:
    reader = JoystickReader()

    try:
        while True:
            reader.read_input()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Beendet durch Benutzer.")

if __name__ == "__main__":
    main()