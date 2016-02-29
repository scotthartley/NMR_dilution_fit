""" A simple python script that uses the leastsq function from SciPy to carry out a nonlinear
regression. Outputs a bunch of different measures to be used in judging the fit. Requires an input
file with x and y columns, no headings. Pass filename as an argument.


"""
import numpy, sys
from scipy.optimize import leastsq

# Define the function here, using p as an array of parameters. Functions must be able to take arrays
# as arguments (use numpy version of exp, for example).
def func(p, x):
    return (p[0] - p[1])*(1+(1-numpy.sqrt(8*p[2]*x+1))/(4*p[2]*x)) + p[1]

# Initial guesses for the parameters.
p0 = [10, 5, 600] # Pd Pm Ke


datafile = open(sys.argv[1])
x, y = numpy.array([]), numpy.array([])
for line in datafile:
    curline = line.replace("\n", "").split() # Splits at any whitespace.
    x = numpy.append(x, float(curline[0]))
    y = numpy.append(y, float(curline[1]))

# Defines the error function for leastsq. In for regression, it is just the residuals.
def func_res(p, x, y):
    return y - func(p, x)

dof = len(x) - len(p0) # Degrees of freedom

fit_parameters, covariance_matrix, info, msg, success \
    = leastsq(func_res, p0, args=(x,y), full_output=True)

sum_squares_residuals = sum(info["fvec"]*info["fvec"])
sum_squares_mean_dev = sum((y - numpy.mean(y))**2)

# The errors for each parameter are obtained by multiplying the covariance matrix by the residual
# variance (= sum_squares_residuals / dof).
errors = []
for i in range(len(covariance_matrix)):
    errors.append(numpy.sqrt(covariance_matrix[i,i]*sum_squares_residuals/dof))

print("**Regression results for file \"{}\"**".format(sys.argv[1]))
print()

print("Data (x, y, yfit)")
print("=================")
for n in range(len(x)):
    print("{}, {}, {}".format(x[n], y[n], y[n] - info["fvec"][n]))
print()

print("Optimized parameters")
print("====================")
for n in range(len(fit_parameters)):
    print("{} +/- {}".format(fit_parameters[n], errors[n]))
print()

print("Regression data")
print("===============")

# See leastsq documentation for descriptions of flags.
print("Flag: {}".format(success))

print("Std Deviation of residuals: {}".format(numpy.sqrt(sum_squares_residuals/dof)))
print("chi2 (sum square residuals): {}".format(sum_squares_residuals))

# Ideally, (reduced chi2)/(std dev of measurement) = 1.
print("Reduced chi2 (chi2/dof): {}".format(sum_squares_residuals/dof))
print("R2 = {}".format(1 - sum_squares_residuals/sum_squares_mean_dev))
print("Adjusted R2 = {}".format(1 - (sum_squares_residuals/dof)/(sum_squares_mean_dev/(len(x)-1))))
print("Covariance matrix:")
print(covariance_matrix*sum_squares_residuals/dof)
print("Residuals:")
print(info["fvec"])
