# coding: utf-8
import sherpa.ui as ui

ui.load_data("bb_data.dat")
ui.load_template_model('bb1', "bb_index.dat", template_interpolator_name=None)
ui.set_method('gridsearch')
ui.set_method_opt('sequence', [[2000, 0], [2100,0]])
ui.set_source('bb1')
ui.fit()
