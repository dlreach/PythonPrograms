import PySimpleGUI as sg
import random

sg.ChangeLookAndFeel("DarkAmber")

WIN_W = 90
WIN_H = 25

menu_layout = [['Help', ['About']]]

layout = [[sg.Menu(menu_layout)],
         [sg.Text('Ephemera Dice Roller')],
         [sg.Text("Number"), sg.Text(" Type"), sg.Text(" Modifier"), sg.Text("Roll"), sg.Text("     Result")],
         [sg.Input(default_text="0", key='-NumD4-', size=(8,1)), sg.Text('D4   '), sg.Input(default_text="0", key='-D4Mod-', size=(5,1)), sg.Button('RollD4'), sg.Text('   Result', key="-D4-") ],
         [sg.Input(default_text="0", key='-NumD6-', size=(8,1)), sg.Text('D6   '), sg.Input(default_text="0", key='-D6Mod-', size=(5,1)), sg.Button('RollD6'), sg.Text('   Result', key="-D6-")],
         [sg.Input(default_text="0", key='-NumD8-', size=(8,1)), sg.Text('D8   '), sg.Input(default_text="0", key='-D8Mod-', size=(5,1)), sg.Button('RollD8'), sg.Text('   Result', key="-D8-")],
         [sg.Input(default_text="0", key='-NumD10-', size=(8,1)), sg.Text('D10 '), sg.Input(default_text="0", key='-D10Mod-', size=(5,1)), sg.Button('RollD10'), sg.Text('  Result', key="-D10-")],
         [sg.Input(default_text="0", key='-NumD12-', size=(8,1)), sg.Text('D12 '), sg.Input(default_text="0", key='-D12Mod-', size=(5,1)), sg.Button('RollD12'), sg.Text('  Result', key="-D12-")],
         [sg.Input(default_text="0", key='-NumD20-', size=(8,1)), sg.Text('D20 '), sg.Input(default_text="0", key='-D20Mod-', size=(5,1)), sg.Button('RollD20'), sg.Text('  Result', key="-D20-")],
         [sg.Input(default_text="0", key='-NumD100-', size=(7,1)), sg.Text('D100 '), sg.Input(default_text="0", key='-D100Mod-', size=(5,1)), sg.Button('RollD100'), sg.Text('Result', key="-D100-")]]


window = sg.Window ('Ephemera', layout, text_justification='right')

def rollDice(num_die, type_die, mod):
    numberrolled = 0
    rollsvalue = 0
    while numberrolled < num_die:
        rollsvalue = rollsvalue + random.randrange(1,(type_die+1))
        numberrolled = numberrolled + 1
    return(rollsvalue + mod)


while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Cancel', 'Exit'):
        break
    if event == 'RollD4':
        window.FindElement("-D4-").Update(text_color='red', value =rollDice(int(values["-NumD4-"]), 4, int(values["-D4Mod-"])))
    if event == 'RollD6':
        window.FindElement("-D6-").Update(text_color='red', value =rollDice(int(values["-NumD6-"]), 6, int(values["-D6Mod-"])))
    if event == 'RollD8':
        window.FindElement("-D8-").Update(text_color='red', value =rollDice(int(values["-NumD8-"]), 8, int(values["-D8Mod-"])))
    if event == 'RollD10':
        window.FindElement("-D10-").Update(text_color='red', value =rollDice(int(values["-NumD10-"]), 10, int(values["-D10Mod-"])))
    if event == 'RollD12':
        window.FindElement("-D12-").Update(text_color='red', value =rollDice(int(values["-NumD12-"]), 12, int(values["-D12Mod-"])))
    if event == 'RollD20':
        window.FindElement("-D20-").Update(text_color='red', value =rollDice(int(values["-NumD20-"]), 20, int(values["-D20Mod-"])))
    if event == 'RollD100':
        window.FindElement("-D100-").Update(text_color='red', value =rollDice(int(values["-NumD100-"]), 100, int(values["-D100Mod-"])))

window.close()

exit()
