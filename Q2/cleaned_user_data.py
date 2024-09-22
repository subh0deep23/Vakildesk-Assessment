import pandas as pd
import re

def is_valid_email(email):
    # Simple regex for validating email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def clean_user_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Remove duplicate entries based on 'user_id'
    df = df.drop_duplicates(subset='user_id')

    # Filter out rows with invalid email formats
    df = df[df['email'].apply(is_valid_email)]

    # Write the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = 'user_data.csv'  # Input CSV file
    output_file = 'cleaned_user_data.csv'  # Output CSV file
    clean_user_data(input_file, output_file)
    