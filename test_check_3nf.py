from Types import *
from Util import *
from FD import *


# Test check_3nf
def test_3nf_assignment2_optionA():
    r = R("R(ABCDEF)")
    r1 = R("R(ABDF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert check_3nf(r, r1, s) == None


def test_3nf_assignment2_optionB():
    r = R("R(ABCDEF)")
    r1 = R("R(ADEF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert check_3nf(r, r1, s) == None


def test_3nf_assignment2_optionC():
    r = R("R(ABCDEF)")
    r1 = R("R(BCF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert check_3nf(r, r1, s) == None


def test_3nf_assignment2_optionD():
    r = R("R(ABCDEF)")
    r1 = R("R(CEF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert check_3nf(r, r1, s) == None


def test_3nf_slide17():
    r = R("R(ABCD)")
    r1 = R("R(ABCD)")
    s = S("AB->C;C->D;D->A")
    assert check_3nf(r, r1, s) == None


def test_3nf_slide22():
    r = R("R(ABCD)")
    r1 = R("R(ABCD)")
    s = S("B->C;B->D")
    assert check_3nf(r, r1, s) != None


def test_3nf_slide24():
    r = R("R(ABCD)")
    r1 = R("R(ABCD)")
    s = S("A->B;B->C;C->D;D->A")
    assert check_3nf(r, r1, s) == None


def test_3nf_slide28():
    r = R("R(ABCDE)")
    r1 = R("R(ABCDE)")
    s = S("AB->C;DE->C;B->E")
    assert check_3nf(r, r1, s) != None
