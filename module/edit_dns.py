import os
import json

def get_file_path(filename="dns_entries.json"):
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)
    # Construct the path for the 'data' folder
    data_dir = os.path.join(script_dir, 'data')
    # Ensure the 'data' directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    # Construct the file path in the 'data' directory
    return os.path.join(data_dir, filename)

def save_dns_to_file(dns_entries, filename="dns_entries.json"):
    file_path = get_file_path(filename)
    # Save DNS entries as a dictionary to the file
    with open(file_path, "w") as file:
        json.dump(dns_entries, file, indent=4)

def read_dns_from_file(filename="dns_entries.json"):
    file_path = get_file_path(filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return {}

def main():
    print("Add your new DNS settings:")

    # Load existing DNS entries
    dns_entries = read_dns_from_file()
    
    while True:
        dns_name = input("Enter DNS name: ")
        dns1 = input("Enter DNS 1: ")
        dns2 = input("Enter DNS 2: ")
        
        # Add the new DNS entry to the dictionary
        dns_entries[dns_name] = {
            "dns1": dns1,
            "dns2": dns2
        }
        
        # Save the DNS entries to a file
        save_dns_to_file(dns_entries)
        
        # Print the DNS entries
        print("\nDNS settings entered:")
        for name, entry in dns_entries.items():
            print(f"Name: {name}, DNS 1: {entry['dns1']}, DNS 2: {entry['dns2']}")
        
        # Exit the loop after adding one set of DNS entries
        break
    input("Press Enter...")

