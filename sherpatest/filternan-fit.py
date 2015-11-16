from sherpa.astro.ui import *

# Case 1: single dataset with NaNs on the X
# I expect the stat to be not NaN
load_data("with_nan.fits")
set_source(powlaw1d.p)
set_stat("chi2datavar")
fit(filter_nan=True)
s=get_stat_info()[0].statval

# Case 2: simultaneous fit with NaNs on both X axes
# I expect the stat to be not NaN
load_data(2, "with_nan.fits")
set_source(powlaw1d.p2)
fit(filter_nan=True)
