class MinorMusicGenerator:
    # notes in music21 are enumerated from 0 to 127
    # C4 (middle C) = 60
    # scale is a number from 59 (B) to 70 (Bb)
    def __init__(self, scale=60):
        self.minor_chords = None
        self.correct_notes = None
        self.baselines = None
        # check if scale is integer and in a range of (59, 70)
        if not isinstance(scale, int):
            raise ValueError("scale must be an integer")
        elif scale < 59 or scale > 70:
            raise ValueError("scale must be in a range from 59 to 70")
        else:
            # If the scale is valid, it sets the scale attribute, and then calls two methods:
            self.scale = scale
        self.correct_minor_chords()
        self.create_baselines()
        self.calculate_correct_notes()

    # calculates a list of corrected notes based on a predefined set of shifts.
    # store the result in the correct_notes attribute.
    def calculate_correct_notes(self):
        shifts = [0, 2, 3, 5, 7, 8, 10]
        notes = [(self.scale + shift) for shift in shifts]
        self.correct_notes = notes

    # creates a minor chord based on a given note
    @classmethod
    def get_minor_chord(cls, note):
        return [note, note + 3, note + 7]

    # creates three minor chords using the get_minor_chord method.
    # The chords are based on the current scale, shifted by specific values.
    # The resulting chords are stored in the minor_chords attribute.
    def correct_minor_chords(self):
        first_chord = self.get_minor_chord(self.scale - 12)
        second_chord = self.get_minor_chord(self.scale + 5 - 12)
        third_chord = self.get_minor_chord(self.scale + 7 - 12)
        self.minor_chords = [first_chord, second_chord, third_chord]

    # creates a sequence of notes for the left hand
    @staticmethod
    def create_one_baseline(scale):
        cur_note = scale - 24
        return [cur_note, cur_note + 3, cur_note + 7, cur_note + 12,
                cur_note + 15, cur_note + 19, cur_note + 24, cur_note + 19,
                cur_note + 15, cur_note + 12, cur_note + 7, cur_note + 3]

    # creates 3 different sequences of notes for the left hand
    def create_baselines(self):
        first_baseline = self.create_one_baseline(self.scale)
        second_baseline = self.create_one_baseline(self.scale + 5)
        third_baseline = self.create_one_baseline(self.scale + 7)
        self.baselines = [first_baseline, second_baseline, third_baseline]