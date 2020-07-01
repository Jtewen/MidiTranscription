"""
master.py recieves the midi input and 
routes it to the proper functions
"""


import mido
import midiparser
import identifier

notesPlay = []
inport = mido.open_input()


# logs the midi input as the msg variable
msg = inport.receive()

# handles the input and sends to midiparser.py to parse
for msg in inport:
    notesPlay = midiparser.refresh(notesPlay, midiparser.parse(msg))
    if notesPlay != []:
        print(identifier.noteCheck(notesPlay) + identifier.chordCheck(notesPlay))
    
