from sherpa.astro.ui import *

load_image("center_box_0.25pix.fits")
notice2d("BOX(88.16875,75.8625,70.416667,68.508334)")

load_psf("psf", box2d.b1)
set_psf(psf)
psf.size = [5,5]
psf.center = [89,77]
b1.xlow = 0
#b1.xlow.min=53
#b1.xlow.max=123
b1.xhi = 169
#b1.xhi.min=53
#b1.xhi.max=123
b1.ylow = 0
#b1.ylow.min=42
#b1.ylow.max=110
b1.yhi = 147
#b1.yhi.min=42
#b1.yhi.max=110
b1.ampl.min = -1
b1.ampl.max = 1

set_source(gauss2d.g1 + const2d.c1)
c1.c0 = 1.0
g1.fwhm = 6
g1.xpos = 84
g1.ypos = 73
g1.ampl = 55
freeze(c1.c0)

set_method("simplex")
set_method_opt("iquad",0)
set_method_opt("finalsimplex",0)
set_stat("cash")
fit()
