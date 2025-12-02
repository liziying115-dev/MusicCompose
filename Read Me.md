
# TECHIN 509: 01 

## Overview
This project aims to design a simple music composer using **Python**. The composer will automatically generate short melodies following basic musical rules. 

## Input
### Information needed
* Key Notes & Pitch
* Music Style
* Length of Melody
* BPM
* ending notes: ./

### Input from users - **optional**.
* Users can provide inputs to adjust the outcomes.
  

## Output
* Text based 
  * Melody (D major, 100 BPM)
* Melody Visualizaiton based on the pitch.
* **MIDI file** saved as melody.mid for playback.

### Output Example:
Generated Melody: ('C4', 0.5), ('E4', 1.0)

### Representation 
* Pitch: letter + octave (A3, B2)
* Optional: Accidental (sharp # or flat b)
* Beats:
  * 1.0 → quarter note
  * 0.5 → eighth note
  * 2.0 → half note

## Logic
### How does the program decide what note comes next?
**Rule-based system**
  * Follows melodic patterns, and avoid melodies like large jumps, prefer stepwise motion.
### How does the program know when to terminate music generation?
* Include a logical “ending” rule to end on the tonic note.

## Extensions
### Blockers for generating longer pieces
* Random generation may sound chaotic.
* Repetitive pattern/rhythm
* Long pieces need various structures to remain interesting