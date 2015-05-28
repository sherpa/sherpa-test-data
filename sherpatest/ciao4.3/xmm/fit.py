from sherpa.astro.ui import *
load_pha('pn_pi_src_bin10.ds')
load_arf('pn_pi_src.arf')
load_rmf('epn_ff20_dY9.rmf')
notice(2.,10.)
set_source(xswabs.gal*xswabs.intrin*xspowerlaw.phard)
gal.nH= 0.0119
freeze(gal.nh)
intrin.nH.max=30
fit()
