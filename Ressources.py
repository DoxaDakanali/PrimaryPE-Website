from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from annotated_text import annotated_text
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
import tempfile
import random
import openai
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---- LOAD ASSETS ----
img_Head = Image.open("IMAGES/head1.png")
img_Head = img_Head.resize((1080, 150), Image.LANCZOS)
st.image(img_Head)
img1 = Image.open("IMAGES/MY_PLATE.png")
img3 = Image.open("IMAGES/CASTLE_WARS.png")
img_loc1 = Image.open("IMAGES/locom.png")
img_whathappens =Image.open("IMAGES/whathappens.png")
img_cloud = Image.open("IMAGES/cloud.png")
img_rock = Image.open("IMAGES/rock.png")
img_waspital= Image.open("IMAGES/wasp.png")
img_volcanoes= Image.open("IMAGES/volcanoes.png")
img_battle= Image.open("IMAGES/batlle.png")
img_pacman= Image.open("IMAGES/pacman.png")
img_yogabingo = Image.open("IMAGES/yogabingo.png")
img_yogadice = Image.open("IMAGES/rolldiceyoga.png")
img_grossdice = Image.open("IMAGES/groosmotordice.png")
img_beanbagchallenge = Image.open("IMAGES/beanbagactivity.png")
img_WhyEx = Image.open("IMAGES/whyExercise.png")
img_label = Image.open("IMAGES/labelsummer.png")
img_selfassesment = Image.open("IMAGES/selfassesment.png")
img_expect = Image.open("IMAGES/P.E.expect.png")
img_sportsmanship = Image.open("IMAGES/3.png")
img_doingexe = Image.open("IMAGES/κανεις γυμναστική.png")
img_cloud = Image.open("IMAGES/wordcloud.png")
img_calculator = Image.open("IMAGES/my-healthy-plate.jpg")
img_calculator = img_calculator.resize((400, 400), Image.LANCZOS)
img_personalassistant = Image.open("IMAGES/personalassistant.jpg")

current_dir = Path.cwd()
LocomotorVisual_file = current_dir / "PDF" / "locomotor.pdf"
whathappensVisual_file = current_dir/"PDF"/ "WhatHappens.pdf"
Pacman = current_dir/"PDF"/ "Pacman.pdf"
Waspital =current_dir/"PDF"/ "Waspital.pdf"
Batlle = current_dir/"PDF"/ "Rock Paper Scissors Battle1 (3).pdf"
Volcanoes = current_dir/"PDF"/ "Volcanos and icecream cones.pdf"
beanbagChallenge = current_dir/"PDF"/ "beanbag challenge.pdf"
grossmotordice =current_dir/"PDF"/ "us-a-167-gross-motor-roll-and-exercise-activity_ver_1.pdf"
yogadice =current_dir/"PDF"/ "au-t-1660137362-roll-a-yoga-pose-brain-break-dice_ver_1.pdf"
yogabingo =current_dir/"PDF"/ "yoga Bingo.pdf"
whyex =current_dir/"PDF"/ "Γιατί χρεαζομαι γυμναστική (2).pdf"
labelsummer =current_dir/"PDF"/ "Label the Summer Olympic Sports.pdf"
selfassesment = current_dir/"PDF"/ "Self - Assessment.pdf"
sportsmanship = current_dir/"PDF"/ "p.e. sportsmanship.pdf"
expectations = current_dir/"PDF"/ "P.Eexpect.pdf"
doingexe =current_dir/"PDF"/ "ΚΑΝΕΙΣ ΓΥΜΝΑΣΤΙΚΗ.pdf"

