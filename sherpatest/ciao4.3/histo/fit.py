from sherpa.astro.ui import *
import numpy
load_data(1, 'cstat.dat', colkeys=('zabs1.nh', 'p1.gamma', 'p1.ampl'))

x=None; y=None
# Can compare numpy version strings this way
if (numpy.version.version < "1.3.0"):
    y, x = numpy.histogram(get_data().y, bins=50, normed=True, new=True)
else:
    y, x = numpy.histogram(get_data().y, bins=50, normed=True)
x = x[:-1]
load_arrays(1, x, y)
set_model(1, gauss1d.g1)
set_stat('chi2xspecvar')
fit()
set_method('neldermead')
set_stat('cstat')
fit()
