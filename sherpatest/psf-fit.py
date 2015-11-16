from sherpa.astro.ui import *

load_image("center_box_0.25pix.fits")
notice2d("BOX(88.16875,75.8625,70.416667,68.508334)")

load_psf("psf", "psf_f1_norm_0.25pix.fits")
psf.size = [72,72]
psf.center = [128,129]
set_psf(psf)
set_source(gauss2d.g1 + const2d.c1)
c1.c0 = 1.0
g1.fwhm = 6
g1.xpos = 90
g1.ypos = 80
g1.ampl = 100
freeze(c1.c0)

set_method("neldermead")
set_method_opt("iquad",0)
set_method_opt("finalsimplex",0)
set_stat("cash")
fit()
