from sherpa.astro.ui import *

load_pha("bubble.pi")
set_stat("cstat")
notice(0.3,7)

set_source(xsphabs.abs1*xsmekal.mek1)
mek1.norm=1e-5
mek1.kT=10
abs1.nh=0.056
freeze(abs1)
fit()
proj()
covar()
