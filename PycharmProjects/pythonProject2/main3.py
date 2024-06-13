import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([[2],[4],[5],[4],[5]])

X = np.concatenate([np.ones((len(X),1)),X],axis=1)

theta_init = np.zeros((2,1))
learning_rate = 0.01
num_iterations = 100

def cost_function(X,y, theta):
    m = len(y)
    y_hat = X.dot(theta)
    J = (1/m)* np.sum(np.square(y_hat - y))

    return J

def gradient(X,y, theta):
    m = len(y)
    y_hat = X.dot(theta)
    grad = (1/m)*X.T.dot(y_hat - y)

    return grad

def stochastic_gradient_descent(X,y, theta_init, learning_rate, num_iterations):
    m = len(y)
    theta = theta_init.copy()
    J_history = np.zeros(num_iterations)

    for i in range(num_iterations):
        rand_index = np.random.randint(0,m)

        X_i = np.array([X[rand_index,:]]).reshape(1,-1)
        y_i = np.array([y[rand_index,:]]).reshape(1,-1)

        grad = gradient(X_i,y_i,theta)
        theta = theta - learning_rate * grad

        J_history[i] = cost_function(X,y, theta)

    return theta, J_history

theta, J_history = stochastic_gradient_descent(X,y,theta_init,learning_rate,num_iterations)

plt.plot(J_history)
plt.xlabel('iterations')
plt.ylabel('Cost')
plt.show()

print('Optimized weight: ', theta[1])
print('Optimized bias: ', theta[0])
print('Minimum cost value :', J_history[num_iterations - 1])