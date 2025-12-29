# Process Ranker

This is a simple python project that collects memory usage data by commands and then display it on chart.

It uses linux command "ps" to get data from system, then stores it as a csv and read it using pandas then it will put it into an
numpy array and then diplay it on matplotlib bar.


## Tree Structure

.
├── garbage\n
├── LICENSE\n
├── ProcRank.py\n
├── scripts\n
│   ├── chart.py\n
│   ├── convert.py\n
│   ├── extract.py\n
│   └── save.py\n
└── utils\n
    └── clear.sh\n


## Installation

Python Libraries used:

Default Libraries:
- os
- shutil
- platform
- subprocess
- datetime

Third Party Libraries:
- numpy
- pandas 
- matplotlib

After checking if all of the libraries installed then look for if python is installed, i used version 3.13.5 on linux.

```bash
pip install numpy pandas matplotlib
```

## Usage

Clone the repository and run the main script:

```bash
git clone https://github.com/mapllr/ProcRank.git
cd ProcRank.git
py ProckRank.py
```

## Goal 

The goal of this project was to get to libraries like matplotlib, pandas and numpy and overall get more comfortable with python.
