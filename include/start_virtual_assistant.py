# This program implements the real time listening capability of the virtual assistant. It also
# implements text input capability to the virtual assistant.
import sys

import virtual_assistant_functions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise RuntimeError("Incorrect number of arguments. Enter either \"text_input\" or \"voice_input\".")

    cli_arg = sys.argv[1]
    if cli_arg == "text_input":
        enable_text_input = True
    elif cli_arg == "voice_input":
        enable_text_input = False
    else:
        raise RuntimeError("Invalid argument. Enter either \"text_input\" or \"voice_input\".")
    
    
    virtual_assistant_functions.activate_virtual_assistant(enable_text_input)

