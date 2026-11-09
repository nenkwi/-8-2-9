import tkinter as tk
from tkinter import messagebox


def calculate():
    try:

        kurs_buy = float(entry_buy.get())
        kurs_sell = float(entry_sell.get())
        amount = float(entry_amount.get())


        if operation_var.get() == 1:
            result = kurs_buy * amount
        else:
            result = kurs_sell * amount


        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, f"{result:.2f}")
        entry_result.config(state="readonly")

    except ValueError:

        messagebox.showerror("Помилка", "Будь ласка, введіть коректні числові дані у поля!")


def clear_fields():
    entry_amount.delete(0, tk.END)
    entry_result.config(state="normal")
    entry_result.delete(0, tk.END)
    entry_result.config(state="readonly")


def update_arrow(*args):
    if operation_var.get() == 1:
        label_arrow.config(text="<=")
    else:
        label_arrow.config(text="=>")



root = tk.Tk()
root.title("Обмін валют")
root.geometry("450x280")
root.resizable(False, False)


operation_var = tk.IntVar(value=2)
operation_var.trace("w", update_arrow)


rb_buy = tk.Radiobutton(root, text="Купівля", variable=operation_var, value=1, font=("Arial", 10))
rb_buy.place(x=50, y=20)

rb_sell = tk.Radiobutton(root, text="Продаж", variable=operation_var, value=2, font=("Arial", 10))
rb_sell.place(x=280, y=20)


tk.Label(root, text="Курс купівлі:").place(x=50, y=60)
entry_buy = tk.Entry(root, width=15)
entry_buy.place(x=50, y=85)
entry_buy.insert(0, "5.0")

tk.Label(root, text="Курс продажу:").place(x=280, y=60)
entry_sell = tk.Entry(root, width=15)
entry_sell.place(x=280, y=85)
entry_sell.insert(0, "5.2")


label_arrow = tk.Label(root, text="=>", font=("Arial", 14, "bold"))
label_arrow.place(x=210, y=120)


tk.Label(root, text="Сума (USD):").place(x=50, y=130)
entry_amount = tk.Entry(root, width=15)
entry_amount.place(x=50, y=155)

tk.Label(root, text="Результат (UAH):").place(x=280, y=130)
entry_result = tk.Entry(root, width=15, state="readonly")
entry_result.place(x=280, y=155)


btn_calc = tk.Button(root, text="Конвертувати", width=12, command=calculate)
btn_calc.place(x=40, y=210)

btn_clear = tk.Button(root, text="Очистити", width=12, command=clear_fields)
btn_clear.place(x=170, y=210)

btn_exit = tk.Button(root, text="Вихід", width=12, command=root.destroy)
btn_exit.place(x=300, y=210)

root.mainloop()