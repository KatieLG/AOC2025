Expected ← (
  [{1023 5899}               # day 1
   {38158151648 45283684555} # day 2
   {17316 171741365473332}   # day 3
   {1437 8765}               # day 4
  ]
)
SolutionMap ← map+1⇡⊸⧻Expected
GetSolution ← get⊙SolutionMap

TestDay ← (
  ⟜(&p $"Executing tests for day _" ↙₋₂$"0_")
  GetSolution                                   # get the correct solution
  ⊃(⊙⋅∘°□⊢|⊙∘°□⊣)                               # align actual & expected output
  ˙⍤≍                                           # assert part a is correct
  ˙⍤≍                                           # assert part b is correct
  &p $"Tests passed with runtime: _s\n" ⁅₃¯-now # output runtime
)

NoSolution ← "No Solution"
TooLong    ← "Runtime too long"
Missingb   ← "Missing part b"
SkipDay ← (
  &p $"Skipping tests for day _: _\n" ↙₋₂$"0_" # skip with reason
)

# ---- Tests -----
now
~ "../solutions/day_01.ua"
TestDay 1

now
~ "../solutions/day_02.ua"
TestDay 2

now
~ "../solutions/day_03.ua"
TestDay 3

now
~ "../solutions/day_04.ua"
TestDay 4
