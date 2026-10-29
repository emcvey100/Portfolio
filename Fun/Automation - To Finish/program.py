class Make:
    '''Makes the program for use'''
    def __init__():
        self.__code=[]
    def __get_code():
        return self.__code
    def __set_code(code):
        self.__code = code
    def ___click(x=False, y=False):
        self.__code.append(['click',x,y])
    def __space_wait():
        self.__code.append(['wait','space'])
    def __time_wait(time=0):
        self.code.append(['timeWait', time])
from tkinter import * 
import keyboard
import pyautogui
program = Make()
def __start():
    window = Tk()
    label_title = Label(window, text = "Automation Program Bots")
    label_title.pack()
    button_next = Button(window,text="Next", command=main)
    button_next.pack()
    def main():
        window.destroy()
        next_GUI()
    window.mainloop()
def next_GUI():
    window = Tk()
    button_click=Button(window, text="click", command=destroy_click)
    button_click.pack()
    def destroy_click():
        window.destroy()
        click()
    button_wait =Button(window, text="wait till space", command=destroy_wait)
    button_wait.pack()
    def destroy_wait():
        window.destroy()
        wait() 
    window.mainloop()
def click():
    pyautogui.alert(text="Drag mouse to area needed and press space.", title="instructions", button="Ready")
    keyboard.wait('space')
    x,y=pyautogui.position()
    program.__click(x,y)
    next_GUI()
def wait():
    pyautogui.alert(text="A wait until space has been added.", title="alert", button="Ready")
    program.__space_wait()
    next_GUI()
start()
