import tkinter as tk
from tkinter import *
import random
window = Tk()
window.geometry('350x350')
window.title('Sentence Category Prediction')

entry = tk.Entry(window)
entry.pack()

def function():
    class word_category:
        GREET = "GREET"
        COMPLIMANT = "COMPLIMANT"
        PERIOD = "PERIOD"

    inputs = str(entry.get())

    train_x = ['Hi bro','Hello sir','Whatsupp',
              'Nice job','Goodjob dude','Youre nice',
              'Morning','Morning you','Good morning','Goodnight','Its evening already']
    train_y = [word_category.GREET,word_category.GREET,word_category.GREET,
              word_category.COMPLIMANT,word_category.COMPLIMANT,word_category.COMPLIMANT,
              word_category.PERIOD,word_category.PERIOD,word_category.PERIOD,word_category.PERIOD,word_category.PERIOD,]
    
    from sklearn.feature_extraction.text import CountVectorizer

    vectorizer = CountVectorizer(binary=True)
    vectors = vectorizer.fit_transform(train_x)

    from sklearn import svm

    clf_svm = svm.SVC(kernel='linear')
    clf_svm.fit(vectors,train_y)

    test_x = vectorizer.transform([inputs])
    prediction = clf_svm.predict(test_x)

    label = tk.Label(window, text=prediction)
    label.pack()

button = tk.Button(window,text='Show Category',command=function)
button.pack()

window.mainloop()
