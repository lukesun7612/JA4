#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: lukes
@project: JA4
@file: barplot.py
@time: 2021/4/28 10:45
"""
import pandas as pd
import numpy as np
from pyecharts.charts import Bar3D
from pyecharts import options as opts
from itertools import zip_longest
input1 = "D:/博士/论文/JA4/paneldata_hours1.csv"
input2 = "D:/博士/论文/JA4/paneldata_hours2.csv"
df1 = pd.read_csv(input1, header=0, index_col='ID')
df2 = pd.read_csv(input2, header=0, index_col='ID')
x_axis = pd.concat([df2['Date'], df1['Date']]).unique().tolist()
y_axis = df1['Time'].unique().tolist()
range_color = ['#FFFFE0', '#F0E68C', '#FFD700', '#FFA500', '#D2691E', '#B22222']
for n, p in enumerate(['Overspeed', 'Highspeedbrake', 'Harshacceleration', 'Harshdeceleration']):
    df1['Incidence'] = (df1[p] / df1['Kilo']).replace(np.nan, 0)
    df2['Incidence'] = (df2[p] / df2['Kilo']).replace(np.nan, 0)
    bar3d = Bar3D(init_opts=opts.InitOpts(width="1000px", height="550px"))
    for i, j in zip_longest(df1.index.unique(), df2.index.unique()):
        dfn = pd.DataFrame(0, index=range(144), columns=['Date', 'Time', 'Incidence'])
        if j is None:
            data = pd.concat([dfn, df1.loc[[str(i)], ['Date', 'Time', 'Incidence']]])
        else:
            data = pd.concat([df2.loc[[str(j)], ['Date', 'Time', 'Incidence']], df1.loc[[str(i)], ['Date', 'Time', 'Incidence']]])
        data = [[d[0], d[1], d[2]] for d in data.values.tolist()]
        bar3d.add(
            "",
            data,
            shading="lambert",
            xaxis3d_opts=opts.Axis3DOpts(data=x_axis, type_="category", name="Date", name_gap=50, interval=1),
            yaxis3d_opts=opts.Axis3DOpts(data=y_axis, type_="category", name="Hours", name_gap=80, interval=1),
            zaxis3d_opts=opts.Axis3DOpts(type_="value", name="Incidence"),
            grid3d_opts=opts.Grid3DOpts(width=100, height=150, depth=300)
        )
    if n == 0:
        max_v = 5
    elif n == 1:
        max_v = 5
    elif n == 2:
        max_v = 50
    elif n == 3:
        max_v = 30
    bar3d.set_global_opts(title_opts=opts.TitleOpts(title=p, pos_right='50%', pos_top='10%'),
                          visualmap_opts=opts.VisualMapOpts(max_=max_v, range_color=range_color, is_calculable=False, pos_right='20%', pos_top='15%')
                          )
    bar3d.set_series_opts(**{"stack": "stack"})
    bar3d.render("bar3d_stack"+str(n+1)+".html")


if __name__ == '__main__':
    pass
