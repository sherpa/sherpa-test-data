# coding: utf-8

import sherpa.ui as ui

ui.load_data("default_interp", "bb_data.dat")
ui.load_template_model('bb1', "bb_index.dat")
ui.set_model("default_interp", bb1)
ui.set_method('gridsearch')
ui.set_method_opt('sequence', ui.get_model_component('bb1').parvals)
ui.fit("default_interp")
