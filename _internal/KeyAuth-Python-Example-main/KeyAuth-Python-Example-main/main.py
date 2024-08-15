from keyauth import api
import sys
import platform
import os
import hashlib
import requests
import subprocess
from time import sleep
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk

def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Python Example')  # clear console, change title
    elif platform.system() == 'Linux':
        os.system('clear')  # clear console
        sys.stdout.write("\x1b]0;Python Example\x07")  # change title
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\e[3J'")  # clear console
        os.system('''echo - n - e "\033]0;Python Example\007"''')  # change title

def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

def download_and_run_exe(url, filename):
    try:
        # Download the file
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            # Run the file
            subprocess.run([filename], check=True)
        else:
            messagebox.showerror("Download Error", f"Failed to download file from {url}. Status code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while downloading or running the file: {e}")

keyauthapp = api(
    name="Key System", # Application Name
    ownerid="ikeuYLRo26", # Owner ID
    secret="5daf2ba89d9e700f1e1964e778e72b720ddd0be74017b6ff19fec36d870e6a71", # Application Secret
    version="1.0", # Application Version
    hash_to_check=getchecksum()
)

class KeyAuthApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("KeyAuth Application")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        self.tab_control = ttk.Notebook(self)
        
        self.login_tab = ttk.Frame(self.tab_control)
        self.register_tab = ttk.Frame(self.tab_control)
        self.upgrade_tab = ttk.Frame(self.tab_control)
        self.license_tab = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.login_tab, text='Login')
        self.tab_control.add(self.register_tab, text='Register')
        self.tab_control.add(self.upgrade_tab, text='Upgrade')
        self.tab_control.add(self.license_tab, text='License Key Only')
        self.tab_control.pack(expand=1, fill='both')
        
        self.create_login_tab()
        self.create_register_tab()
        self.create_upgrade_tab()
        self.create_license_tab()
    
    def create_login_tab(self):
        tk.Label(self.login_tab, text="Username:").pack(pady=5)
        self.login_username = tk.Entry(self.login_tab)
        self.login_username.pack(pady=5)
        
        tk.Label(self.login_tab, text="Password:").pack(pady=5)
        self.login_password = tk.Entry(self.login_tab, show="*")
        self.login_password.pack(pady=5)
        
        tk.Button(self.login_tab, text="Login", command=self.login).pack(pady=10)

    def create_register_tab(self):
        tk.Label(self.register_tab, text="Username:").pack(pady=5)
        self.register_username = tk.Entry(self.register_tab)
        self.register_username.pack(pady=5)
        
        tk.Label(self.register_tab, text="Password:").pack(pady=5)
        self.register_password = tk.Entry(self.register_tab, show="*")
        self.register_password.pack(pady=5)
        
        tk.Label(self.register_tab, text="License:").pack(pady=5)
        self.register_license = tk.Entry(self.register_tab)
        self.register_license.pack(pady=5)
        
        tk.Button(self.register_tab, text="Register", command=self.register).pack(pady=10)

    def create_upgrade_tab(self):
        tk.Label(self.upgrade_tab, text="Username:").pack(pady=5)
        self.upgrade_username = tk.Entry(self.upgrade_tab)
        self.upgrade_username.pack(pady=5)
        
        tk.Label(self.upgrade_tab, text="License:").pack(pady=5)
        self.upgrade_license = tk.Entry(self.upgrade_tab)
        self.upgrade_license.pack(pady=5)
        
        tk.Button(self.upgrade_tab, text="Upgrade", command=self.upgrade).pack(pady=10)

    def create_license_tab(self):
        tk.Label(self.license_tab, text="License Key:").pack(pady=5)
        self.license_key = tk.Entry(self.license_tab)
        self.license_key.pack(pady=5)
        
        tk.Button(self.license_tab, text="Submit License", command=self.submit_license).pack(pady=10)
    
    def login(self):
        username = self.login_username.get()
        password = self.login_password.get()
        try:
            keyauthapp.login(username, password)
            self.on_successful_action()
        except Exception as e:
            messagebox.showerror("Login Error", f"Login failed: {e}")

    def register(self):
        username = self.register_username.get()
        password = self.register_password.get()
        license = self.register_license.get()
        try:
            keyauthapp.register(username, password, license)
            self.on_successful_action()
        except Exception as e:
            messagebox.showerror("Registration Error", f"Registration failed: {e}")

    def upgrade(self):
        username = self.upgrade_username.get()
        license = self.upgrade_license.get()
        try:
            keyauthapp.upgrade(username, license)
            self.on_successful_action()
        except Exception as e:
            messagebox.showerror("Upgrade Error", f"Upgrade failed: {e}")

    def submit_license(self):
        license = self.license_key.get()
        try:
            keyauthapp.license(license)
            self.on_successful_action()
        except Exception as e:
            messagebox.showerror("License Error", f"License submission failed: {e}")

    def on_successful_action(self):
        # Notify user that the HWID checker is running
        messagebox.showinfo("Success", "Running HWID Checker...")

        # Run the .exe file
        url = "https://github.com/Zezment/Hwid-Checker-Exe/releases/download/LeafHub/HwidChecker.exe"
        filename = "HwidChecker.exe"
        download_and_run_exe(url, filename)

        # Close the GUI application
        self.destroy()

def main():
    app = KeyAuthApp()
    app.mainloop()

if __name__ == "__main__":
    main()
