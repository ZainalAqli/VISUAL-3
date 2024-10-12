import PySimpleGUI as sg
sg.theme("Darkgreen4")
sg.theme_text_color("#ffff00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS", font=("arial",25))],
                           [sg.Text("NPM    : 2210010145")],
                           [sg.Text("NAMA   : MUHAMMAD ZAINAL AQLI")],
                           [sg.Text("KELAS  : 5 N REG BANJARMASIN")]],
                           size=(500,200),
                           font=("Times", 18))
window()
window.close()