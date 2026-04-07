"""
Task 4: Visualizations
TrendPulse: Data Visualization and Dashboard Creation
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================================================
# TASK 1: Setup (2 marks)
# ============================================================================

# Load the analyzed data from Task 3
csv_file = 'data/trends_analysed.csv'

if not os.path.exists(csv_file):
    print(f"Error: {csv_file} not found. Please run Task 3 first.")
    exit(1)

# Read the CSV into a DataFrame
df = pd.read_csv(csv_file)

print("=== DATA LOADING AND SETUP ===\n")
print(f"Loaded {len(df)} stories from {csv_file}")
print(f"Columns: {list(df.columns)}\n")

# Create outputs folder if it doesn't exist
output_dir = 'outputs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Created folder: {output_dir}")
else:
    print(f"Folder already exists: {output_dir}")

# ============================================================================
# TASK 2: Chart 1 - Top 10 Stories by Score (6 marks)
# ============================================================================

print("\n" + "=" * 50)
print("CREATING CHART 1: TOP 10 STORIES BY SCORE")
print("=" * 50 + "\n")

# Sort stories by score and get top 10
top_10_stories = df.nlargest(10, 'score')

# Shorten titles longer than 50 characters for better readability
top_10_stories = top_10_stories.copy()
top_10_stories['title_short'] = top_10_stories['title'].apply(
    lambda x: x[:47] + '...' if len(x) > 50 else x
)

# Create figure for Chart 1
fig1, ax1 = plt.subplots(figsize=(12, 8))

# Create horizontal bar chart
bars = ax1.barh(range(len(top_10_stories)), top_10_stories['score'], color='steelblue')

# Set y-axis labels to shortened titles
ax1.set_yticks(range(len(top_10_stories)))
ax1.set_yticklabels(top_10_stories['title_short'])

# Add title and axis labels
ax1.set_xlabel('Score', fontsize=12, fontweight='bold')
ax1.set_ylabel('Story Title', fontsize=12, fontweight='bold')
ax1.set_title('Top 10 Stories by Score', fontsize=14, fontweight='bold', pad=20)

# Add value labels on the bars for clarity
for i, (idx, row) in enumerate(top_10_stories.iterrows()):
    ax1.text(row['score'] + 10, i, str(int(row['score'])), 
             va='center', fontsize=10)

# Invert y-axis so highest score is at top
ax1.invert_yaxis()

# Add grid for better readability
ax1.grid(axis='x', alpha=0.3, linestyle='--')

plt.tight_layout()

# Save Chart 1
chart1_path = os.path.join(output_dir, 'chart1_top_stories.png')
plt.savefig(chart1_path, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {chart1_path}")
plt.close()

# ============================================================================
# TASK 3: Chart 2 - Stories per Category (6 marks)
# ============================================================================

print("\n" + "=" * 50)
print("CREATING CHART 2: STORIES PER CATEGORY")
print("=" * 50 + "\n")

# Count stories per category
category_counts = df['category'].value_counts().sort_values(ascending=False)

# Create figure for Chart 2
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Create bar chart with different colours for each category
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
bars = ax2.bar(category_counts.index, category_counts.values, color=colors[:len(category_counts)])

# Add title and axis labels
ax2.set_xlabel('Category', fontsize=12, fontweight='bold')
ax2.set_ylabel('Number of Stories', fontsize=12, fontweight='bold')
ax2.set_title('Stories per Category', fontsize=14, fontweight='bold', pad=20)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Add grid for better readability
ax2.grid(axis='y', alpha=0.3, linestyle='--')

plt.tight_layout()

# Save Chart 2
chart2_path = os.path.join(output_dir, 'chart2_categories.png')
plt.savefig(chart2_path, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {chart2_path}")
plt.close()

# ============================================================================
# TASK 4: Chart 3 - Score vs Comments (Scatter Plot) (6 marks)
# ============================================================================

print("\n" + "=" * 50)
print("CREATING CHART 3: SCORE VS COMMENTS SCATTER PLOT")
print("=" * 50 + "\n")

# Create figure for Chart 3
fig3, ax3 = plt.subplots(figsize=(10, 7))

# Separate data by popularity
popular_stories = df[df['is_popular'] == True]
non_popular_stories = df[df['is_popular'] == False]

# Create scatter plot with different colours for popular vs non-popular
ax3.scatter(non_popular_stories['score'], non_popular_stories['num_comments'],
            c='lightcoral', label='Non-Popular', s=100, alpha=0.6, edgecolors='darkred')
ax3.scatter(popular_stories['score'], popular_stories['num_comments'],
            c='limegreen', label='Popular', s=100, alpha=0.6, edgecolors='darkgreen')

# Add title and axis labels
ax3.set_xlabel('Score', fontsize=12, fontweight='bold')
ax3.set_ylabel('Number of Comments', fontsize=12, fontweight='bold')
ax3.set_title('Score vs Comments (Popular vs Non-Popular Stories)', 
              fontsize=14, fontweight='bold', pad=20)

# Add legend
ax3.legend(loc='upper left', fontsize=11, framealpha=0.9)

# Add grid for better readability
ax3.grid(True, alpha=0.3, linestyle='--')

plt.tight_layout()

# Save Chart 3
chart3_path = os.path.join(output_dir, 'chart3_scatter.png')
plt.savefig(chart3_path, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {chart3_path}")
plt.close()

# ============================================================================
# BONUS: Dashboard - Combined Figure (3 marks)
# ============================================================================

print("\n" + "=" * 50)
print("CREATING BONUS: TRENDPULSE DASHBOARD")
print("=" * 50 + "\n")

# Create a figure with 2x2 subplots layout
fig_dashboard = plt.figure(figsize=(16, 12))
fig_dashboard.suptitle('TrendPulse Dashboard', fontsize=18, fontweight='bold', y=0.995)

# ---- Subplot 1: Top 10 Stories (horizontal bar) ----
ax_dash1 = plt.subplot(2, 2, 1)
top_10_stories_reset = top_10_stories.reset_index()
ax_dash1.barh(range(len(top_10_stories_reset)), top_10_stories_reset['score'], color='steelblue')
ax_dash1.set_yticks(range(len(top_10_stories_reset)))
ax_dash1.set_yticklabels(top_10_stories_reset['title_short'], fontsize=9)
ax_dash1.set_xlabel('Score', fontsize=10, fontweight='bold')
ax_dash1.set_title('Top 10 Stories by Score', fontsize=12, fontweight='bold')
ax_dash1.invert_yaxis()
ax_dash1.grid(axis='x', alpha=0.3, linestyle='--')

# ---- Subplot 2: Stories per Category (bar) ----
ax_dash2 = plt.subplot(2, 2, 2)
ax_dash2.bar(category_counts.index, category_counts.values, 
             color=colors[:len(category_counts)])
ax_dash2.set_xlabel('Category', fontsize=10, fontweight='bold')
ax_dash2.set_ylabel('Number of Stories', fontsize=10, fontweight='bold')
ax_dash2.set_title('Stories per Category', fontsize=12, fontweight='bold')
plt.setp(ax_dash2.xaxis.get_majorticklabels(), rotation=45, ha='right', fontsize=9)
ax_dash2.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels on bars
for bar in ax_dash2.patches:
    height = bar.get_height()
    ax_dash2.text(bar.get_x() + bar.get_width()/2., height,
                  f'{int(height)}', ha='center', va='bottom', fontsize=9)

# ---- Subplot 3: Score vs Comments Scatter ----
ax_dash3 = plt.subplot(2, 2, 3)
ax_dash3.scatter(non_popular_stories['score'], non_popular_stories['num_comments'],
                c='lightcoral', label='Non-Popular', s=80, alpha=0.6, edgecolors='darkred')
ax_dash3.scatter(popular_stories['score'], popular_stories['num_comments'],
                c='limegreen', label='Popular', s=80, alpha=0.6, edgecolors='darkgreen')
ax_dash3.set_xlabel('Score', fontsize=10, fontweight='bold')
ax_dash3.set_ylabel('Number of Comments', fontsize=10, fontweight='bold')
ax_dash3.set_title('Score vs Comments', fontsize=12, fontweight='bold')
ax_dash3.legend(loc='upper left', fontsize=9, framealpha=0.9)
ax_dash3.grid(True, alpha=0.3, linestyle='--')

# ---- Subplot 4: Summary Statistics ----
ax_dash4 = plt.subplot(2, 2, 4)
ax_dash4.axis('off')  # Remove axes for text display

# Calculate summary statistics
total_stories = len(df)
popular_pct = (df['is_popular'].sum() / total_stories) * 100
avg_score = df['score'].mean()
avg_comments = df['num_comments'].mean()
max_engagement = df['engagement'].max()

# Create summary text
summary_text = f"""
SUMMARY STATISTICS

