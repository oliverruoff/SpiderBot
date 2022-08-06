from machine import Pin, PWM
from time import sleep

SG90_DATA_PINS = [29, 28, 27, 26, 15, 14, 8, 7]
pwms = []

for pin in SG90_DATA_PINS:
    pwm = PWM(Pin(pin))
    pwm.freq(50)
    pwms.append(pwm)

def set_angle(pos, pwm, angle, delay=0.2):
    if angle >= 0 and angle <= 180:
        if pos == 0:
            angle = 180 - angle
        elif pos == 1:
            pass
        elif pos == 2:
            angle = 180 - angle
        elif pos == 3:
            angle = 180 - angle
        elif pos == 4:
            pass
        elif pos == 5:
            pass
        elif pos == 6:
            angle = 180 - angle
        elif pos == 7:
            pass
                
        ms = int((angle/180*8000)+1000)
        print('ms:', ms)
        pwm.duty_u16(ms)
        sleep(delay)
        if delay > 0:
            pwm.duty_u16(0) #turn off holding torque
    else:
        print('Angle not in range:', angle)


legs = [(4, pwms[4]), (3, pwms[3]), (1, pwms[1]), (6, pwms[6])]
feet = [(5, pwms[5]), (2, pwms[2]), (0, pwms[0]), (7, pwms[7])]

fll = legs[0] # front left leg
flf = feet[0] # front left foot

frl = legs[1]
frf = feet[1]

brl = legs[2] # back right leg
brf = feet[2] # back right foot

bll = legs[3]
blf = feet[3]

def sit_down():
    set_angle(bll[0], bll[1], 180, 0)
    set_angle(brl[0], brl[1], 180, 0)
    set_angle(blf[0], blf[1], 90, 0)
    set_angle(brf[0], brf[1], 90, 0)
    
    set_angle(fll[0], fll[1], 100, 0)
    set_angle(frl[0], frl[1], 100, 0)
    set_angle(flf[0], flf[1], 25, 0)
    set_angle(frf[0], frf[1], 25, 0)

def attack_pose():
    for leg in legs:
        set_angle(leg[0], leg[1], 100, 0)

    for foot in feet:
        set_angle(foot[0], foot[1], 25, 0)
        
def wave_right():
    set_angle(frf[0], frf[1], 150, 0)
    set_angle(frl[0], frl[1], 50, 0.2)
    set_angle(frl[0], frl[1], 130, 0.2)
    set_angle(frl[0], frl[1], 50, 0.2)
    set_angle(frl[0], frl[1], 130, 0.2)
    set_angle(frl[0], frl[1], 50, 0.2)
    set_angle(frl[0], frl[1], 130, 0.2)
    set_angle(frl[0], frl[1], 50, 0.2)
    set_angle(frl[0], frl[1], 130, 0.2)
    

def walking_pose():
    for leg in legs:
        set_angle(leg[0], leg[1], 50, 0)

    for foot in feet:
        set_angle(foot[0], foot[1], 25, 0)

def walk(steps):
    for i in range(steps):
        set_angle(frf[0], frf[1], 90)      # rechts vorne Fuß hoch
        set_angle(frl[0], frl[1], 85, 0)   # rechts vorne Bein vor
        set_angle(brl[0], brl[1], 85, 0)   # rechts hinten Bein hinter
        set_angle(fll[0], fll[1], 95)     # links vorne Bein hinter
        set_angle(frf[0], frf[1], 25, 0)   # rechts vorne Fuß runter
        set_angle(brf[0], brf[1], 90)      # rechts hinten Fuß hoch
        set_angle(frl[0], frl[1], 95, 0)  # rechts vorne Bein hinter
        set_angle(brl[0], brl[1], 95)     # rechts hinten Bein vor
        set_angle(brf[0], brf[1], 25, 0)   # rechts hinten Fuß runter
        
        set_angle(flf[0], flf[1], 90)      # links vorne Fuß hoch
        set_angle(fll[0], fll[1], 85, 0)   # links vorne Bein vor
        set_angle(bll[0], bll[1], 85, 0)   # links hinten Bein hinter
        set_angle(frl[0], frl[1], 95)     # rechts vorne Bein hinter
        set_angle(flf[0], flf[1], 25, 0)   # links vorne Fuß runter
        set_angle(blf[0], blf[1], 90)      # links hinten Fuß hoch
        set_angle(fll[0], fll[1], 95, 0)  # links vorne Bein hinter
        set_angle(bll[0], bll[1], 95)     # links hinten Bein vor
        set_angle(blf[0], blf[1], 25, 0)   # links hinten Fuß runter
    
sit_down()
sleep(1)
wave_right()
sleep(1)
attack_pose()
sleep(2)
while True:

    
    walk(5)
    
    continue
    
    for i in range(5):
    
        set_angle(bll[0], bll[1], 50, 0)
        set_angle(brl[0], brl[1], 50, 0)
        set_angle(blf[0], blf[1], 90, 0)
        set_angle(brf[0], brf[1], 90, 0)
        
        sleep(0.5)
        
        set_angle(bll[0], bll[1], 100, 0)
        set_angle(brl[0], brl[1], 100, 0)
        set_angle(blf[0], blf[1], 25, 0)
        set_angle(brf[0], brf[1], 25, 0)

        sleep(0.5)

    for moves in range(10):
        set_angle(fll[0], fll[1], 100, 0)
        set_angle(frl[0], frl[1], 100)
        
        set_angle(flf[0], flf[1], 90, 0)
        set_angle(frf[0], frf[1], 90)
        
        set_angle(fll[0], fll[1], 70, 0)
        set_angle(frl[0], frl[1], 70)
        
        set_angle(flf[0], flf[1], 25, 0)
        set_angle(frf[0], frf[1], 25)
        
    
    
    sleep(2)

# [0] = BRF 0 -> up
# [1] = BRL 0 -> mid

# [2] = FRF 0 -> up
# [3] = FRL 0 -> out

# [4] = FLL 0 -> mid
# [5] = FLF 0 -> down

# [6] = BLL 0 -> out
# [7] = BLF 0 -> down
