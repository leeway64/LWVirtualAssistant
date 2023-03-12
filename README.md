# LWVirtualAssistant
LWVirtualAssistant is a very basic voice-controlled virtual assistant that can take a selfie, set a
timer, and create a note, among other features.


## Installation
```bash
git clone https://github.com/leeway64/LWVirtualAssistant.git
cd LWVirtualAssistant
pip install -r requirements.txt
```
For Ubuntu, you will also have to install portaudio by running `sudo apt install portaudio19-dev`.


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
