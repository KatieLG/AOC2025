~ "../solutions/day_07.ua" ~ Data Nbrs Start Traverse

AddPipe ← ⍜⊡(≡⍥⋅@|⊸=@.)         # Draw pipes at coords
Draw    ← (⍉⊃[=@S|=@^|=@|])     # Add colours for start, caret & pipe
InRange ← <142⊢                 # Check if a coordinate is in grid range
Next    ← ▽⊸≡InRange◴/◇⊂⊸⍚⌟Nbrs # get all nbrs of all positions
End     ← >+1/↧≡⊢°□⊓⊣⧻          # Check if all positions have reached the bottom of the grid

Generate ← (
  Start Data           # Get start coord and grid
  {¤}                  # Accumulator
  ⍢(⊂⊙(⍜°□Next)⟜⊣|End) # Use current positions to find next positions
  ≡⌟◇AddPipe           # Place pipes under positions landed on
)

SaveAnimation ← (
  $"animations/_.gif" # Filename
  &fwa⊙(gif 20 ≡▽₂4)  # Scale up & save
)

≡Draw Generate
SaveAnimation "day_07_animated_flow"

≡Draw \↥ Generate # keep history of movement
SaveAnimation "day_07_animated_history"
