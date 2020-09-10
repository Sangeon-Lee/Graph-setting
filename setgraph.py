# -*- coding: utf-8 -*-

import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MaxNLocator)
import matplotlib.text as text
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker


def set_fig(fig, **kwargs):
    
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Arial'
    
    params = kwargs
    
    for o in fig.findobj(lambda x:hasattr(x, 'set_major_locater') or hasattr(x,'set_minor_locater') or hasattr(x, 'tick_params')):
        
        o.tick_params(which = 'both', direction = 'in', bottom =1, top =1, left = 1, right =1 )
        if 'xinv' in params:
            xloc = plticker.MultipleLocator(base = params.get('xinv'))
            o.xaxis.set_major_locator(xloc)
        if 'yinv' in params:
            yloc = plticker.MultipleLocator(base = params.get('yinv'))
            o.yaxis.set_major_locator(yloc)
        if 'xpad' in params:
            o.tick_params(axis = 'x', pad = params.get('xpad'))
        if 'ypad' in params:
            o.tick_params(axis = 'y', pad = params.get('ypad'))
            
        o.xaxis.set_minor_locator(AutoMinorLocator(2))
        o.yaxis.set_minor_locator(AutoMinorLocator(2))
   
    for o in fig.findobj(text.Text):
        if 'fontsize' in params:
            plt.setp(o, 'fontsize', params.get('fontsize'))
        else: break

def ycommon_label(fig, labelname, **kwargs):
    
    params = kwargs
    ax = fig.add_subplot(111, frameon= False)   
    ax.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False, color = 'none')
    if 'pad' and 'fontsize' in params:
        ax.set_ylabel(labelname, labelpad = params.get('pad'), fontsize = params.get('fontsize'))
    elif 'fontsize' in params:
        ax.set_ylabel(labelname,  fontsize = params.get('fontsize'))
    elif 'pad' in params:
        ax.set_ylabel(labelname,  labelpad = params.get('pad'))
    else:
        ax.set_ylabel(labelname)
        
        

