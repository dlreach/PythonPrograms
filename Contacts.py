import PySimpleGUI as sg
import pathlib
sg.ChangeLookAndFeel('BrownBlue') # change style
i = 1
dict = {}
WIN_W = 90
WIN_H = 25
file = None
keys_to_clear = [f'-Name-{i}-', '-Phone-', '-Email-', '-Bday-', '-Notes-']

menu_layout = [['File', ['New (Ctrl+N)', 'Open (Ctrl+O)', 'Save (Ctrl+S)', '---', 'Exit']],
              ['Tools'],
              ['Help', ['About']]]


layout = [[sg.Menu(menu_layout)],
          [sg.Text('Click to add a New Contact to the bottom.'), sg.B('+', key='-B2-'), sg.B("Sort", key='-B3-')],
          [sg.Text("Name", size=(13,1)), sg.Text("Phone Number", size=(13,1), justification="left"), sg.Text("Email", size=(22,1)), sg.Text("Birthday", size=(13,1)), sg.Text("Notes", size=(24,1))],
          [sg.Text(i), sg.Input(key=f'-Name-{i}-', size=(15,1)), sg.Input(key='-Phone-', size=(15,1)), sg.Input(key='-Email-', size=(25,1)), sg.Input(key='-Bday-', size=(15,1)), sg.Input(key='-Notes-', size=(25,1))]]


window = sg.Window('Contact Books', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
#
# def about_me():
#     '''A short, pithy quote'''
#     sg.popup_no_wait('"All great things have small beginnings" - Peter Senge')

while True:
    event, values = window.read()
    if event in ('Save (Ctrl+S)', 's:83'):
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            window.SaveToDisk(filename)
            # save(values)
    elif event in ('Open (Ctrl+O)', 'o:79'):
        filename = sg.popup_get_file('Load Settings', no_window=True)
        window.LoadFromDisk(filename)
        # load(form)
    if event == 'Clear':
        for key in keys_to_clear:
            window[key]('')
    if event in (None, 'Cancel', 'Exit'):
        break
    if event == '-B2-':
        i += 1
        window.extend_layout(window, [[sg.Text(i), sg.Input(key=f'-Name-{i}-', size=(15,1)), sg.Input(key=f'-Phone-{i}-', size=(15,1)), sg.Input(key=f'-Email-{i}-', size=(25,1)), sg.Input(key=f'-Bday-{i}-', size=(15,1)), sg.Input(key=f'-Notes-{i}-', size=(25,1))]])
    #if event == '-B3-':
        

    # if event == 'New Contact':
    #     layout.append([sg.Input(key='-Name1-', size=(15,1)), sg.Input(key='-Phone-', size=(15,1)), sg.Input(key='-Email-', size=(25,1)), sg.Input(key='-Bday-', size=(15,1)), sg.Input(key='-Notes-', size=(25,1))])

        #window1 = sg.Window('Contact Books', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
        #window.Close()
        #window = window1
    # if event in ('New (Ctrl+N)', 'n:78'):
    #     file = new_file()
    # if event in ('Open (Ctrl+O)', 'o:79'):
    #     file = open_file()
    # if event in ('Save (Ctrl+S)', 's:83'):
    #     save_file(file)
    # if event in ('Save As',):
    #     file = save_file_as()
    # if event in ('Word Count',):
    #     word_count()
    # if event in ('About',):
    #     about_me()

    window.close()

    exit()
