~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_09"
  ⊜(⊜⋕⊸≠@,)⊸≠@\n
)

Area ← /×+₁⌵-⊃⊢⊣ # Area of square between two coords
Check ← memo(
  ⊓(⍆|⇌⍆) # sort by coord
  ↧⊓⊢⊣⊃>< # check p1 < c2 AND p2 > c1 
)
Intersects ← memo(↧⊃(Check∩≡⊢|Check∩≡⊣)) # check x & y intersections
Edges      ← ⧈∘2 ⊂⟜⊢Data

# Part A
/↥ ≡Area ⧅<2 Data # Find area of each combination and pick the best 

# Part B
⊸⊞Intersects Edges ⧅<2 Data # check pairwise intersections with corner combination
/↥ ≡Area ▽¬/↥               # keep combinations with no intersections and find best area
