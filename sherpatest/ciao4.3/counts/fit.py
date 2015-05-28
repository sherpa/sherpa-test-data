from sherpa.astro.ui import *
    
load_pha("q1127_src1.pi")
load_pha(2, "q1127_src1_grp30.pi")

counts_data1 = calc_data_sum(1,15)
counts_data2 = calc_data_sum(2,15)

notice_id(1, 0.3, 7.0)
notice_id(2, 0.3, 7.0)

set_source(xsphabs.abs1*xszphabs.zabs1*powlaw1d.p1)
abs1.nH = 0.041
freeze(abs1.nH)
zabs1.redshift=0.312

counts_model1 = calc_model_sum(1,15)
eflux1 = calc_energy_flux()

set_source(2, xsphabs.abs2*xszphabs.zabs2*powlaw1d.p2)
abs2.nH = 0.041
freeze(abs2.nH)
zabs2.redshift=0.312

counts_model2 = calc_model_sum(2,15)
eflux2 = calc_energy_flux(2,15)
pflux1 = calc_photon_flux(2,15)

