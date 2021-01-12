import PySimpleGUI as sg
from datetime import date

sg.ChangeLookAndFeel("DarkAmber")

today = date.today()
WIN_W = 90
WIN_H = 25
file = None

menu_layout = [['File', ['Open (Ctrl+O)', 'Save (Ctrl+S)', '---', 'Exit']],
              ['Tools'],
              ['Help', ['About']]]

keys_to_clear = ['-IN-','-IN1-','-IN2-','-IN3-','-IN4-','-IN5-','-IN6-','-IN7-','-IN8-','-IN9-','-IN10-','-IN11-','-IN12-','-IN13-', '-InNote1-', '-InNote2-', '-InNote3-', '-InNote4-',
                    '-InNote5-', '-InNote6-', '-InNote7-', '-InNote8-', '-InNote9-', '-InNote10-', '-InNote11-', '-InNote12-', '-InNote13-']

layout = [[sg.Menu(menu_layout)],
         [sg.Text('Ephemera Day Planner')],
         [sg.Text('Current Date: ', font=('Consolas', 10), key='_INFO_'), sg.Input(key='-IN-', size=(20,1)), sg.CalendarButton('Select Date', close_when_date_chosen=True,  target='-IN-', location=(0,0), no_titlebar=False, format = '%Y:%m:%d')],
         [sg.Text('8:00 AM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN1-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote1-', size=(20,1))],
         [sg.Text('9:00 AM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN2-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote2-', size=(20,1))],
         [sg.Text('10:00 AM:'), sg.Checkbox('Completed'), sg.Input(key='-IN3-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote3-', size=(20,1))],
         [sg.Text('11:00 AM:'), sg.Checkbox('Completed'), sg.Input(key='-IN4-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote4-', size=(20,1))],
         [sg.Text('12:00 AM:'), sg.Checkbox('Completed'), sg.Input(key='-IN5-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote5-', size=(20,1))],
         [sg.Text('1:00 PM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN6-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote6-', size=(20,1))],
         [sg.Text('2:00 PM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN7-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote7-', size=(20,1))],
         [sg.Text('3:00 PM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN8-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote8-', size=(20,1))],
         [sg.Text('4:00 PM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN9-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote9-', size=(20,1))],
         [sg.Text('5:00 PM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN10-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote10-', size=(20,1))],
         [sg.Text('6:00 PM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN11-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote11-', size=(20,1))],
         [sg.Text('7:00 PM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN12-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote12-', size=(20,1))],
         [sg.Text('8:00 PM:  '), sg.Checkbox('Completed'), sg.Input(key='-IN13-', size=(50,1)), sg.Text('Notes: '), sg.Input(key='-InNote13-', size=(20,1))],
         [sg.Button('OK'), sg.Button('Clear'), sg.Button('Cancel')]]


window = sg.Window('Ephemera', layout, text_justification='right')


while True:
    event, values = window.read()
    print(event, values)
    if event == 'Clear':
        for key in keys_to_clear:
            window[key]('')
    if event in ('Save (Ctrl+S)', 's:83'):
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            window.SaveToDisk(filename)
            # save(values)
    elif event in ('Open (Ctrl+O)', 'o:79'):
        filename = sg.popup_get_file('Load Settings', no_window=True)
        window.LoadFromDisk(filename)
        # load(form)
    if event in (None, 'Cancel', 'Exit'):
        break


window.close()

exit()
