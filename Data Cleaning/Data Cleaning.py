import pandas as pd

# Load data
df = pd.read_csv(r'C:/Users/alexr/Desktop/Carbon data/Datasets/sustainability_data.csv')

df = df.dropna()          # remove missing rows
df = df.drop_duplicates() # remove duplicates

# Order season here for PowerBI
season_order = ['Winter', 'Spring', 'Summer', 'Autumn']
df['Season'] = pd.Categorical(df['Season'], categories=season_order, ordered=True)

# Create KPI's
df['CO2_per_unit'] = (df['CO2_Emissions_kg'] / df['Units_Produced']).round(2)
df['Energy_per_unit'] = (df['Energy_Use_kWh'] / df['Units_Produced']).round(2)
df['Water_per_unit'] = (df['Water_Use_L'] / df['Units_Produced']).round(2)
df['Waste_per_unit'] = (df['Waste_kg'] / df['Units_Produced']).round(2)

# Efficiency score (simple average, lower = better)
df['Efficiency_Score'] = (
    (df['CO2_per_unit'].max() - df['CO2_per_unit']) +
    (df['Energy_per_unit'].max() - df['Energy_per_unit']) +
    (df['Waste_per_unit'].max() - df['Waste_per_unit'])
) / 3
df['Efficiency_Score'] = df['Efficiency_Score'].round(2)


# Group products in categories
def categorize_product(product):
    if 'Milk' in product: return 'Milk Products'
    elif 'Cheese' in product: return 'Cheese Products'
    elif 'Yogurt' in product: return 'Yogurt Products'
    elif 'Butter' in product: return 'Butter Products'
    elif 'Cream' in product: return 'Cream Products'
    else: return 'Other'

df['Product_Category'] = df['Product'].apply(categorize_product)


# Save
df.to_csv(r'C:/Users/alexr/Desktop/Carbon data/Datasets/clean_data.csv', index=False)


