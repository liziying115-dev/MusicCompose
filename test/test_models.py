import unittest
import os
import tempfile


def load_melodies(path: str) -> list[list[str]]:
    """Load melodies from a text file, each line is a melody with notes separated by spaces."""
    try:
        with open(path, 'r') as file:
            melodies = []
            for line in file:
                line = line.strip()
                if line:
                    notes = line.split()
                    melodies.append(notes)
            return melodies
    except FileNotFoundError:
        print(f"File not found: {path}")
        print("Please make sure the dataset file exists.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def save_melodies(melodies: list[list[str]], path: str) -> None:
    """Save melodies to a text file, one melody per line."""
    try:
        with open(path, 'w') as file:
            for melody in melodies:
                line = ' '.join(melody)
                file.write(line + '\n')
    except Exception as e:
        print(f"Error saving file: {e}")

def parse_note(note_str: str) -> tuple[str, float]:
    """Parse a note string like 'C4_0.25' into (note, duration)."""
    parts = note_str.split('_')
    if len(parts) == 2:
        note_name = parts[0]
        duration = float(parts[1])
        return note_name, duration
    else:
        raise ValueError(f"Invalid note format: {note_str}")


class TestMelodyFunctions(unittest.TestCase):
    
    def test_load_melodies_valid_file(self):
        """Test loading melodies from a valid file."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write('C4_0.25 D4_0.25 E4_0.5\n')
            f.write('G3_0.5 F3_0.25 C4_0.25\n')
            temp_path = f.name
        try:
            melodies = load_melodies(temp_path)
            self.assertEqual(len(melodies), 2)
            self.assertEqual(melodies[0], ['C4_0.25', 'D4_0.25', 'E4_0.5'])
            self.assertEqual(melodies[1], ['G3_0.5', 'F3_0.25', 'C4_0.25'])
        finally:
            os.unlink(temp_path)

    def test_load_melodies_nonexistent_file(self):
        """Test behavior when file does not exist."""
        melodies = load_melodies('nonexistent_file.txt')
        self.assertEqual(melodies, [])

    def test_load_melodies_skips_empty_lines(self):
        """Test that empty lines are ignored when loading melodies."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write('C4_0.25 D4_0.25\n')
            f.write('\n')
            f.write('E4_0.5 F4_0.25\n')
            temp_path = f.name
        try:
            melodies = load_melodies(temp_path)
            self.assertEqual(len(melodies), 2)
            self.assertEqual(melodies[0], ['C4_0.25', 'D4_0.25'])
            self.assertEqual(melodies[1], ['E4_0.5', 'F4_0.25'])
        finally:
            os.unlink(temp_path)

    def test_save_melodies_creates_file(self):
        """Test saving melodies writes correct file content."""
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as f:
            temp_path = f.name
        try:
            test_melodies = [
                ['C4_0.25', 'D4_0.25', 'E4_0.5'],
                ['G3_0.5', 'F3_0.25']
            ]
            save_melodies(test_melodies, temp_path)
            with open(temp_path, 'r') as f:
                lines = f.readlines()
            self.assertEqual(len(lines), 2)
            self.assertEqual(lines[0].strip(), 'C4_0.25 D4_0.25 E4_0.5')
            self.assertEqual(lines[1].strip(), 'G3_0.5 F3_0.25')
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)

    def test_save_and_load_round_trip(self):
        """Test saving and then loading melodies returns original data."""
        with tempfile.NamedTemporaryFile(delete=False, suffix='.txt') as f:
            temp_path = f.name
        try:
            original_melodies = [
                ['C4_0.25', 'D4_0.25', 'E4_0.5'],
                ['G3_0.5', 'F3_0.25'],
                ['A3_0.25', 'C4_0.25', 'E4_0.25']
            ]
            save_melodies(original_melodies, temp_path)
            loaded_melodies = load_melodies(temp_path)
            self.assertEqual(original_melodies, loaded_melodies)
        finally:
            if os.path.exists(temp_path):
                os.unlink(temp_path)

    def test_parse_note_valid(self):
        """Test parsing valid note strings."""
        name, duration = parse_note('C4_0.25')
        self.assertEqual(name, 'C4')
        self.assertAlmostEqual(duration, 0.25)
        name, duration = parse_note('A#3_0.5')
        self.assertEqual(name, 'A#3')
        self.assertAlmostEqual(duration, 0.5)

    def test_parse_note_invalid(self):
        """Test parsing invalid note strings raises ValueError."""
        with self.assertRaises(ValueError):
            parse_note('C4')  # Missing duration
        with self.assertRaises(ValueError):
            parse_note('InvalidNote')


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False, verbosity=2)
