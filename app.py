from pathlib import Path
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

EMAIL = "harrisongetchell@gmail.com"

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

SOCIAL_MEDIA = {
    ":link: LinkedIn": "https://www.linkedin.com/in/harrison-getchell-744386237/",
    ":link: Github": "https://github.com/HSG16",
    ":link: Discord": "https://discord.com/channels/@me",
    ":link: Instagram": "https://www.instagram.com/harrisongetch/?next=%2Fbgc_ventura%2F&hl=en",
    

}

local_css("style/style.css")

lottie_coding = load_lottieurl("https://lottie.host/2c498441-24cc-486b-aa83-497ec86f5963/dy7DrLLaso.json")
img_sccc = Image.open("images/SCCC.png")
img_pgh = Image.open("images/PGH.png")
img_gym = Image.open("images/gym.png")
img_ext = Image.open("images/ext.png")

# --- Introduction ---
with st.container():
    st.subheader("Hi, I'm Harrison Getchell! :wave:")
    st.title("A Computer Science Major :computer:  and Business Minor :briefcase:  Looking for Internship Opportunities for The Summer of 2024")
    st.write(":email:", EMAIL)
# --- Social Media ---#
    st.write("#")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


# --- Who I am ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who I Am ")
        st.write('##')
        st.write(
            """
            I am a second-year student at the University of Pittsburgh pursuing a major in computer science and a minor in business.
            Ever since I was a child, I've had a passion for learning how things work and the inner workings of large systems.
            This is where I discovered my passion for coding. As I grew older, I began to discover my love for not only coding
            but the stock market and investing as well. This is where I learned of investment banking and managing money. Being 
            interested in both coding and investing made me decide to pursue a major in computer science and minor in business. 
            I believe learning and mastering both degrees will allow me to pursue a career in a field that allows me to showcase
            my skills in the world of computer science and business in the landscape of finance and technology driven industries.
            I am seeking any internship opportunities for the summer of 2024 so feel free to contact me via any of the provided 
            links above! Thank you so much for taking the time to read and learn more about me!

            """
        
        )
        with right_column:
            st_lottie(lottie_coding, height=400, key = "coding")

# --- Extended Resume ---
with st.container():
    st.write("---")
    st.header("Extended Resume")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_pgh)
    with text_column:
        st.subheader(":cityscape: Where I Live")
        st.write(
            """
            I was born and raised in Pittsburgh, PA. I grew up loving sports and being a huge Steelers, Pirates, and Penguins fan.
            My dream was to attend Pitt for academics which I was able to accomplish. I always loved learning the inner workings
            of large scale systems. In highschool I took AP Computer Science Principles which is how I discovered my love for coding.
            I also always had a love for investing and the stock market. This is why I decided to pursue a major in Computer Science
            and a minor in Business.

            """
        )
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_sccc)
    with text_column:
        st.subheader(":male-office-worker: Where I Work")
        st.write(
            """
            Over the last five years, I have held the position of a Caddy and Bagroom Attendant at St. Cair Country Club. 
            During this time, I actively engaged in skill development and contributed to the enhancement of the club's facilities. 
            Additionally, I established valuable communication and cultivated strong connections with club members.
            This job has been truly a privelage to have seeing the skills and leadership experience this has allowed me to attain.

            """
        )
        st.markdown("[:link: Check out their website!](https://www.stclaircc.org/)")

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_gym)
    with text_column:
        st.subheader(":man-golfing: Hobbies & Interests")
        st.write(
            """
            I love to play golf in my free time. Getting out on the course and getting to clear my head while having fun and getting 
            fresh air is one of my favorite hobbies. I also love going to the gym to workout. Being able to take 1-2 hours of my day to work
            on myself both physically and mentally is one of my favorite and most important things to do during the day. I also am a huge 
            sports and car enthusiast. I love watching NFL football and MLB baseball. I also love learning about cars and keeping
            up to date on the latest automobiles. Investing and coding are additional hobbies I enjoy partaking in on a day-to-day basis.

            """
        )

with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_ext)
    with text_column:
        st.subheader(":chart_with_upwards_trend: Activities")
        st.write(
            """
            - Delta Sigma Phi Fraternity ([:link: Delta Sigma Phi Website](https://deltasig.org/))
            - Computer Science Club ([:link: Computer Science Club Webiste](https://csclubatpitt.org/))
            - Undergraduate Finance Club ([:link: Undergraduate Finance Club LinkedIn](https://www.linkedin.com/company/undergraduate-finance-club-at-pitt/))

            """
        )

# --- Contact ---
with st.container():
    st.write("---")
    st.header(":mailbox_with_mail: Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/harrisongetchell@gmail.com" method="POST">
        <input type= "hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder= "Your name" required>
        <input type="email" name="email" placeholder= "Your email" required>
        <textarea name = "message" placeholder= "Your message here" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """ 

    left_column, right_column = st.column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
