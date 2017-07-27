import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

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
textbox.setPlaceholderText("Zip Code")
textbox2.move(20, 90)
textbox2.resize(280,40)
# Set window size.
w.setFixedSize(460, 240)

# Create a button in the window
button = QPushButton('Submit', w)
button.move(20,190)

# Create the actions
@pyqtSlot()
def on_click():
    address = textbox.text()
    zipCode = textbox2.text()


# connect the signals to the slots
button.clicked.connect(on_click)

# Show the window and run the app
w.setFocus()
w.show()
app.exec_()
