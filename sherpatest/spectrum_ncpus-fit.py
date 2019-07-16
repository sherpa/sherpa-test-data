from sherpa.astro.ui import *
from sherpa.utils import _ncpus

load_pha("data1.pi")
load_arf("arf1.fits")
load_rmf("rmf1.fits")
ignore()
notice(0.5,7)

set_source(xsphabs.abs2*(xsmekal.mek1+xsmekal.mek2))

abs2.nh=1.1
mek1.kt=0.8
mek1.norm=0.7
mek2.kt=2.4
mek2.norm=1.

mek1.norm.max=1.e10
mek2.norm.max=1.e10
mek1.norm.min=1.e-10
mek2.norm.min=1.e-10
set_method_opt('numcores', _ncpus)
fit()
