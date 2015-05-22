from sherpa.astro.ui import *
import sherpa.astro.ui as ui
execfile("acis_bkg_model.py", locals())

ids = [1,2,3,4]

for ii in ids:

    load_pha(ii,'obs%i.pi' % ii)
    load_bkg_rmf(ii, 'obs%i.rmf' % ii)
    load_bkg_arf(ii, 'obs%i.arf' % ii)

    bkg_arf = get_bkg_arf(ii)
    bkg_rmf = get_bkg_rmf(ii)

    bkg_arf_in_src = unpack_arf('obs%i.arf' % ii)
    bkg_rmf_in_src = unpack_rmf('obs%i.rmf' % ii)

    scale = get_bkg_scale(ii)
    
    rsp = get_response(ii)

    create_model_component("const1d", "c%i" % ii)
    const = get_model_component("c%i" % ii)

    bkg_model = const * acis_bkg_model('acis7s')

    set_full_model(ii, (rsp(xsphabs.abs1*powlaw1d.pow1) + scale * bkg_rmf_in_src(bkg_model)))
    set_bkg_full_model(ii, bkg_rmf(bkg_model))


# Fitting and confidence

set_method("levmar")
set_stat("cstat")

fit_bkg()

freeze(c1, c2, c3, c4)

ignore(None,0.5)
ignore(7.,None)

set_par(abs1.nh,0.0223)
freeze(abs1)
fit()
set_method("neldermead")
fit()

# Source filtered and ungrouped, background filtered and grouped by 5
for ii in ids:
    group_counts(ii, 5, bkg_id=1)
    get_bkg(ii, bkg_id=1).notice(.5,7.)


fit()

for ii in ids:
    ungroup(ii, bkg_id=1)
notice()

# Source filtered and grouped, background filtered and grouped according to source

for ii in ids:

    # group and filter source
    group_counts(ii, 10)
    ignore_id(ii, None, 0.5)
    ignore_id(ii, 7., None)

    # group background using source flags and filter
    grps = get_grouping(ii)
    set_grouping(ii, grps, bkg_id=1)
    if (get_bkg(ii, bkg_id=1).grouped == True):
        ungroup(ii, bkg_id=1)
    group(ii, bkg_id=1)
    bkg = get_bkg(ii, bkg_id=1)
    bkg.ignore(None,0.5)
    bkg.ignore(7.,None)

fit()
