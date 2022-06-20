# LWVirtualAssistant
LWVirtualAssistant is a basic voice-controlled virtual assistant that can take a selfie, set a
timer, and create a note, among other features. 


## Installation
LWVirtualAssistant is compatible with Ubuntu.


```sh
git clone https://github.com/leeway64/LWVirtualAssistant.git
sudo apt install portaudio19-dev
pip install -r requirements.txt
```


## Examples

### Using voice input

```
python include/start_virtual_assistant.py voice_input
```


### Using text input

```
python include/start_virtual_assistant.py text_input
```


## Documentation
This project was part of an undergraduate research project, completed in August 2020. You may read
more about this project in the [documentation](doc/README.md).


## References
I would like to thank UW Bothell professor Dr. Kaibao Nie for giving me helpful suggestions
throughout this project.

Refer to the [bibliography](doc/Bibliography.md) for all sources behind this project.


## Third-party tools

- [gTTS](https://pypi.org/project/gTTS/) (MIT License): Google Text-to-Speech.
- [OpenCV](https://pypi.org/project/opencv-python/) (MIT License): Open Source Computer Vision
  Library.
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) (BSD-3-Clause, GPL-2.0): Speech
  recognition using Python.
- [Playsound](https://pypi.org/project/playsound/) (MIT License): Package for playing sounds using
  Python.

