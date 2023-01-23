"Data Cleaning"
"Performed under Internship at BioRobotics lab"
"Student - Anushree Sabnis"
"Mentor - Andrea di Russo"
import os
import pandas as pd



class Energy_Study :
    def __init__(self):
        self.state = None
        # Experiment subfolders - Seperate analyses to be performed on each subfolder
        self.folder = ['fixed_cpgs', 'fixed_balance', 'fixed_frequency', 'fixed_reflexes', 'full_control']
        self.root_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
        self.current_path = None
        self.parindices = []
        self.partbl = pd.DataFrame()
        self.setindex = False
        self.aspeedarray = []
        self.asteplengtharray = []
        self.astepdurationarray = []


    def read_data(self, speed_flag):
        self.current_path = self.root_path + '//spinal-modulation'
        for path in os.listdir(self.current_path) :
            if (path.endswith(self.folder[speed_flag])):
                for file in os.listdir(self.current_path + '//' + path):
                    if file.endswith('.par'):
                        filename = file[:-4]
                        speed = float(filename.split("_")[0][-3:])/100
                        step_length = float(filename.split("_")[1][-3:])/100
                        step_duration = float(filename.split("_")[2][-3:])/100
                        print(filename)
                        self.aspeedarray.append(speed)
                        self.asteplengtharray.append(step_length)
                        self.astepdurationarray.append(step_duration)
                        file_path = self.current_path + '//' + path + '//' + file
                        par = pd.read_csv(file_path, delim_whitespace=True, header=None)
                        par.pop(2)
                        par.pop(3)
                        self.parindices = par.T.iloc[0].values
                        parvalues = par.T.iloc[1].values
                        if self.setindex == False:
                            self.partbl = self.partbl.append(pd.Series(self.parindices), ignore_index = True)
                            self.setindex = True
                        print(self.partbl)
                        self.partbl = self.partbl.append(pd.Series(parvalues), ignore_index = True)
            
        print('speed', self.aspeedarray)
        print('sd', self.astepdurationarray)
        print('sl', self.asteplengtharray)
        df = {'speed' : self.aspeedarray, 'step_duration' : self.astepdurationarray, 'step_length' : self.asteplengtharray}
        df = pd.DataFrame.from_dict(df)
        self.partbl.set_index = self.partbl.iloc[1]
        print(self.partbl)
        df3 = pd.concat([self.partbl, df], axis=1)
        df3.to_csv(self.current_path + "//fixed_balance//par.csv", header=None)


if __name__ == '__main__' :
    en = Energy_Study()
    # To set experiment subfolder
    en.read_data(1)
