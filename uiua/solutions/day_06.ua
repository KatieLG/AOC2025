~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_06"
  ⊜∘⊸≠@\n
)

Apply    ← ⨬/+/×=@*⊢              # Apply the operation to num array
TryParse ← ⍣(⋕▽⊸≠@ )∞             # Convert to int if numeric or inf if whitespace
Ops      ← ⊜∘⊸≠@ ⊣Data            # Extract operations from the grid
NumGrid  ← ↘¯1Data                # Grid with operations row removed
NumRows  ← ⍉≡⊜⋕⊸≠@ NumGrid        # Extract col group rows
NumCols  ← ⊜□⊸≠∞≡TryParse⍉NumGrid # Extract col group columns

# Part A
/+ ≡Apply Ops NumRows

# Part B
/◇+ ⍚Apply Ops NumCols
