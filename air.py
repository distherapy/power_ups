#<sixie6e@paracosmoclast>
#
#pseudolayout
#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ezodf

class air():	
	def __init__(self, name, types):
		self.name = name
		self.types = types
init_data = pd.read_csv("/home/sixie6e/exploitation/basics/mapping/wdi_exp_growth_air/air.csv")
plt.show()
#kwh0gain
#kwh0cost
