import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1
if __name__ == "__main__":
    array =  np.random.randint(0,100,20).reshape(2,10)
    print(array)
    plt.boxplot(array)  
    plt.show()

# Task 2
if __name__ == "__main__":
    print ("Mean is: ",np.mean(array))
    print ("Median is: ",np.median(array))
    print ("25th Percentile: ",np.percentile(array,25))
    print ("75th Percentile: ",np.percentile(array,75))
