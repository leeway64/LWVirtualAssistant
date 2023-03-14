# LWVirtualAssistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/leeway64/LWVirtualAssistant)

LWVirtualAssistant is a very basic voice-controlled virtual assistant that can take a selfie, set a
timer, and create a note, among other features.


## Installation
```bash
git clone https://github.com/leeway64/LWVirtualAssistant.git
cd LWVirtualAssistant
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For Ubuntu, you will also have to install portaudio by running `sudo apt install portaudio19-dev` before installing requirements.


## Usage
To use voice input to control the virtual assistant, run:
```bash
python include/start_virtual_assistant.py voice_input
```

To use text input to control the virtual assistant, run:
```bash
python include/start_virtual_assistant.py text_input
```

For a full list of tasks LWVirtualAssistant can perform, speak "help" if you are using voice input,
or type "help" if you are using text input. For example, if you are using text input:

```bash
$ python include/start_virtual_assistant.py text_input


...


Ready for a command
	Enter a command: assistant help

'LWVirtualAssistant usage'
	Every command must include "assistant" to activate the virtual assistant
	To quit, simply type "quit"

Feature			Trigger word(s)/usage

Say hello			hello
Introduce self		your name
Tell a joke			joke
Display date		date
Display time		the time
Set a timer			timer for [MIN] minutes, [SEC] seconds (MIN and SEC being numerals)
Take a selfie		selfie
Create a note		note, reminder, write this down, remember
Print usage			help
```

### Example
Here is an example LWVirtualAssistant session, using shown here with text input enabled for ease of
demonstration:

```bash
$ python include/start_virtual_assistant.py text_input


 _     __        ____     __ _        _                  _     _               _       _                  _   
| |    \ \      / /\ \   / /(_) _ __ | |_  _   _   __ _ | |   / \    ___  ___ (_) ___ | |_   __ _  _ __  | |_ 
| |     \ \ /\ / /  \ \ / / | || '__|| __|| | | | / _` || |  / _ \  / __|/ __|| |/ __|| __| / _` || '_ \ | __|
| |___   \ V  V /    \ V /  | || |   | |_ | |_| || (_| || | / ___ \ \__ \\__ \| |\__ \| |_ | (_| || | | || |_ 
|_____|   \_/\_/      \_/   |_||_|    \__| \__,_| \__,_||_|/_/   \_\|___/|___/|_||___/ \__| \__,_||_| |_| \__|
                                                                                                              


Ready for a command
	Enter a command: hello assistant
Hello to you too

Ready for a command
	Enter a command: assistant, what is your name
My name is LWVirtualAssistant, pleased to meet you.

Ready for a command
	Enter a command: assistant, what is the date
The date is 12 March 2023

Ready for a command
	Enter a command: assistant, what is the time
The time is 5 29 p.m.

Ready for a command
	Enter a command: take a selfie
Trigger phrase was not detected. Please include "assistant" in your command.

Ready for a command
	Enter a command: quit

Thank you for using this virtual assistant!
```


## Documentation
This project was part of an undergraduate research project, completed in August 2020. You may read
more about this project in the [documentation](doc/README.md).


## References
I would like to thank UW Bothell professor Dr. Kaibao Nie for giving me helpful suggestions
throughout this project.

Refer to the [bibliography](doc/Bibliography.md) for all sources behind this project.


## Third-Party Software
- [gTTS](https://pypi.org/project/gTTS/) (MIT License): Google Text-to-Speech.
- [OpenCV](https://pypi.org/project/opencv-python/) (MIT License): Open Source Computer Vision
  Library.
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) (BSD-3-Clause, GPL-2.0): Speech
  recognition using Python.
- [Playsound](https://pypi.org/project/playsound/) (MIT License): Package for playing sounds using
  Python.
- [ART](https://pypi.org/project/art/) (MIT License): ASCII art Python module.
