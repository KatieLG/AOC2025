~ "../helpers/input.ua" ~ ReadInput

Req  ← ⊙(⊜⋕⊸≠@ )⊟∩⋕°$"_x_: _"    # Parse a requirement line
Gift ← ⊜(≠@#)?⊸≠@\n↘+₁⊸(˜⨂@\n)↘1 # Parse a gift line

Data ← (
  ReadInput "day_12"
  ⊜□⊸(¬⌕"\n\n")  # split into gifts & requirements
  ⊃(⍚Gift↘(¯1)   # Parse gift lines
  | ⊜Req⊸≠@\n°□⊣ # Parse requirement lines
  )
)

# Part A
/+≤ ⊙≡/+ ≡/×⌊÷₃ ◌Data # take 3x3 grids, and see if enough for present count

# Part B
0
