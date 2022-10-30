import tkinter as tk

import pandas as pd
from sklearn.linear_model import LinearRegression
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root)
canvas1.create_window(200, 140, window=entry1)


def predict():
    mtext = entry1.get()


    df = pd.read_csv(r'C:/xampp1/htdocs/facedetect/markedattendance.csv')

    row, column = df.shape
    df1 = df.iloc[:, 5:column].copy()
    print(df1)

    df1['sum'] = df1[df1.columns].sum(axis=1)
    df1['avg'] = (df1['sum'] / (len(df1.columns) - 1)) * 100


    df['%'] = df1['avg']
    print(df)


    x = df.iloc[:, [0]].values
    y = df.iloc[:, column].values



    reg = LinearRegression()
    reg.fit(x, y)
    y_pred = reg.predict([[int(mtext)]])
    y_pred=y_pred.flatten()
    x=int(y_pred)
    if x<65:
        string='attendance low:'+str(x)+', please be regular to classes '
    else:
        string = 'attendance :' + str(x) + ', attendance up to date'

    label1 = tk.Label(root, text=string)
    canvas1.create_window(200, 230, window=label1)






button1 = tk.Button(text='Get predicted attendance of student', command=predict)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
