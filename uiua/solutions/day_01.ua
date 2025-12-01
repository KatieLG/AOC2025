~ "../helpers/input.ua" ~ ReadInput

Parse ← ×+1¯×2=@L⊃(⊢|⋕↘₁) # Multiply clicks by direction

Data ← (
  ReadInput "day_01" # Read in
  ⊜Parse⊸≠@\n        # Parse each line
)

C ← (
  ˜⊂     # Append start position
  ◿100\+ # Collect positions after each click
  /+=0   # Count zeroes 
)

# Part A
C Data 50

# Part B
C ▽⊃⌵±Data 50 # use keep to split into individual clicks
