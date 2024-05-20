import pandas as pd
import matplotlib.pyplot as plt

# Parameters
cost_per_gb_per_month = 0.023  # Example cost of S3 storage per GB per month

# Function to load data
def load_data(file_path):
    df = pd.read_csv(file_path)
    df['file_timestamp'] = pd.to_datetime(df['file_timestamp'])
    return df

# Function to calculate yearly costs
def calculate_yearly_costs(df):
    df['year'] = df['file_timestamp'].dt.year
    yearly_costs = df.groupby('year')['file_size'].sum() * cost_per_gb_per_month * 12
    return yearly_costs

# Function to calculate monthly costs
def calculate_monthly_costs(df):
    df['month'] = df['file_timestamp'].dt.to_period('M')
    monthly_costs = df.groupby('month')['file_size'].sum() * cost_per_gb_per_month
    return monthly_costs

# Function to calculate yearly storage volume in TB
def calculate_yearly_storage_volume(df):
    df['year'] = df['file_timestamp'].dt.year
    yearly_storage_tb = df.groupby('year')['file_size'].sum() / 1024
    return yearly_storage_tb

# Function to plot yearly costs
def plot_yearly_costs(yearly_costs):
    plt.figure(figsize=(10, 6))
    plt.plot(yearly_costs.index, yearly_costs.values, marker='o', linestyle='-', color='r', label='Accumulated Cost ($)')
    plt.xlabel('Year')
    plt.ylabel('Accumulated Cost ($)')
    plt.title('Yearly S3 Storage Costs')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot yearly storage volume
def plot_yearly_storage_volume(yearly_storage_tb):
    plt.figure(figsize=(10, 6))
    plt.plot(yearly_storage_tb.index, yearly_storage_tb.values, marker='o', linestyle='-', color='b', label='Storage Volume (TB)')
    plt.xlabel('Year')
    plt.ylabel('Storage Volume (TB)')
    plt.title('Yearly S3 Storage Volume')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to plot monthly costs
def plot_monthly_costs(monthly_costs):
    plt.figure(figsize=(15, 7))
    monthly_costs.plot(kind='bar', color='g', title='Monthly S3 Storage Costs')
    plt.ylabel('Cost ($)')
    plt.xlabel('Month')
    plt.grid(True)
    plt.show()

# Main function to perform the analysis
def main(file_path):
    df = load_data(file_path)
    
    yearly_costs = calculate_yearly_costs(df)
    monthly_costs = calculate_monthly_costs(df)
    yearly_storage_tb = calculate_yearly_storage_volume(df)
    
    plot_yearly_costs(yearly_costs)
    plot_yearly_storage_volume(yearly_storage_tb)
    plot_monthly_costs(monthly_costs)

# Run the main function
file_path = "s3_inventory.csv"  # Update this to your actual file path
main(file_path)
