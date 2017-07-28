import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from data import *
# create our window
app = QApplication(sys.argv)
app.setWindowIcon(QIcon('home.png'))
w = QWidget()
w.setWindowTitle('Home Value Calculator')

# Create addressBox
addressBox = QLineEdit(w)
addressBox.setPlaceholderText("Address")
addressBox.move(20, 20)
addressBox.resize(280,30)

postalBox = QLineEdit(w)
postalBox.setPlaceholderText("Zip Code")
postalBox.move(20, 70)
postalBox.resize(280,30)

#Create Value Label
value = QLabel("", w)
value.move(250,170)
value.resize(330,20)

addressLabel = QLabel("", w)
addressLabel.move(250,140)
addressLabel.resize(330, 20)
# Set window size.
w.setFixedSize(600, 210)

# Create a button in the window
button = QPushButton('Calculate', w)
button.move(20,170)

# Create the actions
@pyqtSlot()
def on_click():
    address = addressBox.text()
    zipCode = postalBox.text()
    value.setText("Value: " + getResults(address, zipCode))
    addressLabel.setText(getAddress(address, zipCode))

    #app.exit()

# connect the signals to the slots
button.clicked.connect(on_click)

# Show the window and run the app
w.setFocus()
w.show()
app.exec_()
