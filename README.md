# Sales Data Pipeline

A beginner-friendly data pipeline built with Python and Pandas to process, validate, clean, and analyze sales data from a CSV file.

## Project Overview

This project implements a simple ETL (Extract, Transform, Load) workflow. It reads raw sales data, validates data quality, removes records with missing or empty product names, detects potential duplicate sales, calculates sales totals, and generates revenue reports.

## Features

- Load sales data from a CSV file
- Validate required columns and data types
- Validate dates, quantities, and unit prices
- Remove records with missing or empty product names
- Detect and log potential duplicate sales
- Calculate the total price of each sale
- Calculate total revenue
- Generate revenue summaries by product
- Export processed data to a CSV file
- Log pipeline execution and errors
- Run automated tests with pytest

## Technologies

- Python
- Pandas
- pytest
- Git and GitHub

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

4. Activate the virtual environment.

   On Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   On Linux or macOS:

   ```bash
   source .venv/bin/activate
   ```

5. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Usage

Run the pipeline from the project root directory:

```bash
python main.py
```

The pipeline processes the raw sales data and saves the output to:

```text
data/processed_sales.csv
```

Execution details and errors are recorded in the pipeline log.

## Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

The tests cover data validation, cleaning, sales calculations, reporting, and duplicate detection.

## Learning Goals

This project is part of my learning journey in Python, data processing, data quality, automated testing, and data engineering fundamentals.

## Future Improvements

- Generate reports in additional formats
- Integrate a relational database
- Automate pipeline execution
- Improve duplicate detection using a unique sale identifier