import PySimpleGUI as sg
sg.theme("Darkred1")
sg.theme_text_color("#0000ff")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM    : 2210010145")],
                           [sg.Text("NAMA   : MUHAMMAD ZAINAL AQLI")],
                           [sg.Text("KELAS  : 5 N REG BANJARMASIN")],
                           [sg.Text("MATKUL : PEMROGRAMAN VISUAL 3")]],
                           size=(430,200),
                           font=("Times", 18))
window()
window.close()