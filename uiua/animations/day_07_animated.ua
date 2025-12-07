~ "../solutions/day_07.ua" ~ Data Start Traverse

AddPipe ← ⍜⊡(≡⍥⋅@|⊸=@.)     # Draw pipes at coords
Draw    ← (⍉⊃[=@S|=@^|=@|]) # Add colours for start, caret & pipe

GeneratePaths ← (
  ⊸Traverse Start Data # Traverse through the grid
  ⍆◴/◇⊂                # Get coordinates of all paths
  ⊜□⊸≡⊢                # Partition into rows
  ≡⌟◇AddPipe           # Add pipes to routes
)

SaveAnimation ← (
  $"animations/_.gif" # Filename
  &fwa⊙(gif 12 ≡▽₂27) # Scale up & save
)

≡Draw GeneratePaths
SaveAnimation "day_07_animated_flow"

≡Draw \↥ GeneratePaths # keep history of movement
SaveAnimation "day_07_animated_history"
