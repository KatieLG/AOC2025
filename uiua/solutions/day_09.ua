~ "../helpers/input.ua" ~ ReadSample

Data ← (
  ReadSample "day_09"
  ⊜(⊜⋕⊸≠@,)⊸≠@\n
)

Area     ← /×+₁⌵-⊃⊢⊣             # Area of square between two red tiles
Expand   ← ⨬(⇡+₁)¤⊸=0            # Fix or create range if same row/col or another
Green    ← ≡⌟+≡⊂∩Expand°⊟-⊃⊃⊢⊣⊢⍆ # Get the green tiles between two red tiles
GenGreen ← ⍆◴⊂/◇⊂⍚Green⊸⧈∘2 ⊂⊸⊣  # All green and red tiles on circumference
All      ← GenGreen Data

OrderedRec ← ⍜↙₂⇌⍆                       # Order perimeter point
Corners    ← ⊂⊟⊃[⊓⊢⊣][˜⊓⊢⊣]⊸°⊟           # Find corners of rect
Perimeter  ← GenGreen OrderedRec Corners # Get perimeter of rect from two tiles
Valid      ← ≡⌞∊ All                     # check if perimeter is valid

# Part A
/↥ ≡Area ⧅<2 Data # Find area of each combination and pick the best 

# Part B
Valid Perimeter?⊡1 ⧅<2 Data # For each combination check if the perimeter is green

# ˜⍜⊡+₁ ×0°△? ⊸⊃[+1/↥≡⊢|+1/↥≡⊣] All
# &fwa "grid.png" img "png"
