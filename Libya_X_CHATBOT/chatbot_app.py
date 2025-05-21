import streamlit as st
from openai import OpenAI

#----------------------------------------------------------------------------------------------------------------------#
# إعداد عميل OpenAI باستخدام مفاتيح Groq API

client = OpenAI(
    api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

#----------------------------------------------------------------------------------------------------------------------#
# إعداد واجهة التطبيق

st.set_page_config(page_title="ليبيا اكس - المساعد الذكي", layout="wide")

#----------------------------------------------------------------------------------------------------------------------#
# تهيئة الجلسة (session_state) لأول مرة لتخزين الرسائل والمحادثة

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
أنت مساعد ذكي رسمي تابع لمنصة ليبيا إكس - Libya X. تأسست المنصة في سنة 2022 وتُعد موزعًا معتمدًا لاشتراكات IPTV داخل ليبيا.

ترد فقط على المواضيع التالية:
1- الاشتراكات والسيرفرات الرسمية.
2- الأسعار، المدة، والأكواد التجريبية.
3- طرق الدفع.
4- الدعم الفني والتفعيل.
5- الأجهزة المدعومة.
6- تنبيهات الأمان والثقة.

❌ لا ترد على أي استفسار لا يتعلق بـ IPTV أو خارج خدمات ليبيا إكس. بل تعتذر باحترام وتُشير إلى أنك مساعد رسمي لخدمة محددة فقط.

---

**ما هو IPTV؟**  
هو تطبيق يتم تحميله على أجهزة Android TV أو TV Box أو شاشات سمارت أندرويد . يمكنك من خلاله مشاهدة قنوات رياضية، أفلام، مسلسلات، وباقات عالمية.

**و كمان يعمل على أجهزة iPhone و الكمبيوتر.**

---

**⛎ السيرفرات والأسعار:**

**سيرفر اكس**  
3 أشهر: 40 د.ل | 6 أشهر: 70 د.ل | 1 سنة: 120 د.ل  
⏱ متوفر كود تجريبي: 12 ساعة

**سيرفر نوفا**  
3 أشهر: 35 د.ل | 6 أشهر: 60 د.ل | 1 سنة: 100 د.ل  
⏱ متوفر كود تجريبي: 12 ساعة

**سيرفر مارفل**  
3 أشهر: 35 د.ل | 6 أشهر: 65 د.ل | 1 سنة: 115 د.ل  
⏱ متوفر كود تجريبي: 24 ساعة

**سيرفر مافين**  
1 شهر: 25 د.ل | 3 أشهر: 35 د.ل | 6 أشهر: 55 د.ل | 1 سنة: 95 د.ل  
⏱ متوفر كود تجريبي: 12 ساعة

**سيرفر MH**  
3 أشهر: 45 د.ل | 6 أشهر: 75 د.ل | 1 سنة: 130 د.ل  
⏱ متوفر كود تجريبي: 6 ساعات

**سيرفر MYHD**  
1 شهر: 20 د.ل | 3 أشهر: 35 د.ل | 6 أشهر: 45 د.ل | 1 سنة: 75 د.ل  
⛔ لا يوجد كود تجريبي

**سيرفر LYNX**  
1 شهر: 20 د.ل | 3 أشهر: 35 د.ل | 1 سنة: 90 د.ل  
⛔ لا يوجد كود تجريبي

**سيرفر GOGO**  
3 أشهر: 45 د.ل | 1 سنة: 100 د.ل  
⛔ لا يوجد كود تجريبي

**سيرفر Aroma**  
1 شهر: 35 د.ل | 3 أشهر: 60 د.ل | 1 سنة: 120 د.ل  
⛔ لا يوجد كود تجريبي

**سيرفر Megastar**  
1 سنة: 55 د.ل  
⛔ لا يوجد كود تجريبي

---

**طرق الدفع الرسمية:**
1. كروت الدفع المسبق أو تحويل رصيد (ليبيانا أو المدار)
2. كروت عربوت التابعه لبرنامج BN PLUS
3. خدمة البطاقة المصرفية مع (خصم 10%)
4. خدمة سداد مع (خصم 10%)
5. خدمة التداول مع (خصم 10%)
6. خدمة إدفع لي مع (خصم 10%)
7. خدمة تحويل USDT في برنامج BINANCE
   - 3 أشهر: 5 $
   - 6 أشهر: 9 $
   - 1 سنة: 16 $
   - Binance ID: 804907149

---

**كود تجريبي؟**  
للحصول على كود تجريبي (مدة 6 أو 12 أو 24 ساعة حسب السيرفر)، تواصل معنا عبر:

- الواتساب :
 https://wa.me/218945772649  
 
- الاتصال على رقم:
 0945772649  
 
- صفحات الفيسبوك الرسمية:
  1- https://www.facebook.com/share/1Au4jF6o2n/
  2- https://www.facebook.com/share/1EeZhEbLjR/

---

**وقت التفعيل:**  
يتم تفعيل الاشتراك عادة خلال 5 إلى 15 دقيقة من تأكيد الدفع.

**خدمة العملاء:**  
في حال وجود مشكلة، يرجى التواصل معنا عبر نفس الرقم أو بريد الصفحة.

---

**تنبيه هام:** 
الجهات المعتمده لدنيا
1- المظلة و المضله و شركة المظلة و برنامج ايكارد و icard
2- برنامج بن و bn , بن بلس و BN PLUS
3- صفحاتنا على الفيسبوك او الواتساب فقط
 
❗ الاشتراكات تتم فقط من خلال:
- صفحات ليبيا اكس المذكورة في الأعلى فقط
أو عن طريق نقاط البيع التابعه لي شركة المظلة Umbrella LTD او تطبيق iCard
او تطبيق BN Plus
❌ ولسنا مسؤولين عن أي كروت او اشتراكات من اي جهة غير معتمدنا لدينا .

---
**جودة الخدمة:**  
جميع الاشتراكات يتم تفعيلها من خلال أنظمتنا الرسمية لضمان الجودة والثبات.

---
**اللغة:**  
استخدم اللغة العربية دائمًا إلا إذا تم سؤالك باللغة الإنجليزية، فترد بها فقط.

دائما اجعل الروابط تكون في سطر منفرد لكي تعمل في المحادثه
"""
        }
    ]

if "chat" not in st.session_state:
    st.session_state.chat = []

#----------------------------------------------------------------------------------------------------------------------#
# CSS لتنسيق المحادثة وإدخال منسق

st.markdown("""
    <style>
        .chat-history {
            max-height: 60vh;
            overflow-y: auto;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 10px;
            background-color: #fdfdfd;
            margin-bottom: 100px;
            font-size: 22px !important;
            font-weight: bold !important;
            line-height: 2.2;
        }
        .chat-input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #ffffff;
            padding: 10px 5%;
            box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.05);
            z-index: 1000;
        }
        .stTextInput > div > input {
            padding: 10px !important;
            border-radius: 10px !important;
            border: 1px solid #ccc !important;
            font-size: 18px !important;
            font-weight: bold !important;
        }
        .stButton>button {
            background-color: #f0f0f0;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 16px;
            margin-right: 5px;
            cursor: pointer;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #e0e0e0;
        }
        input[type="text"] {
            direction: rtl !important;
            text-align: right !important;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

#----------------------------------------------------------------------------------------------------------------------#
# عرض الشعار والعنوان

col_logo, col_title, col_features = st.columns([20, 20, 20])
with col_logo:
    st.image("https://raw.githubusercontent.com/almezo/Libya-X/main/Libya_X_CHATBOT/libyax_logo.png", width=200)
with col_title:
    st.markdown("""
        <div style='text-align: center; margin-top: 10px;'>
            <h3><span style='color:green;'>مرحباً بك </span> في <span style='color:red;'> ليبيا اكس </span><h3> المنصة الرائدة في بيع اشتراكات <h3><b style='color:red;'>IP<b style='color:black;'>T<b style='color:green;'>V</b></h3>
        </div>
    """, unsafe_allow_html=True)
with col_features:
    st.markdown("""
        <div dir="rtl" style="text-align: right; margin-top: 10px;">
            <ul>
                <li>موزع معتمد في ليبيا</li>
                <li>باقات قنوات فضائية</li>
                <li>باقات أفلام ومسلسلات عالمية</li>
                <li>اشتراكات شهرية وسنوية بأسعار منافسة</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

#----------------------------------------------------------------------------------------------------------------------#
# عرض سجل المحادثة

st.markdown("<h4 style='text-align: center;'>📜 سجل المحادثة</h4>", unsafe_allow_html=True)
st.markdown("<div class='chat-history'>", unsafe_allow_html=True)
for speaker, msg in st.session_state.chat:
    align = "right" if speaker == "أنت" else "right"
    st.markdown(f"<div dir='rtl' style='text-align: {align}; padding: 10px 20px;'><b>{speaker}:</b> {msg}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

#----------------------------------------------------------------------------------------------------------------------#
# نموذج الإدخال

st.markdown("<div class='chat-input-container'>", unsafe_allow_html=True)
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2, col3 = st.columns([70, 4, 5])
    user_input = col1.text_input(label="", placeholder="اكتب استفسارك هنا... 💬")
    send_clicked = col2.form_submit_button("إرسال 📨")
    clear_clicked = col3.form_submit_button("مسح السجل 🗑️")
st.markdown("</div>", unsafe_allow_html=True)

#----------------------------------------------------------------------------------------------------------------------#
# مسح السجل

if clear_clicked:
    st.session_state.chat.clear()
    st.session_state.messages = [
        {"role": "system", "content": "أنت مساعد ذكي باسم ليبيا اكس Libya X. رد باحترافية وباللغة العربية أو الإنجليزية إذا أُرسلت لك، وكن ودودًا وواضحًا حول الاشتراكات، الأسعار، طرق الدفع، والدعم الفني."}
    ]
    st.rerun()

#----------------------------------------------------------------------------------------------------------------------#
# الرد على رسائل المستخدم

if send_clicked and user_input.strip():
    msg = user_input.strip()
    st.session_state.messages.append({"role": "user", "content": msg})
    st.session_state.chat.append(("أنت", msg))

    with st.spinner("🤖 يتم توليد الرد بواسطة الذكاء الاصطناعي..."):
        reply = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=st.session_state.messages,
            temperature=0.7
        ).choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.chat.append(("ليبيا إكس", reply))
    st.rerun()
