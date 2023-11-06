from hal import hal_input_switch as switch
from hal import hal_led as led
from time import sleep


def main():
    switch.init()
    led.init()
    led_state = 0  # Initialize LED state as off

    while True:
        switch_state = switch.read_slide_switch()

        if switch_state == 1:  # Switch is in the left position
            led.set_output(0, 1)  # Turn the LED on
            sleep(0.1)  # Adjust the delay for a 10 Hz blink
        else:
            led.set_output(0, 0)


# Main entry point
if __name__ == "__main__":
    main()