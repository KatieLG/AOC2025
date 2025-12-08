~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput"day_07"
  ⊜∘⊸≠@\n
)

Adj   ← ≡⊂0A₁  # Left & right offsets
Start ← ⊢⊚⊸⌕@S # get start pos

Timelines ← |2 memo(
  =@^◡⊡                  # check if a caret
  ⨬(⍣Timelines0+1_0      # if not, return timelines from below
  | +1/+≡⌟Timelines+Adj¤ # if it is, get nbrs, and add timelines for each
  )
)

Splits ← |2 memo(
  =@^◡⊡                      # check if a caret
  ⨬(⍣Splits[0_0]+1_0         # if not, return timelines from below
  | ⊂⊙(◴/◇⊂⍚⌟Splits)⟜(+Adj¤) # if it is, get nbrs, and add timelines for each
  )
)

# Part A
-₁⧻◴Splits Start Data

# Part B
+1 Timelines Start Data
