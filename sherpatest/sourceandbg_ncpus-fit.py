from sherpa.astro.ui import *
from sherpa.utils import _ncpus

load_pha("source.pi")
load_arf("source.arf")
load_rmf("source.rmf")
load_bkg("back.pi")
load_bkg_arf("back.arf")
load_bkg_rmf("back.rmf")

notice(0.3, 10)

set_source(xswabs.a1 * xsbbody.b1)
try:
    set_bkg_source(a1 * xsbbody.b2)
except:
    set_bkg_model(a1 * xsbbody.b2)

a1.nH = 0.0336676
b1.kT = 20
b1.kT.max=20
b1.norm = 1e-02
b2.kT = 0.5
set_par(b2.norm, 1e-05, 1e-6)
set_method_opt('numcores', _ncpus)
fit()
