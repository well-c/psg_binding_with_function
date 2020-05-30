import PySimpleGUI as sg

def left_click(self):
    print("Left clicked")
    # do function
    return 'break'

def right_click(self):
    print("Right clicked")
    # do function
    return 'break'

layout = [[sg.Button('Left/Right click me', key='-BUTTON-')]]
window = sg.Window('Window Title', layout=layout, finalize=True)

window['-BUTTON-'].Widget.bind('<Button-1>', left_click)
window['-BUTTON-'].Widget.bind('<Button-3>', right_click)

while True:
    event, values = window.read()
    print(event, values)
    if event == None:
        break
window.close()