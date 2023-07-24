# Domain Sniper - Python Application
This python application checks whether domains are available for purchase using the Wix API and the GoDaddy API. If they are available, it sends an email to notify the user.

<br>

## Requirements
- Python3: [python.org/downloads](https://www.python.org/downloads/)
- Gmail Account: [mail.google.com](https://mail.google.com/)
- GoDaddy API: [developer.godaddy.com](https://developer.godaddy.com/)

<br>

## Installation 
Using the python domain sniper requires a Gmail app specific password: [support.google.com](https://support.google.com/accounts/answer/185833)

1. Input each value into the main.py file:

![inputs in main.py file](img/mainpy.jpg)

2. Execute "python3 main.py" to run the sniper.

All of the packages used in the application are default Python packages. There is no installation required as long as you have Python 3.

<br>

## Continuous Running
Using [PythonAnywhere](https://pythonanywhere.com/), the script can run 24/7 - this is done using the "task" function. 
