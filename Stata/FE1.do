cd D:\博士\论文\JA4

xtnbreg overspeed brakes range speed rpm accelerator enginefuelrate date1-date6,fe nolog exposure(kilo)
estimates store overspeed_date

xtnbreg overspeed brakes range speed rpm accelerator enginefuelrate time1-time24,fe nolog exposure(kilo)
estimates store overspeed_time

xtnbreg highspeedbrake brakes range speed rpm accelerator enginefuelrate date1-date6,fe nolog exposure(kilo)
estimates store highspeedbrake_date

xtnbreg highspeedbrake brakes range speed rpm accelerator enginefuelrate time1-time24,fe nolog exposure(kilo)
estimates store highspeedbrake_time

xtnbreg harshacceleration brakes range speed rpm accelerator enginefuelrate date1-date6,fe nolog exposure(kilo)
estimates store harshacceleration_date

xtnbreg harshacceleration brakes range speed rpm accelerator enginefuelrate time1-time24,fe nolog exposure(kilo)
estimates store harshacceleration_time

xtnbreg harshdeceleration brakes range speed rpm accelerator enginefuelrate date1-date6,fe nolog exposure(kilo)
estimates store harshdeceleration_date

xtnbreg harshdeceleration brakes range speed rpm accelerator enginefuelrate time1-time24,fe nolog exposure(kilo)
estimates store harshdeceleration_time

esttab overspeed_date highspeedbrake_date harshacceleration_date harshdeceleration_date using report1.csv,replace wide
esttab overspeed_time highspeedbrake_time harshacceleration_time harshdeceleration_time using report2.csv,replace wide

estimates stats *
