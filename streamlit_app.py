#The Rapid Reach Arm.com
from streamlit_js_eval import streamlit_js_eval
import streamlit as st
import pandas as pd
from PIL import Image
from streamlit.components.v1 import html
import base64
from pathlib import Path
import base64
from streamlit.components.v1 import html
from PIL import Image
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
from email.message import EmailMessage

st.set_page_config(layout="wide")
st.markdown("""
<style>

    @media (max-width: 600px) {
        .responsive-video {
                display: flex;
                justify-content: center;
                margin-top: 12px;
                margin-bottom: 12px;
        }
    }
    @media (min-width: 601px) {
        .responsive-video video {
            width: 100%;
            max-width: 100%;
            height: auto;
            object-fit: contain;
        }
    }
    
    @media (max-width: 600px) {
        .responsive-text {
            font-size: 24px;
        }
    }
    @media (max-width: 600px) {
        .responsive-text2 {
            font-size: 16px;
        }
    }
    @media (max-width: 600px) {
        .responsive-text3 {
            font-size: 16px;
        }
    }

    @media (min-width: 601px) {
        .responsive-text {
            font-size: 32px;
        }
    }
    @media (min-width: 601px) {
        .responsive-text2 {
            font-size: 24px;
        }
    }
    @media (min-width: 601px) {
        .responsive-text3 {
            font-size: 20px;
        }
    }
    
    .stApp {
        background-color: #ffffff;
    }

    /* Sticky container for header + tabs */
    .sticky-tabs {
        position: sticky;
        top: 48px;
        z-index: 999;
        background-color: #1c4574;
        box-shadow: 0 2px 10px rgba(35,134,147,255));
        margin-bottom: 10px;
        text-align: center;
        width: 100%;
    }

        
    /* Header styling inside the sticky container */
    .custom-header {
        background-color: #287793;
        box-shadow: 0 2px 10px rgba(35,134,147,255);
        top: 0px;
        color: #287793;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        width: 100%;
        
    }

    /* Tab list styling */
    div[data-baseweb="tab-list"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        position: fixed !important;
        top: 48px;
        left: 0;
        width: 100vw !important;
        background-color: #287793 !important;
        padding: 12px 0;
        box-shadow: 0 2px 10px rgba(35,134,147,255);
        z-index: 1001;
    }

    div[data-baseweb="tab-list"]::after {
    content: "";
    display: block;
    height: 60px;
    }

    /* Individual tabs */
    button[data-baseweb="tab"] {
        color: #379991 !important;
        background-color: white !important;
        font-size: 16px;
        padding: 10px 20px;
    }

    /* Hover effect */
    button[data-baseweb="tab"]:hover {
        background-color: white !important;
    }

    /* Selected tab */
    button[data-baseweb="tab"][aria-selected="true"] {
        border-bottom: 3px solid #379991 !important;
        color: #379991 !important;
    }

    /* Add some padding below sticky container so content not hidden */
    .sticky-Tabs + div {
        padding-top: 60px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

screen_width = streamlit_js_eval(js_expressions='screen.width', key='SCR')
screen_height = streamlit_js_eval(js_expressions='screen.height', key='SCR1')
print(f"screen_width is: {screen_width}")
print(f"screen_height is: {screen_height}")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["About the Device", "About the Team", "Market Impact", "Clinical Problem", "Contact Us"])
with tab1: 
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("RapidReachLogoT.png", caption='RapidReach: Patent Pending', use_container_width=False, width=150)
    with col2:
        st.markdown('<div class="responsive-text"><p style="color: #227e94; text-align: center;">' \
    '<strong>About The RapidReach Arm<sup style="font-size: 0.4em;">Patent Pending</small</sup></strong></p></div>', unsafe_allow_html=True)
    with col3:
        st.image('Figure 1_ Labeled RapidReach Arm.jpg', caption='Rapid Reach Arm Side View', use_container_width=False, width=150)
    st.write()
    st.markdown('<div class="responsive-text2"><p style="color: #379991; text-align: center;"> Device In Use </p></div>', unsafe_allow_html=True)
    video_path = Path("General Demonstration.mp4")
    video_bytes = video_path.read_bytes()
    encoded = base64.b64encode(video_bytes).decode()
    if (screen_height is not None and screen_width is not None):
        width_sc = (int(700/1440 * screen_width))
        height_sc = (int(332/900 * screen_height))
        video_html = f"""
        <div style="display: flex; flex-direction: column; align-items: center; margin-top: 12px;">
        <div class="responsive-video">
            <video width={width_sc} autoplay muted loop controls>
            <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
            Your browser does not support the video tag.
            </video>
        </div>
        <div class="responsive-text">
            <p style="margin-top: 8px; color: #212529; text-align: center;">
        The RapidReach Surgical Retractor Arm is the first ever
        rapidly adjustable one-handed surgical retractor arm.
        </p>
        </div>
        </div>
        """
        html(video_html, height=height_sc)
    else:
        st.warning("Waiting for screen dimensions... Please reload if nothing appears.")
    st.markdown('<div class="responsive-text2"> <p style="color: #379991; text-align: center;">VOC Interview Feedback on Previous Products</p></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="responsive-text3"><p style="color: #212529; text-align: center;">\"After doing something a lot you work around the limitations and stop thinking about it.\"</p></div>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529; text-align: center;"> — Dr. Elwood, MD at Emory Healthcare Network</p>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="responsive-text3"><p style="color: #212529; text-align: center;">\"Can take 5, 6, 7 hours which can add to the frustration just trying to position the retractor perfectly.\"</p></div>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529; text-align: center;"> — Dr. Kamdar, MD at Emory Healthcare Network</p>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="responsive-text3"><p style="color: #212529; text-align: center;">\"Some retractors slip and you must keep moving around.\"</p></div>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529; text-align: center;"> — Dr. Scarborough, MD at Emory Healthcare Network</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="responsive-text2"><p style="color: #379991; text-align: center;">User Feedback</p></div>', unsafe_allow_html=True)
    col4, col5 = st.columns(2)
    with col4:
        st.markdown(f'<div class="responsive-text3"><p style="color: #212529; text-align: center;"> \"This is better than what\'s out there.\" </p></div>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529; text-align: center;"> — Charles Hower, MS3</p>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<div class="responsive-text3"><p style="color: #212529; text-align: center;"> \"I\'ve never seen anything like this.\" </p></div>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529; text-align: center;"> — Roberto Soriano, MD</p>', unsafe_allow_html=True)


Michael = Image.open('Michael.jpg')
David = Image.open('David.png')
John = Image.open('John.jpg')
Stefano = Image.open('Stefano.jpg')
Rohan = Image.open('Rohan.jpg')

with tab2:
    st.markdown('<div class="responsive-text"><p style="color:#379991; text-align: center;"> About the Team </p></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(Michael, caption='Michael Pavelchek', use_container_width=True, width=150)
        st.markdown('<p style="font-size:16px; color:#212529; text-align: center;"> Michael graduated with a BS in Biomedical Engineering from Georgia Tech with a minor in Robotics in Spring 2025. \
        He will begin the MBID program at Georgia Tech in Fall 2025. </p>', unsafe_allow_html=True)
    with col2:
        st.image(David, caption='Dawei Liu', use_container_width=True, width=150)
        st.markdown('<p style="font-size:16px; color:#212529; text-align: center;"> Dawei is an aspiring physician-scientist and graduated from Georgia Tech with a BS in Biomedical Engineering. He plans to become a Research Technician at the Cleveland Clinic. </p>', unsafe_allow_html=True)
    with col3:
        st.image(John, caption='John Cutrone', use_container_width=True, width=150)
        st.markdown('<p style="font-size:16px; color:#212529; text-align: center;"> John has recently graduated with a BS in Biomedical Engineering with the Research Option from Georgia Tech. \
        He is currently studying in the Johns Hopkins CBID Master’s Program. </p>', unsafe_allow_html=True)

    col4, col5 = st.columns([1,3])
    with col4:
        st.image(Stefano, caption='Stefano Poma', use_container_width=True, width=150)
        st.markdown('<p style="font-size:16px; color:#212529; text-align: center;"> Stefano has recently graduated with a BS in Biomedical Engineering from Georgia Tech with a minor in Artificial Intelligence. He will begin his PhD in Neuroscience and Neurotechnology at Georgia Tech in Fall 2025. </p>', unsafe_allow_html=True)
    with col5:
        st.image(Rohan, caption='Rohan Ravula', use_container_width=True, width=150)
        st.markdown('<p style="font-size:16px; color:#212529; text-align: center;"> Rohan just graduated with a BS in Biomedical Engineering with a minor in Supply Chain from Georgia Tech. \
         He will begin the MS BMED program at Georgia Tech in Fall 2025. </p>', unsafe_allow_html=True)
with tab3:
    st.markdown('<div class="responsive-text"><p style="color:#212529; text-align: center;"><strong>Market Impact</strong></p></div>', unsafe_allow_html=True)
    st.image("TAM_SAM.jpg", caption = "TAM and SAM for Surgical Retractor Arm", use_container_width=True)
    st.markdown('<p style="font-size:16px; color:#212529; text-align: center;">Here are the listed Total Addressable Market (TAM) and Serviceable Addressable Market (SAM) for surgical retractor arms.</p>', unsafe_allow_html = True)
    st.markdown('<p style="font-size:16px; color:#212529; text-align: center;">TAM was calculated as the maximum number of ORs that could be in use at any given moment in all hospitals and ambulatory service centers across the US. This maximum number was then multiplied by the price of a competing predicate device of $5,500.</p>', unsafe_allow_html = True)
    st.markdown('<p style="font-size:16px; color:#212529; text-align: center;">SAM instead was calculated similarly to TAM but on the global stage using the maximum number of ORs in all hospitals and ambulatory service centers across the entire world times the cost of the predicate device.</p>', unsafe_allow_html = True)
with tab4:
    st.markdown('<div class="responsive-text"><p style="color:#212529; text-align: center;"><strong>Clinical Importance</strong></p></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:16px; color: #212529; justify-content: center; text-align: left;"> More than <strong>30 million</strong> ENT and Plastic surgeries occur'
    ' in the US annually, many of which rely on surgical retractors to maintain visibility, preserve sterility,'
    'and minimize tissue damage.</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:16px; color:#212529; justify-content: center; text-align: left;"> However, current surgical retractor holders typically rely on screw based locking' \
    ' mechanisms that take up to <strong>2 minutes</strong> to adjust making them impractical as ENT and Plastic surgeries usually require' \
    ' retractor repositioning once every <strong>10 minutes</strong>. This forces OR staff to manually hold and adjust surgical retractors'
    ' for the full <strong>5-8 hour duration</strong> of the average ENT and Plastic surgery.</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:16px; color: #212529; justify-content: center; text-align: left;"> This leads to: </p>', unsafe_allow_html=True)
    st.markdown("""<ul style="font-size:16px; color: #212529; justify-content: center; text-align: left;">
    <li>Slippage of the retractor</li>
    <li>Physical strain on staff</li>
    <li>Diverted Attention from critical surgical tasks</li>
    <li>Increased risk to both patient safety and surgical outcomes</li>
   </ul>""", unsafe_allow_html=True)
    st.markdown('<p style="font-size:16px; color: #212529; justify-content: center; text-align: left;"> This is not a minor issue; retractor-related slippage injuries' \
    ' have been estimated to occur in up to <strong>30%</strong> of all surgeries.</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:16px; color: #212529; justify-content: center; text-align: left; max-width: 1000px"> The Rapid Reach Surgical Retractor Arm addresses these issues' \
    ' by enabling one-handed, rapid adjustments in 15 seconds, a reduction of over <strong>88%</strong> in adjustment time.</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:16px; color: #212529; justify-content: center; text-align: left; max-width: 1000px;"> This innovation' \
    ' can recover up to <strong>50 minutes</strong> of surgery, potentially <strong>saving millions of hours and billions of dollars</strong> for hospitals' \
    ' annually across the US, while improving surgeon workflow and reducing OR staff and patient injuries.</p>',
      unsafe_allow_html=True)
with tab5:
    col1, col2 = st.columns(2)
    with col1:
        st.image("RapidReachLogoT.png", caption='RapidReach: Patent Pending', use_container_width=False, width=150)
    with col2:
        st.markdown('<div class="responsive-text"><p style="color: #212529;"><strong>Contact Us</strong></p></div>', unsafe_allow_html=True)
    with st.form("Email Form"):
        st.markdown('<div style="margin-bottom: -8px;"><label style="color:#212529; font-size:16px;">Subject</label></div>',unsafe_allow_html=True)
        subject = st.text_input(label=" ", placeholder="Please enter the subject line for your email.")
        st.markdown('<div style="margin-bottom: -8px;"><label style="color:#212529; font-size:16px;">Name</label></div>', unsafe_allow_html=True)
        fullName = st.text_input(label=" ", placeholder="Please enter your full name here for when we reach out.")
        st.markdown('<div style=margin-bottom: -8px;"><label style="color:#212529; font-size:16px;">Email</label></div>', unsafe_allow_html=True)
        email = st.text_input(label=" ", placeholder="Please enter your email address so that we can reach out.")
        st.markdown('<div style=margin-bottom: -8px"><label style="color:#212529; font-size:16px">Info</label></div>', unsafe_allow_html=True)
        text = st.text_area(label=" ", placeholder="Please enter any comments or questions that you have here.")
        uploaded_file = st.file_uploader("Attachment", type=["pdf", "docx", "png", "jpg", "tiff", "mp4"])
        submit_res = st.form_submit_button(label="Send")
    if submit_res:
        if subject and fullName and email and text:
            msg = EmailMessage()
            msg["Subject"] = f"New Contact Submission Form from {fullName}"
            msg["From"] = st.secrets['email']['address']
            msg["To"] = st.secrets['email']['address']
            msg.set_content(f"From: {fullName} <{email}>\n\nMessage:\n{text}")

            if uploaded_file:
                file_data = uploaded_file.read()
                file_name = uploaded_file.name
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            try:
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(st.secrets['email']['address'], st.secrets['email']['password'])
                    smtp.send_message(msg)
                st.success("Your message has been sent!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill out all required fields.")

