from sherpa.astro.ui import *
from sherpa.utils import _ncpus

load_data(1, 'data.txt', 3, ("col1", "col3", "col4"))
set_source(beta1d.b1)
b1.r0 = 4.2
b1.beta = 0.5
b1.ampl.max = 100
b1.ampl = 12

load_psf('psf', 'king_kernel.txt')
psf.radial=1
psf.size=1082
set_psf(psf)
set_method_opt('numcores', _ncpus)
fit()
