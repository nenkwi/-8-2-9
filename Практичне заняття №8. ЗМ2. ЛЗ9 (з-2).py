import tkinter as tk
from PIL import Image, ImageTk


class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Анкета студента")
        self.root.geometry("550x420")


        title_label = tk.Label(root, text="Анкета студента", font=("Times New Roman", 16, "bold"), fg="purple")
        title_label.place(x=170, y=20)


        self.info_text = "Прізвище: Гришин\nІм'я: Микита\nГрупа: Ік-51"
        self.lbl_info = tk.Label(root, text=self.info_text, font=("Arial", 12), justify="left")
        self.lbl_info.place(x=30, y=80)


        try:
            pil_img1 = Image.open("photo1.png")
            pil_img1 = pil_img1.resize((180, 220), Image.Resampling.LANCZOS)
            self.img1 = ImageTk.PhotoImage(pil_img1)
        except Exception as e:
            self.img1 = None
            print("Помилка photo1:", e)


        try:
            pil_img2 = Image.open("photo2.png")
            pil_img2 = pil_img2.resize((180, 220), Image.Resampling.LANCZOS)
            self.img2 = ImageTk.PhotoImage(pil_img2)
        except Exception as e:
            self.img2 = None
            print("Помилка photo2:", e)


        self.lbl_image = tk.Label(root, text="[Тут буде фото]", bg="lightgray")
        self.lbl_image.place(x=310, y=80, width=180, height=220)


        self.btn_portrait = tk.Button(root, text="Портретна фотографія", width=22, command=self.show_portrait)
        self.btn_portrait.place(x=30, y=220)

        self.btn_art = tk.Button(root, text="Художня фотографія", width=22, command=self.show_art)
        self.btn_art.place(x=30, y=260)

        self.btn_hide = tk.Button(root, text="Забрати фотографію", width=22, command=self.hide_photos, state="disabled")
        self.btn_hide.place(x=30, y=300)

    def show_portrait(self):
        if self.img1:
            self.lbl_image.config(image=self.img1, text="")
        else:
            self.lbl_image.config(text="Не вдалося завантажити photo1.jpg")
        self.btn_hide.config(state="normal")

    def show_art(self):
        if self.img2:
            self.lbl_image.config(image=self.img2, text="")
        else:
            self.lbl_image.config(text="Не вдалося завантажити photo2.jpg")
        self.btn_hide.config(state="normal")

    def hide_photos(self):
        self.lbl_image.config(image="", text="[ Фото приховано ]")
        self.btn_hide.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()