def gradient_descent(y,x,e,n_iterations):
  '''
  Inputs:
  y: array of length n
  x: array of length n (lengths of y and x must match)
  e: learning rate
  n_iterations: desired number of iterations for gradient descent algorithm

  Returns:
  b: value that minimizes L(b) = ||y-b x||^2
  '''
  b = 0
  for i in range(n_iterations):
    b += - e*np.sum(-2*(x)*(y-b*x))
  return(b)

'''
Use following lines to test algorithm
Change value of N to desired length of vectors x and y
Change value of E to desired learning rate
Change value of N_ITERATIONS to desired number of iterations
'''

N=50
E=0.01
N_ITERATIONS=200
y = np.random.normal(size=N)
x = np.random.normal(size=N)
print("Gradient descent: b=",gradient_descent(y,x,E,N_ITERATIONS),"Exact: b=",np.sum(x*y)/np.sum(x**2))

'''
1) When the algorithm does converge, a larger value e leads to faster convergence (lower number of steps to achieve same 
accuracy)
2) Sometimes, the algorithm diverges. This occurs more often with vectors of higher dimensions. In these cases, lower values
of e can prevent divergence.
'''
