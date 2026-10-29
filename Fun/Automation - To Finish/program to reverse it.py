import pyautogui, keyboard, time
def run_program(program):
    for i in program:
        if i[0] == 'click':
            pyautogui.click(i[1],i[2])
        elif i[0] =='':
            continue
        elif i[0]=='wait':
            keyboard.wait(i[1])
        elif i[0] == 'timeWait':
            time.sleep(i[1])
            
