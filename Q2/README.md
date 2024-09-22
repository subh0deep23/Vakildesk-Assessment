# CSV User Data Cleaner

This project reads a CSV file containing user data, removes duplicate entries based on `user_id`, filters out rows with invalid email formats, and writes the cleaned data to a new CSV file.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Input CSV Format](#input-csv-format)
5. [Migrations](#migrations)
6. [Requirements](#requirements)
7. [Notes](#notes)

## Project Overview

This script helps clean user data by:
- Removing duplicate entries based on `user_id`.
- Validating email formats using a simple regex.
- Outputting the cleaned data into a new CSV file.

## Installation

To set up this project, follow the steps below:

1. **Clone the repository or download the files**:
    ```bash
    git clone <repo_url>
    ```

2. **Install Python dependencies**:
    Install required packages listed in `requirements.txt` using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place the input CSV file (`user_data.csv`) in the same directory as the script.
   
2. **Run the script**:
    Execute the script with the following command:
    ```bash
    python clean_user_data.py
    ```

3. **Output**:
    The cleaned data will be written to `cleaned_user_data.csv` in the same directory.

### Input CSV Format

The input CSV file (`user_data.csv`) should contain at least the following columns:
- `user_id`: Unique identifier for the user
- `email`: User email address

Example of the CSV format:

```csv
user_id,email
1,john.doe@example.com
2,jane.doe@example
3,bob.smith@example.com
4,jane.doe@example.com
Notes

    The script uses a simple regex to validate email formats, but more complex validation rules can be added.
    Be sure to modify the file paths (input_file and output_file) if needed.

yaml


---

### Key Steps to Include:

- **Installation**: Document the installation of dependencies via `requirements.txt`.
- **Usage**: Describe how to place the input CSV file and run the script.
- **CSV Format**: Clarify the expected structure of the input CSV file.
- **Output**: Specify what the output file will look like and where it will be saved.

