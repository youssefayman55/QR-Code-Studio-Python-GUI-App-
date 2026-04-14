import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode


class QRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Studio 🚀")
        self.root.geometry("900x650")
        self.root.configure(bg="#eef2f3")

        self.gallery = []
        self.current_img = None
        self.current_tk_img = None

        self.build_tabs()

    # ================= UI =================
    def build_tabs(self):
        style = ttk.Style()
        style.theme_use("clam")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_generate = ttk.Frame(self.notebook)
        self.tab_gallery = ttk.Frame(self.notebook)
        self.tab_reader = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_generate, text="Generate")
        self.notebook.add(self.tab_gallery, text="Gallery")
        self.notebook.add(self.tab_reader, text="Read QR")

        self.build_generate_tab()
        self.build_gallery_tab()
        self.build_reader_tab()

    # ================= Generate =================
    def build_generate_tab(self):
        frame = self.tab_generate

        tk.Label(frame, text="Website URL:", font=("Helvetica", 12, "bold"), bg="#eef2f3").grid(row=0, column=0, sticky="w", padx=15, pady=10)

        self.url_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.url_var, width=50).grid(row=1, column=0, columnspan=2, padx=15)

        # options
        self.ec_var = tk.StringVar(value="M")
        self.box_size = tk.IntVar(value=10)
        self.border = tk.IntVar(value=4)
        self.fname_var = tk.StringVar()

        tk.Label(frame, text="File Name:", bg="#eef2f3").grid(row=2, column=0, padx=15, sticky="w")
        tk.Entry(frame, textvariable=self.fname_var).grid(row=2, column=1, sticky="w")

        tk.Button(frame, text="Generate QR Code", command=self.generate_qr,
                  bg="#2c3e50", fg="white", padx=10).grid(row=3, column=0, columnspan=2, pady=10)

        self.qr_label = tk.Label(frame, text="Preview will appear here", bg="#eef2f3")
        self.qr_label.grid(row=4, column=0, columnspan=2, pady=10)

        btn_frame = tk.Frame(frame, bg="#eef2f3")
        btn_frame.grid(row=5, column=0, columnspan=2)

        tk.Button(btn_frame, text="Download", command=self.download_qr, bg="#27ae60", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Save to Gallery", command=self.save_to_gallery, bg="#2980b9", fg="white").pack(side="left", padx=5)

    def generate_qr(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Warning", "Enter URL first")
            return

        qr = qrcode.QRCode(box_size=self.box_size.get(), border=self.border.get())
        qr.add_data(url)
        qr.make(fit=True)

        self.current_img = qr.make_image(fill_color="black", back_color="white")

        display = self.current_img.resize((220, 220))
        self.current_tk_img = ImageTk.PhotoImage(display)
        self.qr_label.configure(image=self.current_tk_img, text="")

    def download_qr(self):
        if not self.current_img:
            return

        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            self.current_img.save(path)

    def save_to_gallery(self):
        if not self.current_img:
            return

        self.gallery.append({
            "name": self.fname_var.get() or f"QR_{len(self.gallery)+1}",
            "url": self.url_var.get(),
            "img": self.current_img.copy()
        })
        self.refresh_gallery()

    # ================= Gallery =================
    def build_gallery_tab(self):
        frame = self.tab_gallery

        self.gallery_listbox = tk.Listbox(frame, width=40, height=10)
        self.gallery_listbox.pack(pady=10)
        self.gallery_listbox.bind("<<ListboxSelect>>", self.show_gallery_item)

        self.gallery_preview = tk.Label(frame)
        self.gallery_preview.pack()

        tk.Button(frame, text="Download", command=self.gallery_download).pack(pady=5)
        tk.Button(frame, text="Delete", command=self.gallery_delete).pack(pady=5)

    def refresh_gallery(self):
        self.gallery_listbox.delete(0, tk.END)
        for item in self.gallery:
            self.gallery_listbox.insert(tk.END, item["name"])

    def show_gallery_item(self, event):
        sel = self.gallery_listbox.curselection()
        if not sel:
            return

        item = self.gallery[sel[0]]
        img = item["img"].resize((180, 180))
        tk_img = ImageTk.PhotoImage(img)

        self.gallery_preview.configure(image=tk_img)
        self.gallery_preview.image = tk_img

    def gallery_download(self):
        sel = self.gallery_listbox.curselection()
        if not sel:
            return

        item = self.gallery[sel[0]]
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if path:
            item["img"].save(path)

    def gallery_delete(self):
        sel = self.gallery_listbox.curselection()
        if not sel:
            return

        self.gallery.pop(sel[0])
        self.refresh_gallery()

    # ================= Reader =================
    def build_reader_tab(self):
        frame = self.tab_reader

        tk.Button(frame, text="Open Image", command=self.read_qr).pack(pady=10)

        self.reader_preview = tk.Label(frame)
        self.reader_preview.pack()

        self.decoded_text = tk.StringVar()
        tk.Entry(frame, textvariable=self.decoded_text, width=50, state="readonly").pack(pady=5)

    def read_qr(self):
        path = filedialog.askopenfilename()
        if not path:
            return

        img = Image.open(path)
        decoded = decode(img)

        if decoded:
            result = decoded[0].data.decode("utf-8")
            self.decoded_text.set(result)

            img = img.resize((180, 180))
            tk_img = ImageTk.PhotoImage(img)
            self.reader_preview.configure(image=tk_img)
            self.reader_preview.image = tk_img


if __name__ == "__main__":
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()
