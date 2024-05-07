from Types import *
from Util import *
from FD import *

r = R("R(ABCD)")
s = S("AB->C;C->D;C->A")
a = A("AB")

print(r)  # R(ABCD)
print(s)  # {{C} -> {A}, {AB} -> {C}, {C} -> {D}}

print(attribute_closure(a, s))  # ABCD
print(superkeys(r, s))  # [BC, BCD, AB, ABC, ABD, ABCD]
print(keys(r, s))  # [BC, AB]
print(prime_attributes(r, s))  # ABC


print("=======")
r = R("R(ABCDEF)")
s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")

print("Q1", keys(r, s))
print("Q2", prime_attributes(r, s))
print("Q4", decompose_bcnf(r, s))
print("Q5", decompose_3nf(r, s))
