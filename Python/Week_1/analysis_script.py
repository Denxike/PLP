import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io

# Create a dummy CSV file content for demonstration
# In a real scenario, you would have your data in a file like 'your_dataset.csv'
csv_data = """Date,Product,Category,SalesAmount,Quantity,Region
2023-01-01,A,Electronics,1500,10,North
2023-01-01,B,Clothing,500,25,South
2023-01-02,A,Electronics,1600,11,North
2023-01-02,C,Books,300,20,East
2023-01-03,B,Clothing,550,28,South
2023-01-03,A,Electronics,1550,10,North
2023-01-04,C,Books,320,21,East
2023-01-04,D,Home,800,5,West
2023-01-05,A,Electronics,1700,12,North
2023-01-05,B,Clothing,600,30,South
2023-01-06,D,Home,850,6,West
2023-01-06,C,Books,350,23,East
2023-01-07,A,Electronics,1750,13,North
2023-01-07,B,Clothing,620,31,South
2023-01-08,D,Home,900,7,West
2023-01-08,A,Electronics,1800,14,North
2023-01-09,C,Books,380,25,East
2023-01-09,B,Clothing,650,33,South
2023-01-10,A,Electronics,1850,15,North
2023-01-10,D,Home,950,8,West
2023-01-11,B,Clothing,680,35,South
2023-01-11,C,Books,400,26,East
2023-01-12,A,Electronics,1900,16,North
2023-01-12,D,Home,1000,9,West
2023-01-13,B,Clothing,700,36,South
2023-01-13,C,Books,420,28,East
2023-01-14,A,Electronics,1950,17,North
2023-01-14,D,Home,1050,10,West
2023-01-15,B,Clothing,720,38,South
2023-01-15,A,Electronics,2000,18,North
2023-01-16,C,Books,450,30,East
2023-01-16,D,Home,1100,11,West
2023-01-17,A,Electronics,2100,19,North
2023-01-17,B,Clothing,750,40,South
2023-01-18,D,Home,1150,12,West
2023-01-18,C,Books,480,32,East
2023-01-19,A,Electronics,2200,20,North
2023-01-19,B,Clothing,780,42,South
2023-01-20,D,Home,1200,13,West
2023-01-20,A,Electronics,2300,21,North
"""

# Use io.StringIO to simulate reading from a file
# In a real scenario, replace this with the actual path:
csv_file_path = io.StringIO(csv_data)


# --- Task 1: Load and Explore the Dataset ---
print("--- Task 1: Load and Explore the Dataset ---")

df = None # Initialize df to None

try:
    # Load the dataset
    # In a real scenario, replace csv_file_path with the actual path:
    # df = pd.read_csv('your_dataset.csv')
    df = pd.read_csv(csv_file_path)
    print("Dataset loaded successfully.")

    # Display the first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Explore the structure and check for missing values
    print("\nDataset Info:")
    df.info()

    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Clean the dataset (Example: Dropping rows with any missing values)
    initial_rows = df.shape[0]
    df.dropna(inplace=True)
    rows_after_dropping = df.shape[0]
    if initial_rows > rows_after_dropping:
        print(f"\nDropped {initial_rows - rows_after_dropping} rows with missing values.")
    else:
        print("\nNo missing values found, no rows dropped.")

    # Convert 'Date' column to datetime objects
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        print("\n'Date' column converted to datetime.")
    else:
        print("\n'Date' column not found in the dataset.")


except FileNotFoundError:
    print(f"Error: The file was not found.") # Using generic message as path might be internal to tool
except pd.errors.EmptyDataError:
    print(f"Error: The file is empty.")
except pd.errors.ParserError:
    print(f"Error: Could not parse the file. Check the format.")
except Exception as e:
    print(f"An unexpected error occurred during file loading: {e}")

# --- Task 2: Basic Data Analysis ---
print("\n--- Task 2: Basic Data Analysis ---")

