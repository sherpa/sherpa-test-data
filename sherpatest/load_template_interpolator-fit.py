# coding: utf-8

import sherpa.ui as ui
from sherpa.models.template import KNNInterpolator

ui.load_data("custom_interp", "load_template_interpolator-bb_data.dat")
ui.load_template_interpolator('knn', KNNInterpolator, k=2, order=1)
ui.load_template_model('bb1', "bb_index.dat", template_interpolator_name='knn')
ui.set_model("custom_interp", "bb1")
ui.freeze("bb1.dummy")
ui.fit("custom_interp")

