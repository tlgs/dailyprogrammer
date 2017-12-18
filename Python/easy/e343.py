# 18/12/2017

def note(major_scale, solfege_name):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    solfege = {"Do": 0, "Re": 2, "Mi": 4, "Fa": 5, "So": 7, "La": 9, "Ti": 11}
    return notes[(notes.index(major_scale) + solfege[solfege_name]) % 12]
