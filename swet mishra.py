import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Data Generation --- #
# Set a random seed for reproducibility
np.random.seed(42)

# Generate a DataFrame with random integer data
# The data will have 30 rows and 6 columns, with values between 10 and 99.
df = pd.DataFrame(np.random.randint(10, 100, (30, 6)),
                  columns=["Performance", "Sports", "Transport", "Disease", "Sales", "Health"])

# Add a 'Day' column ranging from 1 to 30
df["Day"] = range(1, 31)

print("Original DataFrame Head  Untitled2:18 - swet mishra.py:18")
print(df.head())
print("\n  Untitled2:20 - swet mishra.py:20")

# --- Descriptive Statistics --- #
# Display general descriptive statistics for the DataFrame
print("Descriptive Statistics  Untitled2:24 - swet mishra.py:24")
print(df.describe())
print("\n  Untitled2:26 - swet mishra.py:26")

# --- Visualizations --- #

# 1. Line plots for each column against 'Day' (time series style)
plt.figure(figsize=(15, 10))
plt.suptitle('Daily Trends of Different Metrics', fontsize=16, y=1.02)

for i, col in enumerate(df.columns[:-1], 1): # Exclude the 'Day' column for this loop
    plt.subplot(3, 2, i) # Arrange plots in 3 rows, 2 columns
    sns.lineplot(x="Day", y=col, data=df)
    plt.title(f'{col} Over Days')
    plt.xlabel('Day')
    plt.ylabel(col)
    plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0, 1, 0.98]) # Adjust layout to prevent title overlap
plt.show()

# 2. Histograms to show the distribution of each metric
plt.figure(figsize=(15, 10))
plt.suptitle('Distribution of Each Metric (Histograms)', fontsize=16, y=1.02)

for i, col in enumerate(df.columns[:-1], 1):
    plt.subplot(3, 2, i)
    sns.histplot(df[col], kde=True, bins=10, color='skyblue')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.show()

# 3. Box plots to show central tendency, spread, and outliers for each metric
plt.figure(figsize=(15, 10))
plt.suptitle('Box Plots of Each Metric', fontsize=16, y=1.02)

for i, col in enumerate(df.columns[:-1], 1):
    plt.subplot(3, 2, i)
    sns.boxplot(y=df[col], color='lightgreen')
    plt.title(f'Box Plot of {col}')
    plt.ylabel(col)

plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.show()

# 4. Correlation Analysis
print("Correlation Matrix  Untitled2:73 - swet mishra.py:73")
correlation_matrix = df.corr()
print(correlation_matrix)
print("\n  Untitled2:76 - swet mishra.py:76")

# Heatmap of the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix of All Variables')
plt.show()