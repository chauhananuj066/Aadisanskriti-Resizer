import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Output folder
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def resize_images(filepaths):
    for path in filepaths:
        try:
            img = Image.open(path)
            img = img.resize((1200, 900), Image.Resampling.LANCZOS)
            base_name = os.path.splitext(os.path.basename(path))[0]
            save_path = os.path.join(output_folder, f"{base_name}.jpg")
            img.convert("RGB").save(save_path, "JPEG")
        except Exception as e:
            print(f"Error: {e}")

    messagebox.showinfo("Success", f"{len(filepaths)} images resized successfully and saved in 'output' folder.")

def browse_and_resize():
    filepaths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.webp")]
    )
    if filepaths:
        resize_images(filepaths)

# Create GUI window
root = tk.Tk()
root.title("Image Resizer - 1200x900")
root.geometry("400x250")
root.resizable(False, False)

# Instruction Label
label = tk.Label(root, text="Select or Drag & Drop images to resize", font=("Arial", 12))
label.pack(pady=20)

# Browse Button
btn = tk.Button(root, text="Select Images", command=browse_and_resize, font=("Arial", 12), bg="lightblue")
btn.pack(pady=10)

# Output Folder Info
output_label = tk.Label(root, text="Resized images will be saved in 'output' folder", font=("Arial", 10))
output_label.pack(pady=5)

# Run the app
root.mainloop()
