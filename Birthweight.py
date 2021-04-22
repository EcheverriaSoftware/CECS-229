import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    fileName =  "birthweight.csv"
    df = pd.read_csv(fileName, sep = ',')
    #print(df)
    #np_all = df.values
    #print(np_all)
    np_x = df['fheight'].to_numpy()
    #print(np_x)
    np_y = df['Birthweight'].to_numpy()
    #print(np_y)
    plt.scatter(np_x, np_y)
    plt.xlabel('Father Height')
    plt.ylabel('Birthweight')
    plt.title('Birthweight vs Father Height')
    plt.show()
