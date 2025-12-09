~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_09"
  ⊜(⊜⋕⊸≠@,)⊸≠@\n
)

Area ← /×+₁⌵-⊃⊢⊣ # Area of square between two coords

# Part A
/↥ ⊸≡Area ⧅<2 Data # Find area of each combination and pick the best 
