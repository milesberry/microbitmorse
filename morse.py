from microbit import *

def wait_for_keydown():
    while not button_a.is_pressed():
        sleep(10)
        
def wait_for_keyup():
    while button_a.is_pressed():
        sleep(10) 
        
morse_code_lookup = {
    ".-":    "A",
    "-...":    "B",
    "-.-.":    "C",
    "-..":    "D",
    ".":    "E",
    "..-.":    "F",
    "--.":    "G",
    "....":    "H",
    "..":    "I",
    ".---":    "J",
    "-.-":    "K",
    ".-..":    "L",
    "--":    "M",
    "-.":    "N",
    "---":    "O",
    ".--.":    "P",
    "--.-":    "Q",
    ".-.":    "R",
    "...":    "S",
    "-":    "T",
    "..-":    "U",
    "...-":    "V",
    ".--":    "W",
    "-..-":    "X",
    "-.--":    "Y",
    "--..":    "Z",
    ".----":    "1",
    "..---":    "2",
    "...--":    "3",
    "....-":    "4",
    ".....":    "5",
    "-....":    "6",
    "--...":    "7",
    "---..":    "8",
    "----.":    "9",
    "-----":    "0"
}

def try_decode(bit_string):
    if bit_string in morse_code_lookup.keys():
        return(morse_code_lookup[bit_string])
    else:
        return(".")        
        
DOT = Image ("00000:"
             "00000:"
             "00900:"
             "00000:"
             "00000:")
DASH = Image ("00000:"
             "00000:"
             "09990:"
             "00000:"
             "00000:")


key_down_time = 0
key_down_length = 0
key_up_length = 0

while True:
    key_up_time = running_time()
    buffer=""
    string=""

    while not button_b.is_pressed():
        wait_for_keydown()
        display.clear()
        key_down_time=running_time()
        key_up_length=key_down_time-key_up_time
        if len(buffer)>0 and key_up_length>500 :
            char=try_decode(buffer)
            string=string+char
            buffer=""
            display.show(char)
        wait_for_keyup()
        key_up_time = running_time()
        key_down_length = key_up_time - key_down_time
        if key_down_length > 250:
            buffer=buffer+"-"
            display.show(DASH)
        else:
            buffer=buffer+"."
            display.show(DOT)
        
    display.scroll(string)
