from gpiozero import LEDBoard, Button
from time import sleep
import random
from signal import pause

sol = []
leds = LEDBoard(blue=12, orange=16, red=20)

blueButton = Button(26)
orangeButton = Button(21)
redButton = Button(19)

buttons = [blueButton, orangeButton, redButton]

def convertSequence(sequence):
    res = []
    for led in sequence:
        if led == '12':
            res.append(str(blueButton.pin).strip('GPIO'))
        if led == '16':
            res.append(str(orangeButton.pin).strip('GPIO'))
        if led == '20':
            res.append(str(redButton.pin).strip('GPIO'))
    return res

def generate_sequence(amount, frequency):

    randomlist = random.choices(leds, k=amount)
    #print('Sequence starting:')
    sequence = []
    for led in randomlist:
        sequence.append(str(led.pin).strip("GPIO"))
        led.on()
        sleep(frequency)
        led.off()
        sleep(frequency)
    #print(sequence)
    return sequence


def play(level):
    
    #print("Starting level " + level["level"] + '!')
    sequence = generate_sequence(level["amount"], level["frequency"])
    #print("What was the sequence?")
    return (capture_input(convertSequence(sequence), level["time_to_press"]))

def capture_input(buttonSequence, time_to_press):
    inp = 0
    ans = []
    timer = 0
    while True:
        if(blueButton.is_pressed == True):
            timer = 0
            if('26' != buttonSequence[inp]):
                return ('you lose')
                break
            inp = inp + 1
            ans.append('26')
            blueButton.wait_for_release()
        if(orangeButton.is_pressed == True):
            timer = 0
            if('21' != buttonSequence[inp]):
                return ('you lose')
                break
            inp = inp + 1
            ans.append('5')
            orangeButton.wait_for_release()
        if(redButton.is_pressed == True):
            timer = 0
            if('19' != buttonSequence[inp]):
                return ('you lose')
                break
            inp = inp + 1
            ans.append('13')
            redButton.wait_for_release()
        if(inp == len(buttonSequence)):
            break
        timer = timer + 0.1
        if(timer >= time_to_press):
            return ('too slow')
            break
        sleep(0.1)
        
        
    if(ans == buttonSequence):
        return ('you won!')

