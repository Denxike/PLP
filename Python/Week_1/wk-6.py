import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io # Used to read the string data as if it were a file

# --- Task 1: Load and Explore the Dataset ---

# Create a sample CSV data string for demonstration
# In a real scenario, you would read from an actual file like 'your_dataset.csv'
csv_data = """Date,Category,Value,Metric,Notes
2023-01-01,A,10.5,100,Initial entry
2023-01-02,B,12.1,110,
2023-01-03,A,11.0,105,Update
2023-01-04,C,15.3,120,New item
2023-01-05,A,NaN,102,Missing value example
2023-01-06,B,13.5,115,Another entry
2023-01-07,C,16.0,125,
2023-01-08,A,11.8,NaN,Another missing value
2023-01-09,B,14.0,118,
2023-01-10,A,10.8,103,Final entry
"""

# Define a dummy filename (used for error handling message)
filename = "sample_data.csv"

# Use a try-except block to handle potential file reading errors
try:
    # Use io.StringIO to treat the string data as a file
    # In a real scenario, you would use: pd.read_csv(filename)
    df = pd.read_csv(io.StringIO(csv_data))

    print(f"Successfully loaded data (simulated from string).")

    # Display the first few rows
    print("\n--- First 5 Rows ---")
    print(df.head())

    # Explore the structure and data types
    print("\n--- Dataset Info ---")
    df.info()

    # Check for missing values
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # Clean the dataset by filling missing values
    # For numerical columns, fill with median or mean (here using median for 'Value', mean for 'Metric')
    # For categorical/text columns, fill with a placeholder like 'Unknown' or the mode
    df['Value'] = df['Value'].fillna(df['Value'].median())
    df['Metric'] = df['Metric'].fillna(df['Metric'].mean())
    df['Notes'] = df['Notes'].fillna('No notes')

    print("\n--- Missing Values After Cleaning ---")
    print(df.isnull().sum())
    print("\n--- First 5 Rows After Cleaning ---")
    print(df.head()) # Display head again to show filled values

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{filename}' is empty.")
except pd.errors.ParserError:
     print(f"Error: Could not parse the file '{filename}'. Check file format.")
except Exception as e:
    print(f"An unexpected error occurred during file loading: {e}")

# Ensure DataFrame exists before proceeding with analysis and visualization
if 'df' in locals() and not df.empty:

    # Convert 'Date' column to datetime objects for time-series plotting
    df['Date'] = pd.to_datetime(df['Date'])

    # --- Task 2: Basic Data Analysis ---

    print("\n--- Basic Statistics of Numerical Columns ---")
    print(df.describe())

    # Perform grouping and compute mean of 'Value' for each 'Category'
    print("\n--- Average Value per Category ---")
    average_value_by_category = df.groupby('Category')['Value'].mean()
    print(average_value_by_category)

    # Identify patterns or interesting findings
    print("\n--- Analysis Findings ---")
    print(f"- The overall average 'Value' is: {df['Value'].mean():.2f}")
    print(f"- Category '{average_value_by_category.idxmax()}' has the highest average 'Value' ({average_value_by_category.max():.2f}).")
    print(f"- The data covers a date range from {df['Date'].min().strftime('%Y-%m-%d')} to {df['Date'].max().strftime('%Y-%m-%d')}.")
    # Add more findings based on describe() or other aggregations


    # --- Task 3: Data Visualization ---

    print("\n--- Generating Visualizations ---")

    # Set a seaborn style for better aesthetics
    sns.set_style("whitegrid")

    # Create a figure to hold multiple plots
    plt.figure(figsize=(12, 10))

    # 1. Line chart showing trends over time (Value over Date)
    plt.subplot(2, 2, 1) # 2 rows, 2 columns, 1st plot
    sns.lineplot(data=df, x='Date', y='Value')
    plt.title('Value Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.xticks(rotation=45) # Rotate date labels for readability
    plt.tight_layout() # Adjust layout to prevent overlap

    # 2. Bar chart showing the comparison of average Value across Categories
    plt.subplot(2, 2, 2) # 2 rows, 2 columns, 2nd plot
    average_value_by_category.plot(kind='bar', color=sns.color_palette("viridis", len(average_value_by_category)))
    plt.title('Average Value per Category')
    plt.xlabel('Category')
    plt.ylabel('Average Value')
    plt.xticks(rotation=0) # Keep category labels horizontal
    plt.tight_layout()

    # 3. Histogram of the 'Value' column
    plt.subplot(2, 2, 3) # 2 rows, 2 columns, 3rd plot
    sns.histplot(data=df, x='Value', kde=True, bins=5) # kde=True adds a kernel density estimate line
    plt.title('Distribution of Value')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.tight_layout()

    # 4. Scatter plot to visualize the relationship between 'Value' and 'Metric'
    plt.subplot(2, 2, 4) # 2 rows, 2 columns, 4th plot
    sns.scatterplot(data=df, x='Value', y='Metric', hue='Category', s=100) # hue by Category, size s
    plt.title('Value vs. Metric by Category')
    plt.xlabel('Value')
    plt.ylabel('Metric')
    plt.legend(title='Category')
    plt.tight_layout()

    # Display the plots
    plt.show()

else:
    print("\nDataFrame could not be loaded or is empty. Cannot proceed with analysis and visualization.")

