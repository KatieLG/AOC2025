~ "../helpers/input.ua" ~ ReadSample

Data ← (
  ReadSample "day_04"
  ⊜(=@@)⊸≠@\n
)

O ← ⊂A₂C₂      # Nbr offsets
N ← ▽⤚⬚0⊡≡⌟+O  # Get neighbouring rolls
P ← ▽⤚(±⊡)♭₂°⊡ # Get Roll positions
R ← <4⧻N       # Check if roll is removable (<4 Nbrs)
K ← ▽⤚≡⌟R⊸P    # Get removable roll positions

# Part A
⧻K Data # Count removable rolls

# Part B
◌⍢(⊙+⊃⍜⊡×₀⧻⊸K|>0⧻K) ⊙0 Data # Remove and count removable rolls until none left
