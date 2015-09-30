F0 = 0
F1 = 1
F2 = 1
count = 0


while len(str(F2)) < 1000:
  F0 = F1
  F1 = F2
  F2 = F1 + F0
  count += 1
print (F2)
print (count)