import mido

emptyNote = []
notesPlay = []
inport = mido.open_input()
msg = inport.receive()


# assigning midi values to notes
cnotes = [36,48,60,72,84]
csnotes = [x + 1 for x in cnotes]
dnotes = [x + 2 for x in cnotes]
dsnotes = [x + 3 for x in cnotes]
enotes = [x + 4 for x in cnotes]
fnotes = [x + 5 for x in cnotes]
fsnotes = [x + 6 for x in cnotes]
gnotes = [x + 7 for x in cnotes]
gsnotes = [x + 8 for x in cnotes]
anotes = [x + 9 for x in cnotes]
asnotes = [x + 10 for x in cnotes]
bnotes = [x + 11 for x in cnotes]

# chord definitions
majTri = [0,4,7]
majSix = [0,4,7,9]
domSev = [0,4,7,10]
majSev = [0,4,7,11]
augTri = [0,4,8]
augSev = [0,4,8,10]
minTri = [0,3,7]
minSix = [0,3,7,9]
minSev = [0,3,7,10]
minMajSev = [0,3,7,11]
dimTri = [0,3,6]
dimSev = [0,3,6,9]
halfDimSev = [0,3,6,10]


def ccheck(notes):
    base = notes[0]
    notes.sort()
    basenote = 'c'
    
    # checks the note for the chord
    if base in cnotes:
        basenote = 'C'
    elif base in csnotes:
        basenote = 'C#'
    elif base in dnotes:
        basenote = 'D'
    elif base in dsnotes:
        basenote = 'D#'
    elif base in enotes:
        basenote = 'E'
    elif base in fnotes:
        basenote = 'F'
    elif base in fsnotes:
        basenote = 'F#'
    elif base in gnotes:
        basenote = 'G'
    elif base in gsnotes:
        basenote = 'G#'
    elif base in anotes:
        basenote = 'A'
    elif base in asnotes:
        basenote = 'A#'
    elif base in bnotes:
        basenote = 'B'


    # checks the chord type
    notes = [x - base for x in notes]
    if notes == majTri:
        print(basenote + ' Major Triad')
    elif notes == majSix:
        print(basenote + ' Major Sixth Chord')
    elif notes == domSev:
        print(basenote + ' Dominant Seventh Chord')
    elif notes == majSev:
        print(basenote + ' Major Seventh Chord')
    elif notes == augTri:
        print(basenote + ' Augmented Triad')
    elif notes == augSev:
        print(basenote + ' Augmented Seventh Chord')
    elif notes == minTri:
        print(basenote + ' Minor Triad')
    elif notes == minSix:
        print(basenote + ' Minor Sixth Chord')
    elif notes == minSev:
        print(basenote + ' Minor Seventh Chord')
    elif notes == minMajSev:
        print(basenote + ' Minor-Major Seventh Chord')
    elif notes == dimTri:
        print(basenote + ' Diminished Triad')
    elif notes == dimSev:
        print(basenote + ' Diminished Seventh Chord')
    elif notes == halfDimSev:
        print(basenote + ' Half-diminished Seveneth Chord')
    else:
        print(basenote)


for msg in inport:
    if msg.type == 'note_off':
        if msg.note in notesPlay:
            notesPlay.remove(msg.note)
            if len(notesPlay) >0:
                ccheck(notesPlay)
    else:
        notesPlay.append(msg.note)
        ccheck(notesPlay)
    