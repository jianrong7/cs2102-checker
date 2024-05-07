from Types import *
from Util import *
from FD import *


# Test check_bcnf
def test_bcnf_success():
    r = R("R(ABCD)")
    r1 = R("R(ABCD)")
    s = S("A->B;B->C;C->D;D->A")
    assert check_bcnf(r, r1, s) == None


def test_bcnf_failure():
    r = R("R(ABCD)")
    r1 = R("R(ABCD)")
    s = S("B->C;B->D")
    assert check_bcnf(r, r1, s) != None  # B -> CD
    assert check_bcnf(r, r1, s) == F("B->CD")


def test_bcnf_assignment2_optionA():
    r = R("R(ABCDEF)")
    r1 = R("R(ABDF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert check_bcnf(r, r1, s) != None


def test_bcnf_assignment2_optionB():
    r = R("R(ABCDEF)")
    r1 = R("R(ADEF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert check_bcnf(r, r1, s) == None


def test_bcnf_assignment2_optionC():
    r = R("R(ABCDEF)")
    r1 = R("R(BCF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert check_bcnf(r, r1, s) == None


def test_bcnf_assignment2_optionD():
    r = R("R(ABCDEF)")
    r1 = R("R(CEF)")
    s = S("F->DE;CE->DF;CEF->D;DE->AF;ABD->CF")
    assert check_bcnf(r, r1, s) != None


def test_bcnf_slide41():
    r = R("R(ABCD)")
    r1 = R("R(ABCD)")
    s = S("AB->C;C->D;D->A")
    assert check_bcnf(r, r1, s) != None


def test_bcnf_slide42():
    r = R("R(ABCD)")
    r1 = R("R(ABCD)")
    s = S("B->C;B->D")
    assert check_bcnf(r, r1, s) != None


def test_bcnf_slide44():
    r = R("R(ABCD)")
    r1 = R("R(ABCD)")
    s = S("A->B;B->C;C->D;D->A")
    assert check_bcnf(r, r1, s) == None


def test_bcnf_slide47():
    r = R("R(ABCDE)")
    r1 = R("R(ABCDE)")
    s = S("AB->C;C->E;E->A;E->D")
    assert check_bcnf(r, r1, s) != None


def test_bcnf_slide48():
    r = R("R(ABCD)")
    r1 = R("R(ABCD)")
    s = S("AB->D;BD->C;CD->A;AC->B")
    assert check_bcnf(r, r1, s) == None


def test_bcnf_slide78_79():
    r = R("R(ABCD)")
    r1 = R("R(AB)")
    r2 = R("R(ACD)")
    r3 = R("R(AD)")
    r4 = R("R(CD)")
    s = S("BC->D;D->A;A->B")
    assert check_bcnf(r, r1, s) == None
    assert check_bcnf(r, r2, s) != None
    assert check_bcnf(r, r3, s) == None
    assert check_bcnf(r, r4, s) == None
