from sherpa.astro.ui import *

load_pha("q1127_src1.pi")
load_pha(2, "q1127_src1_grp30.pi")

notice_id(1, 0.3, 7.0)
notice_id(2, 0.3, 7.0)

set_source(xsphabs.abs1*xszphabs.zabs1*powlaw1d.p1)
abs1.nH = 0.041
freeze(abs1.nH)
zabs1.redshift=0.312
set_source(2, xsphabs.abs2*xszphabs.zabs2*powlaw1d.p2)
abs2.nH = 0.041
freeze(abs2.nH)
zabs2.redshift=0.312

fit()

set_stat('leastsq')
stat_lsqr = calc_stat()
set_stat('chi2modvar')
stat_chi2m = calc_stat()
set_stat('cash')
stat_cash = calc_stat()
set_stat('chi2constvar')
stat_chi2c = calc_stat()
set_stat('chi2gehrels')
stat_chi2g = calc_stat()
set_stat('chi2datavar')
stat_chi2d = calc_stat()
set_stat('chi2xspecvar')
stat_chi2x = calc_stat()
set_stat('cstat')
stat_cstat = calc_stat()
