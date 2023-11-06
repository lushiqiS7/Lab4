import src.hal.hal_input_switch as HIS
import src.hal.hal_led as HLED
from threading import Thread
from time import sleep
def led_bink():
    global Run_Multithread, waiting, LED1
    while (Run_Multithread):
        if LED1:
            HLED.set_output(0,1)
            sleep(0.2)
            HLED.set_output(0, 0)
            sleep(0.2)
        else:
            if waiting:
                HLED.set_output(0, 1)
                sleep(0.1)
                HLED.set_output(0, 0)
                sleep(0.1)
            else:
                HLED.set_output(0, 0)

def fivesecwaits():
    global waiting, Wgo, Run_Multithread, Done
    while (Run_Multithread):
        if Wgo and Done:
            timing = 5
            waiting = True
            while timing > 0:
                timing -= 1
                sleep(1)
            waiting = False
            Done = False

def main():
    HIS.init()
    HLED.init()
    global Run_Multithread, LED1, waiting, Wgo, Done
    Wgo, LED1, waiting, Done = False, False, False, False
    Run_Multithread = True
    LED = Thread(target=led_bink)
    LED.start()
    count = Thread(target=fivesecwaits)
    count.start()

    while True:
        if HIS.read_slide_switch():
            LED1 = True
            Wgo = False
            Done = True
        else:
            LED1 = False
            Wgo = True



if __name__ == "__main__":
    main()