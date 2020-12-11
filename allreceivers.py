# John Owens 2019
# Northern Illinois University
# This program creates seismograms for all receivers so you should only
# have to change source parameters.

import obspy
import instaseis
import os
import matplotlib.pyplot as plt
from datetime import datetime
plt.rcParams['figure.figsize'] = (12,8)
db=instaseis.open_db("http://instaseis.ethz.ch/icy_ocean_worlds/Tit124km-33pNH-hQ_2s")
ntwk='ST'

# Define M0 from shear modulus (mu), area of rupture along the fault (A),
# and the average slip along the fault (D).
# Adapted from Stein & Wysession (2003).
mu = 2.0e+9
A = 6.66e+8
D = 0.5
Mzero = mu*A*D

R01=instaseis.Receiver(latitude=-10.0, longitude=-165.0, network=ntwk,\
	 station='01')
R02=instaseis.Receiver(latitude=-8.8, longitude=-167.4, network=ntwk,\
	 station='02')
R03=instaseis.Receiver(latitude=-7.6, longitude=-169.8, network=ntwk,\
	 station='03')
R04=instaseis.Receiver(latitude=-6.4, longitude=-172.3, network=ntwk,\
	 station='04')
R05=instaseis.Receiver(latitude=-5.2, longitude=-174.7, network=ntwk,\
	 station='05')
R06=instaseis.Receiver(latitude=-3.9, longitude=-177.1, network=ntwk,\
	 station='06')
R07=instaseis.Receiver(latitude=-2.7, longitude=-179.5, network=ntwk,\
	 station='07')
R08=instaseis.Receiver(latitude=-1.5, longitude=178.1, network=ntwk,\
	 station='08')
R09=instaseis.Receiver(latitude=-0.3, longitude=175.6, network=ntwk,\
	 station='09')
R10=instaseis.Receiver(latitude=0.9, longitude=173.2, network=ntwk,\
	 station='10')
R11=instaseis.Receiver(latitude=2.1, longitude=170.8, network=ntwk,\
	 station='11')
R12=instaseis.Receiver(latitude=3.3, longitude=168.4, network=ntwk,\
	 station='12')
R13=instaseis.Receiver(latitude=4.5, longitude=166.0, network=ntwk,\
	 station='13')
R14=instaseis.Receiver(latitude=5.74, longitude=163.5, network=ntwk,\
	 station='14')
R15=instaseis.Receiver(latitude=7.0, longitude=161, network=ntwk,\
	 station='15')
source=instaseis.Source.from_strike_dip_rake(latitude=-3.0, longitude=160.0,\
	 depth_in_m=2000, strike=85, dip=2, rake=90, M0=Mzero,\
	 origin_time=obspy.UTCDateTime(datetime.now()))
receivers = [R01, R02, R03, R04, R05, R06, R07, R08, R09, R10, R11, R12,\
	 R13, R14, R15]
i=0
while i < 15:
	 print("Exporting receiver %s" % receivers[i].station)
	 seismogram=db.get_seismograms(source=source,receiver=receivers[i],\
	 	 components=['N','E','Z','R','T'],kind=u'velocity', dt=0.02)
	 recname='%s_%s' % (ntwk,receivers[i].station)
	 srcname='%s_Mw_%3.1f' % (source.origin_time.date,\
				source.moment_magnitude)
	 filename='%s_%s' % (recname,srcname)
	 filename=filename.replace('.','_')
	 seismogram.write(os.path.join('OUTPUT','%s%s' % (ntwk,\
				       receivers[i].station),\
				       filename),format='sac')
	 i+=1
print("Export successful.")
