import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **The EDA App**
This is the **EDA App** created in Streamlit using the **pandas-profiling** library.
---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file]""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        #pr = ProfileReport(df, explorative=True)
        #st.header('**Input DataFrame**')
        #st.write(df)
        #st.write('---')
        #st.header('**Pandas Profiling Report**')
        #st_profile_report(pr)
        
        
        # data=df.sample(n=10)
        #data = pd.DataFrame(data) 
        #st.write(data)
        #st.write("pearson correlation")
        #st.write(data.corr(method="pearson")) \

        import seaborn as sns
        kashti=sns.load_dataset("titanic")
        df =kashti.sample(10)
               
        def f_cor(meth_name):
            return df.corr(method=meth_name)
        
    
        u_input=st.text_input("enter the name of method ")
        if u_input =="pearson" or u_input=="spearman" or u_input=="kendall" :
            a= f_cor(u_input)
            st.write(a)
        else:
            print("you entered wrong input ....check and try again")
            """    list= ['pearson', 'spearman',"kendall"]
                st.write(list)
                a=st.text_input('First name')
                st.write(a)
        """
    """ 
        if st.text_input=="pearson":  

            print("pearson method applied")
            st.write(data.corr(method="pearson"))
                


        elif st.text_input=="spearman":

            st.write(data.corr(method="spearman"))
                

        elif st.text_input=="kendall":

            st.write(data.corr(method="kendall"))
                
        else:

             print("some error")


    """
            




