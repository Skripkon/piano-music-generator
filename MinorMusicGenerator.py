class MinorMusicGenerator:
    # scale is a number from 59 (B) to 70 (Bb)
    def __init__(self, scale=60):
        self.minor_chords = None
        self.correct_notes = None
        self.baselines = None
        if not isinstance(scale, int):
            raise "scale must be an integer"
        elif scale < 59 or scale > 70:
            raise "scale must be in a range from 59 to 70"
        else:
            self.scale = scale
        self.correct_minor_chords()
        self.create_baselines()
        self.correct_notes()

    def correct_notes(self):
        shifts: list[int] = [0, 2, 3, 5, 7, 8, 10]
        notes = [(self.scale + shift) for shift in shifts]
        self.correct_notes = notes

    @classmethod
    def get_minor_chord(cls, note):
        return [note, note + 3, note + 7]

    def correct_minor_chords(self):
        first_chord = self.get_minor_chord(self.scale - 12)
        second_chord = self.get_minor_chord(self.scale + 5 - 12)
        third_chord = self.get_minor_chord(self.scale + 7 - 12)
        self.minor_chords = [first_chord, second_chord, third_chord]

    @staticmethod
    def create_one_baseline(scale):  # 12 notes separately: Scale - 24 ... Scale + 24 ... Scale - 21
        cur_note = scale - 24
        return [cur_note, cur_note + 3, cur_note + 7, cur_note + 12,
                cur_note + 15, cur_note + 19, cur_note + 24, cur_note + 19,
                cur_note + 15, cur_note + 12, cur_note + 7, cur_note + 3]

    def create_baselines(self):
        first_baseline = create_one_baseline(self.scale)
        second_baseline = create_one_baseline(self.scale + 5)
        third_baseline = create_one_baseline(self.scale + 7)
        self.baselines = [first_baseline, second_baseline, third_baseline]