from MinorMusicGenerator import MinorMusicGenerator
from music21 import note, stream, chord
import random


def generate_music02(scale: int, filepath: str):
    OCTAVE_SHIFT = 12
    new_song_generator = MinorMusicGenerator(scale)
    myStream = stream.Stream()

    intervals = 30
    note_duration = [4, 2, 1, 0.66]
    number_of_notes = [2, 2, 8, 12]

    volumes = [100, 50, 60, 60, 70, 80, 100, 80, 70, 60, 50, 50]

    def add_one_interval(current_index=0, right_hand_shift: int = 0,
                         current_velocity: int = 90, left_hand_shift: int = 0):
        # generating notes for the right hand
        current_index_for_the_right_hand = current_index
        current_note_duration_index = random.randint(0, len(note_duration) - 1)
        current_number_of_notes = number_of_notes[current_note_duration_index]
        current_duration = note_duration[current_note_duration_index]
        shift: int = right_hand_shift * OCTAVE_SHIFT

        # generating the sequence of notes for the right hand
        for note_i in range(current_number_of_notes):
            if random.randint(0, 8) % 7 != 0:
                random_note = new_song_generator.correct_notes[random.randint(0, 6)] + shift
                my_note = note.Note(random_note, quarterLength=current_duration + 1.5)
                my_note.volume.velocity = current_velocity
                myStream.insert(current_index_for_the_right_hand, my_note)
            current_index_for_the_right_hand += current_duration

        # generating the sequence of notes for the left hand
        sequence_of_notes = new_song_generator.baselines[random.randint(0, 2)]

        for note_i in range(0, 12):
            cur_note = sequence_of_notes[note_i]
            if random.randint(0, 8) % 7 != 0:
                for note_in_a_chord in range(len(sequence_of_notes)):
                    note_in_a_chord += OCTAVE_SHIFT * left_hand_shift
                new_note = note.Note(cur_note, quarterLength=1.5)
                new_note.volume.velocity = volumes[note_i]
                myStream.insert(current_index, new_note)
            current_index += 0.33

    for i in range(intervals):
        add_one_interval(current_index=4 * i,
                         right_hand_shift=random.randint(-1, 1),
                         current_velocity=random.randint(80, 110),
                         left_hand_shift=random.randint(-3, -1))
    add_one_interval(current_index=4 * intervals, current_velocity=50)
    myStream.write('midi', fp=filepath)


if __name__ == '__main__':
    generate_music02(70, 'example.midi')
