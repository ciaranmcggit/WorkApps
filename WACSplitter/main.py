import configparser as cp
import tkinter as tk
from tkinter import filedialog
import WACSplitter.functions as f

config = cp.ConfigParser()
config.read("settings.ini")

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

dest_folder = config.get("settings", "destination_folder")
file_count = config.get("settings", "file_count")
file_prefix = config.get("settings", "file_prefix")

f.split_csv(file_path, dest_folder, file_count, file_prefix)

