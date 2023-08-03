import streamlit as st
import joblib
import pandas as pd
from reportlab.pdfgen import canvas #provides functionality for generating PDF documents
from reportlab.lib.pagesizes import letter # predefined page sizes for creating PDF 
from pathlib import Path # directory path  
import pyarrow as pa #PyArrow provides columnar data structures
import re



#set up layout
st.set_page_config(page_title='Blood Disease Diagnose Sys',page_icon='💊',layout="wide")

# Load the models
typhoid_model = joblib.load("typhoid_model.joblib")
influenza_model = joblib.load("influenza_model.joblib")
uti_model = joblib.load("uti_model.joblib")
malaria_model1 = joblib.load("malaria_model.joblib")
dengue_model = joblib.load("dengue_model.joblib")

# Create a function to predict diseases
def predict_disease(disease, Gender, age, wbc, hgb, rbc, plt, lym, mid, grand, hct, mcv, mch, mchc):
    input_data = [[Gender, age, wbc, hgb, rbc, plt, lym, mid, grand, hct, mcv, mch, mchc]]
    
    if disease == "Typhoid":
        prediction = typhoid_model.predict(input_data)[0]
    elif disease == "Influenza":
        prediction = influenza_model.predict(input_data)[0]
    elif disease == "UTI":
        prediction = uti_model.predict(input_data)[0]
    elif disease == "Malaria":
        prediction = malaria_model1.predict(input_data)[0]
    elif disease == "Dengue":
        prediction = dengue_model.predict(input_data)[0]
    else:
        prediction = None
    
    if prediction is not None:
        result = "Positive" if prediction == 1 else "Negative"
    else:
        result = "Invalid disease selection"
    
    return result


#hide header , footer , menu


def hide_streamlit_style():
    hide_header_style = """
        <style>
        .reportview-container .main header {
            display: none;
        }
        </style>
    """

    hide_menu_style = """
        <style>
        #MainMenu {
            display: none;
        }
        </style>
    """

    hide_footer_style = """
        <style>
        .reportview-container .main footer {
            visibility: hidden;
        }
        footer { display: none; }
        </style>
    """

    st.markdown(hide_header_style, unsafe_allow_html=True)
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    st.markdown(hide_footer_style, unsafe_allow_html=True)


hide_streamlit_style()

# Define page navigation using SessionState
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

state = SessionState(page=None)
    

# Set up the Streamlit app layout for Home page
def home():
    # Add a title
    #st.title(" 🩸 Disease Prediction Web App ")
