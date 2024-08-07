import json
import os
import subprocess

def load_dns_entries(file_path):
    """Load DNS entries from a JSON file."""
    if not os.path.exists(file_path):
        print("File not found.")
        return {}
    with open(file_path, 'r') as file:
        return json.load(file)

def get_current_dns():
    """Get the current DNS settings."""
    try:
        result = subprocess.run(
            ["netsh", "interface", "ip", "show", "dns", "name=\"Wi-Fi\""],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return ""

def set_dns(dns_name, dns_entries):
    """Set DNS settings based on the selected DNS profile."""
    dns_entry = dns_entries.get(dns_name)
    if not dns_entry:
        print("DNS entry not found.")
        return
    
    dns1 = dns_entry['dns1']
    dns2 = dns_entry['dns2']
    
    current_dns = get_current_dns()
    
    if dns1 in current_dns and dns2 in current_dns:
        print("DNS is already set to the selected profile.")
        return
    
    try:
        # Set the preferred DNS server
        subprocess.run([
            "netsh", "interface", "ip", "set", "dns", "name=\"Wi-Fi\"", 
            "source=static", f"addr={dns1}", "register=primary"
        ], check=True)
        
        # Set the alternate DNS server
        subprocess.run([
            "netsh", "interface", "ip", "add", "dns", "name=\"Wi-Fi\"", 
            f"addr={dns2}", "index=2"
        ], check=True)
        
        print(f"DNS settings updated:\nPreferred DNS: {dns1}\nAlternate DNS: {dns2}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def main():
    # Update file path to include the 'data' directory
    file_path = os.path.join('module','data', 'dns_entries.json')
    dns_entries = load_dns_entries(file_path)
    
    if not dns_entries:
        print("No DNS entries found.")
        return
    
    print("Choose a DNS profile by entering the corresponding number:")
    for i, (key, entry) in enumerate(dns_entries.items(), start=1):
        print(f"{i}: {key}")
    
    try:
        choice = int(input("Enter the number of your choice: "))
        if 1 <= choice <= len(dns_entries):
            dns_name = list(dns_entries.keys())[choice - 1]
            set_dns(dns_name, dns_entries)
        else:
            print("Invalid choice. Please select a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    input("Press Enter...")
