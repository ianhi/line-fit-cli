import numpy as np
xdata = np.linspace(0, 4, 50)
y = xdata*4 + 10 + np.random.randn(len(xdata))

np.savetxt('heck.csv', np.hstack((xdata[:,None], y[:, None])))
