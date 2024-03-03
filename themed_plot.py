import numpy as np
import matplotlib.pyplot as plt

# переменные чтобы удобно менять цвет было
main_color = "#343434" # задний фон
second_color = "#B1B1B1" # акцент - текст, риски
plot_font = "Consolas" # шрифт 

# Создаем объект Figure
fig, ax = plt.subplots()

# Меняем цвета фона
ax.set_facecolor(main_color)
fig.set_facecolor(main_color)

# Меняем цвет и толщину осей
ax.spines['bottom'].set_color(second_color) # Цвет нижней границы
ax.spines['bottom'].set_linewidth(1) # выбор тощины границы
ax.spines['left'].set_color(second_color)   
ax.spines['left'].set_linewidth(1)
ax.spines['top'].set_color(main_color)   
ax.spines['top'].set_linewidth(1)
ax.spines['right'].set_color(main_color)
ax.spines['right'].set_linewidth(1)

# меняем цветь обозначения на грфике
ax.tick_params(axis='x', color=second_color, width=1)  # Изменяет цвет рисок и их подписей на оси X
ax.tick_params(axis='y', color=second_color, width=1)

# Изменение цифр у рисок
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_color(second_color) # цвет
    label.set_weight('regular') # вес - толщина шрифта
    label.set_fontsize(9) # размер
    label.set_fontname(plot_font) # шрифт

# Обозначения
ax.set_xlabel('x', color=second_color, fontsize=12, fontweight='regular', fontname=plot_font)
ax.set_ylabel('x^a', color=second_color, fontsize=12, fontweight='regular', fontname=plot_font)
ax.set_title('Графики функции x^a', color=second_color, fontsize=14, fontweight='regular', fontname=plot_font)

# Создаём массив точек
x1 = np.linspace(0, 10, 100)
y1 = x1 ** 2

x2 = np.linspace(0, 10, 100)
y2 = x2 ** 1.7

x3 = np.linspace(0, 10, 100)
y3 = x3 ** 1.5

# Строим графики и красим под ними

line_colors = [
    '#A23BAB', # 0 фиолетовый
    '#55c6f7', # 1 голубой
    '#3BAB61', # 2 зеленый
    '#AB6A3B', # 3 оранжевый
    '#C13131', # 4 красный
    '#C1BC31', # 5 желтый
    '#D21EB5', # 6 розовый
    '#1ED2A7', # 7 бирюзовый
]

lines = []
lines.append(ax.plot(x1, y1, color=line_colors[5], linewidth=1, label='x^2')[0]) # ставим нужный цвет линии
ax.fill_between(x1, y1, color=line_colors[5], alpha=0.1) # закрашиваем под ноими
lines.append(ax.plot(x2, y2, color=line_colors[1], linewidth=1, label='x^1.7')[0])
ax.fill_between(x2, y2, color=line_colors[1], alpha=0.1)
lines.append(ax.plot(x3, y3, color=line_colors[7], linewidth=1, label='x^1.5')[0])
ax.fill_between(x3, y3, color=line_colors[7], alpha=0.1)

# Добавляем легенду с настройкой стиля
legend = ax.legend(
        loc='upper left', # Расположение
          
        frameon=True, # Включить рамку
        edgecolor=second_color, # Цвет рамки
        facecolor=main_color, # Цвет фона
        framealpha=1, # Прозрачность фона
          
        shadow=False, # Тень
          
        title='легенда', # Заголовок легенды
        prop={'family': plot_font, 'size': 10}, # Настройки шрифта
        
        borderpad=0.5, # Внутренний отступ рамки
        labelspacing=0.5, # Расстояние между метками
        handlelength=1, # Длина маркеров в легенде
        borderaxespad=1, # Отступ рамки от осей
        handletextpad=0.5) # Расстояние между маркером и текстом

# меняем цвет текста легенды
plt.setp(legend.get_title(), color=second_color) # заголовок
plt.setp(legend.get_texts(), color=second_color) # текст

### обработчик мышки

# Инициализируем аннотацию
annot = ax.annotate("", xy=(0,0), xytext=(-55, 10), textcoords="offset points",
                    bbox=dict(boxstyle="round", fc=main_color, ec=second_color, lw=1),
                    fontname=plot_font, fontsize=9, color=second_color)
annot.set_visible(False)

# Функция для обновления аннотации
def update_annot(ind, line):
    x,y = line.get_data()
    annot.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    text = f"{line.get_label()}:\nнед. {x[ind['ind'][0]]:.2f},\nсум. {y[ind['ind'][0]]:.2f}"
    annot.set_text(text)
    annot.get_bbox_patch().set_alpha(0.4)

# Обработчик событий перемещения мыши
def hover(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        for line in lines:
            cont, ind = line.contains(event)
            if cont:
                update_annot(ind, line)
                annot.set_visible(True)
                fig.canvas.draw_idle()
                return
    if vis:
        annot.set_visible(False)
        fig.canvas.draw_idle()

# Подключаем обработчик события
fig.canvas.mpl_connect("motion_notify_event", hover)

# покзать график
plt.show();