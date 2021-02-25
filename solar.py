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

class solar():	
	def __init__(self, name, types):
		self.name = name
		self.types = types

#kwh0gain, kwh0cost
mono = kwh0
poly = kwh1
thin = kwh2
