from Types import *
from Util import *

"""
Functional Dependency Algorithms
"""


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
            if fd.src <= res and not (fd.dst <= res):
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
    # find the power set of attributes
    # find attribute_closure of each subset
    # if the closure is equal to the relation, then append to ans
    ans = []
    for subset in +rel.attrs:
        if attribute_closure(subset, sigma) == rel.attrs:
            ans.append(subset)
    return ans


# Find the key of relation
#   with respect to a set of FD sigma
# input
#   - rel  : Rel
#   - sigma: Sigma
# output
#   - res: [Attrs]
def keys(rel, sigma):
    # find superkeys
    # for each superkey, remove an attriubute and see if we can still get the closure
    # if we can, that means it is not minimal
    # if we cannot, that means it is minimal
    ans = []
    sks = superkeys(rel, sigma)
    for sk in sks:
        is_minimal = True
        for attr in sk:
            reduced_superkey = sk - A(attr)
            if attribute_closure(reduced_superkey, sigma) == rel.attrs:
                is_minimal = False
                break
        if is_minimal:
            ans.append(sk)
    return ans


# Find the prime attributes of relation
#   with respect to a set of FD sigma
# input
#   - rel  : Rel
#   - sigma: Sigma
# output
#   - res: Attrs
def prime_attributes(rel, sigma):
    # determine all keys
    # take the union of all keys
    ans = Attrs()
    for key in keys(rel, sigma):
        ans = ans | key
    return ans


# Find the projection of attributes with respect to a set of FD sigma.
# Output a set of FD which is a projection of sigma on attrs.
# input
#  - attrs: Attrs
#  - sigma: Sigma
# output
#  - res: Sigma
def projection(attrs, sigma):
    # Consider all subsets of attributes
    # Let FD = {}
    # For each subset, compute closure but add a -> a+ & Attr(R) to FD
    # return FD
    ans = []
    for subset in +attrs:
        closure = attribute_closure(subset, sigma)
        non_trivial_and_decomposed = (closure - subset) & attrs
        if non_trivial_and_decomposed != Attrs():
            ans.append(FD(subset, non_trivial_and_decomposed))
    return Sigma(*ans)


# Check if r1 is in BCNF with respect to sigma, given that
# r1 is a decomposed schema from rel.
# output None is there is no violation (in BCNF) or FD that causes violation (not in BCNF)
# input
#  - rel: Rel
#  - r1: Rel
#  - sigma: Sigma
# output
#  - res: None | FD
def check_bcnf(rel, r1, sigma):
    # compute closure of each attribute subset
    # check if there is a more but not all closure
    # if there is, return the FD
    # if not, return None
    for subset in +r1.attrs:
        closure = attribute_closure(subset, sigma)
        non_trivial_and_decomposed = closure & r1.attrs
        if (
            non_trivial_and_decomposed == r1.attrs
            or non_trivial_and_decomposed == subset
        ):
            continue
        else:
            return FD(subset, non_trivial_and_decomposed - subset)

    return None


# Check if r1 is in 3NF with respect to sigma, given that
# r1 is a decomposed schema from rel.
# output None is there is no violation (in 3NF) or FD that causes violation (not in 3NF)
# input
#  - rel: Rel
#  - r1: Rel
#  - sigma: Sigma
# output
#  - res: None | FD
def check_3nf(rel, r1, sigma):
    # derive keys
    # for each FD, check if LHS is a superkey or each attribute is a prime attribute
    # if not, return the FD
    # if all FDs are satisfied, return None
    sk = []
    for tsk in superkeys(rel, sigma):
        if tsk <= r1.attrs:
            sk.append(tsk)
    pa = prime_attributes(rel, sigma) & r1.attrs
    prj = projection(r1.attrs, sigma)
    for p in prj:
        if p.src in sk or p.src <= pa:
            continue
        else:
            return p
    return None


# Return True if decomposition of rel to all r in rn is a lossless-join decomposition
# Otherwise, return False
# Caveat: This function will only handle up to 4 decompositions
# input
#  - rel: Rel
#  - rn: [Rel]
#  - sigma: Sigma
# output
#  - res: bool
def is_lossless(rel, rn, sigma):
    # For each rel, find the common attribute (a)
    # Compute the closure of a
    # If Attr(R1) or Attr(R2) is a subset of a, then it is lossless
    def helper(r1, r2, sigma):
        a = r1 & r2
        closure = attribute_closure(a.attrs, sigma)
        if r1.attrs <= closure or r2.attrs <= closure:
            return True
        else:
            return False

    if len(rn) == 2:
        return helper(rn[0], rn[1], sigma)
    elif len(rn) == 3:
        return (
            (helper(rn[0], rn[1], sigma) and helper(rn[0] | rn[1], rn[2], sigma))
            or (helper(rn[0], rn[2], sigma) and helper(rn[0] | rn[2], rn[1], sigma))
            or (helper(rn[1], rn[2], sigma) and helper(rn[1] | rn[2], rn[0], sigma))
        )
    elif len(rn) == 4:
        return (
            (
                helper(rn[0], rn[1], sigma)
                and helper(rn[2], rn[3], sigma)
                and helper(rn[0] | rn[1], rn[2] | rn[3], sigma)
            )
            or (
                helper(rn[0], rn[2], sigma)
                and helper(rn[1], rn[3], sigma)
                and helper(rn[0] | rn[2], rn[1] | rn[3], sigma)
            )
            or (
                helper(rn[0], rn[3], sigma)
                and helper(rn[1], rn[2], sigma)
                and helper(rn[0] | rn[3], rn[1] | rn[2], sigma)
            )
        )
    else:
        raise Exception("Only for 2 - 4 decompositions")