with open(LocomotorVisual_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(whathappensVisual_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(yogabingo, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(Pacman, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with open(Waspital, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(Batlle, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(Volcanoes, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(beanbagChallenge, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(grossmotordice, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(yogadice, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(whyex, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(labelsummer, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(selfassesment, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(sportsmanship, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(expectations, "rb") as pdf_file:
   PDFbyte = pdf_file.read()
with open(doingexe, "rb") as pdf_file:
   PDFbyte = pdf_file.read()

#file_names = [LocomotorVisual_file, whathappensVisual_file, yogabingo, Pacman, Waspital, Batlle, Volcanoes,
#              beanbagChallenge, grossmotordice, yogadice, whyex, labelsummer, selfassesment, sportsmanship,
#              expectations,doingexe]

#PDFbyte = []

#for file_name in file_names:
#    with open(file_name, "rb") as pdf_file:
#        PDFbyte.append(pdf_file.read())


# # ---- NAVIGATION BAR ----
selected = option_menu(
    menu_title=None,

    options=[
        'P.E. Visuals', 'Warm up games',
        'Fitness Activities', 'Health and Nutrition','Assessment',
        'P.E. APPS',
    ],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#31333F"},
        "icon": {"color": "orange", "font-size": "10px"},
        "nav-link": {
            "font-size": "15px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#3290a6",
        },
        "nav-link-selected": {"background-color": "#3290a6"},
    },
)

#------ Display titles based on selected option-----
if selected == "P.E. Visuals":
    st.title(f'{selected}')
    with st.container():
        st.write("---")
        st.write("##")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            COL1, COL2=st.columns(2)
            with COL1:
                annotated_text(
                    ("lOCOMOTOR POSTER", "", "#0B1520", "#3290a6")
                )
            st.image(img_loc1)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=LocomotorVisual_file.name,
                    mime="application/octet-stream",
            )

        with col2:
            COL1, COL2=st.columns(2)
            with COL1:
                annotated_text(
                    ("What Happens To My Body POSTER", "", "#0B1520", "#3290a6")
                )
            st.image(img_whathappens)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=whathappensVisual_file.name,
                    mime="application/octet-stream",
            )

        with col3:
            COL1, COL2=st.columns(2)
            with COL1:
                annotated_text(
                    ("Sportsmanship Poster", "", "#0B1520", "#3290a6")
                )
            st.image(img_sportsmanship)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=sportsmanship.name,
                    mime="application/octet-stream",
            )

        with col4:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("P.E. EXPECTATIONS", "", "#0B1520", "#3290a6")
                )
            st.image(img_expect)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=expectations.name,
                    mime="application/octet-stream",
                )

elif selected == 'Warm up games':
    st.title(f'{selected}')
    with st.container():
        col_left, col_right = st.columns(2)
        with col_left:
            col1, col2 = st.columns(2)
            with col1:
                st.image(img3)
            with col2:
                st.subheader("CASTLE WARS")
                st.write(
                """
                Castle wars is a very popular pe game for the gym or the school yard.
                With this game the kids will develop skills like throwing, catching, defending space 
               strea and team building and they will have a lots of fun
                """
                    )
            st.markdown("[Watch Video...](https://www.youtube.com/watch?v=WAs18iZtYFU)")
        with col_right:
            col1, col2 = st.columns(2)
            with col1:
                st.image(img_rock)
            with col2:
                st.subheader("ROCK PAPER SCISSORS")
                st.write(
                    """
                    Epic battles, in this epic game. A fun pe game for the gym or the school yard.You can practice 
                    skills like 2 feet hopping, 1 foot hopping and running and at the same time have lots of fun.

                    """
                )
            st.markdown("[Watch Video...](https://www.youtube.com/watch?v=TQD7OhYFCY0)")
    with st.container():
        st.write("---")
        st.write("##")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("WASPITAL GAME ", "", "#0B1520", "#3290a6")
                )
            st.image(img_waspital)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=Waspital.name,
                    mime="application/octet-stream",
                )

        with col2:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("PACMAN GAME", "", "#0B1520", "#3290a6")
                )
            st.image(img_pacman)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=Pacman.name,
                    mime="application/octet-stream",
                )

        with col3:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("VOLCANOES AND ICECREAM CONES ", "", "#0B1520", "#3290a6")
                )
            st.image(img_volcanoes)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=Volcanoes.name,
                    mime="application/octet-stream",
                )

        with col4:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("ROCK PAPER SCISSORS  ", "", "#0B1520", "#3290a6")
                )
            st.image(img_battle)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=Batlle.name,
                    mime="application/octet-stream",
                )
    st.write("######")
    st.write("######")
    st.write("######")
