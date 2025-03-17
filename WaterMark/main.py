from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

FONT_NAME = "Courier"


class WaterMarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WaterMark")
        self.root.config(padx=20, pady=20)

        self.image_path = None
        self.image = None
        self.tk_image = None

        # UI Elements
        self.title_label = Label(text="WaterMark", font=(FONT_NAME, 30))
        self.title_label.grid(column=1, row=0, columnspan=2, pady=10)

        self.input_button = Button(text="Select Image", command=self.open_file_explorer)
        self.input_button.grid(column=0, row=1, pady=10)

        self.add_watermark_button = Button(text="Add WaterMark", command=self.add_watermark)
        self.add_watermark_button.grid(column=1, row=1, pady=10)

        self.save_button = Button(text="Save Image", command=self.save_image)
        self.save_button.grid(column=2, row=1, pady=10)

        self.label = Label(text="No file selected", font=(FONT_NAME, 12))
        self.label.grid(column=1, row=2, columnspan=2, pady=10)

        self.canvas = Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.grid(column=1, row=3, columnspan=2, pady=10)

    def open_file_explorer(self):
        file_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png"), ("JPEG Images", "*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            self.image = Image.open(self.image_path)
            self.image.thumbnail((400, 400))
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(200, 200, image=self.tk_image, anchor=CENTER)
            self.label.config(text=f"Selected File:\n{file_path}", wraplength=400)

    def add_watermark(self):
        if self.image is None:
            self.label.config(text="No image selected!")
            return

        watermark_text = "Watermark"
        watermark = self.image.copy()
        draw = ImageDraw.Draw(watermark)
        font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]

        # Position watermark in bottom-right
        position = (watermark.width - text_width - 10, watermark.height - text_height - 10)
        draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)

        # Update the image with watermark
        self.image = watermark
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(200, 200, image=self.tk_image, anchor=CENTER)

    def save_image(self):
        if self.image is None:
            self.label.config(text="No image to save!")
            return
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg;*.jpeg")])
        if save_path:
            self.image.save(save_path)
            self.label.config(text="Image saved successfully!")


if __name__ == "__main__":
    window = Tk()
    app = WaterMarkApp(window)
    window.mainloop()
