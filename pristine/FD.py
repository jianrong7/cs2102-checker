from Types import *
from Util  import * 

'''
Functional Dependency Algorithms
'''

# Attribute closure
#   with respect to a set of FD sigma
# input
#   - attrs: Attrs
#   - sigma: Sigma
# output
#   - res: Attrs
def attribute_closure(attrs, sigma):
  res = attrs.copy()
  prv = Attrs()

  # this uses a fix-point algorithm
  while prv != res:
    prv = res.copy()
    for fd in sigma:
      if fd.src <= res and not(fd.dst <= res):
        res = res | fd.dst
  return res


# Find the superkey of relation
#   with respect to a set of FD sigma
# input
#   - rel  : Rel
#   - sigma: Sigma
# output
#   - res: [Attrs]
def superkeys(rel, sigma):
  pass


# Find the key of relation
#   with respect to a set of FD sigma
# input
#   - rel  : Rel
#   - sigma: Sigma
# output
#   - res: [Attrs]
def keys(rel, sigma):
  pass


# Find the prime attributes of relation
#   with respect to a set of FD sigma
# input
#   - rel  : Rel
#   - sigma: Sigma
# output
#   - res: Attrs
def prime_attributes(rel, sigma):
  pass
