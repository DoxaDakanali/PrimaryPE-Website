import streamlit as st
from PIL import Image
from annotated_text import annotated_text
import requests
from streamlit_lottie import st_lottie
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

 # ---- LOAD ASSETS ----
lottie_python = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_t9h3vpwn.json")
img_Head = Image.open("IMAGES/head1.png")
img_Head = img_Head.resize((1080, 150), Image.LANCZOS)
st.image(img_Head)
st.write("---")
img_doxa = Image.open("IMAGES/doxa.png")
img_doxa = img_doxa.resize((350, 350), Image.LANCZOS)
img_Pre = Image.open("IMAGES/pe-for-preschool-activities-800x600.jpg")
img_Pre = img_Pre.resize((570, 400), Image.LANCZOS)

  # -----IF I WANT TO RUN A VIDEO FROM PC---
#video_file = open('IMAGES/promo.mp4', 'rb', 2)
#video_bytes = video_file.read()



with st.container():
    left_column, right_column = st.columns(2)
    with right_column:
        st.image(img_doxa)
    with left_column:
        st.write("######")


        st.header('Why Primary P.E?')
        st.subheader('Simplify Your Life as a PE Teacher')
        import streamlit as st

        annotated_text(

            ("Are you feeling overwhelmed? "
             "Do you struggle to find the time to plan engaging activities and games?"
             "Look no further than Primary PE - the ultimate solution for busy physical education instructors."
             "Our online platform is designed to support both aspiring and experienced teachers in delivering "
             "outstanding physical education experiences. "
             "With Primary PE, you gain access to a wealth of valuable resources and information. "
             "Our comprehensive blog offers practical tools and strategies for building and maintaining "
             "a top-notch physical education program. "
             "Additionally, we provide many meticulously crafted resources, "
             "including PE activities, games, field day materials, templates, visuals, posters, sign packages, "
             "PowerPoint presentations, and much more! "
             "Take control of your physical education curriculum and join Primary PE today. Let us empower you "
             "to create engaging and impactful learning environments for your students!", " PRIMARY  P.E.",
             "#0B1520", "#3290a6")
        )
st.write("######")
st.write("######")
st.write("######")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.image(img_Pre)
    with right_column:
         st.write("######")
         st.write("######")
         st.subheader("About Doxa Dakanali")

         annotated_text(

            ("DOXA DAKANALI , creator of Primary PE, "
            "is a physical education teacher with more than 25 years teaching experience. Doxa is committed to "
            "advancing  and enriching physical education  worldwide , both within schools and communities. This "
            "website and community serve as a central hub for physical education teachers, providing them with "
            "inspiration, resources, and support throughout their journey in teaching physical education."
            "With a vision in mind, she created Primary P.E. to establish a website and community dedicated to PE "
            "resources. The goal is to guide every teacher, regardless of their experience, through well-structured"
            "units , lessons , and mindsets that will assist them in enhancing their teaching skills. The aim is to"
            " equip teachers with the necessary resources for success, enabling them to continually grow and become"
            " better educators for their students.The ultimate objective is to inspire teachers to inspire their "
            "students.With a deep passion for children, the mission is to support physical education teachers in a"
            " manner that empowers students to reach their full potential. Recognizing the exceptional opportunity"
            " that physical education offers, it aims to positively impact students' lives by promoting mental"
            " health, physical well - being, and social - emotional development.", " ", "#0B1520", "#3290a6")
            )
st.write("######")
st.write("######")
st.write("######")
st.write("######")
with st.container():
    left_column, right_column = st.columns([1, 2])
    with right_column:
        st.write("######")
        st.write("######")
        #st.video(video_bytes)
        st.video("https://www.youtube.com/watch?v=Ufz4JstsKig")
    with left_column:
        st.write("######")
        st.write("######")
        st.markdown('**Doxa says:**')
        st.markdown("***'One of the greatest aspects of being a physical education teacher is that our efforts have"
                 " a genuine impact on the lives of our students. The influence of our work extends beyond "
                 "their time in school and carries into their adulthood. It is our hope that the fundamental"
                 " principles of movement, knowledge of fitness and health, social interaction strategies, "
                 "outlets for self-expression, and leadership abilities that we impart will remain ingrained "
                 "in them throughout their lifetime.'***")
st.write("######")
st.write("######")
st.write("######")
# ---- WHAT I DO ----
with st.container():

    left_column, right_column = st.columns([1 , 2])
    with right_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel, I create videos for kids, families, P.E. Teachers:
            - Fun informative videos about a balanced diet for kids.
            - Interactive P.E. games
            - Interactive P.E. games .
            - P.E. games for the schoolyard or gym.
            - Yoga for kids.
            - Dance for kids.

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@doxadakanalipe772)")
    with left_column:
        st_lottie(lottie_python, height=450, key="python")