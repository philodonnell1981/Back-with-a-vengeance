print ((4 < 5) and (5 < 6)) # both have to be true for outcome to be true
print ((4 < 5) and (9 < 6))
print ((1 == 2) or (2 == 2)) # only one has to be true for overall outcome to be true
spam = 4

#you can also use multiple Boolean operators in an express, along with comparison ops
print(2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2)

