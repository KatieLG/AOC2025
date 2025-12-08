~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_08"
  ⊜(⊜⋕⊸≠@,)⊸≠@\n
)

Dist      ← √/+˙×-°⊟         # Distance between a pair of coords
NumCoords ← ⧻Data            # Number of coordinates
Pairs     ← ⊏⍏⊸≡Dist⧅<2 Data # Order pairs by distance between them
Start     ← ⊃{⊢}↘₁ Pairs     # Initial Pairs & Circuits
Lengths   ← ⇌⍆≡°□⍚⧻          # Ordered (desc) Circuit Lengths

Loop ← (
  ⊙⊃⊢↘₁                # Get next pair and remove from list
  ◡⍚⌟(/↥≡⌞∊)           # Mark pair in existing circuits
  ⊚≡°□                 # Find locations where pair lives in circuits
  ⊸⧻                   # Find number of circuits where a coord was found
  ⨬(⊂⊙□◌               # New circuit
  | ⍜⊡(⍜°□(◴⊂))⊢       # Join to circuit
  | ⊂⊃(▽¬≡⌞∊⊙°⊏|□/◇⊂⊏) # join 2 circuits
  )
)

# Part A
/×↙₃ Lengths⊙◌⍥(Loop)999 Start # Loop 999 times (to make 1000 total) them mult length of top 3

# Part B
⊢/×⋅⊢ ⍢(Loop|<NumCoords⧻°□⊢⊙◌Loop) Start # Loop until the first circuit would contain everything then mult x coords
