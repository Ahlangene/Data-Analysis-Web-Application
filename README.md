# Data-Analysis-Web-Application
Web application designed to allow user to upload any CSV files and to visualize the data using a graph

**Features**
- Upload CSV files and automatically extract metadata (filename, size, columns, rows)
- Display uploaded data in a styled HTML table
- Perform basic data analysis and present insights (e.g., column count, row count)
- View file details in a user-friendly format
- Lightweight, responsive front-end using HTML and CSS

**Technologies Used**
- Python (Flask)
- Pandas for data processing
- HTML/CSS for frontend display
- Heroku

**Project structure**
├── app.py                 # Main Flask application
├── data_analysis.py       # Data analysis class
├── templates/
│   └── index.html         # Main HTML template
│   └── table_display.html # Second display template
├── static/
│   └── styles.css         # CSS styling
├── requirements.txt       # Python dependencies
├── Procfile               # For Heroku deployment
├── runtime.txt            # Python version for Heroku
└── README.md              # This file

**Setup instructions**
1. Clone the Repository
2. Create a virtual environment
3. Install Dependencies
4. Run app loacally
