from sherpa.astro.ui import *
from sherpa.utils import _ncpus
load_table(1,"1838_rprofile_rmid.fits", 3, ["RMID","SUR_BRI","SUR_BRI_ERR"])
set_source(beta1d.src)
src.r0 = 105
src.beta = 4
src.xpos = 0
src.ampl = 0.00993448
src.ampl.max = 10
freeze(src.xpos)
set_method_opt('numcores', _ncpus)
fit()
