import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from data import *
# create our window
app = QApplication(sys.argv)
app.setWindowIcon(QIcon('home.png'))
w = QWidget()
w.setWindowTitle('Home Value Calculator')

# Create textbox
textbox = QLineEdit(w)
textbox.setPlaceholderText("Address")
textbox.move(20, 20)
textbox.resize(280,30)

textbox2 = QLineEdit(w)
textbox2.setPlaceholderText("Zip Code")
textbox2.move(20, 70)
textbox2.resize(280,30)

textbox3 = QLineEdit(w)
textbox3.move(250, 170)
textbox3.resize(90,20)
textbox3.isReadOnly()


textbox4 = QLineEdit(w)
textbox4.move(250, 140)
textbox4.resize(330,20)
textbox4.isReadOnly()
#Create Value Label
value = QLabel()
# Set window size.
w.setFixedSize(600, 210)

# Create a button in the window
button = QPushButton('Calculate', w)
button.move(20,170)

# Create the actions
@pyqtSlot()
def on_click():
    address = textbox.text()
    zipCode = textbox2.text()
    #print("Value: " + getResults(address, zipCode))

    #FIX THIS!
    textbox3.setPlaceholderText("Value: " + getResults(address, zipCode))
    textbox4.setPlaceholderText("Address: " + getAddress(address, zipCode))
    #app.exit()

# connect the signals to the slots
button.clicked.connect(on_click)

# Show the window and run the app
w.setFocus()
w.show()
app.exec_()
