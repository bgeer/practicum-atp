This repository contains the workbooks for the course 'Advanced Technical Programming' (TCTI-VKATP-17) of the University of Applied Sciences Utrecht.


# Notebook instructions

To use and run this notebook, do the following:
* Install Python-jupyter:
  * run `pip3 install jupyter` (run as administrator if you have installed Python3 into your Program Files directory!)
  * OR install the Anaconda Python platform, which includes jupyter notebook; please consult [the Jupyter documentation](http://jupyter.readthedocs.io/en/latest/install.html) for instructions
* Clone this repository to a folder on your computer
* Open a console and change directory to your local copy of the repository
* Run `jupyter notebook` to start the notebook (a browser will open to show the notebook; if not, open a browser yourself and go to `localhost:8888`).
* Select the workbook of your choice.

# ATP Aquarium Project

## Setup

To setup the project:

1. Clone the repository: `git clone https://github.com/bgeer/practicum-atp.git`
2. Navigate to the project directory: `cd practicum-atp`
3. Create a virtual environment for python version 3.6: `python3.6 -m venv ".venv"`
4. Install dependencies: `pip3 install -r`
5. Install g++ compiler: `https://code.visualstudio.com/docs/cpp/config-mingw`

## Testing

To test certain functionalitys of the code:

1. Navigate to the test directory: `cd simulator-Bas\tests`
2. To run the unit tests: `python unit_tests.py`
3. To run the integration tests: `python integration_tests.py`
4. To run the system tests: `python system_test.py`

## Run

To run the simulato:

1. Navigate to the simulator directory: `cd simulator-Bas\`
2. Compile the c++ binded files: `python setup.py build_ext --inplace`
2. To start the simulator: `python main.py`