# Return True if decomposition of rel to all r in rn is a dependency-preserving decomposition
# Otherwise, return False
# Caveat: This function will only handle up to 4 decompositions
# input
#  - rel: Rel
#  - rn: [Rel]
#  - sigma: Sigma
# output
#  - res: bool
def is_preserving(rel, rn, sigma):
    # For each fragment, find projection
    # Union all of them
    sigma_ = Sigma()
    for r in rn:
        prj = projection(r.attrs, sigma)
        sigma_ = sigma_ | prj
    # Check if you can form the FDs in the original sigma
    for fd in sigma:
        if not fd.dst <= attribute_closure(fd.src, sigma_):
            return False
    return True


# CS2102 BCNF decomposition algorithm. Guaranteed to be a lossless-join decomp.
def decompose_bcnf(rel, sigma):
    # Find a "more but not all" closure
    # Decompose into 2 tables -> R1 contains all attributes in closure, R2 contains the rest
    # Check if the decomposed tables are in BCNF
    m = check_bcnf(rel, rel, sigma)
    if m is None:
        return [rel]

    r1_attr = m.src | m.dst
    r2_attr = rel.attrs - m.dst

    r1 = decompose_bcnf(R(f"R({repr(r1_attr)})"), sigma)
    r2 = decompose_bcnf(R(f"R({repr(r2_attr)})"), sigma)

    return r1 + r2


def minimal_basis(rel, sigma):
    # transform FDs so that each RHS only contains one attribute
    decomposed_sigma = []
    for fd in sigma:
        for attr in fd.dst:
            decomposed_sigma.append(FD(fd.src, A(attr)))

    # remove redundant attributes on LHS of FDs
    no_redundant_attributes_sigma = Sigma(*decomposed_sigma)

    for fd in decomposed_sigma:
        if len(fd.src) == 1:
            continue
        for attr in fd.src:
            if fd.dst <= attribute_closure(
                fd.src - A(attr), no_redundant_attributes_sigma
            ):
                temp = []
                for x in no_redundant_attributes_sigma:
                    if x == fd:
                        temp.append(FD(fd.src - A(attr), fd.dst))
                    else:
                        temp.append(x)
                no_redundant_attributes_sigma = Sigma(*temp)

    # print(no_redundant_attributes_sigma)
    # remove redundant FDs
    no_redundant_sigma = Sigma(*no_redundant_attributes_sigma)

    for fd in no_redundant_attributes_sigma:
        no_redundant_sigma = Sigma(*no_redundant_sigma)
        temp = []
        for x in no_redundant_sigma:
            if x != fd:
                temp.append(x)
        temp = Sigma(*temp)
        if fd.dst <= attribute_closure(fd.src, temp):
            no_redundant_sigma = temp

    # return the minimal basis
    return no_redundant_sigma


def decompose_3nf(rel, sigma):
    # derive minimal basis
    mb = minimal_basis(rel, sigma)
    # combine FDs with the same LHS
    dict = {}
    combined_sigma = Sigma()
    for fd in mb:
        if fd.src in dict:
            dict[fd.src] = fd.dst | dict[fd.src]
        else:
            dict[fd.src] = fd.dst
    for k, v in dict.items():
        combined_sigma = combined_sigma | Sigma(FD(k, v))

    # Create a table for each FD
    ans = []
    for fd in combined_sigma:
        ans.append(R(f"R({repr(fd.src | fd.dst)})"))

    # If none of the tables contain a key of rel, create a table that contains a key of rel (any key)
    k = keys(rel, sigma)
    found_key = False
    for r in ans:
        for key in k:
            if key <= r.attrs:
                found_key = True
                break
        if found_key:
            break

    if not found_key:
        ans.append(R(f"R({repr(k[0])})"))

    print(ans)

    # Removed subsumed tables
    temp = []
    for i in range(len(ans)):
        is_subsumed = False
        for j in range(len(ans)):
            if i == j:
                continue
            if ans[i].attrs <= ans[j].attrs:
                is_subsumed = True
                break
        if not is_subsumed:
            temp.append(ans[i])
    return temp
