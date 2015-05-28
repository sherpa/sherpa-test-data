from sherpa.astro.ui import *
load_table(1,"rprofile_rmid.fits", 3,
           ["RMID","SUR_BRI","SUR_BRI_ERR"])
load_psf("psf","psf_rprofile_rmids.fits", 3,
           ["RMID","SUR_BRI"])
set_source(beta1d.src)
src.r0 = 120
src.beta = 4
src.ampl = 5
psf.radial = 1
psf.size = 36
psf.center = 18
set_psf(psf)
fit()
