Installation Instructions for Modules
=====================================

Certain required modules for the virtual assistant may be confusing to install. This document
clears up some of the confusion by providing instructions for the modules that can't be installed
directly using pip install.


How to install ChatterBot
-------------------------

ChatterBot is the package that allows for a simple chatbot.

1. Go to https://github.com/gunthercox/ChatterBot and download the ZIP folder of the master file
   (click on “Code” and then click on “Download ZIP”). Refer to this StackOverflow thread for more
   information: https://stackoverflow.com/questions/44925395/error-while-installing-chatterbot.

2. Extract the zip folder and cut and paste the extracted folder into
   the same location where you pasted the .whl file for PyAudio.

3. Open the “ChatterBot-master” folder.

4. Inside the terminal window, type in ``python setup.py install``. This should install the
   ChatterBot module. Refer to this webpage for more information:
   https://www.activestate.com/resources/quick-reads/how-to-manually-install-python-packages/.


How to install spaCy
--------------------

spaCy is package for advanced NLP (natural language processing). This package is a requirement for
the ChatterBot package.

1. Follow the steps to install PyAudio but install spacy-2.3.0-cp38-cp38-win_amd64.whl
   instead.

2. Then, run as administrator the following command in the cmd prompt:
   ``python -m spacy download en``

3. Note: there are several methods to run the Command Prompt as administrator

   a. Press Windows key + R. Type cmd, then press shift + control + enter.

   b. Press the Windows key and search for cmd. Right click on the “Command Prompt” result that
      shows up, then select “Run as administrator”.
