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

#Create Address Label
addressLabel = QLabel("Address: ", w)
addressLabel.move(310,20)
addressLabel.resize(330, 20)


#Create Value Label
value = QLabel("Value: ", w)
value.move(310,50)
value.resize(330,20)

#Create Realistic Value Label
realValueLabel = QLabel("Realistic Value: ", w)
realValueLabel.move(310,80)
realValueLabel.resize(330, 20)


#Create Bid Label
bidLabel = QLabel("Maximum Bid: ", w)
bidLabel.move(310,110)
bidLabel.resize(330, 20)


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
    realValueLabel.setText("Realistic Value: $" + realisticSale(address, zipCode))
    bidLabel.setText("Maximum Bid(@1.5x Profit): " + getMaxBid(address, zipCode))

    #app.exit()

# connect the signals to the slots
button.clicked.connect(on_click)

# Show the window and run the app
w.setFocus()
w.show()
app.exec_()
