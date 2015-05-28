from sherpa.astro.ui import *
load_data("phas.dat")
set_source(gauss1d.g)
g.ampl=100
g.pos=810
g.fwhm=30
fit(1)

covar(1)
proj(1)

fit_res1 = get_fit_results()
covar_res1 = get_covar_results()
proj_res1 = get_proj_results()
#xconf(1)

load_pha(2, "sis0.pha")

load_arf(2, "sis0.arf")
load_rmf(2, "sis0.rmf")

notice_id(2, 1, 2.5)
set_source(2, xswabs.xs1 * powlaw1d.p)
p.ref = 0.1
p.ampl.max = 10
p.gamma = 1.70
p.ampl = 0.6
xs1.nh = 0.15
fit(2)
covar(2)
proj(2)

fit_res2 = get_fit_results()
covar_res2 = get_covar_results()
proj_res2 = get_proj_results()
#xconf(2)
