~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_09"
  ⊜(⊜⋕⊸≠@,)⊸≠@\n
)

Area       ← /×+₁-⊃⊢⊣              # Area of square between two coords
Check      ← ↧⊓⊢⊣⊃<>               # check p1 < c2 AND p2 > c1 
Intersects ← ↧⊃(Check∩≡⊢|Check∩≡⊣) # check x & y intersections
Combos     ← ≡⍜⍉≡⍆ ⧅<2 Data        # pairs with sorted x & y coords
Edges      ← ≡⇌≡⍆ ⧈∘2 ⊂⟜⊢Data      # edges with sorted x & y coords

# Part A
/↥ ≡Area Combos # Maximum area of corner combinations

# Part B
⊸⊞Intersects Edges Combos # check pairwise intersections with corner combination
/↥ ≡Area ▽¬/↥             # keep combinations with no intersections and find best area
