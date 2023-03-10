def solve(numheads, numlegs):
   chickens = (numlegs - (4 * numheads)) / -2
   rabbits = numheads - chickens
   return int(chickens), int(rabbits)