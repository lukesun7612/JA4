#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: lukes
@project: JA4
@file: barplot.py
@time: 2021/5/6 12:26
"""


import pandas as pd
import numpy as np
from pyecharts.charts import Bar
from pyecharts import options as opts




if __name__ == '__main__':
    input = "D:/博士/论文/JA4/paneldata_hours0.csv"
    df = pd.read_csv(input, header=0, index_col='Date')
    x_axis1 = df.index.unique().tolist()
    x_axis2 = df['Time'].unique().tolist()

    y1, y2, y3, y4, y5, y6, y7, y8 = [], [], [], [], [], [], [], []
    for d in x_axis1:
        y1.append(df.loc[d]['Overspeed'].sum()/df.loc[d]['Kilo'].replace(np.nan, 0).sum())
        y2.append(df.loc[d]['Highspeedbrake'].sum()/df.loc[d]['Kilo'].replace(np.nan, 0).sum())
        y3.append(df.loc[d]['Harshacceleration'].sum()/df.loc[d]['Kilo'].replace(np.nan, 0).sum())
        y4.append(df.loc[d]['Harshdeceleration'].sum()/df.loc[d]['Kilo'].replace(np.nan, 0).sum())
    c = (
        Bar(init_opts=opts.InitOpts(width="1250px", height="550px"))
            .add_xaxis(x_axis1)
            .add_yaxis("Overspeed", y1, gap='0')
            .add_yaxis("Highspeedbrake", y2, gap='0')
            .add_yaxis("Harshacceleration", y3, gap='0')
            .add_yaxis("Harshdeceleration", y4, gap='0')
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                             )
            .set_global_opts(
            # title_opts=opts.TitleOpts(title="Date Effect"),
                             xaxis_opts=opts.AxisOpts(name='Date', name_location='center', name_gap=50, axislabel_opts=opts.LabelOpts(font_size=10, rotate=40)),
                             yaxis_opts=opts.AxisOpts(name='Incidence', name_location='center', name_gap=40, name_rotate=0, splitline_opts=opts.SplitLineOpts(is_show=True),)
                             )
            .render("./Figure/bar1.html")
    )
    df = df.set_index('Time')
    for t in x_axis2:
        y5.append(df.loc[t]['Overspeed'].sum() / df.loc[t]['Kilo'].replace(np.nan, 0).sum())
        y6.append(df.loc[t]['Highspeedbrake'].sum() / df.loc[t]['Kilo'].replace(np.nan, 0).sum())
        y7.append(df.loc[t]['Harshacceleration'].sum() / df.loc[t]['Kilo'].replace(np.nan, 0).sum())
        y8.append(df.loc[t]['Harshdeceleration'].sum() / df.loc[t]['Kilo'].replace(np.nan, 0).sum())
    c = (
        Bar(init_opts=opts.InitOpts(width="1250px", height="550px"))
            .add_xaxis(x_axis2)
            .add_yaxis("Overspeed", y5, gap='0')
            .add_yaxis("Highspeedbrake", y6, gap='0')
            .add_yaxis("Harshacceleration", y7, gap='0')
            .add_yaxis("Harshdeceleration", y8, gap='0')
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                             )
            .set_global_opts(
            # title_opts=opts.TitleOpts(title="Hour Effect"),
                             xaxis_opts=opts.AxisOpts(name='Hour', name_location='center', name_gap=50, axislabel_opts=opts.LabelOpts(font_size=8, rotate=40)),
                             yaxis_opts=opts.AxisOpts(name='Incidence', name_location='center', name_gap=40, name_rotate=0, splitline_opts=opts.SplitLineOpts(is_show=True),)
                             )
            .render("./Figure/bar2.html")
    )
