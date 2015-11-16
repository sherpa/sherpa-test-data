from sherpa.astro.ui import *
load_pha("s0_mar24_bin.pha")
load_arf("s0_mar24.arf")
load_rmf("s0_mar24.rmf")

set_source(powlaw1d.aa)
aa.gamma=1.6
aa.gamma.min=-4
aa.gamma.max=10
aa.ref=1
aa.ampl=0.000003
aa.ampl.min=0.00000002
aa.ampl.max=1.0

set_analysis("channel")
# As of CIAO 4.5, can filter on channel number,
# even when data are grouped.  This filter
# notices groups 21-66.  Fit results should
# exactly match those in ../grouped/fit.py test.
notice_id(1, 41, 167)
fit()
