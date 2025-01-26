import pandas as pd 

file_path = '../data/london_pharmacies.csv'  # Adjust the path if needed
df = pd.read_csv(file_path)

# Define the phrases to remove
phone_phrase = "Phone number for this organisation is "
address_phrase = "Address for this organisation is "
name_phrase = "navigates to more detail for"
rn_phrase = "\r\n"

# Clean the 'Phone' and 'Address' columns
df['Phone'] = df['Phone'].str.replace(phone_phrase, "", regex=False)
df['Address'] = df['Address'].str.replace(address_phrase, "", regex=False)
df['Name'] = df['Name'].str.replace(name_phrase,"",regex=False)
df['Address'] = df['Address'].str.replace(rn_phrase,"",regex=False)
df['Phone']= df['Phone'].str.replace(rn_phrase, "", regex=False)

# Save the cleaned dataset back to a new CSV file
cleaned_file_path = '../data/london_pharmacies_cleaned.csv'
df.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to '{cleaned_file_path}'.")