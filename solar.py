#!usr/bin/env python
#
#<sixie6e@paracosmoclast>
#
#pseudolayout
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ezodf


class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)


class solar():	
	def __init__(self, name, types):
		self.name = name
		self.types = types

#kwh0gain, kwhcost
mono = kwh0
poly = kwh1
thin = kwh2
