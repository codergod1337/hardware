import pygame


class JoystickReader:
    """Liest Eingaben des Thrustmaster-Joysticks über pygame aus."""

    def __init__(self) -> None:
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() == 0:
            raise RuntimeError("Kein Joystick angeschlossen.")

        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

        print(f"Joystick erkannt: {self.joystick.get_name()}")

    def read_input(self) -> None:
        """Liest Achsen, Buttons und Hat-Switch aus und gibt sie auf der Konsole aus."""
        pygame.event.pump()

        print("Achsen:")
        for i in range(self.joystick.get_numaxes()):
            value = self.joystick.get_axis(i)
            print(f"  Achse {i}: {value:.3f}")

        print("Buttons:")
        for i in range(self.joystick.get_numbuttons()):
            pressed = self.joystick.get_button(i)
            print(f"  Button {i}: {'gedrückt' if pressed else 'nicht gedrückt'}")

        print("Hat-Switch:")
        for i in range(self.joystick.get_numhats()):
            position = self.joystick.get_hat(i)
            print(f"  Hat {i}: {position}")

        print("-" * 40)