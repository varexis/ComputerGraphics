import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 80, 0, 80])

plt.axis('on')
plt.grid(True)




xc=40
yc=40

r=7

P1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-P1)/100

xlast=xc+r*np.cos(P1)
ylast=yc+r*np.sin(P1)


for p in np.arange(P1,p2+dp,dp):
    x=xc+r*np.cos(p)
    y=yc+r*np.sin(p)
    plt.plot([xlast,x],[ylast,y],color='k',linewidth=1)
    xlast=x
    ylast=y

xcb=40
ycb=40
rb=14
P3=0*np.pi/180
p4=360*np.pi/180
dpb=(p4-P3)/90   
xlastb=xcb+rb*np.cos(P3)
ylastb=ycb+rb*np.sin(P3)    
for p in np.arange(P3,p4+dpb,dpb):
    xb=xcb+rb*np.cos(p)
    yb=ycb+rb*np.sin(p)
    plt.plot([xlastb,xb],[ylastb,yb],color='k',linewidth=1,linestyle=':')
    xlastb=xb
    ylastb=yb

Ax = 40
Ay = 40
Bx = 10
By = 40
Cx = 10
Cy = 20
Dx = 40
Dy = 20

xp = [Ax, Bx, Cx, Dx, Ax]
yp = [Ay, By, Cy, Dy, Ay]
plt.plot(xp, yp, color='b',linestyle='--')

###traslaction de rectangulo para obtner el otro rectngulo superior


plt.axes().set_aspect('equal')
plt.show()