from sherpa.astro.ui import *


load_pha("source_bin10.pi")

subtract()
notice(1, 7)

set_source(xswabs.abs1 * powlaw1d.power)

abs1.nh = 1e-01
abs1.nh.min = 1e-07
abs1.nh.max = 10

power.ampl = 9.7652e-06
power.ampl.min = 9.7652e-08
power.ampl.max = 0.01

set_pileup_model(jdpileup.jdp)
jdp.f.min = 0.85
jdp.ftime = 3.2
jdp.fracexp = 1

# The result we expect (so things run faster)
abs1.nH = 6.1237
power.gamma = 1.4197
power.ampl = 0.00196362
jdp.alpha = 0.536952
jdp.f = 0.909478

fit()
