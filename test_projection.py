from Types import *
from Util import *
from FD import *


# Test check_bcnf
def test_bcnf_success():
    r = R("R(ACDE)")
    s = S("A->B;BC->D")
    # print(projection(A("ACDE"), s))
    assert projection(A("ACDE"), s) == S("AC->D;ACE->D")


# def test_bcnf_failure():
#     r = R("R(ABCD)")
#     r1 = R("R(ABCD)")
#     s = S("B->C;B->D")
#     assert check_bcnf(r, r1, s) != None  # B -> CD
#     assert check_bcnf(r, r1, s) == F("B->CD")


# def test_bcnf_assignment2_optionA():
#     r = R("R(ABCDEF)")
#     r1 = R("R(ABDF)")
#     s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
#     assert check_bcnf(r, r1, s) != None


# def test_bcnf_assignment2_optionB():
#     r = R("R(ABCDEF)")
#     r1 = R("R(ADEF)")
#     s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
#     assert check_bcnf(r, r1, s) == None


# def test_bcnf_assignment2_optionC():
#     r = R("R(ABCDEF)")
#     r1 = R("R(BCF)")
#     s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
#     print(check_bcnf(r, r1, s))
#     assert check_bcnf(r, r1, s) == None


# def test_bcnf_assignment2_optionD():
#     r = R("R(ABCDEF)")
#     r1 = R("R(CEF)")
#     s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
#     assert check_bcnf(r, r1, s) != None
