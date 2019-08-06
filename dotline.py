"""
DOTLINE
"""

import matplotlib.pyplot as plt
import numpy as nu

plt.axis([-20, 130, 80, -20])

plt.axis('on')
plt.grid(False) # 不打网格

plt.arrow(0,0,20,0,head_length=4, head_width=3, color='k')
plt.arrow(0,0,0,20,head_length=4, head_width=3, color='k')
plt.text(15,-3,'x')
plt.text(-5,15,'y')


plt.show()
