import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# функция для расчета значения функции
def calculate_func(n0, r, s, t):
    return n0 * np.exp(r * t + s * s * t * t / 2)

# начальные значения параметров
n0_init = 1
r_init = 0.1
s_init = 0.5

# создание фигуры и осей
fig, ax = plt.subplots()

# задание пределов значений для ползунков
n0_slider_ax = plt.axes([0.2, 0.89, 0.65, 0.03])
r_slider_ax = plt.axes([0.2, 0.92, 0.65, 0.03])
s_slider_ax = plt.axes([0.2, 0.95, 0.65, 0.03])

n0_slider = plt.Slider(n0_slider_ax, 'N0', 0.1, 10.0, valinit=n0_init)
r_slider = plt.Slider(r_slider_ax, 'r', -1.0, 1.0, valinit=r_init)
s_slider = plt.Slider(s_slider_ax, 's', 0.1, 2.0, valinit=s_init)

# функция для обновления графика при изменении ползунков
def update(val):
    n0 = n0_slider.val
    r = r_slider.val
    s = s_slider.val
    t = np.linspace(0, 10, 1000)
    y = calculate_func(n0, r, s, t)
    ax.clear()
    ax.plot(t, y)

    # добавление названий осей
    ax.set_xlabel('t')
    ax.set_ylabel('N')

    fig.canvas.draw_idle()

# привязка функции обновления к изменению ползунков
n0_slider.on_changed(update)
r_slider.on_changed(update)
s_slider.on_changed(update)

# расчет и отображение графика с начальными значениями параметров
t = np.linspace(0, 10, 1000)
y = calculate_func(n0_init, r_init, s_init, t)
ax.plot(t, y)

# добавление названий осей
ax.set_xlabel('t')
ax.set_ylabel('N')

# создание окна tkinter
root = tk.Tk()
root.title("graph of the function N(t)=N0*e^(rt+s^2*t^2*1/2)")
root.resizable(False, False)

# добавление поля ввода значения t
t_label = tk.Label(root, text="t:")
t_label.grid(row=0, column=0)

t_entry = tk.Entry(root)
t_entry.grid(row=0, column=1)

# функция для обновления значения y при изменении значения t
def update_t():
    try:
        t_val = float(t_entry.get())
        y_val = calculate_func(n0_slider.val, r_slider.val, s_slider.val, t_val)
        y_label.config(text="y: {:.2f}".format(y_val))
    except ValueError:
        pass

# добавление кнопки "Получить"
update_button = tk.Button(root, text="Получить", command=update_t)
update_button.grid(row=0, column=2)

# добавление метки для вывода значения y
y_label = tk.Label(root, text="N:")
y_label.grid(row=1, column=0)

# добавление холста для графика
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=2, column=0, columnspan=3)

root.protocol("WM_DELETE_WINDOW", root.quit)

# запуск цикла обработки событий tkinter
tk.mainloop()