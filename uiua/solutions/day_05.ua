~ "../helpers/input.ua" ~ ReadSample

Nums   ← ⊜⋕⊸≠
Ranges ← ⊜(Nums@-)⊸≠@\n

Data ← (
  ReadSample "day_05"
  ⊃↘↙⊚⊸⌕"\n\n"        # Split into ingredient ranges and IDs
  ⊓(Nums@\n↘₂|Ranges) # Parse into numeric arrays
)

Compare ← (
  ≡[⊓⊢⊣]⊃≤≥ # Compare number to >=first & <=last of each range
  ˜∊1_1     # If [1 1] is present then fisrt <= num <= last
)

# Part A
/+≡⌟Compare Data # Count the ingredient IDs within the ranges
