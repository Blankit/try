#coding:utf-8
#2017/10/25
'''
 'torch.IntTensor' object has no attribute 'mean'
 'torch.FloatTensor' object has  attribute 'mean'
'''


#compute gradient

import torch
from torch.autograd import Variable
data1 = [[1,-2],[3,-5]]

#to torch

variable =  Variable(torch.IntTensor(data1),requires_grad = True)
variable1 =  Variable()# build a empty variable

v_out = torch.mean(variable*2)
v_out.backward()

print variable.grad
'''
v_out is the mean value of variable, that means v_out is a function about variable. When compute v_out's backward, the gradient of variable generate automatically.
'''
