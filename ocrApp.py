from tkinter import Tk, filedialog, messagebox, Button, Label
from PIL import Image
import pyocr

engines = pyocr.get_available_tools()
if not engines:
    print("OCR tool not found.")
    exit(1)
engine = engines[0]

def select_image():
    filename = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if filename:
        process_image(filename)

def process_image(filename):
    try:
        builder = pyocr.builders.TextBuilder(tesseract_layout=6)
        txt = engine.image_to_string(Image.open(filename), lang="jpn", builder=builder)
        show_text(txt)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_text(txt):
    Label(root, text=txt).pack()

root = Tk()
Button(root, text="Select Image", command=select_image).pack()
root.mainloop()