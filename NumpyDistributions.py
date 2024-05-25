import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label="Normal")
sns.distplot(random.binomial(n=100, p=0.5, size=1000),hist=False, kde='False', label="Binomial")
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label="Poisson")
sns.distplot(random.uniform(0.9, 14, size=100), hist=False, label="Uniform")
sns.distplot(random.logistic(loc=1, scale=2, size=100), hist=False, label="Logistic")
sns.distplot(random.multinomial(n=100, pvals=[1/3, 1/3, 1/3]), hist=False, label="Multinomial")
sns.distplot(random.exponential(scale=5, size=1000), hist=False, label="Exponential")
sns.distplot(random.rayleigh(scale=5, size=1000), hist=False, label="Rayleigh")
sns.distplot(random.chisquare(df=5, size=1000), hist=False, label="ChiSquare")
sns.distplot(random.pareto(a=1.4, size=1000), hist=False, label="Pareto")
plt.show()