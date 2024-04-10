import pandas as pd

# Read data from CSV file
df = pd.read_csv('Asm2_Data.csv')

# Check for null data
null_data = df[df.isnull().any(axis=1)]
if not null_data.empty:
    print("There are rows with null values.")
    # Handle null values here if necessary

# Check for empty data
empty_rows = df[df.applymap(lambda x: isinstance(x, str) and x.strip() == '').all(axis=1)]
if not empty_rows.empty:
    print("There are empty rows.")

# Check and remove duplicate data
duplicate_rows = df[df.duplicated()]
if not duplicate_rows.empty:
    print("There are duplicate rows. Removing duplicate rows...")
    df = df.drop_duplicates()
else:
    print("No duplicate rows.")

# Identify and handle missing data
missing_data = df.isnull().sum()
print("Missing data in each column:")
print(missing_data)

# Convert column 'gender' to the correct format
valid_genders = ['Male', 'Female', 'Other', 'Unknown']
df['gender'] = df['gender'].apply(lambda x: x if x in valid_genders else 'Unknown')

#Check data after conversion
print(df['gender'].value_counts())

# Check and fix email syntax errors
df['email'] = df['email'].str.replace(r'[^@]+@[^@]+\.[^@]+', 'invalid_email')
print(df['email'].value_counts())

# Remove unnecessary attributes
df = df.drop(columns=['id'])

# Identify and handle outliers
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

for column in numerical_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    if not outliers.empty:
        print(f"Outliers detected in column '{column}'. Handling outliers...")
        df.loc[(df[column] < lower_bound) | (df[column] > upper_bound), column] = df[column].median()
    else:
        print(f"No outliers detected in column '{column}'.")

print("Outlier handling completed.")

# Save processed data to a new CSV file
df.to_csv('Asm2_Cleaned_Data.csv', index=False)

print("Data processing completed. The data has been saved to the file Asm2_Cleaned_Data.csv.")
