from sherpa.astro.ui import *

load_data(1, 'data.txt', 3, ("col1", "col3", "col4"))
set_source(beta1d.b1)
b1.r0 = 22
b1.beta = 0.5
b1.ampl = 2
load_psf('psf', beta1d.k1)
k1.r0 = 4.72
k1.beta = 0.6523
k1.ampl = 1
freeze(k1)
psf.size = 75
psf.norm = 0
set_psf(psf)
fit()
