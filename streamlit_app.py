#The Rapid Reach Arm.com
from streamlit_js_eval import streamlit_js_eval
import streamlit as st
import pandas as pd
from PIL import Image
from streamlit.components.v1 import html
import base64
from pathlib import Path
import streamlit as st
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
            font-size: 32px;
        }
    }
    @media (min-width: 601px) {
        .responsive-text {
            font-size: 24px;
        }
    }
    .stApp {
        background-color: #f8f9fa;
    }

    /* Sticky container for header + tabs */
    .sticky-tabs {
        position: sticky;
        top: 48px;
        z-index: 999;
        background-color: #00ff88;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        margin-bottom: 10px;
        width: 100%;
    }

    RRLogo = Image.open('RapidReachLogo.png')
    st.image(RRLogo, caption='RapidReach: Patent Pending', use_container_width=True, width=100)
   
    
    /* Header styling inside the sticky container */
    .custom-header {
        background-color: ffffff;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        top: 0px;
        color: white;
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
        background-color: black !important;
        padding: 12px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        z-index: 1001;
    }

    div[data-baseweb="tab-list"]::after {
    content: "";
    display: block;
    height: 60px;
    }

    /* Individual tabs */
    button[data-baseweb="tab"] {
        color: white !important;
        background-color: black !important;
        font-size: 16px;
        padding: 10px 20px;
    }

    /* Hover effect */
    button[data-baseweb="tab"]:hover {
        background-color: #007bff !important;
    }

    /* Selected tab */
    button[data-baseweb="tab"][aria-selected="true"] {
        border-bottom: 3px solid #00dd44 !important;
        color: #007bff !important;
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

tab1, tab2, tab3, tab4 = st.tabs(["About the Device", "About the Team", "Market Size", "Contact Us"])
with tab1:
    st.markdown('<div class="responsive-text"><p style="color: #212529">' \
    ' The RapidReach <sup><small>Patent Pending</small></sup></p></div>', unsafe_allow_html=True)
    st.write()
    st.markdown('<p style="font-size:20px; color: #212529"> Device in Use </p>', unsafe_allow_html=True)
    video_path = Path("General Demonstration.mp4")
    video_bytes = video_path.read_bytes()
    encoded = base64.b64encode(video_bytes).decode()
    if (screen_height is not None and screen_width is not None):
        width_sc = (int(700/1440 * screen_width))
        height_sc = (int(332/900 * screen_height))
        video_html = f"""
        <div style="display: flex; flex-direction: column; align-items: flex-start; margin-top: 12px;">
        <div class="responsive-video">
            <video width={width_sc} autoplay muted loop controls>
            <source src="data:video/mp4;base64,{encoded}" type="video/mp4">
            Your browser does not support the video tag.
            </video>
        </div>
        <div class="responsive-text">
            <p style="margin-top: 8px; color: #212529;">
            The RapidReach Surgical Retractor Arm is the first ever
            rapidly adjustable one-handed surgical retractor arm.
            </p>
        </div>
        </div>
        """
        html(video_html, height=height_sc)
    else:
        st.warning("Waiting for screen dimensions... Please reload if nothing appears.")
    st.markdown('<div class="responsive-text"> <p style="color: #212529;">VOC Interview Feedback on Previous Products</p></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<p style="font-size:20px; color: #212529;">\"After doing something a lot you work around the limitations and stop thinking about it.\"</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529;"> — Dr. Elwood, MD </p>', unsafe_allow_html=True)
    with col2:
        st.markdown('<p style="font-size:20px; color: #212529;">\"Can take 5, 6, 7 hours which can add to the frustration just trying to position the retractor perfectly.\"</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529;"> — Dr. Kamdar, MD </p>', unsafe_allow_html=True)
    with col3:
        st.markdown('<p style="font-size:20px; color: #212529;">\"Some retractors slip and you must keep moving around.\"</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529;"> — Dr. Scarborough, MD </p>', unsafe_allow_html=True)

    st.markdown('<p style="font-size:32px; color: #212529;"> User Feedback </p>', unsafe_allow_html=True)
    col4, col5 = st.columns(2)
    with col4:
        st.markdown(f'<p style="font-size:20px; color: #212529;"> \"This is better than what\'s out there.\" </p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529;"> — Charles Hower, MS3 </p>', unsafe_allow_html=True)
    with col5:
        st.markdown(f'<p style="font-size:20px; color: #212529;"> \"I\'ve never seen anything like this.\" </p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:14px; color: #212529;"> — Roberto Soriano, MD </p>', unsafe_allow_html=True)


Michael = Image.open('Michael.jpg')
David = Image.open('David.png')
John = Image.open('John.jpg')
Stefano = Image.open('Stefano.jpg')
Rohan = Image.open('Rohan.jpg')

with tab2:
    st.markdown('<p style="font-size:32px; color:#212529;"> About the Team </p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(Michael, caption='Michael Pavelchek', use_container_width=True, width=200)
        st.markdown('<p style="font-size:14px; color:#212529;"> Michael graduated with a BS in Biomedical Engineering from Georgia Tech with a minor in Robotics in Spring 2025. \
        He will begin the MBID program at Georgia Tech in Fall 2025. </p>', unsafe_allow_html=True)
    with col2:
        st.image(David, caption='Dawei Liu', use_container_width=True, width=200)
        st.markdown('<p style="font-size:14px; color:#212529;"> Dawei is an aspiring physician-scientist and graduated from Georgia Tech with a BS in Biomedical Engineering. He plans to become a Research Technician at the Cleveland Clinic. </p>', unsafe_allow_html=True)
    with col3:
        st.image(John, caption='John Cutrone', use_container_width=True, width=200)
        st.markdown('<p style="font-size:14px; color:#212529;"> John has recently graduated with a BS in Biomedical Engineering with the Research Option from Georgia Tech. \
        He is currently studying in the Johns Hopkins CBID Master’s Program. </p>', unsafe_allow_html=True)

    col4, col5 = st.columns(2)
    with col4:
        st.image(Stefano, caption='Stefano Poma', use_container_width=True, width=150)
        st.markdown('<p style="font-size:14px; color:#212529;"> Stefano has recently graduated with a BS in Biomedical Engineering from Georgia Tech with a minor in Artificial Intelligence. </p>', unsafe_allow_html=True)
    with col5:
        st.image(Rohan, caption='Rohan Ravula', use_container_width=True, width=150)
        st.markdown('<p style="font-size:14px; color:#212529;"> Rohan just graduated with a BS in Biomedical Engineering with a minor in Supply Chain from Georgia Tech. \
         He will begin the MBID program at Georgia Tech in Fall 2025. </p>', unsafe_allow_html=True)
with tab3:
    st.markdown('<div class="responsive-text"><p style="color:#212529;"> Market Impact</p></div>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:14px; color: #212529;"> More than 30 million ENT and plastic surgeries occur'
    ' in the US annually, many of which rely on surgical retractors to maintain visibility, preserve sterility,'
    'and minimize tissue damage. However, current surgical retractor holders typically rely on screw based locking' \
    ' mechanisms that take up to 2 minutes to adjust making them impractical as ENT and plastic surgeries usually require' \
    ' retractor repositioning once every 10 minutes. This forces OR staff to manually hold and adjust surgical retractors'
    ' for the full 5-8 hour duration of the average ENT and plastic surgery.</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:14px; color: #212529;"> This leads to: </p>', unsafe_allow_html=True)
    st.markdown("""<ul style="font-size:14px; color: #212529;">
    <li>Slippage of the retractor</li>
    <li>Physical strain on staff</li>
    <li>Diverted Attention from critical surgical tasks</li>
    <li>Increased risk to both patient safety and surgical outcomes</li>
   </ul>""", unsafe_allow_html=True)
    st.markdown('<p style="font-size:14px; color: #212529;"> This is not a minor issue; retractor-related slippage injuries' \
    ' have been estimated to occur in up to 30% of all surgeries.</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size:14px; color: #212529;"> The Rapid Reach Surgical Retractor Arm addresses these issues' \
    ' by enabling one-handed, rapid adjustments in 15 seconds, a reduction of over 88% in adjustment time. This innovation' \
    ' can recover up to 50 minutes of surgery, potentially saving millions of hours and billions of dollars for hospitals' \
    ' annually across the US, while improving surgeon workflow and reducing OR staff and patient injuries.</p>',
      unsafe_allow_html=True)
with tab4:
    st.markdown('<div class="responsive-text"><p style="font-size: 32px; color: #212529;">Contact Us</p></div>', unsafe_allow_html=True)
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

