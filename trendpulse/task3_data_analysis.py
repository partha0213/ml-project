"""
Task 3: Analyze the Data with NumPy
TrendPulse: Statistical Analysis and Feature Engineering
"""

import pandas as pd
import numpy as np
import os

# ============================================================================
# TASK 1: Load and Explore the Data (4 marks)
# ============================================================================

# Load the cleaned CSV from Task 2
csv_file = 'data/trends_clean.csv'

if not os.path.exists(csv_file):
    print(f"Error: {csv_file} not found. Please run Task 2 first.")
    exit(1)

# Load the data into a DataFrame
df = pd.read_csv(csv_file)

print("=== DATA LOADING AND EXPLORATION ===\n")
print(f"Loaded {len(df)} stories from {csv_file}")
print(f"\nDataFrame shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"\nFirst 5 rows:")
print(df.head())

# ============================================================================
# TASK 2: NumPy Statistics (8 marks)
# ============================================================================

print("\n" + "=" * 50)
print("NumPy STATISTICAL ANALYSIS")
print("=" * 50 + "\n")

# Extract the score column as a NumPy array for statistical analysis
scores = np.array(df['score'])

# Calculate key statistics using NumPy functions
mean_score = np.mean(scores)
median_score = np.median(scores)
std_score = np.std(scores)
max_score = np.max(scores)
min_score = np.min(scores)

# Display statistics with formatted output
print("--- Score Statistics ---")
print(f"Mean score   : {mean_score:,.0f}")
print(f"Median score : {median_score:,.0f}")
print(f"Std deviation: {std_score:,.0f}")
print(f"Max score    : {max_score:,.0f}")
print(f"Min score    : {min_score:,.0f}")

# Additional statistical insights
print(f"\n--- Additional Insights ---")
print(f"25th Percentile: {np.percentile(scores, 25):,.0f}")
print(f"75th Percentile: {np.percentile(scores, 75):,.0f}")
print(f"Quartile Range (IQR): {np.percentile(scores, 75) - np.percentile(scores, 25):,.0f}")

# ============================================================================
# TASK 3: Add New Columns (5 marks)
# ============================================================================

print("\n" + "=" * 50)
print("FEATURE ENGINEERING")
print("=" * 50 + "\n")

# Create 'engagement' column: sum of score and num_comments
# This represents total community interaction with the story
df['engagement'] = df['score'] + df['num_comments']

# Create 'is_popular' column: True if engagement > median engagement
# Stories above median engagement are considered "popular"
median_engagement = np.median(df['engagement'])
df['is_popular'] = df['engagement'] > median_engagement

print(f"Created 'engagement' column: score + num_comments")
print(f"Created 'is_popular' column: engagement > median (threshold: {median_engagement:,.0f})")

# Display sample of new features
print(f"\nSample of new columns:")
print(df[['title', 'score', 'num_comments', 'engagement', 'is_popular']].head(10))

# ============================================================================
# CATEGORY AND ENGAGEMENT ANALYSIS
# ============================================================================

print("\n" + "=" * 50)
print("CATEGORY AND ENGAGEMENT ANALYSIS")
print("=" * 50 + "\n")

# Find the category with most stories
category_counts = df['category'].value_counts()
most_stories_category = category_counts.index[0]
most_stories_count = category_counts.values[0]

print(f"Most stories in: {most_stories_category} ({most_stories_count} stories)")

# Find the most commented story
most_commented_idx = df['num_comments'].idxmax()
most_commented_story = df.loc[most_commented_idx]

print(f"\nMost commented story: \"{most_commented_story['title']}\"")
print(f"  Comments: {most_commented_story['num_comments']:,}")
print(f"  Score: {most_commented_story['score']:,}")
print(f"  Engagement: {most_commented_story['engagement']:,}")

# Category breakdown
print(f"\n--- Story Count by Category ---")
print(category_counts.to_string())

# Engagement statistics by category
print(f"\n--- Average Engagement by Category ---")
category_engagement = df.groupby('category')['engagement'].mean().sort_values(ascending=False)
for category, avg_engagement in category_engagement.items():
    print(f"  {category:20s} {avg_engagement:8,.0f}")

# Popular stories count
popular_count = df['is_popular'].sum()
non_popular_count = (~df['is_popular']).sum()

print(f"\n--- Popular vs Non-Popular Stories ---")
print(f"Popular stories (engagement > median):     {popular_count}")
print(f"Non-popular stories (engagement <= median): {non_popular_count}")

# ============================================================================
# TASK 4: Save to CSV (3 marks)
# ============================================================================

print("\n" + "=" * 50)
print("SAVING RESULTS")
print("=" * 50 + "\n")

# Save the analysed dataframe to CSV
output_file = 'data/trends_analysed.csv'
df.to_csv(output_file, index=False)

print(f"Saved {len(df)} rows to {output_file}")
print(f"\nColumns saved: {list(df.columns)}")

# Final summary
print("\n" + "=" * 50)
print("ANALYSIS COMPLETE")
print("=" * 50)
print(f"✓ Loaded and explored {len(df)} stories")
print(f"✓ Computed NumPy statistics (mean, median, std, max, min)")
print(f"✓ Added 'engagement' and 'is_popular' features")
print(f"✓ Saved to {output_file}")
print("\nReady for Task 4: Data Visualization")
