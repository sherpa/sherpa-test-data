from sherpa.astro.ui import *

load_data(1, "data1.dat", 3)

set_model(polynom1d.m1)
thaw(m1.c1)
thaw(m1.c2)
thaw(m1.c3)

fit()

set_model(polynom1d.m2)
thaw(m2.c1)
m2.offset = 4.3979 * m2.c1

fit()
