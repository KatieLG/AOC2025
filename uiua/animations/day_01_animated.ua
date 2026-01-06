~ "../solutions/day_01.ua" ~ Data

# Get click positions
P ← ◿100\+˜⊂˜▽Data 50

# Generate 100 black pixels
Z ← ↯100_3 0_0_0

# Upscale
U ← ≡▽10▽30¤

# Generate frame of animation
G ← U⨬(⍜˜⊡+₁Z|+¤0_1_0 Z)⊸=0

# Limit to first 900 positions for gif size
≡₀G↙₉₀₀P
&fwa "animations/gifs/day_01_animated.gif" gif 45
