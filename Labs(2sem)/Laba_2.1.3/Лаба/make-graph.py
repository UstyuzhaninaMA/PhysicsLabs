import matplotlib.pyplot as plt # импортируем библитеки
import numpy as np

x1 = [0,	1, 	2,	3]
x2 = [0,	1,	2,	3, 4]

y1 = [0 , 1.48- 1.23, 1.73-1.23, 1.97-1.23, 2.22 - 1.23]
y2 = [0,1.26-1.01,1.51-1.01, 1.76-1.01,2.02-1.01]
y3 =[0,1.27-1.02,1.53-1.02,1.78-1.02,2.03-1.02]
y4 =[0,1.29-1.03,1.54-1.03,1.8-1.03]


x_1 = [0, 3]
x_2 = [0, 4]

y_2 = [0, 2.22-1.23]
y_3 =[0, 2.02-1.01]
y_4 =[0, 2.03-1.02]
y_5 =[0, 1.8-1.03]


fig, ax = plt.subplots(figsize = (10, 4), dpi = 200) # создаем пространство для графика
# ax.plot(x, y2, marker = "o", markersize = 10, markevery = 100, markerfacecolor = "red", label = 'Q(h)', color = 'blue') 
# устанавливаем основные параметры графика
ax.plot(x2, y1, 'o')
ax.plot(x2, y2, 'o')
ax.plot(x2, y3, 'o')
ax.plot(x1, y4, 'o')


ax.plot(x_2, y_2, '-.', label = '297 T')
ax.plot( x_2, y_3, '-', label = '308 T')
ax.plot( x_2, y_4, '-.', label = '315 T')
ax.plot( x_1, y_5, '-', label = '323 T')



# ax.set_title('', fontsize = 17, wrap = True)
ax.set_xlabel('Номер резонанса k') 
ax.set_ylabel('Резонансная частота $ f_k - f_0 $, кГц')
ax.set_xlim(0, 4.2)
ax.set_ylim(0, 1.2)


ax.minorticks_on() # включаем метки
ax.grid(which = 'major', linewidth = 1) 
ax.grid(which = 'minor', linestyle = ':')

ax.legend()

fig.savefig('graph.svg')
plt.show()