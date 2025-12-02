~ "../helpers/input.ua" ~ ReadSample

Data ← (
  ReadSample "day_02"
  ▽⊸≠@\n        # Remove new lines
  ⊜(⊜⋕⊸≠@-)⊸≠@, # Extract ranges
)

P ← /◇⊂⍚(+⇡-⊃(⊢|⊣|⊢))Data # Get all product ids from range
I ← ≍⊃↙↘⌊÷2⊸⧻°⋕           # Is Invalid 
R ←

# Part A
/+ ▽⊸≡I P # Sum the invalid product ids

# Part B
