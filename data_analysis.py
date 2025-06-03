import os
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

class Data_analysis:
    # Constructor
    def __init__(self,file,filepath):
        global data
        self.filepath=filepath
        self.file=file
        self.data=pd.read_csv(filepath)
    
    #Function to create a html table
    def htmlOutput(self):
        table=self.data.to_html(classes='data',header='true',index=False)
        return table
 
    #Function to get column names
    def dropdowninput(self):
        columns=list(self.data.columns)
        return columns

    #Function to get file infomation
    def dataInfo(self):
        filename=self.file.filename
        self.file.seek(0,os.SEEK_END)
        filesize=self.file.tell()
        columnno=self.data.shape[1]
        rowno=self.data.shape[0]

        pfilesize=f'{filesize}KB'
        return filename, pfilesize, columnno, rowno
  
    #Function for plotting and image saving
    def graph_plotting(self,column_name,row_name):
        # Setting figure size
        plt.figure(figsize=(10,6))

        # Setting graph theme
        sns.set_theme(style="whitegrid")
        sns.scatterplot(x=self.data[row_name],y=self.data[column_name])

        # Rotating x-axis labels for readability
        plt.xticks(rotation=45,ha="right")
        
        # Graph labels
        stitle=row_name+' vs '+column_name
        plt.title(stitle)
        plt.xlabel(row_name)
        plt.ylabel(column_name)

        # Saving image in web app location
        image_url='static/plot.jpg'
        plt.savefig(image_url,dpi=600)
        plt.close()
        return 'plot.jpg'