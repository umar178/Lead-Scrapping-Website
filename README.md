# How to Use
## Prerequisites
To get started, you’ll need the following tools installed on your system:

- Python
- GoLang
- PyCharm
- Flask (Python library)

## Setup Instructions
Clone or download this repository to your local machine.

### Prepare the Python Environment:

Open the main.py file in PyCharm.
Create a virtual environment (venv) for the project:
In PyCharm, go to File > Settings > Project: <YourProject> > Python Interpreter.
Add a new interpreter and select "New Virtual Environment."
Install Flask in the virtual environment:
bash
Copy code
pip install flask

### Prepare the Google Maps Scraper:

Navigate to the google-maps-scraper folder in your terminal or Command Prompt.
Run the following commands:
bash
Copy code
go mod download
go build
Run the Application:

Go back to PyCharm and run the main.py file.
Once the server starts, you will see a terminal output similar to:
csharp
Copy code
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Open the provided link (http://127.0.0.1:5000/) in your browser.
Features
User-friendly interface for querying and scraping Google Maps data.
Dynamically generated and formatted CSV output.
Local hosting through Flask for easy accessibility.
