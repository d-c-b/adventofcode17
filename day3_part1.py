input = 289326

#define side length of square as n
n = 1

#define square of n
nsq = 1

#function to square number
def squared(number):
  sqrnum = number * number
  return sqrnum

#find the side length n of spiral ring which input is in
# and the largest number in this ring,nsq
while squared(n) < input:
  n += 2
  nsq = squared(n)

#numbers on the corners of this spiral ring in ascending order
corners = [(nsq-(3*(n-1))) , (nsq-(2*(n-1))), (nsq-(n-1)), nsq]

midpoints = []
#add the numbers at midpoints along each side to a list called midpoints
for corner in corners:
  midpoint = corner - ((n-1)/2)
  midpoints.append(midpoint)

differences = []
#find the minimum difference between input and a midpoint of a side
for midpoint in midpoints:
  diff = abs(midpoint - input)
  differences.append(diff)
  mindiff = min(differences)

# sum the minimum difference from a midpoint of a side (one of the two dimensions)
# and the distance from a midpoint in a square
manhatten_dist = ((n-1)/2) + mindiff
print manhatten_dist
