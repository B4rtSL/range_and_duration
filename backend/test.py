import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.interpolate import interp1d

startmass=2200
nompow_prop=290                 #kW
fuelcons_prop=0.23              #kg/kW/h
propnumber=2
altitude=0.
efficiency=0.8
aspectratio=4.721
cx0=0.0865
area=17

#Air density from SI
air_density=1.2255*(1-(altitude/44300))**4.256

#masses needed in calculations
diffmass_prop=propnumber*nompow_prop*fuelcons_prop*0.75 
fuelmass_prop=0.2*startmass-diffmass_prop                 
endmass_prop=startmass-fuelmass_prop                            

#array of velocities
velos=np.linspace(15,100,50)
#print(x)

times=[]
ranges=[]
czs=[]
cxs=[]

for i in velos:
    cz=2*startmass*9.81/air_density/area/i/i
    cx=cx0+cz*cz/3.14/aspectratio
    czs.append(cz)
    cxs.append(cx)

czs_arr=np.array(czs)
cxs_arr=np.array(cxs)

for i in czs:
    cx_h=cx0+i*i/3.14/aspectratio
    time=1000*pow(i,3/2)*2*efficiency/cx_h/9.81/fuelcons_prop*math.sqrt(air_density*area/2/9.81)*(1/pow(endmass_prop,0.5)-1/pow(startmass,0.5))
    range=3600*i/cx_h*efficiency/9.81/fuelcons_prop*np.log(startmass/endmass_prop)
    times.append(time)
    ranges.append(range)


#plt.plot(cxs_arr, czs_arr)

#for i in velos:
    #A_factor=air_density*area*i*i*math.sqrt(cx0*3.14*aspectratio)
    #time=1000*(efficiency/9.81/i/fuelcons_prop)*math.sqrt(3.14*aspectratio/cx0)*(math.atan(2*9.81*startmass/A_factor)-math.atan(2*9.81*endmass_prop/A_factor))
    #range=3.6*i*time
    #times.append(time)
    #ranges.append(range)

times_arr=100*np.array(times)     
ranges_arr=np.array(ranges) 

f=interp1d(velos, times_arr, kind='cubic')

poly_coef=np.polyfit(velos, times_arr, 4)
print(poly_coef)

poly_roots=np.roots(poly_coef)
#print(poly_roots)

def g(x):
    return (-1)*(poly_coef[0]*(x)**4+poly_coef[1]*(x)**3+poly_coef[2]*(x)**2+poly_coef[3]*(x)+poly_coef[4])

res=optimize.minimize_scalar(g, bounds=(15,100), method='bounded')
print(res.x)

x_list=list(velos*3.6)
times_list=list(times_arr)    
ranges_list=list(ranges_arr)

plt.plot(velos,times_arr,'o', velos, f(velos), '-')
#plt.plot(3.6*x,times_arr, 3.6*x, ranges_arr)

plt.show()


return_dict={
    'times_list':times_list,
    'ranges_list':ranges_list,
    'x_list':x_list
}