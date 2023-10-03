import streamlit as st
from PIL import Image

page_bg = """
<style>
[data-testid="stAppViewContainer"] {background-color: #eeeeff;
opacity: 1;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #eeeeff 4px ), repeating-linear-gradient( #ffffff55, #ffffff );
}
"""
st.markdown(page_bg, unsafe_allow_html=True)
st.title("*Amirhossein Pajouhan*")
st.text("Last Update : 9/29/2023")
image = Image.open('profile-pic (1).png')
new_image = image.resize((190, 190))
st.image(new_image)
st.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
#st.write(":heavy_minus_sign:" * 34)

page_bg_sidebar = """
<style>
[data-testid="stSidebar"] {
background: repeating-radial-gradient(circle,#a5a0ff, transparent 20%);
        background-size: 1em 1em;
        background-color: #ffffff;
        opacity: 1
}
"""
st.markdown(page_bg_sidebar, unsafe_allow_html=True)
st.sidebar.markdown('''# :orange[Resume and Projects] :page_with_curl:⚙️''')
st.sidebar.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)


st.sidebar.markdown('''### Resume ###''')
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #F9E79F ;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #17202A;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)
res = st.sidebar.button(":orange[Click Here]")

st.sidebar.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.sidebar.markdown('''### Python Projects ###''')
ai = st.sidebar.button(":orange[AI Projects]")
app = st.sidebar.button(":orange[App Projects]")
opt = st.sidebar.button(":orange[Optimization Projects]")
web = st.sidebar.button(":orange[Web Projects]")
st.sidebar.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.sidebar.markdown('''### Mechanical Engineering Projects ###''')
ansys = st.sidebar.button(":orange[Ansys Projects]")
solid = st.sidebar.button(":orange[Solidworks Projects]")
ees = st.sidebar.button(":orange[EES Projects]")
mat = st.sidebar.button(":orange[Matlab Projects]")
st.sidebar.markdown("""<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
st.sidebar.markdown('''### Manufacturing Projects ###''')
manufacture = st.sidebar.button(":orange[Click]")

if res is True:
    st.markdown('''## PERSONAL DETAILS ##''')
    st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """,
                        unsafe_allow_html=True)
    st.text("Birth          5/4/1998")
    st.text("Phone          +989398664818")
    st.text("Mail           amirhpzh1998@gmail.com")
    str = "https://www.kaggle.com/amirhosseinpzh1998"
    st.markdown("*Kaggle [link](%s)*" % str)
    git = "https://github.com/amirhosseinpzh1009"
    st.markdown("*Github [link](%s)*" % git)

    st.markdown("     ")
    st.markdown("     ")

    st.markdown('''## EDUCATION ##''')
    st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """,
                        unsafe_allow_html=True)
    st.write("##### **Bachelor of Mechanical Engineering** #####")
    st.write("##### **Shahid Bahonar University of Kerman, Kerman, Iran** #####")
    st.write("###### ***CGPA: 15.70/20 (3.14/4)*** ######")
    st.write("###### ***Sep 2016 - Sep 2022*** ######")
    st.write("###### ___________________________________ ######")
    st.write("##### **Diplomas in Mathematics and Physics** #####")
    st.write("##### **Saralah high school and pre-university, Kerman, Iran** #####")
    st.write("###### ***Sep 2012 - May 2016*** ######")

    st.markdown("     ")
    st.markdown("     ")

    st.markdown('''## RESEARCH INTERESTS ##''')
    st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """,
                unsafe_allow_html=True)
    st.write("##### **Artificial Intelligence** #####")
    st.write("##### **Turbomachinery** #####")

    st.markdown("     ")
    st.markdown("     ")

    st.markdown('''## TEACHING EXPERIENCE ##''')
    st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """,
                unsafe_allow_html=True)
    st.write("##### **Teaching Assistance (TA)** #####")
    st.write("##### **Design and Simulation Double Pipe Heat Exchanger** #####")
    st.write("##### **Design and Simulation Shell and Tube Heat Exchanger** #####")
    st.write("###### ***April 2021 - May 2022*** ######")

    st.markdown("     ")
    st.markdown("     ")

    # st.markdown('''## PROJECTS ##''')
    # st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """,
    #             unsafe_allow_html=True)
    # st.write("##### **:white_check_mark:  Simulation of water flow in a pipe with fine, course and medium mesh using Ansys-Fluent** #####")
    # st.markdown("     ")
    # st.write("##### **:white_check_mark:  Design and Simulation of double pipe, shellm and tube heat exchanger using Ansys-Fluent** #####")
    # st.markdown("     ")
    # st.write("##### **:white_check_mark:  Design and Simulation of double pipe, shellm and tube heat exchanger using Ansys-Fluent** #####")
    st.markdown('''## RESEARCH EXPERIENCES ##''')
    st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """,
                 unsafe_allow_html=True)
    st.write("##### **Bachelor's Project : Blood heat exchanger for an open heart operation that blood behaves non-Newtonian manner** #####")

    st.markdown("     ")
    st.markdown("     ")

    st.markdown('''## SKILLS ##''')
    st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """,
                unsafe_allow_html=True)
    st.write("##### **Languages:** #####")
    st.write("###### ***Persian(Mother Tongue)*** ######")
    st.write("###### ***English(Foreign Language)*** ######")
    st.write("###### ***German(Foreign Language)*** ######")
    st.markdown("     ")
    st.markdown("     ")
    st.write("##### **Programming:** #####")
    st.write("###### ***Python(advance), Matlab(intermediate)*** ######")
    st.markdown("     ")
    st.markdown("     ")
    st.write("##### **Software:** #####")
    st.write("###### ***Ansys(fluent, cfx, thermal mechanical, turbomachinery), Solidworks, Star ccm, Concept Nrec, CFturbo, EES, Micriosoft Office*** ######")

    st.markdown("     ")
    st.markdown("     ")

    st.markdown('''## PROJECTS ##''')
    st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """,
                unsafe_allow_html=True)
    st.write("##### **👈 You can check them in Sidebar** #####")
























