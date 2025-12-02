# TECHIN 509: Melody Generator

## Overview
This project is a simple **AI-powered music composer** built with Python that automatically generates short melodies using a **bigram statistical model**. The program learns patterns from existing melodies and creates new, musically coherent sequences that follow similar note-to-note transitions.

## Features
- **Bigram Model Training** - Learns note transition patterns from melody datasets
- **Melody Generation** - Creates new melodies based on learned patterns
- **File I/O** - Load training data and save generated melodies
- **MIDI Playback** - Converts melodies to MIDI files and plays them
- **Unit Testing** - Includes comprehensive tests for reliability
- **Customizable Parameters** - Adjust tempo, length, and number of melodies

## Project Structure
```
TECHIN509/
├── data/
│   └── melody.txt              # Training dataset (input melodies)
├── output/
│   ├── generated_melodies.txt  # Generated melodies (text format)
│   └── melody_*.mid            # Generated MIDI files
├── MusicComp.ipynb             # Main implementation with playback
├── Melody Generation.ipynb     # Core generation algorithms
├── Melody_Representation.ipynb # Data structure documentation
└── README.md                   # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or VSCode with Jupyter extension

### Install Dependencies
```bash
pip install midiutil pygame
```

## Usage

### Quick Start
1. **Prepare your training data**: Create `data/melody.txt` with one melody per line
   ```
   E4_0.25 E4_0.25 E4_0.5 C4_0.25 E4_0.5
   C4_0.5 D4_0.5 E4_1.0 F4_0.5 G4_2.0
   ```

2. **Run the notebook**: Use Part 3 cell in `MusicComp.ipynb`. There may be too many repeated notes. Please try again.

3. **Listen to your generated music**: The program will automatically play the generated melodies!

### Example
```python
# Generate and play 3 melodies
melodies, midi_files = generate_and_play_music(
    input_path='data/melody.txt',
    output_dir='output',
    num_melodies=3,
    melody_length=8,
    tempo=120,
    auto_play=True
)
```

### Advanced Options
```python
# Generate longer, faster melodies without auto-play
generate_and_play_music(
    input_path='data/melody.txt',
    num_melodies=5,
    melody_length=16,
    tempo=150,
    auto_play=False
)

# Replay a specific melody
play_midi('output/melody_1.mid')
```

## Input Format

### Training Data (`data/melody.txt`)
Each line represents one melody. Notes are space-separated in the format:
```
PITCH_DURATION
```

**Examples:**
- `C4_0.25` - C in octave 4, quarter note (0.25 beats)
- `F#5_1.0` - F# in octave 5, whole note (1.0 beat)
- `Bb3_0.5` - B-flat in octave 3, half note (0.5 beats)

**Sample melody:**
```
C4_0.25 D4_0.25 E4_0.5 F4_0.5 G4_1.0
```

## Output

### Text Format (`output/generated_melodies.txt`)
Generated melodies saved in the same format as input:
```
C4_0.5 E4_0.25 G4_1.0 A4_0.5
D4_0.25 F4_0.5 E4_0.25 C4_2.0
```

### MIDI Files (`output/melody_*.mid`)
- Playable in any MIDI-compatible software (GarageBand, QuickTime, etc.)
- Automatically played through pygame during generation
- Can be opened in music production software for further editing

## How It Works

### 1. Bigram Model
The program builds a **statistical model** that tracks which notes typically follow other notes:
```
C4 → {D4: 3 times, E4: 1 time, G4: 2 times}
D4 → {E4: 2 times, F4: 1 time}
```

### 2. Generation Algorithm
1. Start with a beginning token (`^`)
2. Look up possible next notes from the bigram model
3. Choose next note randomly, weighted by frequency
4. Repeat until reaching end token (`$`) or max length
5. Add random durations from common note values

### 3. MIDI Conversion
- Converts note strings (e.g., `C4_0.5`) to MIDI note numbers
- Creates a MIDI file with proper timing and tempo
- Uses pygame to play through system audio

## Customization

### Adjust Tempo
```python
tempo=60   # Slow (1 beat per second)
tempo=120  # Moderate (default)
tempo=180  # Fast
```

### Change Duration Options
Edit the `generate_melody()` function:
```python
durations = [0.25, 0.5, 1.0, 2.0]  # Quarter, half, whole, double whole
```

### Musical Constraints
Add rules to avoid unmusical patterns:
```python
# Avoid large jumps
# Prevent note repetition (3+ times)
# End on tonic note
```

## Testing
The project includes unit tests in `MusicComp.ipynb`:
```python
# Run tests
unittest.main(argv=[''], exit=False, verbosity=2)
```

**Tests cover:**
- File loading and saving
- Note parsing and validation
- Empty line handling
- Missing file handling

## Limitations & Future Improvements

### Current Limitations
- Random generation may occasionally sound chaotic
- Simple bigram model doesn't capture long-term structure
- Limited rhythm variation
- No harmonic considerations

### Potential Extensions
- **Trigram/N-gram models** for better context
- **Duration modeling** based on training data patterns
- **Key signature enforcement** (scale constraints)
- **Rhythm patterns** separate from pitch
- **Multi-track generation** (melody + harmony)
- **Longer compositions** with verse/chorus structure
- **Style transfer** between different musical genres
