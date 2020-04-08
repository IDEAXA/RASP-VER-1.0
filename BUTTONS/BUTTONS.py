import RPi.GPIO as GPIO
import time

button1 = 16
button2 = 18
button3 = 22
button4 = 7



def setup():
       GPIO.setmode(GPIO.BOARD)
       GPIO.setup(button1, GPIO.IN)
       GPIO.setup(button2, GPIO.IN)
       GPIO.setup(button3, GPIO.IN)
       GPIO.setup(button4, GPIO.IN)
    
def loop():
        while True:
              button_state1 = GPIO.input(button1)
              button_state2 = GPIO.input(button2)
              button_state3 = GPIO.input(button3)
              button_state4 = GPIO.input(button4)
              print(button_state1,button_state2,button_state3,button_state4)


if __name__ == '__main__':
          
          setup()
          
          try:
                 loop()
                 time.sleep(1)
          
          except KeyboardInterrupt:
                 print('keyboard interrupt detected')
                 #endprogram()
