import scipy.special as sci
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


n = int(input('Number of data points: '))
p = 1/100


#Bernoulli distribution
def Bernoulli(n,p,k):
    return sci.comb(n,k)*p**k*(1-p)**(n-k)

data = [Bernoulli(n,p,k) for k in range(n)]

#Create the plotting object with initial data
fig, ax = plt.subplots()
ber, = ax.plot(data)
ax.set_title('Bernoulli(p) while varying p')

#Update image with new data
def update(l):
    data = [Bernoulli(n,p*l,k) for k in range(n)]
    ber.set_ydata(data)
    return ber

#create animation
ani = animation.FuncAnimation(fig=fig, func=update, frames = 100, interval = 40)


f = r"/home/manu/Bernoulli.gif"
writergif = animation.PillowWriter(fps=30) 
ani.save(f, writer=writergif)
plt.show()
