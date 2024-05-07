from Types import *
from Util  import *
from FD    import *

r = R('R(ABCD)')
s = S('AB->C;C->D;C->A')
a = A('AB')

print(r) # R(ABCD)
print(s) # {{C} -> {A}, {AB} -> {C}, {C} -> {D}}

print(attribute_closure(a, s)) # ABCD
print(superkeys(r, s))         # [BC, BCD, AB, ABC, ABD, ABCD]
print(keys(r, s))              # [BC, AB]
print(prime_attribute(r, s))   # ABC
