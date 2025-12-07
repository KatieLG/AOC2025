~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_07"
  ⊜∘⊸≠@\n
)

Adj   ← ⊂⊸¯¤0_1                # Left & right offsets
Start ← ⊢⊚⊸⌕@S                 # get start pos
Rows  ← ⊢△Data                 # Number of Rows
Cols  ← ⊣△Data                 # Number of Cols
Valid ← /↧⊃[<Rows⊢|<Cols⊣|≥0⊣] # Coordinate is valid

Timelines ← |2 memo(
  =@^◡⊡                            # check if non empty space
  ⨬(⨬(0|Timelines) ⊸Valid+1_0      # if it is, return timelines from below
  | =@^◡⊡                          # check if a caret
    ⨬(0                            # if not return 0
    | +1/+≡⌟Timelines▽⊸≡Valid+Adj¤ # if it is, get nbrs, and add timelines for each
    )
  )
)

# Part A
1660  # TODO

# Part B
+1 Timelines Start Data
