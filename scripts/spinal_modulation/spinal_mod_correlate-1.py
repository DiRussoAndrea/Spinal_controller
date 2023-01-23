"Correlation Analysis"
"Performed under Internship at BioRobotics lab"
"Student - Anushree Sabnis"
"Mentor - Andrea di Russo"
import os
import numpy as np
import pandas as pd

# Run after spinal_modulation_split.params.py

class Energy_Study :
    def __init__(self):
        # Experiment subfolders - Seperate analyses to be performed on each subfolder
        self.folder = ['fixed_cpgs', 'fixed_balance', 'fixed_frequency', 'fixed_reflexes', 'full_control']
        self.folders = ['']
        self.root_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
        self.current_path = None
        self.expcount = 0
        self.speed = []
        self.studydata = pd.DataFrame()

    def read_data(self, speed_flag):
        self.current_path = self.root_path + '\\spinal-modulation\\' +  self.folder[speed_flag]
        self.studydata = pd.read_csv(self.current_path + "\\par.csv")
        speed_corr = self.correlate('speed')
        step_duration_corr = self.correlate('step_duration')
        step_length_corr = self.correlate('step_length')
        corr_dict = {k:v for k,v in zip(self.studydata.columns, zip(speed_corr, step_duration_corr, step_length_corr))}
        corr_final_df = pd.DataFrame.from_dict(corr_dict)
        corr_final_df.to_csv(self.current_path + "\\corr.csv")

    def correlate(self, flag):
        parameters = self.studydata.columns
        c_effort = []
        for col in parameters :
            M_c = np.corrcoef(list(np.float_(self.studydata[col].values)), self.studydata[flag])
            c = round(M_c[0,1], 2)
            c_effort.append(c)
        return c_effort

if __name__ == '__main__' :
    en = Energy_Study()
    # To set experiment subfolder
    en.read_data(0)
    # en.append_data()
