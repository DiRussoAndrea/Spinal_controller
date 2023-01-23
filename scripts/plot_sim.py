# Brief Visualize kinematics and muscle activity of a SCONE simulation.
#
# authors: Andrea Di Russo <andrea.dirusso@epfl.ch> and Dimitar Stanev <dimitar.stanev@epfl.ch>
# %%
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import read_from_storage
from utils import get_color_gradient
from utils import plot_gait
from utils import plot_muscle


model_file = os.path.abspath('models/gait9dof18musc_Thelen_20170320.osim')
gait_files = [os.path.abspath('spinal_modulation/full_control/speed117_sl157_sd134.sto')]
            # os.path.abspath('spinal_modulation/full_control/speed065_sl109_sd168.sto'),
            # os.path.abspath('spinal_modulation/full_control/speed124_sl155_sd125.sto')
            # os.path.abspath('spinal_modulation/full_control/speed157_sl168_sd107.sto')] # to compare multiple simulations

side = 'r'

muscles = ['iliopsoas', 'glut_max', 'hamstrings', 'bifemsh', 'vasti',
           'rect_fem', 'tib_ant', 'gastroc', 'soleus']

muscles_title = ['ILPSO', 'GMAX', 'HAMS', 'BFSH', 'VAS', 'RF', 'TA', 'GAS', 'SOL']

# plot one simulation:
gait = read_from_storage(gait_files[0])
fig, ax = plt.subplots(1, 5, figsize=(16, 3))
plot_gait(gait, side, 'b', ax)
fig, ax = plt.subplots(3, 3, figsize=(16, 3))
plot_muscle(gait, side, muscles, muscles_title, 'b', ax)

'''
# Compares multiple simulations:
n = len(gait_files)
cb_1 = '#0134FF'
cb_2 = '#001567'
cmap = get_color_gradient(cb_1, cb_2, n)
i = 0
for gait_file in gait_files:
    gait = read_from_storage(gait_file)

    plot_gait(gait, side, cmap[i], ax)
    i += 1

fig, ax = plt.subplots(3, 3, figsize=(16, 3))
j = 0
for gait_file in gait_files:
    gait = read_from_storage(gait_file)

    plot_muscle(gait, side, muscles, muscles_title, cmap[i], ax)
    j += 1
'''

plt.show()
