from MinorMusicGenerator import MinorMusicGenerator
from music21 import note, chord, stream
import random


def generate_music01(scale: int, filepath: str):
    new_song_generator = MinorMusicGenerator(scale)
    myStream = stream.Stream()
    note_duration = [2, 1, 0.5]
    intervals = 20
    volumes = [100, 50, 60, 60, 70, 80, 100, 80, 70, 60, 50, 50]

    def add_one_interval(index: int, octave_shift_from_4: int = 0, velocity: int = 90):
        # generating notes for the right hand
        random_number = random.randint(0, 2)
        number_of_notes = 2 ** (random_number + 1)
        duration = note_duration[random_number]
        shift: int = octave_shift_from_4 * 12
        for note_i in range(number_of_notes):
            random_note = new_song_generator.correct_notes[random.randint(0, 6)] + shift
            my_note = note.Note(random_note, quarterLength=duration)
            my_note.volume.velocity = velocity
            myStream.append(my_note)

        # generating the chord for the left hand
        sequence_of_notes = new_song_generator.baselines[random.randint(0, 2)]
        for note_i in range(0, 12):
            cur_note = sequence_of_notes[note_i]
            new_note = note.Note(cur_note, quarterLength=0.33)
            new_note.volume.velocity = velocity
            new_note.volume.velocity = volumes[note_i]
            myStream.insert(index + (note_i / 3), new_note)

    for i in range(intervals):
        add_one_interval(4 * i, octave_shift_from_4=random.randint(-1, 0), velocity=random.randint(70, 120))
    add_one_interval(2 * intervals, velocity=50)
    myStream.write('midi', fp=filepath)

