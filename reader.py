import mido

emptyNote = []
notesPlay = []
inport = mido.open_input()
msg = inport.receive()

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
    notes.sort()
    base = notes[0]
    notes = [x - base for x in notes]
    if notes == majTri:
        print('Major Triad')
    elif notes == majSix:
        print('Major Sixth Chord')
    elif notes == domSev:
        print('Dominant Seventh Chord')
    elif notes == majSev:
        print('Major Seventh Chord')
    elif notes == augTri:
        print('Augmented Triad')
    elif notes == augSev:
        print('Augmented Seventh Chord')
    elif notes == minTri:
        print('Minor Triad')
    elif notes == minSix:
        print('Minor Sixth Chord')
    elif notes == minSev:
        print('Minor Seventh Chord')
    elif notes == minMajSev:
        print('Minor-Major Seventh Chord')
    elif notes == dimTri:
        print('Diminished Triad')
    elif notes == dimSev:
        print('Diminished Seventh Chord')
    elif notes == halfDimSev:
        print('Half-diminished Seveneth Chord')


for msg in inport:
    if msg.type == 'note_off':
        if msg.note in notesPlay:
            notesPlay.remove(msg.note)
            if len(notesPlay) >0:
                ccheck(notesPlay)
            else:
                print(emptyNote)
    else:
        notesPlay.append(msg.note)
        ccheck(notesPlay)
    