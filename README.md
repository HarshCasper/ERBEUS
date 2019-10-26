# ERBEUS

[![BCH compliance](https://bettercodehub.com/edge/badge/HarshCasper/ERBEUS?branch=master)](https://bettercodehub.com/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4efb701ff0c24a318051ee34a0eadf78)](https://www.codacy.com/manual/HarshCasper/ERBEUS?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=HarshCasper/ERBEUS&amp;utm_campaign=Badge_Grade)

ERBEUS is a Computer Assistant that has been coded on Python 3 Programming Language and is designed to serve as a Computer Assistant which can perform a variety of tasks like performing Google Search, Shutdown/Lock the Computer, fetching Wikipedia content, generating new passwords for us, generating weather reports for us and opening Computer Applications and even fetching is some jokes to help us out of our boredom.

## Requirements 

The Code has been written of Python 3.x with the following dependencies which needs to be installed using PIP before being used: 

- tkinter 
- random
- time
- ctypes
- requests
- pyperclip
- pyautogui
- OS
- webbrowser
- oneliners
- winshell
- wikipedia
- datetime
- pyttsx3

## Performance 

The Python Code can perform various tasks which are briefly listed below: 

- Generating a Password and copying it onto the Clipboard 
- Getting a random fact for the user from a Text File which can be edited to accomodate more facts 
- Lock or Shutdown the Computer
- Screenshot the present screen and save it as a PNG File 
- Empty Recycle-Bin 
- Fetching weather reports 
- Generate jokes when bored
- Track our location
- Opening various Computer Applications (Chrome, VLC, Command Prompt) and play Music and Movies too
- Fetch Information from Wikipedia 
- Perform Google Searches
- Respond to general inquiries and statements

It utilizes a GUI Model built on Tkinter to create an interface between the user and ERBEUS where the user can pass his command (the command must have keywords similar to given in the code which consists of his intent) to allow the ERBEUS to perform his task. It utilizes a pyttsx3 engine for speech conversion to give more functionality to the user. Further additions will be done in future which will allow the user to give Voice Commands for the Assistant using speech_recognition package.
