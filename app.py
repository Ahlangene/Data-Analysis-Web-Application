from data_analysis import Data_analysis
from flask import Flask,request,render_template
import os
import pandas as pd
import numpy as np
from PIL import Image

# Creating a very for class object
dataObject=np.nan
filename=np.nan 
filesize=np.nan 
numColumns=np.nan
numRows=np.nan

# Flask instance
app=Flask(__name__)

# Adding uploads folder to Flask app configuration
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Creating an upload folder when upload folder does not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Web application home initial route
@app.route('/')
def index():
    return render_template('index.html') # Returning the main page for the route

# Web application upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    global dataObject #The global variable
    global filename, filesize, numColumns, numRows
    if 'csvFile' not in request.files:
        return "No file part"
    # Request 
    file =request.files['csvFile']

    # Checking if there is a selected file
    if file.filename =='':
        return "No file selected"
    
    #Creating a file path to save file
    file_path=os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
    # Uploading file to the upload folder in app config 
    file.save(file_path)
    # Checking if file is a csv file
    if (file.filename.endswith('.csv')):
        dataObject=Data_analysis(file,file_path) # Data_analysis instance created
        table=dataObject.htmlOutput() # Extracting the dataframe from object
    
    #File and data info
    filename, filesize, numColumns, numRows=dataObject.dataInfo()

    # Fetching the columns from the dataframe
    columnNames=dataObject.dropdowninput()
    # Returning a new html file for table display and column names for user input
    return render_template('table_display.html',html_table=table,rows=columnNames,
                           columns=columnNames,filename=filename,filesize=filesize,
                           columnno=numColumns,rowno=numRows)

# Route for graph visualization
@app.route('/imagerequest',methods=['POST'])
def imageupload():
    global dataObject
    global filename, filesize, numColumns, numRows
    #Getting input columns from user
    rowInput=request.form['row']
    columnInput=request.form['column']

    #Plotting the graph from object
    img=dataObject.graph_plotting(columnInput,rowInput)
    #Getting table from object
    table=dataObject.htmlOutput()
    #Getting column names from object
    columnNames=dataObject.dropdowninput()

    #Returning table display html woth plot image
    return render_template('table_display.html',html_table=table,rows=columnNames,columns=columnNames,
                           filename=filename,filesize=filesize,columnno=numColumns,rowno=numRows,image=img)

if (__name__=='__main__') :
    app.run(debug=True)