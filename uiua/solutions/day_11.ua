~ "../helpers/input.ua" ~ ReadInput

Parse ← ⊃{↙₃|⊜∘⊸≠@ ↘₅} # generate {input | outputs}

Data ← (
  ReadInput "day_11"
  ⊜Parse⊸≠@\n
)

Inputs  ← ≡(°□⊢) Data                     # Normal array of inputs
Pos     ← ⍣(⊢⊢|⧻Inputs)⊚⌕                 # Find arr position in inputs or return length of inputs
Start   ← Pos "you" Inputs                # Start pos is "You"
Outputs ← ≡⊣ Data                         # Boxed array of outputs
MI      ← ⇡⧻Inputs                        # map inputs to numbers
MO      ← ⍚(≡(⍣(⊢⊢|⧻MI)⊚˜⌕Inputs))Outputs # map outputs to numbers

# Part A
path(
  ≡⊸0 °□˜⊡Outputs˜Pos Inputs # add all next steps with cost 0
| ≍"out"                     # until we get to out
)"you"                       # starting from "you"
⊓⧻◌                          # take path length
