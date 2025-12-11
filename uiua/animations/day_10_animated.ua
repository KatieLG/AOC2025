Jolts     ← &fras "animations/data/day10_jolts.txt"
Solutions ← &fras "animations/data/day10_sols.txt"
Schem     ← &fras "animations/data/day10_schematics.txt"

Nums  ← ⊜⋕⊸≠@,               # Parse comma sep list as numbers
Btns  ← ⬚0⊜(°⊚Nums)⊸≠@;      # Parse btn arrays as toggle matrix
Scale ← ≡▽10▽10              # rotate and scale the pixels
Color ← ≡₀(↧1×[⊸∘˜÷1 100 0]) # Apply intensity as yellow colour
MJ    ← ⊜(/↥Nums)⊸≠@\nJolts  # Max Jolts across all machine

⊜(□Btns)⊸≠@\nSchem     # Parse buttons for all machines
⊜(□Nums)⊸≠@\nSolutions # Parse all the solutions

⬚0∧/◇⊂⍚(≡⍉⍉¤\+▽) # lets gooo
⍉⍉⊢⍉⍉            # join up elements
Color            # Colour it
# &p⊸△
# ≡Scale
# &p⊸△
&fwa "animations/gifs/day_10_animated.gif" gif 25
