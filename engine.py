#!/usr/bin/env python3
"""
synesthesia-engine: unified sensory translation
Where sound becomes color, number becomes music, and sensation crosses every wire.

Magic Trees Productions
Barcelona, March 6, 2026
"""

import colorsys
import math
from typing import Dict, Tuple, Union


class SynesthesiaEngine:
    """Main engine for translating between sensory domains."""
    
    def __init__(self):
        self.notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.scales = {
            'major': [0, 2, 4, 5, 7, 9, 11],
            'minor': [0, 2, 3, 5, 7, 8, 10],
            'phrygian': [0, 1, 3, 5, 7, 8, 10],
            'lydian': [0, 2, 4, 6, 7, 9, 11],
            'mixolydian': [0, 2, 4, 5, 7, 9, 10],
            'dorian': [0, 2, 3, 5, 7, 9, 10],
            'locrian': [0, 1, 3, 5, 6, 8, 10]
        }
    
    def frequency_to_color(self, frequency_hz: float) -> Dict:
        """Convert audio frequency to visible light color."""
        log_freq = math.log10(max(20, min(20000, frequency_hz)))
        log_min, log_max = math.log10(20), math.log10(20000)
        wavelength = 700 - ((log_freq - log_min) / (log_max - log_min)) * 320
        rgb = self._wavelength_to_rgb(wavelength)
        return {
            'rgb': rgb,
            'hex': '#{:02x}{:02x}{:02x}'.format(*rgb),
            'wavelength_nm': round(wavelength, 1),
            'name': self._rgb_to_name(rgb)
        }
    
    def color_to_music(self, rgb: Tuple[int, int, int]) -> Dict:
        """Convert color to musical properties."""
        r, g, b = [x / 255.0 for x in rgb]
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        note_index = int(h * 12) % 12
        root_note = self.notes[note_index]
        
        if v < 0.3:
            scale, mood = 'locrian', 'mystery'
        elif s < 0.3:
            scale, mood = 'dorian', 'introspective'
        elif s > 0.7 and v > 0.7:
            scale = 'phrygian' if (h < 0.15 or h > 0.9) else 'lydian'
            mood = 'tension' if scale == 'phrygian' else 'wonder'
        else:
            scale, mood = ('minor', 'depth') if v < 0.6 else ('mixolydian', 'warmth')
        
        return {'root': root_note, 'scale': scale, 'mood': mood}
    
    def number_to_texture(self, number: Union[int, float]) -> Dict:
        """Convert number to tactile properties."""
        int_part = int(abs(number))
        dec_part = abs(number) - int_part
        
        if dec_part == 0:
            quality = 'sharp' if self._is_prime(int_part) else 'smooth'
        elif 0.31 < dec_part < 0.32:
            quality = 'spiraling'
        elif 0.61 < dec_part < 0.62:
            quality = 'golden'
        else:
            quality = 'flowing' if dec_part < 0.5 else 'rippled'
        
        weight = 'light' if abs(number) < 10 else 'medium' if abs(number) < 1000 else 'heavy'
        temp = ['cold', 'cool', 'warm'][min(2, sum(int(d) for d in str(int_part)) % 20 // 7)]
        
        return {'quality': quality, 'weight': weight, 'temperature': temp}
    
    def _wavelength_to_rgb(self, wl: float) -> Tuple[int, int, int]:
        """Convert wavelength (nm) to approximate RGB."""
        if 380 <= wl < 440:
            r, g, b = -(wl - 440) / 60, 0.0, 1.0
        elif 440 <= wl < 490:
            r, g, b = 0.0, (wl - 440) / 50, 1.0
        elif 490 <= wl < 510:
            r, g, b = 0.0, 1.0, -(wl - 510) / 20
        elif 510 <= wl < 580:
            r, g, b = (wl - 510) / 70, 1.0, 0.0
        elif 580 <= wl < 645:
            r, g, b = 1.0, -(wl - 645) / 65, 0.0
        elif 645 <= wl <= 700:
            r, g, b = 1.0, 0.0, 0.0
        else:
            r, g, b = 0.0, 0.0, 0.0
        
        factor = 1.0 if 420 <= wl <= 650 else 0.3 + 0.7 * ((wl - 380) / 40 if wl < 420 else (700 - wl) / 50)
        return (int(r * factor * 255), int(g * factor * 255), int(b * factor * 255))
    
    def _rgb_to_name(self, rgb: Tuple[int, int, int]) -> str:
        r, g, b = rgb
        if r > 200 and g < 100 and b < 100: return 'red'
        if r > 200 and g > 150: return 'orange' if b < 100 else 'white'
        if g > 150 and r < 150: return 'green'
        if b > 150 and r < 100: return 'blue'
        if b > 150 and r > 100: return 'purple'
        return 'black' if max(r, g, b) < 100 else 'mixed'
    
    def _is_prime(self, n: int) -> bool:
        if n < 2: return False
        return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


if __name__ == '__main__':
    se = SynesthesiaEngine()
    print("🎶 Synesthesia Engine\n")
    print("[Frequency → Color]")
    print(f"  A440: {se.frequency_to_color(440)}")
    print("\n[Color → Music]")
    print(f"  Crimson: {se.color_to_music((220, 20, 60))}")
    print("\n[Number → Texture]")
    print(f"  π: {se.number_to_texture(3.14159)}")
    print("\nThe photon and the phonon are cousins. 🌟")
