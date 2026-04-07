"""
Task 2: Clean the Data & Save as CSV
TrendPulse: Data Processing and Cleaning
"""

import pandas as pd
import json
import os
from datetime import datetime

# ============================================================================
# TASK 1: Load the JSON File (4 marks)
# ============================================================================

# Find the JSON file in the data folder
data_dir = 'data'
json_files = [f for f in os.listdir(data_dir) if f.startswith('trends_') and f.endswith('.json')]

if not json_files:
    print("Error: No trends JSON file found in data/ folder")
    exit(1)

# Load the most recent JSON file
json_file = os.path.join(data_dir, json_files[0])
print(f"Loading data from: {json_file}")

# Read JSON file and convert to DataFrame
with open(json_file, 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

df = pd.DataFrame(raw_data)

# Print initial row count
initial_rows = len(df)
print(f"Loaded {initial_rows} stories from {json_file}\n")

# ============================================================================
# TASK 2: Clean the Data (10 marks)
# ============================================================================

print("Data Cleaning Process:")
print("-" * 50)

# Step 1: Remove duplicates based on post_id
df_no_duplicates = df.drop_duplicates(subset=['post_id'], keep='first')
duplicates_removed = initial_rows - len(df_no_duplicates)
print(f"After removing duplicates: {len(df_no_duplicates)} (removed {duplicates_removed})")

# Step 2: Remove rows with missing values in critical columns
# Drop rows where post_id, title, or score is missing
df_no_nulls = df_no_duplicates.dropna(subset=['post_id', 'title', 'score'])
nulls_removed = len(df_no_duplicates) - len(df_no_nulls)
print(f"After removing nulls in critical columns: {len(df_no_nulls)} (removed {nulls_removed})")

# Step 3: Ensure data types are correct
# Convert score and num_comments to integers
# Handle any non-integer values by converting to int (will truncate decimals if any)
df_no_nulls['score'] = pd.to_numeric(df_no_nulls['score'], errors='coerce').astype('int64')
df_no_nulls['num_comments'] = pd.to_numeric(df_no_nulls['num_comments'], errors='coerce').fillna(0).astype('int64')

# Step 4: Remove low-quality stories (score < 5)
df_high_quality = df_no_nulls[df_no_nulls['score'] >= 5]
low_quality_removed = len(df_no_nulls) - len(df_high_quality)
print(f"After removing low scores (< 5): {len(df_high_quality)} (removed {low_quality_removed})")

# Step 5: Clean whitespace from title column
# Strip leading and trailing whitespace from titles
df_high_quality['title'] = df_high_quality['title'].str.strip()

# Assign the cleaned dataframe back to df for consistency
df = df_high_quality.reset_index(drop=True)

print()

# ============================================================================
# TASK 3: Save as CSV (6 marks)
# ============================================================================

# Define output file path
output_file = os.path.join(data_dir, 'trends_clean.csv')

# Save the cleaned DataFrame to CSV
df.to_csv(output_file, index=False)
final_rows = len(df)

print(f"Saved {final_rows} rows to {output_file}")
print()

# Print summary: stories per category
print("Stories per category:")
category_counts = df['category'].value_counts().sort_values(ascending=False)
for category, count in category_counts.items():
    print(f"  {category:20s} {count:3d}")

print()
print("=" * 50)
print("Data cleaning complete!")
print(f"Total rows cleaned: {initial_rows} -> {final_rows}")
print(f"Rows removed: {initial_rows - final_rows}")
print(f"Data saved to: {output_file}")
