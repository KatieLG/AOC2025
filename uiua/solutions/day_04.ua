~ "../helpers/input.ua" ~ ReadSample

Data ← (
  ReadSample "day_04"
  ⊜(=@@)⊸≠@\n
)

O ← ⊂A₂C₂      # Nbr offsets
N ← ▽⤚⬚0⊡≡⌟+O  # Get neighbouring rolls
P ← ▽⤚(±⊡)♭₂°⊡ # Get Roll positions
R ← <4⧻N       # Check if roll is removable (<4 Nbrs)

# Part A
/+≡⌟R⊸P Data # Count removable rolls
