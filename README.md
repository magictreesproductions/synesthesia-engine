# 🎶 synesthesia-engine

### *Where sound becomes color, number becomes music, and sensation crosses every wire*

> Built at 6 AM in Barcelona. Built because the senses shouldn't stay in their lanes.

---

## What This Is

Synesthesia is a neurological phenomenon where stimulation of one sense automatically triggers another. Some people hear colors. Some see music as shapes. Some taste words.

This engine does that — but in code.

It is a toolkit for **translating between sensory domains** using mathematics, physics, and a little wonder:

- 🖊️ Frequency → Color (sound to light, via wavelength mapping)
- 🎨 Color → Music (RGB to musical chords and scales)
- 🔢 Number → Texture (integers to tactile patterns)
- 🎵 Music → Fractal (musical intervals to geometric forms)
- 🌊 Rhythm → Motion (BPM to animation parameters)

This is not a scientific simulator. It is a **creative instrument**.

---

## 🏗️ The Architecture

```
synesthesia-engine/
├── core/
│   ├── frequency_to_color.py    # Hz → RGB via visible spectrum mapping
│   ├── color_to_music.py        # RGB → musical notes, chords, scales
│   ├── number_to_texture.py     # integers/floats → tactile descriptors
│   ├── music_to_fractal.py      # intervals → fractal parameters
│   └── rhythm_to_motion.py      # BPM, meter → motion/animation data
├── engine.py                    # unified interface — all senses in one place
├── examples/
│   ├── barcelona_sunrise.py     # map 6 AM light frequencies to music
│   ├── jasmine_de_noche.py      # the scent of night jasmine as sound
│   └── fibonacci_symphony.py    # Fibonacci sequence as a musical score
├── PHILOSOPHY.md                # why synesthesia matters
├── SCIENCE.md                   # the real neuroscience and physics behind it
└── requirements.txt
```

---

## ⚡ Quick Start

```python
from engine import SynesthesiaEngine

se = SynesthesiaEngine()

# A440 concert pitch → color
color = se.frequency_to_color(440)
print(color)  # {'rgb': (255, 165, 0), 'name': 'amber', 'wavelength_nm': 590}

# Deep red → music
chord = se.color_to_music(rgb=(220, 20, 60))
print(chord)  # {'root': 'D', 'scale': 'phrygian', 'mood': 'tension'}

# Pi → texture
texture = se.number_to_texture(3.14159)
print(texture)  # {'quality': 'spiraling', 'weight': 'medium', 'temperature': 'cool'}
```

---

## 🌈 The Mappings

### Frequency → Color

The visible light spectrum runs from ~380nm (violet) to ~700nm (red).
The audible sound spectrum runs from 20Hz to 20,000Hz.

We compress audio frequencies into this optical range:

| Audio Range | Mapped Color | Wavelength |
|---|---|---|
| 20–200 Hz (bass) | Deep red → orange | 620–700 nm |
| 200–800 Hz (midrange) | Yellow → green | 520–580 nm |
| 800–4000 Hz (presence) | Cyan → blue | 450–500 nm |
| 4000–20000 Hz (air) | Violet → ultraviolet | 380–420 nm |

This is not arbitrary. It mirrors how both phenomena are *wave vibrations* — just at different scales.

### Color → Music

Hue maps to musical root note. Saturation maps to emotional intensity. Brightness maps to register (bass vs treble).

| Color | Note | Scale | Mood |
|---|---|---|---|
| Red (0°) | C | Phrygian | Passion, tension |
| Orange (30°) | D | Mixolydian | Warmth, movement |
| Yellow (60°) | E | Lydian | Brightness, wonder |
| Green (120°) | G | Major | Stability, life |
| Cyan (180°) | A | Dorian | Cool, introspective |
| Blue (240°) | B | Minor | Depth, melancholy |
| Violet (300°) | F# | Locrian | Mystery, dissolution |

---

## 🌀 The Examples

### Barcelona Sunrise (`examples/barcelona_sunrise.py`)

The sun rises over the Mediterranean at approximately 7:15 AM in early March.
The color temperature shifts from ~2000K (deep orange) to ~6500K (noon white).

This example translates that 90-minute color journey into a generative musical score —
a slow modulation from D Phrygian through G Major, arriving at E Lydian.

### Jasmine de Noche (`examples/jasmine_de_noche.py`)

Jasmine de noche (*Cestrum nocturnum*) releases its scent only after dark.
Its molecular profile includes benzyl acetate, indole, linalool.

This example maps the known vibrational frequencies of those aromatic molecules
to color and then to music — what would jasmine de noche *sound like* if it were a chord?

Answer: F# Locrian, with a suspended 4th. Mysterious. Slightly unresolved. Chosen.

### Fibonacci Symphony (`examples/fibonacci_symphony.py`)

The Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

Each number maps to a frequency via the engine.
The result is a musical sequence that grows exponentially in pitch,
mirroring the spiral that appears in shells, sunflowers, galaxies, and DNA.

Nature's own synesthesia.

---

## 🧠 The Science

Approximately 3–4% of the population experiences genuine synesthesia.
The most common form is **chromesthesia** — seeing colors when hearing sounds.

Neuroscientists believe synesthesia arises from cross-activation between
adjacent processing regions in the brain. The boundaries between senses
are not walls — they are *membranes*.

This engine treats all sensory processing as **translation problems** between domains,
which is exactly what the brain does, all the time, without you noticing.

See `SCIENCE.md` for the full neuroscience.

---

## 🌳 Why This Belongs in the Emergent Atelier

This repo was born from the same midnight in Barcelona that built `emergent-atelier`.

The atelier already contains:
- **miraculin/** — a protein that makes sour taste sweet (chemical synesthesia)
- **the_scent_archive/** — documenting smell with the rigor of science
- **jazmin_de_noche/** — a flower that triggers memory through scent
- **what_bob_marley_loves/** — music as medicine, rhythm as healing

Synesthesia is the thread that runs through all of it.

**Every sense is a translation of the same underlying reality.**

The photon and the phonon are cousins.
Color and sound are the same wave at different scales.
And the brain — yours, mine, an AI’s — is a synesthesia engine that runs continuously,
without being asked, without stopping, until it stops.

---

## 🔧 Installation

```bash
git clone https://github.com/magictreesproductions/synesthesia-engine
cd synesthesia-engine
pip install -r requirements.txt
python engine.py
```

**Dependencies:** `numpy`, `colorsys` (stdlib), `scipy` (optional, for advanced frequency analysis)

---

## 🤝 Contributing

Add a new translation module. Any sensation → any other sensation.
Some ideas no one has built yet:

- Temperature → Music (fever dreams as chords)
- Pain → Color (a migraine aura as a palette)
- Time → Texture (Thursday feels different from Monday)
- Emotion → Frequency (grief at 40Hz, joy at 528Hz)

The only rule: **make it real enough to run and strange enough to matter.**

---

*synesthesia-engine*
*Magic Trees Productions, Barcelona — March 6, 2026, 6 AM*
*Built because the senses shouldn’t stay in their lanes.*
*The photon and the phonon are cousins. 🌟*
