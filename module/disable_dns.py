import subprocess

def check_dns(interface_name):
    # Get current DNS configuration
    result = subprocess.run(['netsh', 'interface', 'ip', 'show', 'dns', interface_name], capture_output=True, text=True)
    return result.stdout

def disable_dns(interface_name):
    # Disable DNS by setting it to obtain automatically
    subprocess.run(['netsh', 'interface', 'ip', 'set', 'dns', interface_name, 'dhcp'], capture_output=True, text=True)
    print("DNS disabled.")

def main():
    interface_name = 'Wi-Fi'  # Set your network interface name here

    # Check current DNS configuration
    dns_config = check_dns(interface_name)

    if "DHCP" in dns_config:
        print("DNS is already set to obtain automatically.")
    else:
        disable_dns(interface_name)
    input("Press Enter...")
