~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_02"
  ▽⊸≠@\n        # Remove new lines
  ⊜(⊜⋕⊸≠@-)⊸≠@, # Extract ranges
)

P ← /◇⊂⍚(+⇡-⊃(⊢|⊣|⊢))Data # Get all product ids from range
I ← ≍⊃↙↘⌊÷2⊸⧻°⋕           # Is Invalid 
W ← =1⧻◴⧈⌞∘               # Check if Window partitions are all same size
F ← ▽¬±⤚◿↘₁⊸⇡⧻            # Get factors of length
S ← >0/+≡W⊃F¤°⋕           # Is made up of repeated substrings

# Part A
/+ ▽⊸≡I P # Sum the invalid product ids

# Part B
▽⊸>₉ P  # Drop any single digit ids
/+ ▽⊸≡S # Sum the product ids for repeats of any size
