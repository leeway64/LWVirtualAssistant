# This program implements the real time listening capability of the virtual assistant. It also
# implements text input capability to the virtual assistant.
# This program also allows the user to chat with a simple chatbot.
import virtual_assistant_functions

if __name__ == "__main__":
    enable_text_input = False
    virtual_assistant_functions.activate_virtual_assistant(enable_text_input)
