from sherpa.astro.ui import *

load_image("image2.fits")

set_coord("physical")
notice2d("circle(4065.5,4250.5,78.8)")

set_stat("cash")
set_method("neldermead")

set_model(gauss2d.g1)

g1.ampl = 20
g1.fwhm = 60
g1.xpos = 4065.5
g1.ypos = 4250.5
freeze(g1.ellip)
freeze(g1.theta)

fit()

freeze(g1)
set_model(g1 + gauss2d.g2)
g2.ampl = 200
g2.fwhm = 5
g2.xpos = 4065.5
g2.ypos = 4250.5
freeze(g2.ellip)
freeze(g2.theta)

fit()