elif selected == 'Fitness Activities':
    st.title(f'{selected}')
    with st.container():
        st.write("---")
        st.write("##")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("Yoga Roll Dice ", "", "#0B1520", "#3290a6")
                )
            st.image(img_yogadice)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=yogadice.name,
                    mime="application/octet-stream",
                )


        with col2:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("Beanbag Challenge Cards", "", "#0B1520", "#3290a6")
                )
            st.image(img_beanbagchallenge)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=beanbagChallenge.name,
                    mime="application/octet-stream",
                )

        with col3:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("Yoga Bingo Game ", "", "#0B1520", "#3290a6")
                )
            st.image(img_yogabingo)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=yogabingo.name,
                    mime="application/octet-stream",
                )

        with col4:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("Gross Motor Dice  ", "", "#0B1520", "#3290a6")
                )
            st.image(img_grossdice)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=grossmotordice.name,
                    mime="application/octet-stream",
                )

elif selected == 'Health and Nutrition':
    st.title(f'{selected}')
    with st.container():
        st.write("---")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img1)
        with text_column:
            st.subheader("MY PLATE")
            st.write(
                """
                Learn all about 'My Plate' and the food groups in this video.
                You will learn how to build healthy meals and snacks to help you grow,
                play, learn, and stay healthy.
                """
            )
            st.write("[YouTube Channel >](https://www.youtube.com/@doxadakanalipe772)")

elif selected == 'Assessment':
    st.title(f'{selected}')
    with st.container():
        st.write("---")
        st.write("##")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("Why i need Exercise? ", "", "#0B1520", "#3290a6")
                )
            st.image(img_WhyEx)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=whyex.name,
                    mime="application/octet-stream",
                )

        with col2:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("Label the Summer Olympic Games", "", "#0B1520", "#3290a6")
                )
            st.image(img_label)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=labelsummer.name,
                    mime="application/octet-stream",
                )

        with col3:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("Self - Assessment ", "", "#0B1520", "#3290a6")
                )
            st.image(img_selfassesment)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=selfassesment.name,
                    mime="application/octet-stream",
                )

        with col4:
            COL1, COL2 = st.columns(2)
            with COL1:
                annotated_text(
                    ("ΕΣΥ ΚΑΝΕΙΣ ΓΥΜΝΑΣΤΙΚΗ;  ", "", "#0B1520", "#3290a6")
                )
            st.image(img_doingexe)
            with COL2:
                st.download_button(
                    label="  Download ",
                    data=PDFbyte,
                    file_name=doingexe.name,
                    mime="application/octet-stream",)


elif selected == 'P.E. APPS':

#    ---- WORD CLOUD GENERATOR -----

    st.title(f'{selected}')

    # Disable warning for deprecated st.pyplot() usage
    st.set_option('deprecation.showPyplotGlobalUse', False)
    with st.container():
        st.write("---")
        st.write("##")
        col1, col2 = st.columns(2)
        with col1:
            st.title("Text to Word Cloud Converter")
            st.image(img_cloud)
        with col2:
            st.write("##")
            st.write("##")

            # Text input
            text_input = st.text_area("Enter your text here", key="text_input_unique_key")

            # Background color selection
            background_color = st.selectbox("Select background color", ("White", "Black", "Orange", "Red", "Purple"),
                                            key="bg_color")

            # Word cloud shape selection
            shape_option = st.selectbox("Select word cloud shape", ("Rectangle", "Cloud"), key="shape_option")

            # Text color selection
            text_color = st.selectbox("Select text color",
                                      ("Default", "Random", "Red", "Green", "Blue", "Yellow", "Cyan", "Magenta"),
                                      key="text_color")

            # Word cloud generation
            if st.button("Generate Word Cloud"):
                # Create WordCloud object
                stopwords = set(STOPWORDS)

                if background_color == "White":
                    bg_color = "white"
                elif background_color == "Black":
                    bg_color = "black"
                elif background_color == "Orange":
                    bg_color = "orange"
                elif background_color == "Red":
                    bg_color = "red"
                else:
                    bg_color = "purple"

                if shape_option == "Rectangle":
                    custom_mask = None  # No custom mask for rectangle shape (default shape)
                else:
                    custom_mask = np.array(Image.open('IMAGES/cloud.png'))

                wc = WordCloud(width=1200, height=800, background_color=bg_color, stopwords=stopwords, mask=custom_mask,
                               contour_width=3, contour_color='black')
                wc.generate(text_input)  # Generate the word cloud first

                if text_color == "Random":
                    color_func = lambda *args, **kwargs: f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"
                elif text_color == "Red":
                    color_func = lambda *args, **kwargs: "rgb(255, 0, 0)"
                elif text_color == "Green":
                    color_func = lambda *args, **kwargs: "rgb(0, 255, 0)"
                elif text_color == "Blue":
                    color_func = lambda *args, **kwargs: "rgb(0, 0, 255)"
                elif text_color == "Yellow":
                    color_func = lambda *args, **kwargs: "rgb(255, 255, 0)"
                elif text_color == "Cyan":
                    color_func = lambda *args, **kwargs: "rgb(0, 255, 255)"
                elif text_color == "Magenta":
                    color_func = lambda *args, **kwargs: "rgb(255, 0, 255)"
                else:
                    color_func = None  # Default text color

                if color_func is not None:
                    wc.recolor(color_func=color_func)  # Apply the color function

                # Display word cloud
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.imshow(wc, interpolation='bilinear')
                ax.axis('off')
                st.pyplot(fig)

                tf = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
                wc.to_file(tf.name)
                #st.write(tf.name)
                with open(tf.name,"rb") as f:
                    st.download_button("Download Word Cloud", f, file_name="wordcloud.png")





