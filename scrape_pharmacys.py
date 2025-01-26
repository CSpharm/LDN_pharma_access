import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL for the NHS pharmacy search
base_url = "https://www.nhs.uk/service-search/pharmacy/find-a-pharmacy/results/London?latitude=51.50740862701867&longitude=-0.12772396792576454"

# Step 2: Make a request to the website
response = requests.get(base_url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    print("Successfully accessed the webpage.")
else:
    print(f"Failed to access the webpage. Status code: {response.status_code}")
    exit()

# Step 4: Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Extract pharmacy information
pharmacies = []
pharmacy_list = soup.find_all("div", class_="nhsuk-grid-row results__details")  # Target the container for each pharmacy

for index, pharmacy in enumerate(pharmacy_list):
    # Extract the pharmacy name
    name_tag = pharmacy.find("h2").find("a")
    name = name_tag.text.strip() if name_tag else "N/A"
    
    # Extract the pharmacy phone number
    phone_id = f"phone_{index}"
    phone_tag = pharmacy.find("p", id=phone_id)
    phone = phone_tag.text.strip() if phone_tag else "N/A"
    
    # Extract the pharmacy address
    address_id = f"address_{index}"
    address_tag = pharmacy.find("p", id=address_id)
    address = address_tag.text.strip() if address_tag else "N/A"
    
    # Append the pharmacy details to the list
    pharmacies.append({"Name": name, "Phone": phone, "Address": address})

# Step 6: Save the data to a CSV file
if pharmacies:
    df = pd.DataFrame(pharmacies)
    df.to_csv("../data/london_pharmacies.csv", index=False)
    print("Pharmacy data saved to '../data/london_pharmacies.csv'.")
else:
    print("No pharmacy data found.")
