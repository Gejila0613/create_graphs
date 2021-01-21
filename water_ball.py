#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: DJ
# CreateTime:  2020/9/22
# FileName:  water_ball 

from pyecharts import options as opts
from pyecharts.charts import Liquid
#,Page
#from pyecharts.globals import SymbolType

def liquid() -> Liquid:
    c = (
        Liquid()
        .add("lq", [0.67, 0.30, 0.15],is_outline_show=False)
        #shape=SymbolType.TRIANGLE,
        #color=['#4B0082']
        .set_global_opts(title_opts=opts.TitleOpts(title="Liquid"))
    )
    return c


liquid().render('./img/liquid.html') 