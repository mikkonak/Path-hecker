import tkinter as tk
from tkinter import filedialog
import os
import tkinter.messagebox

try:
    # Python 3
    from tkinter import simpledialog
except ImportError:
    # Python 2
    import tkSimpleDialog as simpledialog


def check_file_path():
    file_path = filedialog.askopenfilename(title="Выберите файл")

    if not file_path:
        return

    try:
        with open(file_path, 'r'):
            result_label.config(text=f"Успешно открыт файл: {file_path}")
            copy_button.config(state=tk.NORMAL)
            copy_button["command"] = lambda: copy_to_clipboard(file_path)
    except FileNotFoundError:
        result_label.config(text=f"Файл не найден: {file_path}")
        copy_button.config(state=tk.DISABLED)
    except Exception as e:
        result_label.config(text=f"Произошла ошибка при открытии файла {file_path}: {e}")
        copy_button.config(state=tk.DISABLED)


def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # required on Mac OS
    tkinter.messagebox.showinfo("Скопировано", f"Путь скопирован в буфер обмена:\n{text}")


# Создаем основное окно
root = tk.Tk()
root.title("Проверка пути к файлу")

# Добавляем виджеты
check_button = tk.Button(root, text="Выбрать файл и проверить", command=check_file_path)
check_button.pack(pady=20)

result_label = tk.Label(root, text="")
result_label.pack()

copy_button = tk.Button(root, text="Скопировать путь", command=lambda: copy_to_clipboard(result_label.cget("text")),
                        state=tk.DISABLED)
copy_button.pack(pady=10)

# Запускаем главный цикл
root.mainloop()
