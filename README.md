# Sales Data Pipeline

A beginner-friendly data pipeline built with Python and Pandas to process sales data from a CSV file.

## Project Overview

This project reads raw sales data, validates and cleans the records, calculates sales totals, and generates summary reports.

## Features

* Read sales data from a CSV file
* Detect missing values
* Remove records with missing product names
* Validate quantities and unit prices
* Calculate the total price of each sale
* Calculate total revenue
* Generate revenue summaries by product
* Export processed data to a CSV file
* Run automated tests with pytest

## Technologies

* Python
* Pandas
* pytest
* Git and GitHub

## Project Structure

```text
sales-data-pipeline/
├── data/
│   ├── raw_sales.csv
│   └── processed_sales.csv
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_validator.py
│   ├── data_cleaner.py
│   └── sales_report.py
├── tests/
│   └── test_main.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dev-MarcoAntonio/sales-data-pipeline.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sales-data-pipeline
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment on Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the pipeline:

```bash
python main.py
```

The processed sales data will be saved to `data/processed_sales.csv`.

## Running Tests

Run the automated tests with:

```bash
python -m pytest
```

## Learning Goals

This project is part of my learning journey in Python, data processing, data quality, and data engineering fundamentals.

## Future Improvements

* Expand automated test coverage
* Improve data validation
* Generate reports in additional formats
* Integrate a relational database
* Automate pipeline execution