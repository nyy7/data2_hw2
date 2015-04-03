#!/usr/bin/python
from __future__ import division
import math
from numpy import linalg as LA
import numpy as np

class RBFKernel:
	def __init__(self,sigma):
		self.sigma = sigma;
		self.gamma = -1/(2 * sigma**2)
	def dot_product(self,a,b):
		number = 0
		for i in range(len(a)):
			number += a[i] * b[i]
		return number
	def value(self,a,b):
		dot_a = self.dot_product(a,a)
		dot_b = self.dot_product(b,b)
		dot_ab = self.dot_product(a,b)
		difference = dot_a + dot_b - 2 * dot_ab
		return math.exp(self.gamma*difference);
	def kernel_matrix(self, data):
		matrix = []
		for k in data:
			matrix.append([])
		for i in range(len(data)):
			for j in range(len(data)):
				matrix[i].append(self.value(data[i],data[j]))
		return matrix

kernel = RBFKernel(5.0)
matrix = kernel.kernel_matrix([[2.5,1],[3.5,4],[2,2.1]])
matrix_np = np.array(matrix)
print "The kernel matrix is:" 
print matrix_np
k11 = 2.5**2 + 1**2
k1x = 2.0 / 3.0 * (matrix[0][0] + matrix[0][1]+matrix[0][2])
k_total = 0
for i in range(3):
	for j in range(3):
		k_total += matrix[i][j]
result = k11 - k1x + 1 / 9.0 * k_total
result_sqrt = math.sqrt(result)
print "The distance of Xi from mean is:", result_sqrt


w,v = LA.eig(np.array(matrix_np))
print "The dominant eigen value is:", w[0]
print "The dominant eigen vector is:", v[0]
