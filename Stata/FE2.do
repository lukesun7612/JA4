cd D:\博士\论文\JA4

nbreg overspeed brakes range speed rpm accelerator enginefuelrate date1-date11 id2-id256,r nolog exposure(kilo)
estimates store overspeed_date
nbreg overspeed brakes range speed rpm accelerator enginefuelrate time1-time23 id2-id256,r nolog exposure(kilo)
estimates store overspeed_time

nbreg highspeedbrake brakes range speed rpm accelerator enginefuelrate date1-date11 id2-id256,r nolog exposure(kilo)
estimates store highspeedbrake_date
nbreg highspeedbrake brakes range speed rpm accelerator enginefuelrate time1-time23 id2-id256,r nolog exposure(kilo)
estimates store highspeedbrake_time

nbreg harshacceleration brakes range speed rpm accelerator enginefuelrate date1-date11 id2-id256,r nolog exposure(kilo)
estimates store harshacceleration_date
nbreg harshacceleration brakes range speed rpm accelerator enginefuelrate time1-time23 id2-id256,r nolog exposure(kilo)
estimates store harshacceleration_time

nbreg harshdeceleration brakes range speed rpm accelerator enginefuelrate date1-date11 id2-id256,r nolog exposure(kilo)
estimates store harshdeceleration_date
nbreg harshdeceleration brakes range speed rpm accelerator enginefuelrate time1-time23 id2-id256,r nolog exposure(kilo)
estimates store harshdeceleration_time

// esttab * using report1.csv,replace cells(b(fmt(a3) star))

// outreg2 [overspeed_poi overspeed_nb highspeedbrake_poi highspeedbrake_nb harshacceleration_poi harshacceleration_nb harshdeceleration_poi harshdeceleration_nb] using report2.doc,replace tstat

estimates stats *
