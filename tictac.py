from sense_hat import SenseHat
import sense_hat
import time
from time import sleep

sense = sense_hat.SenseHat()
s = SenseHat()
s.low_light = True
up_key = sense_hat.DIRECTION_UP
down_key = sense_hat.DIRECTION_DOWN
left_key = sense_hat.DIRECTION_LEFT
right_key = sense_hat.DIRECTION_RIGHT
pressed = sense_hat.ACTION_PRESSED

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
def set_block (col,row):
  sense.clear()
  sense.set_pixel(col,row, white)
  sense.set_pixel(col,row+1, white)
  sense.set_pixel(col+1,row, white)
  sense.set_pixel(col+1,row+1, white)
  
r= 0
c = 0
set_block (c,r) 
c +=1

while True:
    sleep(.1)
    
    # sense.clear()
    event = sense.stick.wait_for_event()
    print("The joystick was {} {}".format(event.action, event.direction)) 
    if event.direction == "right" and event.action == "released":
      if c >= 1 and c < 7  :
        c +=2
        print("1-- r = ",r , "c", c)
        set_block(c,r)
        c +=1
       
      elif r<7:
        r +=3
        c =0
        print("2---- r = ",r , "c", c)
        set_block(c,r)
        c +=1
    if event.direction == "left"  and event.action == "released":
      if c==1 and r >0 :
          
        r -=3
        c =6
        print("3----- r = ",r , "c", c)
        set_block(c,r)
        c +=1
      elif c>1 and c<=7 and r ==0 :
        c -=4
        print("4---- r = ",r , "c", c)
        set_block(c,r)
        c +=1
      elif r>0:
        c -=4
        print("5---- r = ",r , "c", c)
        set_block(c,r)
        c +=1
       

      
    