if df is not None and not df.empty: # Proceed only if DataFrame was loaded and is not empty
    # Compute basic statistics of numerical columns
    print("\nBasic statistics of numerical columns:")
    print(df.describe())

    # Check if 'Category' and 'SalesAmount' columns exist before grouping
    if 'Category' in df.columns and 'SalesAmount' in df.columns:
        # Perform groupings on a categorical column ('Category') and compute mean of 'SalesAmount'
        print("\nMean SalesAmount per Category:")
        sales_by_category = df.groupby('Category')['SalesAmount'].mean()
        print(sales_by_category)
    else:
        print("\n'Category' or 'SalesAmount' column not found for category sales analysis.")

    # Check if 'Region' and 'Quantity' columns exist before grouping
    if 'Region' in df.columns and 'Quantity' in df.columns:
        # Perform groupings on another categorical column ('Region') and compute mean of 'Quantity'
        print("\nMean Quantity sold per Region:")
        quantity_by_region = df.groupby('Region')['Quantity'].mean()
        print(quantity_by_region)
    else:
         print("\n'Region' or 'Quantity' column not found for region quantity analysis.")


    print("\n--- Insights from Basic Analysis ---")
    print("- The analysis provides summary statistics for numerical columns and calculates mean sales/quantity grouped by categorical features.")
    print("- These statistics help in understanding the typical values, spread, and initial relationships within the data.")


    # --- Task 3: Data Visualization ---
    print("\n--- Task 3: Data Visualization ---")

    # Set a style for the plots
    sns.set_style("whitegrid")

    # 1. Line chart showing trends over time (SalesAmount)
    if 'Date' in df.columns and 'SalesAmount' in df.columns:
        plt.figure(figsize=(12, 6))
        # Group by Date and sum SalesAmount for time series
        sales_over_time = df.groupby('Date')['SalesAmount'].sum().reset_index()
        sns.lineplot(data=sales_over_time, x='Date', y='SalesAmount')
        plt.title('Total Sales Amount Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales Amount')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("\nSkipping Line Chart: 'Date' or 'SalesAmount' column not found.")


    # 2. Bar chart showing the comparison of a numerical value across categories (Average SalesAmount per Category)
    # This requires sales_by_category from Task 2, ensure it was computed
    if 'Category' in df.columns and 'SalesAmount' in df.columns and 'sales_by_category' in locals():
        plt.figure(figsize=(10, 6))
        sns.barplot(x=sales_by_category.index, y=sales_by_category.values, palette='viridis')
        plt.title('Average Sales Amount per Product Category')
        plt.xlabel('Product Category')
        plt.ylabel('Average Sales Amount')
        plt.tight_layout()
        plt.show()
    else:
         print("\nSkipping Bar Chart: Required columns or data for plotting not available.")


    # 3. Histogram of a numerical column (SalesAmount)
    if 'SalesAmount' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['SalesAmount'], bins=10, kde=True)
        plt.title('Distribution of Sales Amount')
        plt.xlabel('Sales Amount')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()
    else:
        print("\nSkipping Histogram: 'SalesAmount' column not found.")


    # 4. Scatter plot to visualize the relationship between two numerical columns (SalesAmount vs. Quantity)
    if 'Quantity' in df.columns and 'SalesAmount' in df.columns and 'Category' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='Quantity', y='SalesAmount', hue='Category', s=100) # Added hue for better insight
        plt.title('Relationship between Quantity and Sales Amount')
        plt.xlabel('Quantity Sold')
        plt.ylabel('Sales Amount')
        plt.legend(title='Product Category')
        plt.tight_layout()
        plt.show()
    elif 'Quantity' in df.columns and 'SalesAmount' in df.columns:
         # Plot without hue if Category is missing but Quantity and SalesAmount exist
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='Quantity', y='SalesAmount', s=100)
        plt.title('Relationship between Quantity and Sales Amount')
        plt.xlabel('Quantity Sold')
        plt.ylabel('Sales Amount')
        plt.tight_layout()
        plt.show()
        print("\nNote: 'Category' column not found for scatter plot hue.")
    else:
        print("\nSkipping Scatter Plot: Required numerical columns ('Quantity' or 'SalesAmount') not found.")


    print("\n--- Insights from Visualizations ---")
    print("- The plots visually represent the data distribution, trends over time, comparisons between categories, and relationships between numerical variables.")
    print("- These visualizations make it easier to identify patterns, outliers, and trends that might not be apparent from raw data or summary statistics alone.")

else:
    print("\nData loading failed or DataFrame is empty, skipping analysis and visualization tasks.")
