#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def fhjfhj():
    return render_template('sum.html')
@app.route('/info',methods=['POST'])
def fgkjgkj():
    if(request.method=='POST'):
        n1=int(request.form['a'])
        n2=int(request.form['b'])
        total=n1+n2
        final='Final Sum is {}'.format(total)
        return render_template('sum.html',afzal=final)
if __name__=='__main__':
    app.run()

