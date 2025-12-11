~ "../helpers/input.ua" ~ ReadInput

Parse ← ⊃{↙₃|⊜∘⊸≠@ ↘₅} # generate {input | outputs}

Data ← (
  ReadInput "day_11"
  ⊜Parse⊸≠@\n
)

Inputs  ← ≡(°□⊢) Data                         # Normal array of inputs
Outputs ← ≡⊣ Data                             # Boxed array of outputs
Pos     ← ⊢⊢⊚⌕                                # Find arr position in inputs 
Nbrs    ← memo(°□˜⊡Outputs˜Pos Inputs)        # Find outputs of a given input
Paths   ← |2 memo(⨬(⍣(/+≡⌟Paths Nbrs|0)|1)◡≍) # Memoised path counter

# Part A
Paths "you" "out"

# Part B
Paths "svr" "fft" # paths from svr to fft
Paths "fft" "dac" # paths from fft to dac
Paths "dac" "out" # paths from dac to out
××                # total paths: svr -> fft -> out
Paths "svr" "dac" # paths from svr to dac
Paths "dac" "fft" # paths from dac to fft
Paths "fft" "out" # paths from fft to out
××                # total paths: svr -> dac -> fft -> out
+                 # Grand total
