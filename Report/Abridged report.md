# 1 Introduction

## 1.1 Project motivation
Machine learning, neural networks, and artificial intelligence are becoming increasingly prevalent in everyone’s daily life. Amazon Alexa, Google Assistant, and Apple Siri are some of the most obvious uses of machine learning, taking advantage of deep learning and natural language processing (Pai), but machine learning has a variety of other uses.

Machine learning helps Amazon give shoppers purchase suggestions. It provides the support behind autonomous driving. It can even be used to provide a 1984-esque level of control over a large population. No matter what happens, machine learning/deep learning is here to stay, with even more applications undoubtedly on the horizon.

## 1.2 Project goals

The primary deliverable for this project was to create a simple virtual assistant using Python, taking advantage of previously built Python program modules. The virtual assistant activates once a certain keyword or phrase has been spoken. Once it detects the keyword, it then listens for other commands. The wake-up word that it detects is “Assistant”, similar to how Amazon’s virtual assistant, Alexa, will respond if you say “Alexa”. The virtual assistant works in real time, meaning that the virtual assistant will constantly listen for the word “Assistant”.

This assistant can execute simple commands, such as setting a timer, telling jokes, or telling the time. Using a text-to-speech program, the assistant can also respond back to the user.

Another major component of the project was creating a selfie function for the virtual assistant. This function allows the user to take pictures of themselves. What makes this function stand out is that it only allows the user to take a picture when it detects that both of the user’s eyes are open, ensuring that all selfies will have open eyes.

In the process of completing the objectives, I used pre-built machine learning packages to learn how others, including people in industry, might apply machine learning in their work. As a beginner in machine learning, I believe that this is an important first step in my machine learning/artificial intelligence education. Since I do not have much theoretical knowledge of machine learning yet, it is important that I utilize what others have built first, before creating my own machine learning programs.

Also, over the course of this project, prior work done in the field of machine learning and the applications of machine learning were investigated. This was done to better understand what types of work had already been accomplished in the field of machine learning, deepening my understanding of the history of the topic.

# 2 Description of approach – Tier 1
Because this project is more focused on serving as a primer into a very complicated subject, this project did not develop its own bespoke neural networks. Instead, it utilized programs written by others to complete the deliverables.

The primary theories of operation behind this virtual assistant are the speech-to-text and text-to-speech capabilities. They are also great examples of machine learning, giving me practice with applying machine learning enabled Python packages.

Like most other virtual assistants, the virtual assistant developed in this project is able to recognize speech to carry out commands. Furthermore, this virtual assistant can also verbally respond back to the user. Initially, though, the virtual assistant must first detect the keyword “assistant” before carrying out any command.

Alternatively, the assistant can also take in text as input. For example, if text input is enabled, then one would type commands into the virtual assistant instead of speaking the commands out loud. If text input is enabled, then the virtual assistant would respond to the user by printing text instead of speaking out loud.

The virtual assistant has a variety of functions or features it can execute, based on the user’s commands. If the user’s speech contains a certain keyword or phrase, then the appropriate command is executed. For instance, the trigger words for creating a note are “note”, “reminder”, “write this down”, and “remember”. If I wanted to set a reminder, I would say something like “Assistant, set a reminder”, and the assistant would carry out the steps needed to set a reminder, because it had detected the word “reminder”.

The major functions included in the assistant are as follows:

1.	Show a random image: shows a random image from the same directory as the project.
2.	Get the current time: tells the time, accounting also for a.m. and p.m.
3.	Get the current date: gives the current day, month, and year.
4.	Set a timer: sets a timer based on the number of minutes and seconds the user specified. When the timer counts down to 0, the assistant repeats the phrase “Your timer is done” three times.
5.	Create a reminder: creates a .txt file. If text input is disabled, then the user may dictate, through speaking, a note/reminder. If text input is enabled, then the user can write a note using text input.
6.	Talk to chatbot: this feature allows the user to have simple conversations with a basic chatbot.
7.	Open Google Chrome: opens the Google Chrome web browser.
8.	Take a selfie: allows the user to take a selfie only when both of the user’s eyes are open.


In addition to the major features that are listed, the virtual assistant can also say hello, introduce itself, and tell a joke.


Once the user is done using the virtual assistant, they can either speak the word “quit” or type “quit” (assuming text input is enabled).


One virtual assistant function that deserves special mention is the selfie feature. One problem that persists when trying to take a picture is that you might blink, ruining that picture. This virtual assistant’s selfie feature only allows the user to take a selfie once it detects that both of the user’s eyes are open. Once the virtual assistant hears the keyword “selfie”, then it activates the computer’s webcam. If the user presses “q” on the keyboard, and if the function detects that both eyes are open, then a picture is taken. The captured image is displayed and saved onto the computer.


Although this function is not very practical (because the user can simply try not to blink while taking a selfie), experimenting with different computer vision programs and packages before deciding on an implementation of the selfie function was a valuable learning experience for me. The computer vision programs/packages that were studied were OpenCV, face_recognition, and the Google Cloud Vision API.

