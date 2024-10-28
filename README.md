# Supermarket Item Finder

A Streamlit application that helps users locate items in a supermarket and find the nearest store location.

## Features
- Find nearest supermarket location
- Search for items and get their aisle/section location
- Simple and intuitive interface

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation (only do this once)

1. Clone this repository:
```bash
git clone https://github.com/pabloluquea/ShopSpot.git
cd ShopSpot
```

2. Install dependencies:

For Windows:
```powershell
.\venv\Scripts\activate
pip install -r requirements.txt
```

For Unix/MacOS:
```bash
# Using Make
source venv/bin/activate
make install

# Or using pip directly
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application

For Windows:
```powershell
streamlit run main.py
```

For Unix/MacOS:
```bash
# Using Make
make run

# Or using Streamlit directly
streamlit run main.py
```

The application will start and automatically open in your default web browser. If it doesn't, you can access it at `http://localhost:8501`.

## Project Structure
```
ShopSpot/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── Makefile             # Make commands for Unix/MacOS
└── README.md            # Project documentation
```

## Development

For Windows:
```powershell
# Clean Python cache files
Get-ChildItem -Path . -Include "__pycache__" -Recurse -Directory | Remove-Item -Recurse -Force
Get-ChildItem -Path . -Include "*.pyc" -Recurse -File | Remove-Item -Force
```

For Unix/MacOS:
```bash
make clean
```

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
* Thanks to all contributors who have helped with this project
* Streamlit for making it easy to create data apps
