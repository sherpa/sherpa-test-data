from sherpa.astro.ui import *

load_pha(1, "pi2278.fits")
load_arf(1, "arf2278.fits")
load_rmf(1, "rmf2278.fits")

load_pha(2, "pi2286.fits")
load_arf(2, "arf2286.fits")
load_rmf(2, "rmf2286.fits")

set_source(1, xswabs.abs1 * powlaw1d.pl1)
set_source(2, abs1 * powlaw1d.pl2)

pl2.gamma = pl1.gamma

fit(1, 2)
