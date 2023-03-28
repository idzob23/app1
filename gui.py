import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_text = sg.InputText(tooltip="Enter to-do")
add_button  = sg.Button("Add")


window = sg.Window('My To-Do App', layout=[[label], [input_text, add_button]])   #putting object in [] alone will display object on separate lines
window.read()       #display windows
print("Hello")

window.close()      #close the windows when press some button