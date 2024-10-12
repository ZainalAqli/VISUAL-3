import PySimpleGUI as sg
sg.theme("Darkgreen4")
sg.theme_text_color("#ffff00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("FTI UNISKA", font=("Helvetica",24))],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
                           [sg.Text("UNISKA MAB BANJARMASIN")]],
                           size=(430,200),
                           font=("Times", 18))
window()
window.close()