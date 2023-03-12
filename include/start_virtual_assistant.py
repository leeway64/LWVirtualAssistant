import sys

import virtual_assistant_functions


# Implements the real time listening and text input capabilities of the virtual assistant.
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
