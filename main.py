from Types import *
from Util import *
from FD import *

import streamlit as st

st.write("# Check your queries about the second half of CS2102 here!")
st.write("## Enter some important information first...")
rel = st.text_input("What is your relation?", "ABCD")
sigma = st.text_input("What are your functional dependencies?", "AB->C;C->D;C->A")

rel = R(f"R({rel})")
sigma = S(sigma)

st.write("### Superkeys")
sks = superkeys(rel, sigma)
st.write(", ".join([str(x) for x in sks]))

st.write("### Keys")
ks = keys(rel, sigma)
st.write(", ".join([str(x) for x in ks]))

st.write("### Prime Attributes")
pas = prime_attributes(rel, sigma)
st.write(", ".join([str(x) for x in pas]))

st.write("## More advanced checks")
st.write(
    """Note: The algorithms are not deterministic. 
    If your relation and FDs have multiple answers, 
    each run may produce a different result. However, they will still be valid."""
)
st.write("### Projection")
r1_projection = st.text_input(
    "What is the fragment that you want to check? We will compute the projection of this fragment.",
    "ABC",
    key="projection",
)
r1_projection = R(f"R({r1_projection})")
p = projection(r1_projection.attrs, sigma)
st.write(p)

st.write("### Check BCNF")
r1_bcnf = st.text_input(
    "What is your fragment that you want to check?", "ABC", key="is_bcnf"
)
r1_bcnf = R(f"R({r1_bcnf})")
is_bcnf = check_bcnf(rel, r1_bcnf, sigma)
if is_bcnf:
    st.write("This fragment is not in BCNF because of:")
    st.write(is_bcnf)
else:
    st.write("This fragment is in BCNF.")

st.write("### Check 3NF")
r1_3nf = st.text_input(
    "What is your fragment that you want to check?", "ABC", key="is_3nf"
)
r1_3nf = R(f"R({r1_3nf})")
is_3nf = check_bcnf(rel, r1_3nf, sigma)
if is_3nf:
    st.write("This fragment is not in 3NF because of:")
    st.write(is_3nf)
else:
    st.write("This fragment is in 3NF.")

st.write("### Check Lossless-join")
r_lossless = st.text_input(
    "Enter the decompositions that you want to check. Only up to 4 decompositions are supported.",
    "ABC,BCD",
    key="is_lossless",
)
r_lossless = [R(f"R({x})") for x in r_lossless.split(",")]
is_l = is_lossless(rel, r_lossless, sigma)
if is_l:
    st.write("This is a lossless-join decomposition.")
else:
    st.write("This is not a lossless-join decomposition.")

st.write("### Check Dependency-preservation")
r_preserving = st.text_input(
    "Enter the decompositions that you want to check.",
    "ABC,BCD",
    key="is_dependency_preserving",
)
r_preserving = [R(f"R({x})") for x in r_preserving.split(",")]
is_p = is_preserving(rel, r_preserving, sigma)
if is_p:
    st.write("This is a dependency-preserving decomposition.")
else:
    st.write("This is not a dependency-preserving decomposition.")

st.write("### Decompose BCNF")
st.write(
    "Note: This will only give an example of a decomposition. It may not be the same as the one you have in mind."
)
decomposed_bcnf = decompose_bcnf(rel, sigma)
for i, r in enumerate(decomposed_bcnf):
    st.write(f"R{i+1}: {r}")


st.write("### Decompose 3NF")
st.write(
    "Note: This will only give an example of a decomposition. It may not be the same as the one you have in mind."
)
decomposed_3nf = decompose_3nf(rel, sigma)
for i, r in enumerate(decomposed_3nf):
    st.write(f"R{i+1}: {r}")
