~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_03"
  ⊜∘⊸≠@\n
)

E ← (
  ⟜⊸(⊢⍖↘¯-1)    # Find the index of the best number to take
  ⊃(⋅⊡|-1|↘+⋅1) # Extract best and drop from there
)
L ← ⍢(⊂⊙E|⋅>₀) # Keep collecting best digits and loop with remaining subarray
B ← ⊙⋅◌⋕L""    # Build up best number from empty string

# Part A
/+ ≡B 2 Data

# Part B
/+ ≡B 12 Data
