~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_04"
  ⊜(=@@)⊸≠@\n
)

O    ← ⊂A₂C₂       # Nbr offsets
N    ← ▽⤚⬚0⊡≡⌟+O   # Get neighbouring rolls
P    ← ▽⤚(±⊡)♭₂°⊡  # Get Roll positions
R    ← <4⧻N        # Check if roll is removable (<4 Nbrs)
RPos ← ▽⤚≡⌟R⊸P     # Get removable roll positions
RRem ← ⊃⍜⊡×₀⧻⊸RPos # Remove & count removable rolls

# Part A
⧻RPos Data # Count removable rolls

# Part B
◌⍢(⊙+RRem|>0⧻RPos) ⊙0 Data # Remove rolls until no longer possible
