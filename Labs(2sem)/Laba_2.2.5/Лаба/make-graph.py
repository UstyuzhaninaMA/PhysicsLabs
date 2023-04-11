import matplotlib.pyplot as plt # импортируем библитеки
import numpy as np

data_x = [29, 38, 44, 62]
data_y = [35,	52,	61,	94]

x = [27, 65]
y =[31.6, 99.3]


fig, ax = plt.subplots(figsize = (10, 5), dpi = 100) # создаем пространство для графика
# ax.plot(data_x, data_y, marker = "o", markersize = 10, markevery = 100, markerfacecolor = "red", label = 'Q(h)', color = 'blue') 
# устанавливаем основные параметры графика
ax.plot(data_x, data_y, 'ro', x, y, '-')

ax.set_title('Зависимость Q(h)', fontsize = 17, wrap = True)
ax.set_xlabel('h, мм') 
ax.set_ylabel('Q, мкл/с')
ax.set_xlim(25, 65)
ax.set_ylim(30, 100)


ax.minorticks_on() # включаем метки
ax.grid(which = 'major', linewidth = 1) 
ax.grid(which = 'minor', linestyle = ':')

ax.legend()

fig.savefig('graph.svg')
plt.show()