# NMR_dilution_fit

A little Python 3 script that can be used to extract association constants from NMR dilution data.
Simply applies equation 36 from [Martin, R. B. *Chem. Rev.* **1996**, *96*,
3043–3064](http://dx.doi.org/10.1021/cr960037v). This equation assumes a monomer–dimer equilibrium
(not polymerization).

The equation for the observed chemical shift as entered into the script:

`(p[0] - p[1])*(1+(1-numpy.sqrt(8*p[2]*x+1))/(4*p[2]*x)) + p[1]`

where `p[0]` is the chemical shift of the dimer, `p[1]` is the chemical shift of the monomer,
`p[2]` is the dimerization constant, and `x` is the concentration.


## Requirements

* Python 3
* NumPy
* SciPy

## Usage

Simply execute as usual, passing the filename of the data as an argument (e.g., (`python3
NMR_dilution_fit.py sample_input.txt`)). This should be a simple text file with x (concentration)
and y (chemical shift) columns. See the included sample file.

