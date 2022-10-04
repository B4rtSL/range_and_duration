import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

def breguetPropeller(startmass,nompow_prop,fuelcons_prop,propnumber,altitude,aspectratio,cx0,area,vmin,vmax,efficiency):

    #Air density from SI
    air_density=1.2255*(1-(altitude/44300))**4.256

    #masses needed in calculations
    diffmass_prop=propnumber*nompow_prop*fuelcons_prop*0.75 
    fuelmass_prop=0.2*startmass-diffmass_prop                 
    endmass_prop=startmass-fuelmass_prop                            

    #array of velocities, counting step - 100
    x=np.linspace(vmin,vmax,100)

    #creating empty arrays for further calculations
    times=[]
    ranges=[]

    #loop calculations of Breguet formulas
    for i in x:
        A_factor=air_density*area*i*i*math.sqrt(cx0*3.14*aspectratio)
        time=1000*(efficiency/9.81/i/fuelcons_prop)*math.sqrt(3.14*aspectratio/cx0)*(math.atan(2*9.81*startmass/A_factor)-math.atan(2*9.81*endmass_prop/A_factor))
        range=3.6*i*time
        times.append(time)
        ranges.append(range)
    
    times_arr=100*np.array(times)    
    ranges_arr=np.array(ranges) 

    #preparing lists of needed values
    x_list=list(x*3.6)
    times_list=list(times_arr)    
    ranges_list=list(ranges_arr)
   
    #returning dictionary, as this is form needed by Plotly
    return_dict={
        'times_list':times_list,
        'ranges_list':ranges_list,
        'x_list':x_list
    }

    return return_dict
    
