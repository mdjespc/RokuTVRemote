import tkinter as tk
from tkinter import messagebox
import requests

class RokuRemote:
    def __init__(self, roku_ip):
        self.roku_ip = roku_ip
        self.base_url = f"http://{self.roku_ip}:8060"

    def send_command(self, command):
        url = f"{self.base_url}/keypress/{command}"
        try:
            response = requests.post(url)
            if response.status_code == 200:
                print(f"Command '{command}' sent successfully.")
            else:
                print(f"Failed to send command '{command}', status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending command: {e}")
            messagebox.showerror("Connection Error", f"Failed to connect to Roku at {self.roku_ip}")

    # Volume controls
    def volume_up(self):
        self.send_command("VolumeUp")

    def volume_down(self):
        self.send_command("VolumeDown")

    def mute(self):
        self.send_command("VolumeMute")

    # Navigation controls
    def home(self):
        self.send_command("Home")

    def up(self):
        self.send_command("Up")

    def down(self):
        self.send_command("Down")

    def left(self):
        self.send_command("Left")

    def right(self):
        self.send_command("Right")

    def select(self):
        self.send_command("Select")

    # Power control (works if CEC or the Roku TV supports it)
    def power_on(self):
        self.send_command("PowerOn")

    def power_off(self):
        self.send_command("PowerOff")

# GUI for Roku Remote Control
class RokuRemoteGUI:
    def __init__(self, root, roku_ip):
        self.remote = RokuRemote(roku_ip)
        self.root = root
        self.root.title("Roku Remote Control")

        # Set up buttons
        self.create_widgets()

    def create_widgets(self):
        # Home button
        home_button = tk.Button(self.root, text="Home", command=self.remote.home, width=10)
        home_button.grid(row=0, column=1)

        # Navigation buttons
        up_button = tk.Button(self.root, text="Up", command=self.remote.up, width=10)
        up_button.grid(row=1, column=1)

        left_button = tk.Button(self.root, text="Left", command=self.remote.left, width=10)
        left_button.grid(row=2, column=0)

        select_button = tk.Button(self.root, text="Select", command=self.remote.select, width=10)
        select_button.grid(row=2, column=1)

        right_button = tk.Button(self.root, text="Right", command=self.remote.right, width=10)
        right_button.grid(row=2, column=2)

        down_button = tk.Button(self.root, text="Down", command=self.remote.down, width=10)
        down_button.grid(row=3, column=1)

        # Volume controls
        volume_up_button = tk.Button(self.root, text="Volume Up", command=self.remote.volume_up, width=10)
        volume_up_button.grid(row=4, column=0)

        volume_down_button = tk.Button(self.root, text="Volume Down", command=self.remote.volume_down, width=10)
        volume_down_button.grid(row=4, column=2)

        mute_button = tk.Button(self.root, text="Mute", command=self.remote.mute, width=10)
        mute_button.grid(row=4, column=1)

        # Power ON button
        power_on_button = tk.Button(self.root, text="Turn ON", command=self.remote.power_on, width=10)
        power_on_button.grid(row=5, column=1)

        #Power OFF button
        power_off_button = tk.Button(self.root, text="Turn OFF", command=self.remote.power_off, width=10)
        power_off_button.grid(row=6, column=1)

def main():
    roku_ip = "ROKU TV IP ADDRESS HERE" 

    root = tk.Tk()
    app = RokuRemoteGUI(root, roku_ip)
    root.mainloop()

if __name__ == "__main__":
    main()

      

