~ "../solutions/day_04.ua" ~ Data RPos RRem

¤Data      # Array for each grid state
⍢(⊸⊢       # Get the current grid state
  ⊙◌RRem   # Remove rolls and drop count
  ⊂        # Join to state array
| >0⧻RPos⊢ # Until no longer possible
)

⇌≡▽₂20 # Scale up by 20
&fwa "animations/gifs/day_04_animated.gif" gif 12
