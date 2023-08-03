import seaborn as sns
import numpy as np
import pandas as pd
import streamlit as st

st.markdown("""# **this is an examplarty app**""")
kashti=sns.load_dataset("titanic")
df =kashti.sample(10)
      
st.markdown("............report................")

#rep=ProfileReport(df ,explorative=True) 

st.write(df) 

#st_profile_report(rep)
#@st.cache

#a = pd.DataFrame(
 #               np.random.rand(100, 5),
  #              columns=['a', 'b', 'c', 'd', 'e']
 #           )
#st.write(a)

def f_cor(meth_name):
    return df.corr(method=meth_name)


u_input=st.text_input("enter the name of method ")
if u_input =="pearson" or u_input=="spearman" or u_input=="kendall" :
    a= f_cor(u_input)
    st.write(a)
else:
    print("you entered wrong input ....check and try again")

st.header(" Basic Statics  ")

a=df.describe()
st.write(a)

from scipy.stats import shapiro
stat,p=shapiro(df[["age","fare","survived","sibsp"]])
st.write("stat of data", stat,"p value of age column",p)
if p >0.05:
    st.write("data is normally distributed")
else:
    st.write("not a normal distribution")




