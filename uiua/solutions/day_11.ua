~ "../helpers/input.ua" ~ ReadInput

Parse ← ⊃{↙₃|⊜∘⊸≠@ ↘₅} # generate {input | outputs}

Data ← (
  ReadInput "day_11"
  ⊜Parse⊸≠@\n
)

Inputs  ← ≡(°□⊢) Data                  # Normal array of inputs
Pos     ← ⍣(⊢⊢|⧻Inputs)⊚⌕              # Find arr position in inputs or return length of inputs
Outputs ← ≡⊣ Data                      # Boxed array of outputs
Nbrs    ← memo(°□˜⊡Outputs˜Pos Inputs) # Find outputs of a given input
Paths!  ← path(≡⊸0 ⍣Nbrs[]|≍^0)        # add all outputs with cost 0, with goal of matching end pos

# Part A
⊓⧻◌ Paths!"out" "you" # paths from "you" to "out"

# Part B
# ⊓⧻◌ Paths!"fft" "svr" # paths from svr to fft
# ⊓⧻◌ Paths!"dac" "fft" # paths from fft to dac
# ⊓⧻◌ Paths!"out" "dac" # paths from dac to out
# ××                    # total paths: svr -> fft -> out

# ⊓⧻◌ Paths!"fft" "svr" # paths from svr to dac
# ⊓⧻◌ Paths!"fft" "dac" # paths from dac to fft
# ⊓⧻◌ Paths!"out" "fft" # paths from fft to out
# ××                    # total paths: svr -> dac -> fft -> out
# ⊸+                    # Grand total
