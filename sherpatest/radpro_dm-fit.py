# Test that CRATES Data Model syntax works as well as in radpro thread
from sherpa.astro.ui import *
load_table(1,"1838_rprofile_rmid.fits[cols rmid,sur_bri,sur_bri_err]")
set_source(beta1d.src)
src.r0 = 105
src.beta = 4
src.xpos = 0
src.ampl = 0.00993448
src.ampl.max = 10
freeze(src.xpos)
fit()
