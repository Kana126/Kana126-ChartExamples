# Пример построения графиков

import tkinter as tk

# Импорт внешних файлов
import chart1
import chart2
import chart3

# Создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

#Функция закрытия программы
def do_close():
    window.destroy()

#Добавление метки заголовка
tblTitle = tk.Label(text = "Примеры построение графиков", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
tblTitle.place(x=55, y=25)

#Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text='График 1', font = ('Helvetica', 10, 'bold'), command=chart1.plot_chart)
btnChart1.place(x=40, y=115, width=90, height=30)

lblChart1 = tk.Label(text = "График синуса matplotlib")
lblChart1.place(x=170, y=122)

#Добавление кнопки и метки для графика 2
btnChart2 = tk.Button(window, text='График 2', font = ('Helvetica', 10, 'bold'),command=chart2.plot_chart)
btnChart2.place(x=40, y=165, width=90, height=30)

lblChart2 = tk.Label(text = "Нормальное распределение")
lblChart2.place(x=170, y=172)

#Добавление кнопки и метки для графика 3
btnChart3 = tk.Button(window, text='График 3', font = ('Helvetica', 10, 'bold'),command=chart3.plot_chart)
btnChart3.place(x=40, y=215, width=90, height=30)

lblChart3 = tk.Label(text = "Нормальное Seaborn")
lblChart3.place(x=170, y=222)

# Добавление кнопки закрытия прогаммы
btnClose = tk.Button(window, text='Закрыть', font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=330, y=400, width=99, height=30)

# Запуск цикла mainloop
window.mainloop()




