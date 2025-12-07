~ "../solutions/day_07.ua" ~ Adj Data Rows Start

AddPipe ← ⍜⊡(≡⍥⋅@|⊸=@.)     # Draw pipes at coords
Draw    ← (⍉⊃[=@S|=@^|=@|]) # Add colours for start, caret & pipe
InRange ← <Rows⊢            # Check if a coordinate is in grid range

Nbrs ← memo(
  =@^⤚⊡   # Check for caret
  ⨬(¤+1_0 # Generate downward nbrs
  | +Adj¤ # Generate adj caret nbrs
  )
)
Next ← ▽⊸≡InRange◴/◇⊂⊸⍚⌟Nbrs # get all nbrs of all positions
End  ← >+1/↧≡⊢°□⊓⊣⧻          # Check if all positions have reached the bottom of the grid

Generate ← (
  Start Data           # Get start coord and grid
  {¤}                  # Accumulator
  ⍢(⊂⊙(⍜°□Next)⟜⊣|End) # Use current positions to find next positions
  ≡⌟◇AddPipe           # Place pipes under positions landed on
)

SaveAnimation ← (
  $"animations/gifs/_.gif" # Filename
  &fwa⊙(gif 20 ≡▽₂4)  # Scale up & save
)

≡Draw Generate
SaveAnimation "day_07_animated_flow"

≡Draw \↥ Generate # keep history of movement
SaveAnimation "day_07_animated_history"
