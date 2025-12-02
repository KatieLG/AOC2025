~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_02"
  ▽⊸≠@\n        # Remove new lines
  ⊜(⊜⋕⊸≠@-)⊸≠@, # Extract pairs
)

R ← +⇡⤚-°⊟          # Extract range
P ← /◇⊂⍚R Data      # Get all product ids from range
I ← ≍⊃↙↘⌊÷2⊸⧻°⋕     # Is Invalid 
S ← ±⧻⊚˜⌕↘¯1↘₁⊸˙⊂°⋕ # Is Repeated Substring

# Part A
/+ ▽⊸≡I P # Sum the invalid product ids

# Part B
/+ ▽⊸≡S P # Sum the product ids for repeats of any size
