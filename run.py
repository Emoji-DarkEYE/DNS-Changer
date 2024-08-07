import sys
import subprocess
import os
import ctypes
import time
from module import disable_dns, edit_dns, set_dns

# Function to check if the script is running with admin privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        return False

# Function to re-run the script with admin privileges
def run_as_admin():
    if sys.argv[-1] != 'as_admin':
        script = sys.argv[0]
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" as_admin', None, 1)
        sys.exit()

# Run as admin if not already running with admin privileges
if not is_admin():
    run_as_admin()

# Function to display loading animation
def show_loading_animation():
    print("Loading", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

# Function to install packages using pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Function to check if a package is installed
def is_installed(package):
    try:
        __import__(package)
        return True
    except ImportError:
        return False

# Ensure that the required packages are installed
def ensure_installed(package):
    if not is_installed(package):
        print(f"{package} not found. Installing...")
        install(package)
    else:
        print(f"{package} is already installed.")

# Check and install necessary libraries
def lb_check():
    packages = ['requests', 'colorama']
    list(map(ensure_installed, packages))

# Functions for DNS operations
def _set_():
    set_dns.main()

def _edit_():
    edit_dns.main()

def _disable_():
    disable_dns.main()

# Main function to display menu and handle user choice
def main():
    try:
        lb_check()
    except Exception as e:
        print(f"[!] Something went wrong: {e} [!]")

    os.system("cls" if os.name == 'nt' else "clear")

    print("Please enter the number corresponding to your choice:")
    print("1: Set DNS")
    print("2: Edit DNS")
    print("3: Disable DNS")
    print("4: Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        _set_()
    elif choice == '2':
        _edit_()
    elif choice == '3':
        _disable_()
    elif choice == '4':
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")

# Show loading animation before running the main function
if __name__ == "__main__":
    show_loading_animation()
    while True:
        main()
