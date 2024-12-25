import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
data = pd.read_csv('Electric_Vehicle_Population_Data.csv')

# Display the first few rows of the dataset
print(data.head())

# Calculate the average model year
average_model_year = data['Model Year'].mean()
print(f"Average Model Year: {average_model_year:.2f}")

# Count the number of vehicles by make
top_makes = data['Make'].value_counts()

# Plot the bar chart
plt.figure(figsize=(12, 6))
top_makes.plot(kind='bar', color='skyblue')
plt.title('Top 10 Electric Vehicle Makes')
plt.xlabel('Make')
plt.ylabel('Number of Vehicles')
plt.xticks(rotation=45)
plt.show()


# Scatter plot of Model Year vs. Electric Range
plt.figure(figsize=(12, 6))
plt.scatter(data['Model Year'], data['Electric Range'], alpha=0.5, color='green')
plt.title('Model Year vs. Electric Range')
plt.xlabel('Model Year')
plt.ylabel('Electric Range (Miles)')
plt.grid(True)
plt.show()

# Select numerical columns for correlation
numerical_data = data[['Model Year', 'Electric Range', 'Base MSRP']]

# Compute the correlation matrix
correlation_matrix = numerical_data.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix Heatmap')
plt.show()

