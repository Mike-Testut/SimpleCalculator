import FreeSimpleGUI as gui

output_box = gui.Text("1 + 2 * 3")
button0 = gui.Button("0")
button1 = gui.Button("1")
button2 = gui.Button("2")
button3 = gui.Button("3")
button4 = gui.Button("4")
button5 = gui.Button("5")
button6 = gui.Button("6")
button7 = gui.Button("7")
button8 = gui.Button("8")
button9 = gui.Button("9")

column1 =gui.Column([[button1], [button4], [button7]])
column2 =gui.Column([[button2], [button5], [button8], [button0]])
column3 =gui.Column([[button3], [button6], [button9]])
layout = [[output_box],
          [column1,column2,column3],]
window = gui.Window(title="calculator", layout=layout)
window.read()
window.close()