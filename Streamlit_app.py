import streamlit as st
from PIL import Image

# ऐप की सेटिंग
st.set_page_config(page_title="बेगूसराय डायरी", layout="centered")

# हेडर: जो स्क्रीन पर सबसे पहले दिखेगा
st.markdown("<h1 style='text-align: center; color: #FF5733;'>🌟 बिहार संवाद: बेगूसराय स्पेशल 🌟</h1>", unsafe_allow_html=True)
st.write("---")

# साइडबार नेविगेशन
menu = ["🏠 होम", "📜 इतिहास और दिनकर", "🖼️ फोटो अपलोड (अपनी यादें)", "🎶 बेगूसराय के लोकगीत", "🍲 स्वाद और चाट"]
choice = st.sidebar.selectbox("कहाँ जाना चाहेंगे?", menu)

if choice == "🏠 होम":
    st.header("प्रणाम उज्वल जी! 🙏")
    st.write("ई ऐप आपके बेगूसराय के गौरव, साहित्य और स्वाद से रूबरू कराएगा।")
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3a/Simaria_Bridge.jpg", caption="भव्य सिमरिया पुल")
    st.info("💡 बेगूसराय को 'बिहार का औद्योगिक द्वार' कहा जाता है।")

elif choice == "📜 इतिहास और दिनकर":
    st.header("✍️ राष्ट्रकवि की कलम से")
    st.subheader("जी.डी. कॉलेज और दिनकर जी")
    st.write("बेगूसराय की मिट्टी में जो ओज है, वो यहाँ के संस्थानों और कवियों की देन है।")
    st.markdown("> **'क्षमा शोभती उस भुजंग को जिसके पास गरल हो...'** - दिनकर")
    st.success("जी.डी. कॉलेज की सीढ़ियों ने बिहार के भविष्य को गढ़ा है।")

elif choice == "🖼️ फोटो अपलोड (अपनी यादें)":
    st.header("📸 अपनी यादें यहाँ सहेजें")
    st.write("बेगूसराय की कोई फोटो (सिमरिया, कावर झील या जी.डी. कॉलेज) अपलोड करें:")
    uploaded_file = st.file_uploader("फोटो चुनें...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='वाह! शानदार फोटो है।', use_container_width=True)
        st.balloons() # फोटो डालने पर जश्न!

elif choice == "🎶 बेगूसराय के लोकगीत":
    st.header("🎵 मिट्टी की सुरीली धुन")
    st.write("यहाँ क्लिक करके बिहार के पारंपरिक लोकगीतों का आनंद लें:")
    # यहाँ आप अपनी पसंद का ऑडियो लिंक डाल सकते हैं
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") 
    st.write("*(नोट: यह एक सैंपल ट्यून है, आप अपनी पसंद के गाने का लिंक यहाँ डाल सकते हैं)*")

elif choice == "🍲 स्वाद और चाट":
    st.header("🌶️ बेगूसराय की चटपटी दुनिया")
    st.write("बेगूसराय में अगर चाट नहीं खाया, तो क्या खाया?")
    st.markdown("""
    - **मशहूर चाट भंडार:** कचहरी रोड और काली स्थान के पास की चाट।
    - **मिठाई:** यहाँ का गरमा-गरम गुलाब जामुन।
    - **सत्तू शरबत:** देसी एनर्जी ड्रिंक।
    """)
