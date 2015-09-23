even = 1
odd = 0
sum = 0

while 1:
  odd = odd + even
  even = odd + even 
  if even < 4000000:
    sum += even
  else
    break
print sum