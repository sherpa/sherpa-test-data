from sherpa.astro.ui import *

load_data("MNLup_2138_0670580101_EMOS1_S001_spec.15grp")

#ignore_bad()
old_abund = get_xsabund()
set_analysis('energy')
ignore(None, .2)
ignore(5., None)
set_xsabund('grsa')
set_stat('chi2xspecvar')
set_model(1, xsapec.a1)
a1.kT  = 1
a1.norm = 1e-4
subtract(1)
set_xsabund(old_abund)
