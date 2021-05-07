# Telegram text counter
    Created by Samuel Luke

This program iterates through Telegram message history and returns statistics on how many total messages, total characters, and average characters are sent by each member of the conversation. Works for any single conversation of any group size. 

Usage: python run.py [name of json file]

In order to count the messages, you must place the text history as a .json file in the same directory as run.py. 

This json file can be obtained from:
Telegram Desktop -> any conversation -> settings -> export chat history -> change "Format" to "Machine-readable JSON" -> "Export"

***Requires MatPlotLib***