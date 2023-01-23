import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils import read_from_storage
from utils import cpgs_reflexes_MN
from utils import plot_input
from utils import get_color_gradient


model_file = os.path.abspath('models/gait9dof18musc_Thelen_20170320.osim')

gait_files = [os.path.abspath('spinal_modulation/full_control/speed065_sl109_sd168.sto'),
              os.path.abspath('spinal_modulation/full_control/speed124_sl155_sd125.sto'),
              os.path.abspath('spinal_modulation/full_control/speed157_sl168_sd107.sto')]

side = 'r'

muscles = ['iliopsoas', 'glut_max', 'hamstrings', 'bifemsh', 'vasti',
           'rect_fem', 'tib_ant', 'gastroc', 'soleus']

hip_muscles = ['iliopsoas', 'glut_max', 'hamstrings']

n = len(gait_files)
cb_1 = '#0134FF'
cb_2 = '#001567'
c_map = get_color_gradient(cb_1, cb_2, n)
fig, ax = plt.subplots(5, 9, figsize=(16, 3))
muscles_title = ['ILPSO', 'GMAX', 'HAMS', 'BFSH', 'VAS', 'RF', 'TA', 'GAS', 'SOL']
i = 0
for gait_file in gait_files:
    gait = read_from_storage(gait_file)
    [activation, input, output, cpgs, balance, reflexes] = cpgs_reflexes_MN(muscles, side, gait)

    count = 0
    for muscle in muscles:
        plot_input(input, output, cpgs, balance, reflexes, muscle, hip_muscles, muscles_title[count], ax, c_map[i], count)

        count += 1
    i += 1
ax[4, 8].legend(['0.6 m/s', '1.2 m/s', '1.6 m/s'])


plt.show()
