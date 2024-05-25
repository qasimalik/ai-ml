import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long"
        "fM3Trans", "fAlpha", "fDist", "class"]
df = pd.read_csv("magic04.data", names=cols)
df.head()

for label in cols[:-1]:
    plt.hist(df[df["class"] == 1][label], color = 'blue', label = "gamma", alpha = 0.7, density = True)
    plt.hist(df[df["class"] == 0][label], color = 'red', label = "hadron", alpha = 0.7, density = True)
    plt.title(label)
    plt.ylabel("probability")
    plt.xlabel(label)
    plt.legend()
    plt.show()