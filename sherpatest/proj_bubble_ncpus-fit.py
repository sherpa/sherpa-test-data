from sherpa.astro.ui import *
from sherpa.utils import _ncpus

load_pha("bubble.pi")
set_stat("cstat")
notice(0.3,7)

set_source(xsphabs.abs1*xsmekal.mek1)
mek1.norm=1e-5
mek1.kT=10
abs1.nh=0.056
freeze(abs1)
set_method_opt('numcores', _ncpus)
fit()
proj()
conf()
covar()
