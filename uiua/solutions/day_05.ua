~ "../helpers/input.ua" ~ ReadInput

Nums   ← ⊜⋕⊸≠
Ranges ← ⊜(Nums@-)⊸≠@\n

Data ← (
  ReadInput "day_05"
  ⊃↘↙⊚⊸⌕"\n\n"        # Split into ingredient ranges and IDs
  ⊓(Nums@\n↘₂|Ranges) # Parse into numeric arrays
)

Compare ← (
  ≡[⊓⊢⊣]⊃≤≥ # Compare number to >=first & <=last of each range
  ˜∊1_1     # If [1 1] is present then fisrt <= num <= last
)

JoinOverlap ← ⊟+⊃(
  +₁˜⊸⊓⊣⊢ # Start of range and max_id so far + 1
  ↥       # Non overlapping start (max + 1 or start)
  ↥0+₁-⊙⊣ # End-Start+1 for amount newly covered
| ⋅⊢      # amount covered so far
| ↥∩⊣     # new max_id so far
)

# Part A
/+≡⌟Compare Data # Count the ingredient IDs within the ranges

# Part B
⊢∧JoinOverlap⊙0_0⍆ ◌ Data # Count unique IDs across overlapping ranges
