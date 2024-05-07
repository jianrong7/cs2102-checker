from Types import *

'''
Utilities
'''
def _unspace(s):
  while ' ' in s:
    s = s.replace(' ','')
  return s.upper()

'''
These functions are used to simplify
the creation of
- A: Set of Attributes
- R: Relation
- F: A single functional dependency
- S: A set of functional dependencies
'''
def A(s): # s is a string, no comma between attributes
  s = _unspace(s)
  return Attrs(*s)
def R(s): # s is a string 'R(ABCD)', no comma between attributes
  s = _unspace(s)
  s = s.split('(')
  return Rel(s[0], A(s[1][:-1]))
def F(s): # s is a string, AB -> CD
  s = _unspace(s)
  return FD(*map(A, s.split('->')))
def S(s): # s is a string, fd1 ; fd2 ; ...
  s = _unspace(s)
  return Sigma(*map(F, s.split(';')))
