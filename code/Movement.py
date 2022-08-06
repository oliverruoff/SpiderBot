from machine import Pin, PWM
from time import sleep

SG90_DATA_PINS = [29, 28, 27, 26, 15, 14, 8, 7]
pwms = []

for pin in SG90_DATA_PINS:
    pwm = PWM(Pin(pin))
    pwm.freq(50)
    pwms.append(pwm)

def set_angle(pos, pwm, angle):
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
        #sleep(0.1)
        #pwm.duty_u16(0)
    else:
        print('Angle not in range:', angle)


legs = [(4, pwms[4]), (3, pwms[3]), (1, pwms[1]), (6, pwms[6])]
feet = [(5, pwms[5]), (2, pwms[2]), (0, pwms[0]), (7, pwms[7])]

while True:

    for leg in legs:
        set_angle(leg[0], leg[1], 50)

    for foot in feet:
        set_angle(foot[0], foot[1], 150)

    sleep(1)

    for leg in legs:
        set_angle(leg[0], leg[1], 90)

    for foot in feet:
        set_angle(foot[0], foot[1], 25)

    sleep(1)

    for leg in legs:
        set_angle(leg[0], leg[1], 120)

    sleep(1)

    for foot in feet:
        set_angle(foot[0], foot[1], 50)
        
    sleep(1)

    for pwm in pwms:
        pwm.duty_u16(0)

    sleep(1)

# Back Left
# leg
set_angle(pwms[6], 70)
# foot
set_angle(pwms[7], 25)

# Back right
# leg
set_angle(pwms[1], 110)
# foot
set_angle(pwms[0], 155)

# Front left
# leg
set_angle(pwms[4], 110)
# foot
set_angle(pwms[5], 25)

# Front right
# leg
set_angle(pwms[3], 110)
# foot
set_angle(pwms[2], 155)

# [0] = BRF 0 -> up
# [1] = BRL 0 -> mid

# [2] = FRF 0 -> up
# [3] = FRL 0 -> out

# [4] = FLL 0 -> mid
# [5] = FLF 0 -> down

# [6] = BLL 0 -> out
# [7] = BLF 0 -> down