#----MY PLATE CALORIES CALCULATOR---


    with st.container():
         st.write("---")
         st.write("##")
         col1, col2 = st.columns(2)
         with col1:
             st.title("'MyPlate' Plan ")
             st.image(img_calculator)
         with col2:
            st.write("##")
            st.subheader("Calories calculator")
            st.write("Put your data to calculate the intake calories in order to maintain your body weight ")
            # Embed the iframe code using st.markdown()
            iframe_code = '<iframe src="https://www.myplate.gov/widgets/myplate-plan-start/sm" scrolling="no" ' \
                          'style="min-height: 300px;"></iframe>'
            st.markdown(iframe_code, unsafe_allow_html=True)


#img_personalassistant
#  ----- CHAT GPT CLONE ----  ( https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps )

#    with st.container():
#        with col2:
#            st.write("##")
#            st.write("##")
#            st.write("##")
#            with st.expander("'My personal assistant' is your ultimate AI-powered companion, utilizing the cutting-edge technology"
#                     " of OpenAI s GPT-3.5 architecture.Picture having a versatile and knowledgeable aide at your "
#                     "fingertips, available round-the-clock to aid you in various tasks.Functioning as a personal"
#                     " assistant this AI marvel adeptly manages an extensive array of tasks, simplifying your daily"
#                     " life. It engages in seamless and natural conversations, making interactions feel genuinely"
#                     " human and compelling."):
#                st.write(
#                    "From dynamic discussions to practical responsibilities, a personal assistant proves its "
#                       'multifaceted capabilities. It drafts emails, generates reports, and tailors content to your '
#                        ' poetry, and delivering personalized recommendations based on your inclinations.'
#                        'The personal assistant transcends the role of a mere information provider. It serves as a '
#                        'comprehensive learning resource, offering lucid explanations on intricate subjects and'
#                        ' expanding your knowledge effortlessly.Organizational tasks become effortless with the '
#                        'personal assistant. It sets reminders, arranges appointments, and furnishes you with weather'
#                        'and sparks innovative ideas for your projects.'
#                        'In summation, the personal assistant is more than just a digital aide; it embodies '
#                        'adaptability, intelligence, and versatility, enhancing your routine across dimensions you might'
#                        ' not have imagined before'
#                    )
#        # Set OpenAI API key from Streamlit secrets
#        openai.api_key = st.secrets["OPENAI_API_KEY"]

        # Set a default model
#        if "openai_model" not in st.session_state:
 #           st.session_state["openai_model"] = "gpt-3.5-turbo"

        # Initialize chat history
#        if "messages" not in st.session_state:
 #           st.session_state.messages = []

        # Display chat messages from history on app rerun
#        for message in st.session_state.messages:
#            with st.chat_message(message["role"]):
#                st.markdown(message["content"])

        # Accept user input
 #       if prompt := st.chat_input("What is up?"):
 #           # Add user message to chat history
 #           st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
#                st.markdown(prompt)
            # Display assistant response in chat message container
#            with st.chat_message("assistant"):
#                message_placeholder = st.empty()
#                full_response = ""

#                model=st.session_state["openai_model"],
#                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
#                stream=True,
#            full_response += response.choices[0].delta.get("content", "")
#       message_placeholder.markdown(full_response)
#        st.session_state.messages.append({"role": "assistant", "content": full_response})