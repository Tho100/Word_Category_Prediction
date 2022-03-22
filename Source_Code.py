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
        QUESTION = "QUESTION"
    inputs = str(entry.get())

    train_x = ['Hi bro','Hello sir','Whatsupp',
              'Nice job','Goodjob dude','Youre nice','You did good',
              'Morning','Morning you','Good morning','Goodnight','Its evening already',
              'Why','Are you fine bro','Where is',"Why cant't",'Is that a','What','What do you']
    train_y = [word_category.GREET,word_category.GREET,word_category.GREET,
              word_category.COMPLIMANT,word_category.COMPLIMANT,word_category.COMPLIMANT,word_category.COMPLIMANT,
              word_category.PERIOD,word_category.PERIOD,word_category.PERIOD,word_category.PERIOD,word_category.PERIOD,
              word_category.QUESTION,word_category.QUESTION,word_category.QUESTION,word_category.QUESTION,word_category.QUESTION,word_category.QUESTION,word_category.QUESTION]
    
    from sklearn.feature_extraction.text import CountVectorizer

    vectorizer = CountVectorizer(binary=True)
    vectors = vectorizer.fit_transform(train_x)

    from sklearn import svm

    clf_svm = svm.SVC(kernel='linear')
    clf_svm.fit(vectors,train_y)

    test_x = vectorizer.transform([inputs])
    prediction = clf_svm.predict(test_x)

    function.label = tk.Label(window, text=prediction)
    function.label.pack()

def clear_func():
    entry.delete(0,'end')   
    function.label.pack_forget()
    
button = tk.Button(window,text='Show Category',command=function)
button.pack()

clear = tk.Button(window, text='Clear',command=clear_func)
clear.pack() 

window.mainloop()
