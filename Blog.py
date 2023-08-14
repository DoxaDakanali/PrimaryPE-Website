import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

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
img_doxa = Image.open("IMAGES/doxa.png")
img_doxa = img_doxa.resize((300, 300), Image.LANCZOS)
img_bones = Image.open("IMAGES/bones.jpg")
img_brain = Image.open("IMAGES/brain.jpg")
img_Effects = Image.open("IMAGES/Effects_exersise.png")
img_happy = Image.open("IMAGES/happy.png")
img_heartfast = Image.open("IMAGES/heart_fast.png")
img_muscle = Image.open("IMAGES/muscle.png")
img_sweat = Image.open("IMAGES/sweat1.jpg")
img_talk = Image.open("IMAGES/talk1.png")
img_tired1 = Image.open("IMAGES/tired1.png")
img_tired2 = Image.open("IMAGES/tired2.png")
img_title = Image.open("IMAGES/title.png")
img_water = Image.open("IMAGES/water.png")
img_breath = Image.open("IMAGES/breath1.jpg")
img_specialist = Image.open("IMAGES/P.E.SPESIALIST.png")
img_Thephyseddepot = Image.open("IMAGES/Thephyseddepot.png")
img_sportsAustralia = Image.open("IMAGES/sportsAustralia.png")
img_PRIMECOACHING = Image.open("IMAGES/PRIMECOACHING.png")
img_PhysEdGames = Image.open("IMAGES/Phys.EdGames.png")
img_PEcentral = Image.open("IMAGES/P.E.Central.png")
img_openPhys = Image.open("IMAGES/OPENPHYSED.png")
img_iPhysEd = Image.open("IMAGES/iPhysEdCom.png")
img_Capt = Image.open("IMAGES/Capt.png")
img_canada = Image.open("IMAGES/canada.png")
img_10topwebsites =Image.open("IMAGES/10TOPWEBSITES.png")
img_responsive=Image.open("IMAGES/responsive.jpg")
img_myplate = Image.open("IMAGES/my_plate.jpg")
img_TGFU = Image.open("IMAGES/TGFU1.jpg")

st.write("---")

# Navigation  Bar

