# coding: utf-8

import sherpa.ui as ui

ui.load_data("default_interp", "bb_data.dat")
ui.load_template_model('bb1', "bb_index.dat")
ui.load_template_model('bb2', "bb_index.dat")
ui.set_model("default_interp", bb1+bb2)
ui.freeze("bb1.dummy")
ui.freeze("bb2.dummy")
ui.fit("default_interp")
