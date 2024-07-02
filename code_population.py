import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("world_population.csv")

# Display the first few rows and check the structure
print(df.head())

# Data cleaning (if needed)
# For example, handling missing values or converting data types

# Basic statistics and information about the dataset
df.info()

# Exploratory Data Analysis (EDA) - Example visualizations

# Rank by Population
plt.figure(figsize=(10, 6))
sns.barplot(x='Rank', y='Country/Territory', data=df.head(10))
plt.title('Top 10 Countries by Population Rank')
plt.xlabel('Rank')
plt.ylabel('Country/Territory')
plt.xticks(rotation=45)
plt.show()

# Population Growth Rate
plt.figure(figsize=(12, 8))
sns.lineplot(x='Country/Territory', y='Growth Rate', data=df.sort_values(by='Growth Rate', ascending=False).head(20))
plt.xticks(rotation=90)
plt.title('Top 20 Countries by Population Growth Rate')
plt.xlabel('Country/Territory')
plt.ylabel('Growth Rate')
plt.show()

# Population Density
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Density (per km²)', y='2022 Population', data=df)
plt.title('Population Density vs. 2022 Population')
plt.xlabel('Density (per km²)')
plt.ylabel('2022 Population')
plt.show()

# Additional visualizations can include time series plots, density maps (using geospatial libraries like GeoPandas), etc.