selected = option_menu(
    menu_title=None,
    options=[
      'All Posts', 'Activities and Games',
      'Fitness Activities', 'Health and Nutrition',
      'P.E. Community',
      'Class Management'
    ],
    default_index=0,
    orientation= "horizontal",
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

# Display titles based on selected option
if selected == "All Posts":
  st.title(f'{selected}')
  col_left, col_right = st.columns([1, 2])
  with col_left:
      st.image(img_title)
  with col_right:
      st.title("Exploring the Effects of Exercise on Your Body: A Guide for Physical Education Teachers")
      st.write("###")
      with st.expander("Understanding how exercise affects our bodies is really important for physical education"
                       " teachers. It helps them create lessons that encourage fitness, teach students about the "
                       "health benefits of being active, and inspire habits that last a lifetime. In this article,"
                       " we'll explore what happens to our bodies when we exercise."):
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("'My heart beats faster'")
              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_heartfast)
              st.write(
                  "When we exercise, our heart beats faster to provide more oxygen and nutrients to our muscles. "
                  "This helps our muscles have the energy they need to do the exercise. The cardiovascular system, "
                  "which includes the heart, helps keep everything in balance by adjusting the heart rate based on "
                  "the intensity of the exercise.")

          with st.container():
              col1, col2 = st.columns([1, 2])
              with col1:
                  st.write("### ")
                  st.write("### ")
                  st.image(img_water)

              with col2:
                  st.subheader("'I start to sweat and get Thirsty'")

                  st.write(
                      "As we exercise, our body temperature goes up, and we start to sweat. Sweating is our body's "
                      "way of cooling down and preventing overheating. The sweat comes out of our skin and then evaporates,"
                      " which cools us down and helps keep our body temperature stable even when we're doing a tough workout "
                      "When we sweat, we also lose water from our body. That's why we feel thirsty when we exercise. Drinking "
                      "enough water is really important during exercise because it helps our body work properly. It helps"
                      " regulate our temperature and makes sure our blood flows well.")

          with st.container():
              col1, col2, = st.columns([1, 2])
              with col1:
                  st.write("### ")
                  st.write("### ")
                  st.write("### ")
                  st.image(img_happy)

              with col2:
                  st.subheader("'My Brain Produces Endorphins'")

                  st.write("### ")
                  st.write("### ")

                  st.write("When we exercise, our brain releases chemicals called endorphins. These chemicals act like"
                           " natural painkillers and make us feel happier. You might have heard of the 'runner's high."
                           " It's when people feel really good after exercising because of the endorphins. So exercise "
                           "not only helps our bodies, but it also boosts our mood and makes us feel good.")

          with st.container():
              col1, col2, = st.columns([1, 2])
              with col1:
                  st.write("### ")
                  st.write("### ")
                  st.write("### ")
                  st.image(img_breath)

              with col2:
                  st.subheader("'I Breathe Harder'")

                  st.write("### ")
                  st.write("### ")
                  st.write("Breathing also changes when we exercise. We breathe faster and deeper to get more oxygen "
                           "into our body. This helps our muscles get the oxygen they need and get rid of waste products "
                           "like carbon dioxide.")

          with st.container():
              col1, col2, = st.columns([1, 2])
              with col1:
                  st.write("### ")
                  st.write("### ")
                  st.write("### ")
                  st.image(img_brain)

              with col2:
                  st.subheader("'Blood Flow Increases to My Brain'")

                  st.write("### ")
                  st.write("### ")
                  st.write("Exercise also increases blood flow to our brain. This means our brain gets more oxygen and"
                           " nutrients, which makes it work better. It can improve our memory, focus, and overall brain"
                           " function. So exercise is good for our brain too.")
          with st.container():
              col1, col2, = st.columns([1, 2])
              with col1:
                  st.write("### ")
                  st.write("### ")
                  st.write("### ")
                  st.image(img_muscle)

              with col2:
                  st.subheader("'Blood Flow Increases to My Muscles'")

                  st.write("### ")
                  st.write("### ")
                  st.write("When we exercise, more blood flows to our muscles. This helps them get more oxygen and "
                           "nutrients, which they need to work properly. After exercise, the increased blood flow also"
                           " helps remove waste products from our muscles, like lactic acid, which can make our muscles "
                           "sore.")
          with st.container():
              col1, col2, = st.columns([1, 2])
              with col1:
                  st.write("### ")
                  st.write("### ")
                  st.write("### ")
                  st.image(img_bones)

              with col2:
                  st.subheader("'Increased Pressure to My Bones'")

                  st.write("### ")
                  st.write("### ")

                  st.write("Some exercises put pressure on our bones, like when we use our body weight to do certain"
                           " movements. This pressure actually helps our bones become stronger and denser. It's like "
                           "giving our bones a workout too, and it reduces the risk of conditions like osteoporosis,"
                           " which makes our bones weak and fragile.")
          with st.container():
              col1, col2, = st.columns([1, 2])
              with col1:
                  st.write("### ")
                  st.write("### ")
                  st.write("### ")
                  st.image(img_tired2)

              with col2:
                  st.subheader("'I Get a Tired Feeling'")

                  st.write("### ")
                  st.write("### ")
                  st.write("During exercise, our muscles can get tired. This is normal because they're working harder"
                           " and using up energy. They may also get little tears in the fibers, which can make them "
                           "feel sore later on. But don't worry, this is all part of the process, and it helps our "
                           "muscles get stronger. As we keep exercising, our body becomes more efficient, and we won't "
                           "feel as tired or sore over time.")
          with st.container():
              col1, col2, = st.columns([1, 2])
              with col1:
                  st.write("### ")
                  st.write("### ")
                  st.write("### ")
                  st.image(img_talk)

              with col2:
                  st.subheader("'It Gets Difficult to Talk'")

                  st.write("### ")
                  st.write("### ")
                  st.write("When we exercise harder, it becomes more difficult to talk because we need more oxygen."
                           " Our breathing gets heavier, and we need to use that oxygen for our muscles, so talking"
                           " becomes a challenge. This is called the 'talk test,' and it's a way to know how intense "
                           "our exercise is by seeing if we can talk comfortably or not.")

          st.write("In summary, exercise has many benefits for our bodies and minds. It helps our muscles, "
                   "heart, and brain work better. It also keeps our bones strong and maintains a healthy weight. "
                   "Physical education teachers can share this knowledge with students and help them understand "
                   "why exercise is important. By teaching about the benefits of exercise, they can inspire "
                   "students to be active and live healthy lives.")

  col_left, col_right = st.columns([1, 2])
  with col_left:
      st.image(img_10topwebsites)
  with col_right:
      st.title("10 Top Quality PE Websites:Essential Resources for Physical Education Teachers")

      with st.expander("Physical Education is an essential subject that promotes physical activity and healthy "
                       "lifestyles among students. As PE's importance continues to grow, it is now more crucial "
                       "than ever for aspiring and practicing PE teachers to have access to credible and innovative "
                       "resources. "):
          st.write("With the internet being a primary source of information today, there are several "
                       "websites that provide valuable resources for physical education and health teachers to take "
                       "advantage of. Some of these websites have been around for a while, while others are relatively"
                       " new.")
          st.header("Top 10 PE Websites for 2023")
          st.write('We have handpicked a collection of websites that excel in features, user-friendliness, and '
                   'high-quality content for physical education. These selected websites offer a wealth of valuable '
                   "resources for PE teachers. To give you a glimpse of each site's strengths, we've provided a "
                   "brief paragraph highlighting their notable features and included a link for your convenience.")
          st.markdown("**:blue[1.PhysEd Games ]**")
          st.markdown(" **:blue[2.The PE Specialist ]** ")
          st.markdown(" **:blue[3.Cap'n Pete's Power PE ]** ")
          st.markdown(" **:blue[4.PE Central ]** ")
          st.markdown(" **:blue[5.iPhysEd.com ]** ")
          st.markdown(" **:blue[6.OPENPhysEd.org  ]** ")
          st.markdown(" **:blue[7.prime coaching sport ]** ")
          st.markdown(" **:blue[8.Sport Australia ]** ")
          st.markdown(" **:blue[9.phys ed depot]** ")
          st.markdown(" **:blue[10.CanadaGo4Sport ]** ")
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['PhysEd Games' ](https://www.https://physedgames.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_PhysEdGames)
              st.write("PhysEd Games is a valuable website specifically designed for physical education teachers "
                       "and professionals seeking game ideas to make their PE classes more exciting and interactive."
                       " With a vast collection of free game videos, the site offers a diverse range of options to "
                       "engage and motivate students. Each video is accompanied by a written explanation, providing"
                       " details on the game's suitability for different grade levels, required equipment, and a brief"
                       " description. PhysEd Games covers a wide spectrum of activities, including fun games,"
                       " sport-themed activities, and team-building exercises that can be customized to suit various"
                       " age groups.")
              st.write("####")

              st.markdown(
                  ":blue[Best Attributes: PhysEd Games stands out as an exceptional resource for PE teachers seeking"
                  " visually-driven content through its video depictions of engaging activities. The videos are "
                  "user-friendly, offering clear and concise instructions that are easy to follow. This makes it"
                  " an ideal platform for educators looking to enhance their teaching repertoire and bring more"
                  " excitement to their physical education classes.")

              with col3:
                  st.write(" ")

          # P.E. SPECIALIST
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['The PE Specialist' ](https://www.https://physedgames.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_specialist)
              st.write("The PE Specialist, founded by Ben Landers @thepespecialist, is a comprehensive website "
                       "dedicated to supporting physical education teachers with a wide range of resources. "
                       "This platform offers valuable classroom management strategies, lesson ideas, unit overviews,"
                       " teaching tips, technology resources, games and activities, music and dance content, virtual"
                       " teaching tips, and much more. Ben, an experienced physical education teacher, shares his "
                       "expertise through an extensive PE blog and a podcast that offers practical insights for both"
                       " new and experienced educators. The site also features a membership program, granting access "
                       "to exclusive member forums and unlimited downloadable content and resources..")
              st.write("####")

              st.markdown(
                  ":blue[Best Attributes:] The PE Specialist excels in providing an abundance of resources and strategies"
                  " to assist physical educators in meeting their students' needs. Moreover, the site serves as a"
                  " valuable source for staying informed about the latest trends in physical education and offers "
                  "valuable advice for navigating the art of teaching PE..")

              with col3:
                  st.write(" ")

          # CAPT'S PETE'S P.E.
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['Cap'n Pete's Power PE' ](https://www.capnpetespowerpe.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='small')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_Capt)
              st.write(
                  "Cap'n Pete's Power PE, founded by Pete Charrette (@capnpetespe), is an online platform designed to"
                  " support both aspiring and practicing physical education teachers in enhancing their instructional "
                  "approach. This website offers a wide range of tools, information, and resources to help educators"
                  " create and maintain exceptional physical education programs. The blog section provides valuable "
                  "insights and practical tips, while the standout feature is the availability of free downloadable "
                  "resources that can be seamlessly incorporated into PE classes. Additionally, Cap'n Pete's Power PE "
                  "boasts an extensive library of over 750 resources, including PE activities, games, field day materials,"
                  " virtual PE resources, templates, visuals, posters, sign packages, PowerPoint presentations, and much"
                  " more. It serves as a comprehensive hub for all things related to physical education and health.")
          # P.E Central
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['P.E Central' ](https://www.https://www.pecentral.org/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='small')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_PEcentral)
              st.write(
                  "PE Central is a well-established and all-encompassing physical education website that stands"
                  " out among its counterparts. It boasts a vast collection of teaching practices, lesson ideas, "
                  "assessment strategies, skill and fitness challenges, and resources tailored to adapted physical"
                  " education across various grade levels. Furthermore, PE Central offers a range of online courses"
                  " and resources that support the growth and professional development of physical education teachers."
                  " The website is also home to a comprehensive video library featuring dances, lessons, and more,"
                  " as well as numerous bulletin board ideas to enhance the aesthetics of gymnasiums or classrooms.")
              st.markdown(
                  ":blue[Best Attributes:] Over the years, PE Central has proven to be an invaluable resource for"
                  " physical and health educators, coaches, and fitness professionals. Its extensive library of lessons"
                  " and activities provides endless possibilities, and the best part is that everything is freely"
                  " accessible and truly remarkable!")

          # iPhysEd.com
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['iPhysEd' ](https://www.iphys-ed.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='small')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_iPhysEd)
              st.write(
                  "iPhysEd.com, developed by Nathan Horne @PEnathan, is a dedicated online platform designed to empower"
                  " physical educators and coaches with the necessary tools to deliver high-quality and purposeful"
                  " physical education experiences to their communities. This website offers a wide array of innovative"
                  " and captivating resources that can greatly enhance the instruction and promotion of physical activity"
                  " among students. From free assessment tools and game resources to visually appealing materials, "
                  "iPhysEd.com equips PE teachers with everything they need to create engaging and effective physical "
                  "education lessons. Additionally, the platform hosts a library of online courses facilitated by "
                  "renowned physical educators from around the world..")
              st.markdown(
                  ":blue[Best Attributes:] iPhysEd.com stands out as a comprehensive online resource that fuels the "
                  "creativity and effectiveness of PE teachers. It provides a wealth of ideas, tools, and support to "
                  "facilitate engaging and impactful physical education experiences. The availability of online courses"
                  " ensures continuous professional growth, while the free assessment tools and visuals serve as "
                  "invaluable resources to enhance PE instruction and create a vibrant learning environment.")

          # OPENPhysEd.org
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['OPENPhysEd' ](https://openphysed.org/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_openPhys)
              st.write(
                  "The website OPEN (Online Physical Education Network), created by Aaron Hart @nyaaronhart, is a"
                  " valuable online platform that provides high-quality and free physical education resources for K-12"
                  " educators and students. With a wide range of offerings including lesson plans, assessments, "
                  "skill-based activities, and fitness challenges, OPEN aims to enhance students' physical literacy and "
                  "overall health. The mission of OPENPhysEd.org is to empower educators by equipping them with the"
                  " necessary tools and resources to promote active and healthy lifestyles, while delivering exceptional"
                  " physical education to all students, regardless of their background or ability level. The website's "
                  "user-friendly interface and adaptable materials enable educators to customize lessons and create"
                  " inclusive, engaging, and safe learning environments tailored to their students' needs. Additionally,"
                  " OPEN offers an extensive array of professional development initiatives, designed to elevate teacher "
                  "performance and foster student growth.")
              st.markdown(
                  ":blue[Best Attributes:] OPEN sets itself apart through its commitment to providing free and easily "
                  "accessible resources. Their library encompasses a comprehensive collection of standards-based"
                  " materials suitable for all levels of teaching. Furthermore, OPEN is supported by a team of national"
                  ""
                  " trainers who deliver unparalleled professional development opportunities for physical educators,"
                  " health teachers, and other classroom-based professionals.")

          # prime coaching sport
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['prime coaching sport' ](https://www.primecoachingsport.com/h)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_PRIMECOACHING)
              st.write(
                  "Prime Coaching Sport, developed by Coach Dale Sidebottom, is a comprehensive website providing "
                  "coaches and physical education teachers with valuable resources. Its extensive collection of "
                  "engaging lesson plans saves educators time and ensures purposeful sessions. The website offers "
                  "diverse game ideas and activities for skill development and teamwork. With a focus on professional"
                  " development, Prime Coaching Sport provides articles, videos, and online courses to enhance coaching"
                  " techniques. Its user-friendly interface allows easy navigation, making lesson planning and"
                  " preparation a seamless experience. It equips educators with tools to deliver high-quality coaching "
                  "and instruction.")
              st.markdown(
                  ":blue[Best Attributes:] Extensive collection of engaging lesson plans,Diverse game ideas and "
                  "activities for skill development, Focus on professional development with articles, videos,"
                  " and online courses,User-friendly interface for easy navigation,Valuable resources for coaches"
                  " and physical education teachers")

          # Sport Australia
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['Sport Australia' ](https://www.sportaus.gov.au/sports_ability)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_sportsAustralia)
              st.write(
                  "As the official website of Australia's premier agency for sport and physical activity, Sport"
                  " Australia offers a wealth of resources, information, and services to foster the growth of sports"
                  " and physical activity across the country. One notable section, Sports Ability, presents activity"
                  " cards designed to be inclusive and accessible to individuals of all abilities. These cards empower "
                  "children by equipping them with the necessary skills to excel in sports while bolstering their"
                  " confidence and motivation. Each card provides detailed instructions for organizing and conducting"
                  " activities, along with insights on adapting elements to ensure the participation of all children. "
                  "By modifying game rules, equipment, and techniques, these cards create enjoyable and rewarding"
                  " opportunities for everyone to engage in sports and achieve success.")
              st.markdown(
                  ":blue[Best Attributes:] Sport Australia's Sports Ability cards stand out for their accessibility and"
                  " user-friendly nature."
                  " Available for free download, these cards offer a comprehensive package of information, including"
                  " setup instructions, required equipment, skill focus, rules, teaching style, safety considerations,"
                  " environmental needs, and student engagement questions. This level of detail makes them particularly "
                  "well-suited for elementary and middle school physical education teachers, providing a valuable "
                  "resource that is easy to understand and implement.")

          # phys ed depot
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['The Phys. Ed. Depot' ](http://www.physeddepot.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_Thephyseddepot)
              st.write(
                  "The Phys. Ed. Depot is a remarkable website that offers a wealth of resources and materials "
                  "for physical education professionals. With a diverse range of tools and content, this website is "
                  "a go-to destination for educators seeking to enhance their physical education programs. The site"
                  " features a vast collection of lesson plans, activity ideas, assessment tools, and curriculum"
                  " resources that are suitable for various grade levels. Additionally, The Phys. Ed. Depot provides "
                  "interactive games, fitness challenges, and instructional videos that engage students and promote "
                  "active participation.")
              st.markdown(
                  ":blue[Best Attributes:] One of the standout features of The Phys. Ed. Depot is its extensive "
                  "library of ready-to-use resources. These materials are well-organized and easily accessible,"
                  " saving educators valuable time in lesson planning and preparation. The website also offers a "
                  "supportive community where teachers can share ideas, collaborate, and seek advice from fellow"
                  " professionals. With its user-friendly interface and comprehensive content, The Phys. Ed. Depot serves"
                  " as a valuable resource hub that empowers physical education teachers to deliver high-quality and "
                  "engaging lessons that promote lifelong fitness and healthy lifestyles."
              )
          # CanadaGo4Sport
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['CanadaGo4Sport' ](https://www.canadago4sport.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_canada)
              st.write(
                  "CanadaGo4Sport is a dynamic website dedicated to promoting physical literacy and active living "
                  "among children and youth in Canada. It offers an extensive array of resources and tools aimed at"
                  " parents, teachers, and community leaders, empowering them to foster physical activity and healthy"
                  " lifestyles in children. The website boasts a diverse range of physical literacy resources, "
                  "encompassing lesson plans, activity ideas, games, and videos carefully designed to cultivate "
                  "fundamental movement skills like running, jumping, throwing, and catching. Additionally, "
                  "CanadaGo4Sport provides valuable guidance on physical activity guidelines, safety considerations,"
                  " and inclusive practices to ensure children of all abilities can participate. Serving as a central "
                  "hub for information and resources on physical literacy and active living, CanadaGo4Sport inspires and "
                  "educates children, encouraging them to embrace healthy and active lives.")
              st.markdown(
                  ":blue[Best Attributes:] Canada Go 4 Sport stands out as an invaluable resource for teachers and "
                  "physical education professionals seeking to foster physical literacy and active living among children "
                  "in Canada and beyond. Its user-friendly homepage offers a wealth of resources, including "
                  "well-structured lesson plans with clear instructions, as well as instructional videos covering "
                  "various aspects of physical education. Whether you're looking for engaging activities or "
                  "comprehensive guidance, Canada Go 4 Sport provides the tools necessary to inspire and educate "
                  "students, making it an essential destination for promoting a healthy and active lifestyle.")
  st.write("### ")
  col_left, col_right = st.columns([1, 2])
  with col_left:
      st.image(img_responsive)
  with col_right:
      st.title("Responsive Classroom (Student-Centered Approach)")
      st.write("###")
      with st.expander("The Responsive Classroom is a well-established and evidence-based student-centered approach "
                       "to teaching. With a focus on engaging academics, fostering a positive community, effective "
                       "management, and developmental awareness, it has been in existence for over 40 years, originally"
                       " starting as an education research lab school."):
          st.write(
              "When it comes to teaching and parenting, there are four main approaches, which share similar"
              " principles:.")

          st.write("### ")

          st.write(
              "1. Authoritarian:"
              "This approach believes in strict obedience without considering the child's opinions"
              " or feelings."
              "Authoritarians enforce rules without negotiation and might say, 'Because I said so,' when questioned."
              "They do not involve children in problem-solving challenges and rely on punishments rather than "
              "teaching better choices.Children raised under authoritarian parents may follow rules, but their "
              "self-esteem can suffer due to their opinions being undervalued. They may also become hostile or "
              "resort to lying to avoid punishment. ")
          st.write("### ")

          st.write(
              "2. Authoritative (Responsive Classroom):"
              "The authoritative approach involves creating and maintaining positive relationships with children and"
              " explaining the reasons behind rules.While enforcing rules and consequences, authoritative "
              "individuals consider the child's feelings and validate their emotions.They invest time and energy "
              "in preventing behavior problems and use positive discipline strategies, such as praise and rewards."
              "Children raised with authoritative discipline tend to be happy, successful, and capable of making "
              "decisions and assessing safety risks independently. They feel comfortable expressing their opinions"
              "and grow into responsible adults. ")
          st.write("### ")
          st.write("3.Permissive:"
                   "Permissive individuals set rules but may not consistently enforce them.Consequences are"
                   " infrequent and may not be firmly applied.They adopt an attitude of leniency, believing that"
                   " 'kids will be kids.'Permissive parents often take on a friend-like role and encourage children"
                   " to talk about their problems. However, they may not actively discourage poor choices or bad "
                   "behavior.Children raised with permissive parenting may struggle academically, exhibit behavioral"
                   " problems, have low self-esteem, and face health issues due to a lack of structure and limits. ")
          st.write("### ")
          st.write("4.Uninvolved/Neglectful:"
                   "Uninvolved parents have little knowledge of their children's activities and provide minimal"
                   " guidance, nurturing, and attention.They may expect children to raise themselves and don't "
                   "devote much time or energy to meeting their basic needs.Uninvolved parents may unintentionally"
                   " neglect their children due to mental health issues, substance abuse problems, lack of knowledge "
                   "about child development, or other overwhelming challenges.Children with uninvolved parents tend "
                   "to experience self-esteem issues, perform poorly in school, exhibit behavioral problems, and "
                   "have lower levels of happiness. ")
          st.write("### ")
          st.write("The Responsive Classroom applies the authoritative approach, which has garnered support from"
                   " 98% of scientific research as the most effective. It adapts this approach to teaching rather"
                   " than parenting, allowing teachers to seamlessly integrate student-centered practices into their"
                   " daily teaching routines ")
          st.write("I highly recommend the book 'Responsive Classroom for Music, Art, PE, and Other Special Areas'"
                   "The book written by special area teachers offers practical advice, examples, and strategies to"
                   " create a positive and engaging classroom environment, leading to better learning outcomes for "
                   "students. ")
          col_1, col_2 = st.columns(2)
          with col_1:
              st.write("Here's a 1-hour webinar by Rachel Atzert about responsive classroom")
          with col_2:
              st.write("[Rachel Atzert Webinar >](https://www.youtube.com/watch?v=NHGaXDUMNQc)")

  col_left, col_right = st.columns([1, 2])
  with col_left:
      st.image(img_myplate)
  with col_right:
      st.title("MyPlate For Our Children")
      st.write("###")
      with st.expander("The Food Guide Pyramid was recently discontinued by the USDA, and in its place, the more"
                       " user-friendly MyPlate has been introduced.MyPlate method offers several notable benefits "
                       "compared to the phased-out pyramid. Here are the main takeaways:"):


          st.write(
              "1. Increase your intake of vegetables and fruits. It's important to introduce children to a variety "
              "of options. Just because a child doesn't immediately enjoy a particular vegetable like broccoli doesn't"
              " mean they won't ever develop a liking for it. Keep offering different options, especially when your"
              " child is hungry. Aim for half of the plate to consist of fruits and vegetables. If you're pressed for"
              " time or on a tight budget, consider using canned or frozen produce – they're better choices than none"
              " at all. Remember, the vibrant colors of fruits and vegetables indicate the presence of beneficial "
              "phytochemicals, in addition to essential vitamins and minerals. These foods also provide important fiber"
              " and fluids for children. Even at fast-food or quick-service restaurants, you can apply these principles"
              " by making mindful choices.. ")
          st.write("### ")

          st.write(
              "2. Prioritize whole grains. This includes foods like 100% whole wheat bread, oatmeal, and even popcorn."
              " About a quarter of the plate should be occupied by grains and starches. If your child isn't fond of"
              " whole wheat pasta, you can explore brands that offer a blend of whole wheat and white flour. ")
          st.write("### ")
          st.write("3.Allocate a quarter of the plate to lean protein. This encompasses lean meats such as chicken and"
                   " fish. Notably, certain cuts of red meat can also be lean, particularly those labeled 'loin,' like "
                   "pork or beef tenderloin. While protein is essential for growth and development, it's important to "
                   "avoid excessive protein consumption, as it can lead to extra calories and fat. Vegetarian options "
                   "like beans, legumes, and tofu are also suitable choices for this portion of the plate. ")
          st.write("### ")
          st.write("4.Opt for water or skim/1% fat milk over sugary beverages. Sweetened drinks like lemonade, fruit "
                   "punch, sweet tea, soft drinks, sports drinks, and energy drinks should be replaced with healthier"
                   " options. While sports drinks have a place during outdoor exercise, they are not suitable as"
                   " beverages during meals. It's worth noting that 2% milk is not recommended; instead, transition to"
                   " truly low-fat or fat-free milk options. ")
          st.write("### ")
          st.write("5.Use smaller plates for children, especially those aged 7 and younger. Consider utilizing salad"
                   " plates to ensure appropriate portion sizes. Serving children from large dinner plates can lead to"
                   " overeating. ")
          st.write("### ")
          st.write("In summary, the USDA has replaced the Food Guide Pyramid with the more user-friendly MyPlate "
                   "approach. This new method emphasizes consuming more vegetables and fruits, choosing whole grains,"
                   " incorporating lean protein, opting for healthier beverages, and being mindful of portion sizes,"
                   " especially for children. ")

  col_left, col_right = st.columns([1, 2])
  with col_left:
      st.image(img_TGFU)
  with col_right:
      st.title("What is Teaching Games for Understanding?")

      with st.expander("The Teaching Games for Understanding (TGfU) strategy emerged from the efforts of researchers "
                       "at Loughborough University in the United Kingdom, aiming to tap into children's innate "
                       "inclination for play."):
          st.write(
              "Bunker and Thorpe (1982) conceptualized TGfU as a method to instruct children in games by immersing them"
              " in gameplay. This approach revolves around inquiry-based education, prioritizing decision-making within"
              " the context of games over the mere refinement of skills..")

          st.write("### ")

          st.write(
              "TGfU champions a learner-centric approach that centers on the needs and capacities of the participants."
              " It elevates students' enjoyment and engagement levels while furnishing them with the proficiencies "
              "necessary for adeptness in a broad spectrum of physical activities. Instructors are encouraged to "
              "introduce games before delving into skill acquisition, under the premise that participants possess "
              "inherent intelligence. Instead of having participants play full-fledged adult versions of sports, games "
              "are simplified to align with the skill levels of the participants, ensuring an appropriate challenge."
              "Butler et al. (2008) identified six fundamental concepts underpinning the Teaching Games for Understanding"
              "approach: ")
          st.write("1.Instruct games through the medium of games themselves. ")

          st.write("2.Dissect games into their most basic formats, progressively augmenting complexity. ")

          st.write("3.Acknowledge participants as adept performers within games ")

          st.write("4.Value the importance of each learner's engagement and involvement. ")

          st.write("5.Foster participants' comprehension of the subject matter.. ")

          st.write("6.Harmonize participants' skill levels with the challenges posed. ")

          st.write("TThe TGfU cycle comprises six key stages: ")
          st.write(
              "1.Game Focus: Learning transpires within a game environment where educators guide students through a "
              "modified version of the game, complete with rules intended to enhance both skills and tactical "
              "acumen. ")

          st.write("2.Game Appreciation: By partaking in modified games, learners develop an appreciation for the rules"
                   " that shape gameplay. ")

          st.write("3.Tactical Awareness: Through gameplay, students are prompted to discern offensive and defensive "
                   "strategies and execute successful tactical maneuvers.")

          st.write("4.Decision Making: Participants learn and apply decision-making in real-time, responding to varying"
                   " scenarios. ")

          st.write("5.Skill Execution: Students identify and practice the requisite skills to elevate their gameplay "
                   "within the context of the game. ")

          st.write(
              "6.Performance: Opportunities are provided for students to amalgamate skills, exercise decision-making,"
              " and employ tactics during actual gameplay situations. ")

          st.write("Thematic Approach: TGfU advocates a thematic pedagogical approach to games instruction. Rather than"
                   " focusing solely on sport-specific units (e.g., volleyball, soccer), students acquire versatile "
                   "skills and knowledge applicable to diverse sports through engagement with various games categorized"
                   " as follows: ")
          st.write("1.Invasion/Territorial Games ")
          st.write("2.Striking & Fielding Games ")
          st.write("3.Net & Wall Games")
          st.write("4.Target Games ")
          st.write("These categories encompass games and activities with shared structural traits. Exposure to the"
                   " primary rules, fundamental skills, and tactical challenges inherent to each category equips "
                   "children and youth with literacy in a spectrum of games, activities, and sports. This broadens their"
                   " understanding and proficiency in the associated skills and tactics ")
          st.write("### ")
          st.write(
              "In adopting a games-based approach, the intention is to stimulate critical thinking, decision-making,"
              " and problem-solving among participants, facilitating learning within and through play. The focus is "
              "on immersing participants in scenarios where decision-making and problem-solving are integral to "
              "successful game performance. This is facilitated through thoughtful questioning aimed at stimulating "
              "strategic thought about the game. Interjecting games with periodic pauses enables participants to "
              "reflect on their gameplay and explore avenues for enhanced performance.")
          st.write("### ")
          st.write(
              "A lesson guided by the TGfU methodology diverges from a conventional physical education class. "
              "The conventional model incorporates warm-up exercises, followed by skill drills, culminating in a game."
              " It assumes that once participants grasp the requisite motor skills, they will excel in the game. In "
              "contrast, the TGfU approach accentuates play, presenting participants with challenges to surmount, "
              "necessitating decision-making. Instructors employ queries and game modifications to prompt students, "
              "eschewing the traditional approach of imparting isolated skills and game regulations.")


elif selected == "Activities and Games":
  st.title(f'{selected}')
  col_left, col_right = st.columns([1, 2])
  with col_left:
      st.image(img_TGFU)
  with col_right:
      st.title("What is Teaching Games for Understanding?")

      with st.expander("The Teaching Games for Understanding (TGfU) strategy emerged from the efforts of researchers "
                       "at Loughborough University in the United Kingdom, aiming to tap into children's innate "
                       "inclination for play."):
          st.write(
              "Bunker and Thorpe (1982) conceptualized TGfU as a method to instruct children in games by immersing them"
              " in gameplay. This approach revolves around inquiry-based education, prioritizing decision-making within"
              " the context of games over the mere refinement of skills..")

          st.write("### ")

          st.write(
              "TGfU champions a learner-centric approach that centers on the needs and capacities of the participants."
              " It elevates students' enjoyment and engagement levels while furnishing them with the proficiencies "
              "necessary for adeptness in a broad spectrum of physical activities. Instructors are encouraged to "
              "introduce games before delving into skill acquisition, under the premise that participants possess "
              "inherent intelligence. Instead of having participants play full-fledged adult versions of sports, games "
              "are simplified to align with the skill levels of the participants, ensuring an appropriate challenge."
              "Butler et al. (2008) identified six fundamental concepts underpinning the Teaching Games for Understanding"
              "approach: ")
          st.write("1.Instruct games through the medium of games themselves. ")

          st.write("2.Dissect games into their most basic formats, progressively augmenting complexity. ")

          st.write("3.Acknowledge participants as adept performers within games ")

          st.write("4.Value the importance of each learner's engagement and involvement. ")

          st.write("5.Foster participants' comprehension of the subject matter.. ")

          st.write("6.Harmonize participants' skill levels with the challenges posed. ")

          st.write("TThe TGfU cycle comprises six key stages: ")
          st.write("1.Game Focus: Learning transpires within a game environment where educators guide students through a "
                   "modified version of the game, complete with rules intended to enhance both skills and tactical "
                   "acumen. ")

          st.write("2.Game Appreciation: By partaking in modified games, learners develop an appreciation for the rules"
                   " that shape gameplay. ")

          st.write("3.Tactical Awareness: Through gameplay, students are prompted to discern offensive and defensive "
                   "strategies and execute successful tactical maneuvers.")

          st.write("4.Decision Making: Participants learn and apply decision-making in real-time, responding to varying"
                   " scenarios. ")

          st.write("5.Skill Execution: Students identify and practice the requisite skills to elevate their gameplay "
                   "within the context of the game. ")

          st.write("6.Performance: Opportunities are provided for students to amalgamate skills, exercise decision-making,"
                   " and employ tactics during actual gameplay situations. ")


          st.write("Thematic Approach: TGfU advocates a thematic pedagogical approach to games instruction. Rather than"
                   " focusing solely on sport-specific units (e.g., volleyball, soccer), students acquire versatile "
                   "skills and knowledge applicable to diverse sports through engagement with various games categorized"
                   " as follows: ")
          st.write("1.Invasion/Territorial Games ")
          st.write("2.Striking & Fielding Games ")
          st.write("3.Net & Wall Games")
          st.write("4.Target Games ")
          st.write("These categories encompass games and activities with shared structural traits. Exposure to the"
                   " primary rules, fundamental skills, and tactical challenges inherent to each category equips "
                   "children and youth with literacy in a spectrum of games, activities, and sports. This broadens their"
                   " understanding and proficiency in the associated skills and tactics ")
          st.write("### ")
          st.write("In adopting a games-based approach, the intention is to stimulate critical thinking, decision-making,"
                   " and problem-solving among participants, facilitating learning within and through play. The focus is "
                   "on immersing participants in scenarios where decision-making and problem-solving are integral to "
                   "successful game performance. This is facilitated through thoughtful questioning aimed at stimulating "
                   "strategic thought about the game. Interjecting games with periodic pauses enables participants to "
                   "reflect on their gameplay and explore avenues for enhanced performance.")
          st.write("### ")
          st.write(
              "A lesson guided by the TGfU methodology diverges from a conventional physical education class. "
              "The conventional model incorporates warm-up exercises, followed by skill drills, culminating in a game."
              " It assumes that once participants grasp the requisite motor skills, they will excel in the game. In "
              "contrast, the TGfU approach accentuates play, presenting participants with challenges to surmount, "
              "necessitating decision-making. Instructors employ queries and game modifications to prompt students, "
              "eschewing the traditional approach of imparting isolated skills and game regulations.")


elif selected == 'Stations and Circuits':
  st.title(f'{selected}')
elif selected == 'Fitness Activities':
    st.title(f'{selected}')
    col_left, col_right = st.columns([1, 2])
    with col_left:
        st.image(img_title)
    with col_right:
        st.title("Exploring the Effects of Exercise on Your Body: A Guide for Physical Education Teachers")
        st.write("###")
        with st.expander("Understanding how exercise affects our bodies is really important for physical education"
                         " teachers. It helps them create lessons that encourage fitness, teach students about the "
                         "health benefits of being active, and inspire habits that last a lifetime. In this article,"
                         " we'll explore what happens to our bodies when we exercise."):

                    with st.container():
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.write(" ")
                        with col2:
                            st.subheader("'My heart beats faster'")
                        with col3:
                            st.write(" ")
                    with st.container():
                        col1, col2 = st.columns([1, 2], gap='large')
                        with col1:
                            st.write(" ")
                        with col2:
                            st.image(img_heartfast)
                        st.write(
                                "When we exercise, our heart beats faster to provide more oxygen and nutrients to our muscles. "
                                "This helps our muscles have the energy they need to do the exercise. The cardiovascular system, "
                                "which includes the heart, helps keep everything in balance by adjusting the heart rate based on "
                                "the intensity of the exercise.")

                    with st.container():
                        col1, col2 = st.columns([1,2])
                        with col1:
                             st.write("### ")
                             st.write("### ")
                             st.image(img_water)

                        with col2:
                            st.subheader("'I start to sweat and get Thirsty'")



                            st.write (
                             "As we exercise, our body temperature goes up, and we start to sweat. Sweating is our body's " 
                             "way of cooling down and preventing overheating. The sweat comes out of our skin and then evaporates," 
                             " which cools us down and helps keep our body temperature stable even when we're doing a tough workout " 
                             "When we sweat, we also lose water from our body. That's why we feel thirsty when we exercise. Drinking " 
                             "enough water is really important during exercise because it helps our body work properly. It helps" 
                            " regulate our temperature and makes sure our blood flows well.")

                    with st.container():
                        col1, col2,  = st.columns([1, 2])
                        with col1:
                            st.write("### ")
                            st.write("### ")
                            st.write("### ")
                            st.image(img_happy)

                        with col2:
                            st.subheader("'My Brain Produces Endorphins'")

                            st.write("### ")
                            st.write("### ")


                            st.write("When we exercise, our brain releases chemicals called endorphins. These chemicals act like"
                                " natural painkillers and make us feel happier. You might have heard of the 'runner's high."
                                " It's when people feel really good after exercising because of the endorphins. So exercise "
                                "not only helps our bodies, but it also boosts our mood and makes us feel good.")

                    with st.container():
                        col1, col2,  = st.columns([1, 2])
                        with col1:
                            st.write("### ")
                            st.write("### ")
                            st.write("### ")
                            st.image(img_breath)

                        with col2:
                            st.subheader("'I Breathe Harder'")

                            st.write("### ")
                            st.write("### ")
                            st.write("Breathing also changes when we exercise. We breathe faster and deeper to get more oxygen "
                                     "into our body. This helps our muscles get the oxygen they need and get rid of waste products "
                                    "like carbon dioxide.")

                    with st.container():
                        col1, col2, = st.columns([1, 2])
                        with col1:
                            st.write("### ")
                            st.write("### ")
                            st.write("### ")
                            st.image(img_brain)

                        with col2:
                            st.subheader("'Blood Flow Increases to My Brain'")

                            st.write("### ")
                            st.write("### ")
                            st.write("Exercise also increases blood flow to our brain. This means our brain gets more oxygen and"
                             " nutrients, which makes it work better. It can improve our memory, focus, and overall brain"
                             " function. So exercise is good for our brain too.")
                    with st.container():
                        col1, col2, = st.columns([1, 2])
                        with col1:
                            st.write("### ")
                            st.write("### ")
                            st.write("### ")
                            st.image(img_muscle)



                        with col2:
                            st.subheader("'Blood Flow Increases to My Muscles'")


                            st.write("### ")
                            st.write("### ")
                            st.write("When we exercise, more blood flows to our muscles. This helps them get more oxygen and "
                                     "nutrients, which they need to work properly. After exercise, the increased blood flow also"
                                     " helps remove waste products from our muscles, like lactic acid, which can make our muscles "
                                    "sore.")
                    with st.container():
                        col1, col2, = st.columns([1, 2])
                        with col1:
                            st.write("### ")
                            st.write("### ")
                            st.write("### ")
                            st.image(img_bones)

                        with col2:
                            st.subheader("'Increased Pressure to My Bones'")

                            st.write("### ")
                            st.write("### ")

                            st.write("Some exercises put pressure on our bones, like when we use our body weight to do certain"
                                 " movements. This pressure actually helps our bones become stronger and denser. It's like "
                                "giving our bones a workout too, and it reduces the risk of conditions like osteoporosis,"
                                " which makes our bones weak and fragile.")
                    with st.container():
                        col1, col2,  = st.columns([1, 2])
                        with col1:
                            st.write("### ")
                            st.write("### ")
                            st.write("### ")
                            st.image(img_tired2)

                        with col2:
                            st.subheader("'I Get a Tired Feeling'")

                            st.write("### ")
                            st.write("### ")
                            st.write("During exercise, our muscles can get tired. This is normal because they're working harder"
                                     " and using up energy. They may also get little tears in the fibers, which can make them "
                                    "feel sore later on. But don't worry, this is all part of the process, and it helps our "
                                    "muscles get stronger. As we keep exercising, our body becomes more efficient, and we won't "
                                     "feel as tired or sore over time.")
                    with st.container():
                        col1, col2,  = st.columns([1, 2])
                        with col1:
                            st.write("### ")
                            st.write("### ")
                            st.write("### ")
                            st.image(img_talk)

                        with col2:
                            st.subheader("'It Gets Difficult to Talk'")

                            st.write("### ")
                            st.write("### ")
                            st.write("When we exercise harder, it becomes more difficult to talk because we need more oxygen."
                                     " Our breathing gets heavier, and we need to use that oxygen for our muscles, so talking"
                                    " becomes a challenge. This is called the 'talk test,' and it's a way to know how intense "
                                    "our exercise is by seeing if we can talk comfortably or not.")



                    st.write("In summary, exercise has many benefits for our bodies and minds. It helps our muscles, "
                             "heart, and brain work better. It also keeps our bones strong and maintains a healthy weight. "
                             "Physical education teachers can share this knowledge with students and help them understand "
                             "why exercise is important. By teaching about the benefits of exercise, they can inspire "
                             "students to be active and live healthy lives.")



elif selected == 'Health and Nutrition':
  st.title(f'{selected}')
  col_left, col_right = st.columns([1, 2])
  with col_left:
      st.image(img_myplate)
  with col_right:
      st.title("MyPlate For Our Children")
      st.write("###")
      with st.expander("The Food Guide Pyramid was recently discontinued by the USDA, and in its place, the more"
                       " user-friendly MyPlate has been introduced.MyPlate method offers several notable benefits "
                       "compared to the phased-out pyramid. Here are the main takeaways:"):


          st.write(
              "1. Increase your intake of vegetables and fruits. It's important to introduce children to a variety "
              "of options. Just because a child doesn't immediately enjoy a particular vegetable like broccoli doesn't"
              " mean they won't ever develop a liking for it. Keep offering different options, especially when your"
              " child is hungry. Aim for half of the plate to consist of fruits and vegetables. If you're pressed for"
              " time or on a tight budget, consider using canned or frozen produce – they're better choices than none"
              " at all. Remember, the vibrant colors of fruits and vegetables indicate the presence of beneficial "
              "phytochemicals, in addition to essential vitamins and minerals. These foods also provide important fiber"
              " and fluids for children. Even at fast-food or quick-service restaurants, you can apply these principles"
              " by making mindful choices.. ")
          st.write("### ")

          st.write(
              "2. Prioritize whole grains. This includes foods like 100% whole wheat bread, oatmeal, and even popcorn."
              " About a quarter of the plate should be occupied by grains and starches. If your child isn't fond of"
              " whole wheat pasta, you can explore brands that offer a blend of whole wheat and white flour. ")
          st.write("### ")
          st.write("3.Allocate a quarter of the plate to lean protein. This encompasses lean meats such as chicken and"
                   " fish. Notably, certain cuts of red meat can also be lean, particularly those labeled 'loin,' like "
                   "pork or beef tenderloin. While protein is essential for growth and development, it's important to "
                   "avoid excessive protein consumption, as it can lead to extra calories and fat. Vegetarian options "
                   "like beans, legumes, and tofu are also suitable choices for this portion of the plate. ")
          st.write("### ")
          st.write("4.Opt for water or skim/1% fat milk over sugary beverages. Sweetened drinks like lemonade, fruit "
                   "punch, sweet tea, soft drinks, sports drinks, and energy drinks should be replaced with healthier"
                   " options. While sports drinks have a place during outdoor exercise, they are not suitable as"
                   " beverages during meals. It's worth noting that 2% milk is not recommended; instead, transition to"
                   " truly low-fat or fat-free milk options. ")
          st.write("### ")
          st.write("5.Use smaller plates for children, especially those aged 7 and younger. Consider utilizing salad"
                   " plates to ensure appropriate portion sizes. Serving children from large dinner plates can lead to"
                   " overeating. ")
          st.write("### ")
          st.write("In summary, the USDA has replaced the Food Guide Pyramid with the more user-friendly MyPlate "
                   "approach. This new method emphasizes consuming more vegetables and fruits, choosing whole grains,"
                   " incorporating lean protein, opting for healthier beverages, and being mindful of portion sizes,"
                   " especially for children. ")


elif selected == 'P.E. Community':
  st.title(f'{selected}')

  col_left, col_right = st.columns([1, 2])
  with col_left:
      st.image(img_10topwebsites)
  with col_right:
      st.title("10 Top Quality PE Websites:Essential Resources for Physical Education Teachers")

      with st.expander("Physical Education is an essential subject that promotes physical activity and healthy "
                       "lifestyles among students. As PE's importance continues to grow, it is now more crucial "
                       "than ever for aspiring and practicing PE teachers to have access to credible and innovative "
                       "resources. "):
          st.write("With the internet being a primary source of information today, there are several "
                       "websites that provide valuable resources for physical education and health teachers to take "
                       "advantage of. Some of these websites have been around for a while, while others are relatively"
                       " new.")
          st.header("Top 10 PE Websites for 2023")
          st.write('We have handpicked a collection of websites that excel in features, user-friendliness, and '
                   'high-quality content for physical education. These selected websites offer a wealth of valuable '
                   "resources for PE teachers. To give you a glimpse of each site's strengths, we've provided a "
                   "brief paragraph highlighting their notable features and included a link for your convenience.")
          st.markdown("**:blue[1.PhysEd Games ]**")
          st.markdown(" **:blue[2.The PE Specialist ]** ")
          st.markdown(" **:blue[3.Cap'n Pete's Power PE ]** ")
          st.markdown(" **:blue[4.PE Central ]** ")
          st.markdown(" **:blue[5.iPhysEd.com ]** ")
          st.markdown(" **:blue[6.OPENPhysEd.org  ]** ")
          st.markdown(" **:blue[7.prime coaching sport ]** ")
          st.markdown(" **:blue[8.Sport Australia ]** ")
          st.markdown(" **:blue[9.phys ed depot]** ")
          st.markdown(" **:blue[10.CanadaGo4Sport ]** ")
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['PhysEd Games' ](https://www.https://physedgames.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_PhysEdGames)
              st.write("PhysEd Games is a valuable website specifically designed for physical education teachers "
                       "and professionals seeking game ideas to make their PE classes more exciting and interactive."
                       " With a vast collection of free game videos, the site offers a diverse range of options to "
                       "engage and motivate students. Each video is accompanied by a written explanation, providing"
                       " details on the game's suitability for different grade levels, required equipment, and a brief"
                       " description. PhysEd Games covers a wide spectrum of activities, including fun games,"
                       " sport-themed activities, and team-building exercises that can be customized to suit various"
                       " age groups.")
              st.write("####")

              st.markdown(
                  ":blue[Best Attributes: PhysEd Games stands out as an exceptional resource for PE teachers seeking"
                       " visually-driven content through its video depictions of engaging activities. The videos are "
                       "user-friendly, offering clear and concise instructions that are easy to follow. This makes it"
                       " an ideal platform for educators looking to enhance their teaching repertoire and bring more"
                       " excitement to their physical education classes.")

              with col3:
                  st.write(" ")

          #P.E. SPECIALIST
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['The PE Specialist' ](https://www.https://physedgames.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_specialist)
              st.write("The PE Specialist, founded by Ben Landers @thepespecialist, is a comprehensive website "
                       "dedicated to supporting physical education teachers with a wide range of resources. "
                       "This platform offers valuable classroom management strategies, lesson ideas, unit overviews,"
                       " teaching tips, technology resources, games and activities, music and dance content, virtual"
                       " teaching tips, and much more. Ben, an experienced physical education teacher, shares his "
                       "expertise through an extensive PE blog and a podcast that offers practical insights for both"
                       " new and experienced educators. The site also features a membership program, granting access "
                       "to exclusive member forums and unlimited downloadable content and resources..")
              st.write("####")

              st.markdown(":blue[Best Attributes:] The PE Specialist excels in providing an abundance of resources and strategies"
                       " to assist physical educators in meeting their students' needs. Moreover, the site serves as a"
                       " valuable source for staying informed about the latest trends in physical education and offers "
                       "valuable advice for navigating the art of teaching PE..")

              with col3:
                  st.write(" ")






          # CAPT'S PETE'S P.E.
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['Cap'n Pete's Power PE' ](https://www.capnpetespowerpe.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='small')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_Capt)
              st.write(
                  "Cap'n Pete's Power PE, founded by Pete Charrette (@capnpetespe), is an online platform designed to"
                  " support both aspiring and practicing physical education teachers in enhancing their instructional "
                  "approach. This website offers a wide range of tools, information, and resources to help educators"
                  " create and maintain exceptional physical education programs. The blog section provides valuable "
                  "insights and practical tips, while the standout feature is the availability of free downloadable "
                  "resources that can be seamlessly incorporated into PE classes. Additionally, Cap'n Pete's Power PE "
                  "boasts an extensive library of over 750 resources, including PE activities, games, field day materials,"
                  " virtual PE resources, templates, visuals, posters, sign packages, PowerPoint presentations, and much"
                  " more. It serves as a comprehensive hub for all things related to physical education and health.")
          #P.E Central
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['P.E Central' ](https://www.https://www.pecentral.org/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='small')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_PEcentral)
              st.write(
                  "PE Central is a well-established and all-encompassing physical education website that stands"
                  " out among its counterparts. It boasts a vast collection of teaching practices, lesson ideas, "
                  "assessment strategies, skill and fitness challenges, and resources tailored to adapted physical"
                  " education across various grade levels. Furthermore, PE Central offers a range of online courses"
                  " and resources that support the growth and professional development of physical education teachers."
                  " The website is also home to a comprehensive video library featuring dances, lessons, and more,"
                  " as well as numerous bulletin board ideas to enhance the aesthetics of gymnasiums or classrooms.")
              st.markdown(
                  ":blue[Best Attributes:] Over the years, PE Central has proven to be an invaluable resource for"
                  " physical and health educators, coaches, and fitness professionals. Its extensive library of lessons"
                  " and activities provides endless possibilities, and the best part is that everything is freely"
                  " accessible and truly remarkable!")

          #iPhysEd.com
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['iPhysEd' ](https://www.iphys-ed.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='small')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_iPhysEd)
              st.write(
                  "iPhysEd.com, developed by Nathan Horne @PEnathan, is a dedicated online platform designed to empower"
                  " physical educators and coaches with the necessary tools to deliver high-quality and purposeful"
                  " physical education experiences to their communities. This website offers a wide array of innovative"
                  " and captivating resources that can greatly enhance the instruction and promotion of physical activity"
                  " among students. From free assessment tools and game resources to visually appealing materials, "
                  "iPhysEd.com equips PE teachers with everything they need to create engaging and effective physical "
                  "education lessons. Additionally, the platform hosts a library of online courses facilitated by "
                  "renowned physical educators from around the world..")
              st.markdown(
                  ":blue[Best Attributes:] iPhysEd.com stands out as a comprehensive online resource that fuels the "
                  "creativity and effectiveness of PE teachers. It provides a wealth of ideas, tools, and support to "
                  "facilitate engaging and impactful physical education experiences. The availability of online courses"
                  " ensures continuous professional growth, while the free assessment tools and visuals serve as "
                  "invaluable resources to enhance PE instruction and create a vibrant learning environment.")

           #OPENPhysEd.org
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['OPENPhysEd' ](https://openphysed.org/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_openPhys)
              st.write(
                  "The website OPEN (Online Physical Education Network), created by Aaron Hart @nyaaronhart, is a"
                  " valuable online platform that provides high-quality and free physical education resources for K-12"
                  " educators and students. With a wide range of offerings including lesson plans, assessments, "
                  "skill-based activities, and fitness challenges, OPEN aims to enhance students' physical literacy and "
                  "overall health. The mission of OPENPhysEd.org is to empower educators by equipping them with the"
                  " necessary tools and resources to promote active and healthy lifestyles, while delivering exceptional"
                  " physical education to all students, regardless of their background or ability level. The website's "
                  "user-friendly interface and adaptable materials enable educators to customize lessons and create"
                  " inclusive, engaging, and safe learning environments tailored to their students' needs. Additionally,"
                  " OPEN offers an extensive array of professional development initiatives, designed to elevate teacher "
                  "performance and foster student growth.")
              st.markdown(
                  ":blue[Best Attributes:] OPEN sets itself apart through its commitment to providing free and easily "
                  "accessible resources. Their library encompasses a comprehensive collection of standards-based"
                  " materials suitable for all levels of teaching. Furthermore, OPEN is supported by a team of national"
                  ""
                  " trainers who deliver unparalleled professional development opportunities for physical educators,"
                  " health teachers, and other classroom-based professionals.")

          #prime coaching sport
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['prime coaching sport' ](https://www.primecoachingsport.com/h)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_PRIMECOACHING)
              st.write(
                  "Prime Coaching Sport, developed by Coach Dale Sidebottom, is a comprehensive website providing "
                  "coaches and physical education teachers with valuable resources. Its extensive collection of "
                  "engaging lesson plans saves educators time and ensures purposeful sessions. The website offers "
                  "diverse game ideas and activities for skill development and teamwork. With a focus on professional"
                  " development, Prime Coaching Sport provides articles, videos, and online courses to enhance coaching"
                  " techniques. Its user-friendly interface allows easy navigation, making lesson planning and"
                  " preparation a seamless experience. It equips educators with tools to deliver high-quality coaching "
                  "and instruction.")
              st.markdown(
                  ":blue[Best Attributes:] Extensive collection of engaging lesson plans,Diverse game ideas and "
                  "activities for skill development, Focus on professional development with articles, videos,"
                  " and online courses,User-friendly interface for easy navigation,Valuable resources for coaches"
                  " and physical education teachers")

          #Sport Australia
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['Sport Australia' ](https://www.sportaus.gov.au/sports_ability)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_sportsAustralia)
              st.write(
                  "As the official website of Australia's premier agency for sport and physical activity, Sport"
                  " Australia offers a wealth of resources, information, and services to foster the growth of sports"
                  " and physical activity across the country. One notable section, Sports Ability, presents activity"
                  " cards designed to be inclusive and accessible to individuals of all abilities. These cards empower "
                  "children by equipping them with the necessary skills to excel in sports while bolstering their"
                  " confidence and motivation. Each card provides detailed instructions for organizing and conducting"
                  " activities, along with insights on adapting elements to ensure the participation of all children. "
                  "By modifying game rules, equipment, and techniques, these cards create enjoyable and rewarding"
                  " opportunities for everyone to engage in sports and achieve success.")
              st.markdown(
                  ":blue[Best Attributes:] Sport Australia's Sports Ability cards stand out for their accessibility and"
                  " user-friendly nature."
                  " Available for free download, these cards offer a comprehensive package of information, including"
                  " setup instructions, required equipment, skill focus, rules, teaching style, safety considerations,"
                  " environmental needs, and student engagement questions. This level of detail makes them particularly "
                  "well-suited for elementary and middle school physical education teachers, providing a valuable "
                  "resource that is easy to understand and implement.")

          #phys ed depot
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['The Phys. Ed. Depot' ](http://www.physeddepot.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_Thephyseddepot)
              st.write(
                  "The Phys. Ed. Depot is a remarkable website that offers a wealth of resources and materials "
                  "for physical education professionals. With a diverse range of tools and content, this website is "
                  "a go-to destination for educators seeking to enhance their physical education programs. The site"
                  " features a vast collection of lesson plans, activity ideas, assessment tools, and curriculum"
                  " resources that are suitable for various grade levels. Additionally, The Phys. Ed. Depot provides "
                  "interactive games, fitness challenges, and instructional videos that engage students and promote "
                  "active participation.")
              st.markdown(
                  ":blue[Best Attributes:] One of the standout features of The Phys. Ed. Depot is its extensive "
                  "library of ready-to-use resources. These materials are well-organized and easily accessible,"
                  " saving educators valuable time in lesson planning and preparation. The website also offers a "
                  "supportive community where teachers can share ideas, collaborate, and seek advice from fellow"
                  " professionals. With its user-friendly interface and comprehensive content, The Phys. Ed. Depot serves"
                  " as a valuable resource hub that empowers physical education teachers to deliver high-quality and "
                  "engaging lessons that promote lifelong fitness and healthy lifestyles."
                  )
          #CanadaGo4Sport
          with st.container():
              col1, col2, col3 = st.columns(3)
              with col1:
                  st.write(" ")
              with col2:
                  st.subheader("['CanadaGo4Sport' ](https://www.canadago4sport.com/)")

              with col3:
                  st.write(" ")
          with st.container():
              col1, col2 = st.columns([1, 2], gap='large')
              with col1:
                  st.write(" ")
              with col2:
                  st.image(img_canada)
              st.write(
                  "CanadaGo4Sport is a dynamic website dedicated to promoting physical literacy and active living "
                  "among children and youth in Canada. It offers an extensive array of resources and tools aimed at"
                  " parents, teachers, and community leaders, empowering them to foster physical activity and healthy"
                  " lifestyles in children. The website boasts a diverse range of physical literacy resources, "
                  "encompassing lesson plans, activity ideas, games, and videos carefully designed to cultivate "
                  "fundamental movement skills like running, jumping, throwing, and catching. Additionally, "
                  "CanadaGo4Sport provides valuable guidance on physical activity guidelines, safety considerations,"
                  " and inclusive practices to ensure children of all abilities can participate. Serving as a central "
                  "hub for information and resources on physical literacy and active living, CanadaGo4Sport inspires and "
                  "educates children, encouraging them to embrace healthy and active lives.")
              st.markdown(
                  ":blue[Best Attributes:] Canada Go 4 Sport stands out as an invaluable resource for teachers and "
                  "physical education professionals seeking to foster physical literacy and active living among children "
                  "in Canada and beyond. Its user-friendly homepage offers a wealth of resources, including "
                  "well-structured lesson plans with clear instructions, as well as instructional videos covering "
                  "various aspects of physical education. Whether you're looking for engaging activities or "
                  "comprehensive guidance, Canada Go 4 Sport provides the tools necessary to inspire and educate "
                  "students, making it an essential destination for promoting a healthy and active lifestyle.")


elif selected == 'Class Management':
  st.title(f'{selected}')
  col_left, col_right = st.columns([1, 2])
  with col_left:
      st.image(img_responsive)
  with col_right:
      st.title("Responsive Classroom (Student-Centered Approach)")
      st.write("###")
      with st.expander("The Responsive Classroom is a well-established and evidence-based student-centered approach "
                       "to teaching. With a focus on engaging academics, fostering a positive community, effective "
                       "management, and developmental awareness, it has been in existence for over 40 years, originally"
                       " starting as an education research lab school."):

              st.write(
                  "When it comes to teaching and parenting, there are four main approaches, which share similar"
                  " principles:.")

              st.write("### ")

              st.write(
                  "1. Authoritarian:"
                  "This approach believes in strict obedience without considering the child's opinions"
                  " or feelings."
                  "Authoritarians enforce rules without negotiation and might say, 'Because I said so,' when questioned."
                  "They do not involve children in problem-solving challenges and rely on punishments rather than "
                  "teaching better choices.Children raised under authoritarian parents may follow rules, but their "
                  "self-esteem can suffer due to their opinions being undervalued. They may also become hostile or "
                  "resort to lying to avoid punishment. ")
              st.write("### ")

              st.write(
                  "2. Authoritative (Responsive Classroom):"
                  "The authoritative approach involves creating and maintaining positive relationships with children and"
                  " explaining the reasons behind rules.While enforcing rules and consequences, authoritative "
                  "individuals consider the child's feelings and validate their emotions.They invest time and energy "
                  "in preventing behavior problems and use positive discipline strategies, such as praise and rewards."
                  "Children raised with authoritative discipline tend to be happy, successful, and capable of making "
                  "decisions and assessing safety risks independently. They feel comfortable expressing their opinions"
                  "and grow into responsible adults. ")
              st.write("### ")
              st.write("3.Permissive:"
                       "Permissive individuals set rules but may not consistently enforce them.Consequences are"
                       " infrequent and may not be firmly applied.They adopt an attitude of leniency, believing that"
                       " 'kids will be kids.'Permissive parents often take on a friend-like role and encourage children"
                       " to talk about their problems. However, they may not actively discourage poor choices or bad "
                       "behavior.Children raised with permissive parenting may struggle academically, exhibit behavioral"
                       " problems, have low self-esteem, and face health issues due to a lack of structure and limits. ")
              st.write("### ")
              st.write("4.Uninvolved/Neglectful:"
                       "Uninvolved parents have little knowledge of their children's activities and provide minimal"
                       " guidance, nurturing, and attention.They may expect children to raise themselves and don't "
                       "devote much time or energy to meeting their basic needs.Uninvolved parents may unintentionally"
                       " neglect their children due to mental health issues, substance abuse problems, lack of knowledge "
                       "about child development, or other overwhelming challenges.Children with uninvolved parents tend "
                       "to experience self-esteem issues, perform poorly in school, exhibit behavioral problems, and "
                       "have lower levels of happiness. ")
              st.write("### ")
              st.write("The Responsive Classroom applies the authoritative approach, which has garnered support from"
                       " 98% of scientific research as the most effective. It adapts this approach to teaching rather"
                       " than parenting, allowing teachers to seamlessly integrate student-centered practices into their"
                       " daily teaching routines ")
              st.write("I highly recommend the book 'Responsive Classroom for Music, Art, PE, and Other Special Areas'"
                       "The book written by special area teachers offers practical advice, examples, and strategies to"
                       " create a positive and engaging classroom environment, leading to better learning outcomes for "
                       "students. ")
              col_1, col_2 = st.columns(2)
              with col_1:
                  st.write("Here's a 1-hour webinar by Rachel Atzert about responsive classroom")
              with col_2:
                  st.write("[Rachel Atzert Webinar >](https://www.youtube.com/watch?v=NHGaXDUMNQc)")