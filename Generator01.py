from MinorMusicGenerator import MinorMusicGenerator
from music21 import note, chord, stream
import random


def generate_music01(scale: int, filepath: str):
    new_song_generator = MinorMusicGenerator(scale)
    new_song_generator.minor_chords += new_song_generator.additional_chords
    number_of_possible_chords = len(new_song_generator.minor_chords)
    myStream = stream.Stream()
    note_duration = [2, 1, 0.5]
    number_of_possible_durations = len(note_duration)
    intervals = 40

    def add_one_interval(index: int, octave_shift_from_4: int = 0, velocity: int = 90):
        # generating notes for the right hand
        random_number = random.randint(0, number_of_possible_durations - 1)
        number_of_notes = 2 ** random_number
        duration = note_duration[random_number]
        shift: int = octave_shift_from_4 * 12
        for note_i in range(number_of_notes):
            random_note = new_song_generator.correct_notes[random.randint(0, 6)] + shift
            my_note = note.Note(random_note, quarterLength=duration + 1)
            my_note.volume.velocity = velocity
            myStream.append(my_note)

        # generating the chord for the left hand

        random_chord = new_song_generator.minor_chords[random.randint(0, number_of_possible_chords - 1)]
        newChord = chord.Chord(random_chord)
        newChord.volume.velocity = 60
        myStream.insert(index, newChord)

    for i in range(intervals):
        add_one_interval(2 * i, octave_shift_from_4=random.randint(-1, 1), velocity=random.randint(70, 70))
    add_one_interval(2 * intervals, velocity=50)

    myStream.write('midi', fp=filepath)


if __name__ == '__main__':
    generate_music01(64, 'example.midi')
