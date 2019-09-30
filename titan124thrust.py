import obspy
import instaseis
import os
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12,8)
db=instaseis.open_db("http://instaseis.ethz.ch/icy_ocean_worlds/Tit124km-33pNH-hQ_2s")
print(db)

#arbitrary network and station names
ntwk="6J"
stn="20STN"
receiver=instaseis.Receiver(latitude=0.0, longitude=20.0, network=ntwk,\
	 station=stn)
#Define source by moment tensor
#source=instaseis.Source(latitude=0.0, longitude=0.0, depth_in_m=1000,\
#	m_rr=1.0e+24,m_tt=1.0e24,m_pp=1.0e+24,\
#	m_rt=0.0,m_rp=0.0,m_tp=0.0,\
#	origin_time=obspy.UTCDateTime(2019,7,18,0,0,0))

#Define source by strike/dip/rake
source=instaseis.Source.from_strike_dip_rake(latitude=0.0, longitude=0.0,\
	 depth_in_m=1000, strike=120, dip=7, rake=90, M0=1E20)

seismogram=db.get_seismograms(source=source,receiver=receiver)
print(seismogram)

#Prompt for plotting seismograms
plotprompt=input("Would you like to plot the seismogram? (type yes or no): ")
if plotprompt == "yes":
	seismogram.plot()
else:
	pass

#Prompt for exporting raw data (SAC).
rawprompt = input("Would you like to export the data? (type yes or no): ")
if rawprompt=="yes":
	recname='%s_%s' % (ntwk,stn)
	srcname='%s_Mw_%3.1f' % (source.origin_time.date,\
				 source.moment_magnitude)
	filename='%s_%s' % (recname,srcname)
	filename=filename.replace('.','_')
	seismogram.write(os.path.join('data_out',filename),format='sac')
	print("Export successful.")
else:
	pass

#Prompt for saving image of plot.
save=input("Would you like to save this plot? (type yes or no): ")
if save == "yes":
	seismogram.plot(outfile='titan124.png')
	print("Saved as: titan124.png")
else:
	print("Sayonara!")
