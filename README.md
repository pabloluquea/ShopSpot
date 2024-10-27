# Supermarket Item Finder

A Streamlit application that helps users locate items in a supermarket and find the nearest store location.

## Features
- Find nearest supermarket location
- Search for items and get their aisle/section location
- Simple and intuitive interface

## Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/pabloluquea/ShopSpot.git
```

2. Install dependencies using Make:
```bash
make install
```

Alternatively, you can install dependencies directly using pip:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Using Make:
```bash
make run
```

2. Or directly using Streamlit:
```bash
streamlit run main.py
```

The application will start and automatically open in your default web browser. If it doesn't, you can access it at `http://localhost:8501`.

## Project Structure
- `main.py`: The main Streamlit application code.
- `requirements.txt`: List of dependencies for the project.
- `Makefile`: Convenience commands for installation and running the application.

## Development

To clean up Python cache files:
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