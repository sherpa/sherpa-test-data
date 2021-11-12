#!/usr/bin/env python
#
# This used to use coord=WCS but this is not
# well supported, so has been changed back to
# coord=physical.
#
from sherpa.astro.ui import *

image_file = "acisf07999_000N001_r0035_regevt3_srcimg.fits"
psf_file = "acisf07999_000N001_r0035b_psf3.fits"
reg_file = "ellipse(3145.8947368421,4520.7894736842,37.0615234375,15.3881587982,92.2273254395)"
srcid = 1

load_data(srcid, image_file)
load_psf("psf%i" % srcid, psf_file)
set_psf(srcid, "psf%i" % srcid)

set_coord(srcid, "physical")
notice2d_id(srcid, reg_file)

# Switch to WCS for fitting
# set_coord(srcid, "wcs")  REMOVED

# Use Nelder-Mead, C-statistic as fit method, statistic
set_method("neldermead")
set_stat("cstat")

set_source(srcid, 'gauss2d.src + const2d.bkg')
guess(srcid, src)

image_file = "acisf08478_000N001_r0043_regevt3_srcimg.fits"
psf_file = "acisf08478_000N001_r0043b_psf3.fits"
reg_file = "ellipse(3144.5238095238,4518.8095238095,25.2978591919,19.1118583679,42.9872131348)"
srcid = 2

load_data(srcid, image_file)
load_psf("psf%i" % srcid, psf_file)
set_psf(srcid, "psf%i" % srcid)

set_coord(srcid, "physical")
notice2d_id(srcid, reg_file)

# Switch to WCS for fitting
# set_coord(srcid, "wcs")  REMOVED

# Use Nelder-Mead, C-statistic as fit method, statistic
set_method("neldermead")
set_stat("cstat")

set_source(srcid, 'gauss2d.src + const2d.bkg')
guess(srcid, src)

fit()
