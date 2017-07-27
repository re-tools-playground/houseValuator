import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from data import *
# create our window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('Home Value Calculator')

# Create textbox
textbox = QLineEdit(w)
textbox.setPlaceholderText("Address")
textbox.move(20, 20)
textbox.resize(280,40)

textbox2 = QLineEdit(w)
textbox2.setPlaceholderText("Zip Code")
textbox2.move(20, 90)
textbox2.resize(280,40)


#Create Value Label
value = QLabel()
# Set window size.
w.setFixedSize(460, 240)

# Create a button in the window
button = QPushButton('Calculate', w)
button.move(20,190)

# Create the actions
@pyqtSlot()
def on_click():
    address = textbox.text()
    zipCode = textbox2.text()
    print("Value: " + getResults(address, zipCode))

    #FIX THIS!
    #value.setText("Value: " + getResults(address, zipCode))
    app.exit()

# connect the signals to the slots
button.clicked.connect(on_click)

# Show the window and run the app
w.setFocus()
w.show()
app.exec_()