Total Stories: {total_stories}
Popular Stories: {df['is_popular'].sum()} ({popular_pct:.1f}%)
Top Category: {category_counts.index[0]} ({category_counts.values[0]} stories)

Score Analysis:
  • Mean Score: {avg_score:.0f}
  • Median Score: {df['score'].median():.0f}
  • Max Score: {df['score'].max():.0f}

Engagement Analysis:
  • Avg Comments: {avg_comments:.0f}
  • Max Engagement: {max_engagement:.0f}
  • Engagement Threshold: {df['engagement'].median():.0f}

Most Commented Story:
  "{df.loc[df['num_comments'].idxmax(), 'title'][:50]}"
  ({df['num_comments'].max()} comments)
"""

ax_dash4.text(0.1, 0.95, summary_text, transform=ax_dash4.transAxes,
              fontsize=11, verticalalignment='top', fontfamily='monospace',
              bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Save Dashboard
dashboard_path = os.path.join(output_dir, 'dashboard.png')
plt.savefig(dashboard_path, dpi=300, bbox_inches='tight')
print(f"✓ Saved: {dashboard_path}")
plt.close()

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 50)
print("VISUALIZATION COMPLETE")
print("=" * 50)
print(f"\n✓ All files saved to {output_dir}/")
print(f"  - chart1_top_stories.png")
print(f"  - chart2_categories.png")
print(f"  - chart3_scatter.png")
print(f"  - dashboard.png (bonus)")
print("\n✓ TrendPulse Pipeline Complete!")
print("  Data: Collected → Cleaned → Analyzed → Visualized")
