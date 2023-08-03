import streamlit as st
import joblib
import pandas as pd
import re

st.set_page_config(page_title='Blood Disease Diagnose Sys', page_icon='💊', layout="centered")

# Load the models
typhoid_model = joblib.load("typhoid_model.joblib")
influenza_model = joblib.load("influenza_model.joblib")
uti_model = joblib.load("uti_model.joblib")
malaria_model = joblib.load("malaria_model.joblib")
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
        prediction = malaria_model.predict(input_data)[0]
    elif disease == "Dengue":
        prediction = dengue_model.predict(input_data)[0]
    else:
        prediction = None

    if prediction is not None:
        result = "Positive" if prediction == 1 else "Negative"
    else:
        result = "Invalid disease selection"

    return result


# hide header, footer, menu
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


state = SessionState(page=None, user_inputs={})


# Set up the Streamlit app layout for Home page
# Set up the Streamlit app layout for Home page
def home():
    # Add a title
    st.title("🏥 Disease Prediction Web App")

    # Add a subheader
    st.subheader("Provide patient information and select the disease to predict")

    # Create input fields for patient information
    patient_name = st.text_input("Patient Name")
    patient_id = st.text_input("Patient ID")
    Refered_by = st.text_input("Refered By")
    Residence_of = st.text_input("Residence Of")

    # Create input fields for disease prediction
    Gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age",step=1)

    st.subheader("Enter Blood Test Results")

    # Create input fields for blood test results
    wbc = st.number_input("White Blood Cell Count (WBC)", step=1)
    hgb = st.number_input("Hemoglobin (HGB)", step=1)
    rbc = st.number_input("Red Blood Cell Count (RBC)", step=1)
    plt = st.number_input("Platelet Count (PLT)", step=1)
    lym = st.number_input("Lymphocytes (LYM)", step=1)
    mid = st.number_input("Mid Cells (MID)", step=1)
    grand = st.number_input("Granulocytes (GRAND)", step=1)
    hct = st.number_input("Hematocrit (HCT)", step=1)
    mcv = st.number_input("Mean Corpuscular Volume (MCV)", step=1)
    mch = st.number_input("Mean Corpuscular Hemoglobin (MCH)", step=1)
    mchc = st.number_input("Mean Corpuscular Hemoglobin Concentration (MCHC)", step=1)

    # Check if all the input fields are filled
    if (
        patient_name
        and patient_id
        and Refered_by
        and Residence_of
        and Gender
        and age
        and wbc
        and hgb
        and rbc
        and plt
        and lym
        and mid
        and grand
        and hct
        and mcv
        and mch
        and mchc
    ):
        # Add a "Proceed Further" button
        if st.button("Proceed Further"):
            # Store user inputs in the state variable
            state.user_inputs = {
                "patient_name": patient_name,
                "patient_id": patient_id,
                "Refered_by": Refered_by,
                "Residence_of": Residence_of,
                "Gender": Gender,
                "age": age,
                "wbc": wbc,
                "hgb": hgb,
                "rbc": rbc,
                "plt": plt,
                "lym": lym,
                "mid": mid,
                "grand": grand,
                "hct": hct,
                "mcv": mcv,
                "mch": mch,
                "mchc": mchc,
            }
            state.page = "🏠Prediction"
        else:
            st.warning("Please click on 'Proceed Further' to continue.")
    else:
        st.warning("Please fill in all the required fields.")

    return


# Set up the Streamlit app layout for Prediction page
# Set up the Streamlit app layout for Prediction page
    def prediction():
        # Add a title
        st.title("Prediction Results")

        # Define the table style
        table_style = """
            <style>
            table {
                color: black;
                text-align: left;
            }
            th {
                background-color: #D033FF;
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

        # Retrieve user inputs from SessionState
        user_inputs = state.user_inputs

        # Call the predict_disease function with user input
        disease_prediction = predict_disease(
            user_inputs["selected_disease"],
            user_inputs["Gender"],
            user_inputs["age"],
            user_inputs["wbc"],
            user_inputs["hgb"],
            user_inputs["rbc"],
            user_inputs["plt"],
            user_inputs["lym"],
            user_inputs["mid"],
            user_inputs["grand"],
            user_inputs["hct"],
            user_inputs["mcv"],
            user_inputs["mch"],
            user_inputs["mchc"],
        )

        # Create a list of lists for the prediction results table
        prediction_data = [
            ["Patient Name", user_inputs["patient_name"]],
            ["Patient ID", user_inputs["patient_id"]],
            ["Refered By", user_inputs["Refered_by"]],
            ["Residence Of", user_inputs["Residence_of"]],
            ["Gender", user_inputs["Gender"]],
            ["Age", user_inputs["age"]],
            ["White Blood Cell Count (WBC)", user_inputs["wbc"]],
            ["Hemoglobin (HGB)", user_inputs["hgb"]],
            ["Red Blood Cell Count (RBC)", user_inputs["rbc"]],
            ["Platelet Count (PLT)", user_inputs["plt"]],
            ["Lymphocytes (LYM)", user_inputs["lym"]],
            ["Mid Cells (MID)", user_inputs["mid"]],
            ["Granulocytes (GRAND)", user_inputs["grand"]],
            ["Hematocrit (HCT)", user_inputs["hct"]],
            ["Mean Corpuscular Volume (MCV)", user_inputs["mcv"]],
            ["Mean Corpuscular Hemoglobin (MCH)", user_inputs["mch"]],
            ["Mean Corpuscular Hemoglobin Concentration (MCHC)", user_inputs["mchc"]],
            ["Predicted Disease", user_inputs["selected_disease"]],
            ["Prediction Result", disease_prediction],
        ]

        # Create a DataFrame from the prediction data
        df_prediction = pd.DataFrame(prediction_data, columns=["Attribute", "Value"])

        # Highlight the predicted disease row in the table
        if disease_prediction == "Positive":
            df_prediction.loc[df_prediction["Attribute"] == "Prediction Result", "Value"] = '<span class="positive">' + disease_prediction + "</span>"

        # Display the prediction results table
        st.table(df_prediction.to_html(escape=False, index=False), unsafe_allow_html=True)

        # Update the state.page variable to "🏠Prediction"
        state.page = "🏠Prediction"

        return

def contact_us():
    st.header("Contact Us")
    st.subheader("Get in touch with us")
    st.write("For any inquiries or feedback, please use the following contact information:")
    st.write("- Email: example@example.com")
    st.write("- Phone: +1 123-456-7890")
    st.write("- Address: 123 Main Street, City, Country")

def about_us():
    st.header("About Us")
    st.subheader("Learn more about our organization")
    st.write("We are a team dedicated to providing innovative solutions and exceptional user experiences.")
    st.write("Our mission is to make a positive impact through technology and empower individuals in their daily lives.")
    st.write("Feel free to reach out to us for more information or partnership opportunities.")


# Main app
if state.page is None:
    state.page = "🏘️Home"

if state.page == "🏘️Home":
    home()
elif state.page == "🏠Prediction":
    prediction()
elif state.page == "📞Contact Us":
    contact_us()
elif state.page == "ℹ️About Us":
    about_us()
else:
    st.error("Invalid page state")
