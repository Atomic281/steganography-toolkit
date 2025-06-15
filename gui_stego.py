import tkinter as tk
from tkinter import filedialog, messagebox
from image_stego import encode_image, decode_image

def encode_gui():
    path = filedialog.askopenfilename()
    msg = input_box.get()
    save_path = filedialog.asksaveasfilename(defaultextension=".png")
    encode_image(path, msg, save_path)

def decode_gui():
    path = filedialog.askopenfilename()
    result = decode_image(path)
    messagebox.showinfo("Decoded Message", result)

app = tk.Tk()
app.title("Steganography Toolkit")

input_box = tk.Entry(app, width=50)
input_box.pack(pady=10)

tk.Button(app, text="Encode Image", command=encode_gui).pack()
tk.Button(app, text="Decode Image", command=decode_gui).pack()

app.mainloop()