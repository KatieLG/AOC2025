~ "../helpers/input.ua" ~ ReadSample

Data ← (
  ReadSample "day_07"
  ⊜∘⊸≠@\n
)

Adj   ← ⊟⊡2⟜⊢A₂        # Left & right offsets
Start ← ⊢⊚⊸⌕@S         # get start pos
Draw  ← ⍜⊡(≡⍥⋅@|⊸=@.∘) # Draw grid traversal from all paths
Count ← /+=@^⊡◴/◇⊂     # Count carets in paths

Nbrs ← (
  =@^⤚⊡       # Check for caret
  ⨬(≡⊸1 ¤+1_0 # Generate downward nbrs with cost of 1
  | ≡⊸0 +Adj¤ # Generate adj caret nbrs with cost of 0 to ensure all routes generated
  )
)

Traverse ← ⊙◌path(
  Nbrs
| =+1⊓⊢⧻ # Keep traversing through grid until bottom row
)

# Part A
Count ⊸Traverse Start Data # Count carets hit on all paths

# Part B
⧻Traverse Start Data # Count the number of traversal paths
