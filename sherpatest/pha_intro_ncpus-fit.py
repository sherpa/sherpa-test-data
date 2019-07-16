from sherpa.astro.ui import *
from sherpa.utils import _ncpus

load_pha("3c273.pi")
notice_id(1, 0.1, 6.0)
subtract()

set_source(xsphabs.abs1 * powlaw1d.p1)
abs1.nH = 0.07
freeze(abs1.nH)

set_method_opt('numcores', _ncpus)
fit()
covariance()