# Add content to the app
    st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a title
    st.markdown("<h1 class='title'>🩸Blood Disease Prediction Web App</h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    # Add some instructions
    st.markdown("<font color='medium turquoise'>Enter the following patient details to predict whether they have certain diseases or not.</font>", unsafe_allow_html=True)
    pattern = r'^[a-zA-Z\s]+$'

    # input fields for user data
    patient_name = st.text_input("Patient Name",key="patient_name")

    # Apply validation conditions
    if patient_name:
        # Check if the length is greater than 3 characters
        if len(patient_name) > 3:
            # Check if the name contains only letters (no numbers or special characters)
            if re.match(pattern, patient_name):
                # Valid input
                pass
            else:
                st.write("Patient Name should not contain numbers or special characters.")
        else:
            st.write("Patient Name should be longer than 3 characters.")
    patient_id = st.text_input("Patient ID")
    # Apply validation conditions
    if patient_id:
        # Check if the length is not greater than 14 digits
        if len(patient_id) <= 14:
            pass
        else:
            st.write("Patient ID should not be greater than 14 digits.")
    Refered_by = st.text_input("Refered By")
    if Refered_by:
        if len(Refered_by)>3:
            
            if re.match(pattern,Refered_by):
                pass
            else:
                st.write("This field should not contain numbers or special characters")
        else:
             st.write("length of this field should be longer than 3 character")      
    Residence_of = st.text_input("Residence of ")

    if Residence_of:
        if len(Residence_of) > 3:
            if re.match(pattern,Residence_of):
                pass
            else:
                st.write("enter valid name")
        else:
            st.write("length of this field should be longer than 3 character")
    selected_date = st.date_input("Select a date")

    if patient_name and patient_id and Refered_by and Residence_of:
            
            st.markdown("<h1 style='text-align: center; color: lightblue;'>Provide CBC Detail</h1>", unsafe_allow_html=True)


         #input field for user cbc data
            Gender = st.selectbox("Gender (1 for Male, 0 for Female)", [1, 0])
            #age = st.slider("Age  (Year.Month) ", min_value=0.0, max_value=120.0, value=30.0, step=0.01)
            age = st.text_input("Age (Year.Month)", value="30.0")
            age =float(age)
            wbc = st.number_input("White Blood Cell Count (WBC)", min_value=1.0, max_value=14.0, value=5.5, step=0.1)
            hgb = st.number_input("Hemoglobin (HGB)",min_value=1.0, max_value=20.0, value=13.0, step=.1)
            rbc = st.number_input("Red Blood Cell Count (RBC)", min_value=1.0, max_value=20.0, value=5.0, step=.1)
            plt = st.number_input("Platelet Count (PLT)",min_value=1.0, max_value=600.0, value=250.0, step=1.0)
            lym = st.number_input("Lymphocytes (LYM)",min_value=5.0, max_value=70.0, value=30.0, step=0.1)
            mid = st.number_input("Mid Cells (MID)", min_value=1.0, max_value=20.0,value=15.0, step=0.1)
            grand = st.number_input("Granulocytes (GRAND)", min_value=15.0, max_value=90.0,value=55.0, step=0.1)
            hct = st.number_input("Hematocrit (HCT)", min_value=1.0, max_value=100.0, value=44.0,step=0.1)
            mcv = st.number_input("Mean Corpuscular Volume (MCV)",  min_value=20.0, max_value=100.0, value=80.0, step=0.1)
            mch = st.number_input("Mean Corpuscular Hemoglobin (MCH)", min_value=10.0, max_value=100.0, value=26.0, step=0.1)
            mchc = st.number_input("Mean Corpuscular Hemoglobin Concentration (MCHC)", min_value=5.0, max_value=100.0, value=28.0, step=0.1)

            
        # Dropdown menu for selecting the disease
            # Display select box label with larger font size
            st.markdown("<h2 style='text-align: center; color: lightblue'>Select Your Required Disease</h2>", unsafe_allow_html=True)

            # Display select box
            selected_disease = st.selectbox("", ("Malaria","UTI","Influenza","Typhoid","Dengue"))
            # When the user clicks the 'Predict' button, make a prediction
            st.markdown("<h2 style='text-align: center; color: lightblue'>Click On Predict Button To Predict  Disease</h2>", unsafe_allow_html=True)

            if st.button("Predict"):
                # Call the predict_diseases function with user input
                results = predict_disease(selected_disease, Gender, age, wbc, hgb, rbc, plt, lym, mid, grand, hct, mcv, mch, mchc)

                # Display the predictions
                st.subheader("Prediction Results")

                # Define the table style
                table_style = """
            <style>
            table {
                color: black;
                text-align: left;
            }
            th {
                font-weight: bold;
                color: black;
                padding: 10px;
            }
            td {
                padding: 10px;
            }
            td.positive {
                background-color: yellow;
                font-weight: bold;
            }
            tr td:first-child {
                padding-right: 20px;
            }
        </style>
        """

                # Set the table style
                st.markdown(table_style, unsafe_allow_html=True)

                # Display the prediction results in a table
                table_data = []
                

                # Set the table style
                st.markdown(table_style, unsafe_allow_html=True)

                # Display the table
                # st.table(df)
                    # Create a list of dictionaries for the table data
                    # Call the predict_disease function with user input
                disease_prediction = predict_disease(selected_disease, Gender, age, wbc, hgb, rbc, plt, lym, mid, grand, hct, mcv, mch, mchc)

                    # Create a list of lists for the table data
                table_data = [["Patient Name", patient_name], ["Patient ID", patient_id],["Refered By",Refered_by],["Residence Of",Residence_of] ,[selected_disease, disease_prediction]]

                    # Create the DataFrame
                # Create the DataFrame
                # Create the DataFrame
                df = pd.DataFrame(table_data[1:], columns=table_data[0])
                csv_data = df.to_csv(index=False)  # Convert DataFrame to CSV string
                
                

                # Apply automatic fixes to make the DataFrame Arrow-compatible
                df = pa.Table.from_pandas(df)

                # Display the table
                st.table(df.to_pandas())
                st.markdown("<h3 style='text-align: center; color: lightblue'>Click on download button to download a file </h3>", unsafe_allow_html=True)


                st.download_button(label="download button",data=csv_data)        
                            

    else:
        st.warning("Please Fill The Above Required Field To Proceed Further")
    
            
#With this modification, the table will include the personal details (patient name and ID) along wi
# Set up the Streamlit app layout for Contact Us page
def contact_us():
    
    st.title("Contact Us!")
    st.markdown("Welcome to streamlit blood disease prediction web app!")
    st.write("Please email us if you have any queries about the site, advertising, or anything else.")
    st.image("https://lh3.googleusercontent.com/-BA7qy8h_v1g/YLVCWDNZdCI/AAAAAAAAALw/rsHNJWX0BK4P5CuB0ymG8QkJ9A9E8KchgCLcBGAsYHQ/w320-h87/email-us-1805514__480.webp", use_column_width=True)
    st.markdown("<i class='far fa-envelope'></i> **Email:** [qazianas123@gmail.com](mailto:qazianas123@gmail.com)", unsafe_allow_html=True)
    st.markdown("<i class='fab fa-whatsapp-square'></i> **WhatsApp:** +923235394154", unsafe_allow_html=True)
    st.header("We will revert to you as soon as possible!")
    st.markdown("Thank you for contacting us! Have a great day.")
# Set up the Streamlit app layout for About Us page
def about_us():
    st.title("Disease Prediction App - About Us")
    st.markdown("<h2>About Us!</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Welcome To <span id='W_Name1'>blood disease diagnose system</span></h3>", unsafe_allow_html=True)
    st.markdown("<p><span id='W_Name2'>blood disease diagnose system</span> is a Professional <span id='W_Type1'>diagnosis or recommendation related to blood diseases.</span> Platform. Here we will provide you only interesting content, which you will like very much. We're dedicated to providing you the best of <span id='W_Type2'>diagnosis or recommendation related to blood diseases.</span>, with a focus on dependability .<br><br> <span id='W_Spec'>A blood disease diagnosis system is a type of web application or website that allows users to input their symptoms, medical history, and other relevant information in order to receive a potential diagnosis or recommendation related to blood diseases. <br><br>Our system typically utilize algorithms and medical knowledge to analyze the provided information and generate results based on known patterns and correlations</span>. We're working to turn our passion for <span id='W_Type3'>diagnosis or recommendation related to blood diseases.</span> into a booming <a href='https://www.blogearns.com/2021/05/free-about-us-page-generator.html' rel='do-follow' style='color: inherit; text-decoration: none;'>online website</a>. We hope you enjoy our <span id='W_Type4'>diagnosis or recommendation related to blood diseases.</span> as much as we enjoy offering them to you.</p>", unsafe_allow_html=True)
    st.markdown("I will keep posting more important posts on my Website for all of you. Please give your support and love.")
    st.markdown("<p style='font-weight: bold; text-align: center;'>Thanks For Visiting Our Site<br><br><span style='color: blue; font-size: 16px; font-weight: bold; text-align: center;'>Have a nice day!</span></p>", unsafe_allow_html=True)

# Define the main app function
def app():
    pages = {
        "🏘️Home": home,
        "📞Contact Us": contact_us,
        "📝About Us": about_us
    }

    st.sidebar.title("BDD System")
    page = st.sidebar.radio("Main Pages", tuple(pages.keys()))
    

    # Set the current page in SessionState
    state.page = page

    # Run the current page function
    pages[state.page]()

if __name__ == '__main__':
    try:
        state = st.session_state
        app()  # Call the app function
    except Exception as e:
        print(f"An error occurred: {e}")

