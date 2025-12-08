~ "../helpers/input.ua" ~ ReadSample

Data ← (
  ReadSample "day_08"
  ⊜(⊜⋕⊸≠@,)⊸≠@\n
)

Dist    ← √/+˙×-°⊟         # Distance between a pair of coords
Pairs   ← ⊏⍏⊸≡Dist⧅<2 Data # Order pairs by distance between them
Start   ← ⊃{⊢}↘₁ Pairs     # Initial Pairs & Circuits
Lengths ← ⇌⍆≡°□⍚⧻          # Ordered (desc) Circuit Lengths

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
/×↙₃ Lengths⊙◌⍥(Loop)9 Start # Loop 9 times (to make 10 total) them mult length of top 3
