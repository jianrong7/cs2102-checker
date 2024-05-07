from Types import *
from Util import *
from FD import *


# Test is_preserving
def test_is_preserving_q7():
    r = R("R(ABCDEF)")
    r1 = R("R(ADEF)")
    r2 = R("R(ACE)")
    r3 = R("R(BCE)")
    r4 = R("R(CF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert is_preserving(r, [r1, r2, r3, r4], s) == False


def test_is_preserving_q9():
    r = R("R(ABCDEF)")
    r1 = R("R(ABDF)")
    r2 = R("R(ADEF)")
    r3 = R("R(BCF)")
    r4 = R("R(CEF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert is_preserving(r, [r1, r2, r3, r4], s) == True
