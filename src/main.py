from ReadFiles import ReadFiles
from Setup import Setup
from AnalysisToolBox import AnalysisToolBox
from plot import plot
from LoadData import LoadData
from FileConverter import FileConverter

import time

start = time.time()


PathData = '/home/oline/Documents/CERN/CHub/AEgIS/OnlineTools/LivePlotting/'
PathSettings_csv = 'settings/settings.csv'
PathSettings_txt = 'settings/settings.txt'
folder   = 'Data/'

FC = FileConverter(PathSettings_csv, PathSettings_txt)
FC.Txt2CSV()

param = LoadData(PathSettings_csv)
param.Initiate() 

RF = ReadFiles(PathData, folder)
data = RF.GetCSV()

build = Setup(data, param)
data, ActivationMatrix= build.Initiate() 

#ATB = AnalysisToolBox(data, param, ActivationMatrix, CoordinateMatrix)
#ATB.Initiate_Standard_Analysis()

#P = plot(data, param, ActivationMatrix, param.CoordinateMatrix)
#P.plot_FACT_live()

end = time.time()
print('Full Run: %.5f' % (end - start), 's')

