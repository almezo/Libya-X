# استدعاء مكتبة Streamlit لإنشاء واجهة تفاعلية
import streamlit as st

# استدعاء مكتبة OpenAI للوصول إلى واجهات الذكاء الاصطناعي عبر API
from openai import OpenAI

# ----------------------------------------------------------------------------------------------------------------------#
# تهيئة عميل OpenAI باستخدام مفتاح API الخاص بمنصة Groq، والمخزن في إعدادات التطبيق
client = OpenAI(
    api_key=st.secrets["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1"
)

# ----------------------------------------------------------------------------------------------------------------------#
# إعداد عنوان الصفحة وتخطيطها (عرض عريض)
st.set_page_config(page_title="ليبيا اكس - المساعد الذكي", layout="wide")

# ----------------------------------------------------------------------------------------------------------------------#
# إنشاء قائمة الرسائل لأول مرة إذا لم تكن موجودة مسبقاً في session_state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
    أنت مساعد ذكي رسمي تابع لمنصة ليبيا إكس - Libya X. تأسست المنصة في سنة 2022 ومملوكه من قبل مهندسين لبيين وتُعد هذه المنصه موزعًا معتمدًا لاشتراكات IPTV داخل ليبيا.

    ترد فقط على المواضيع التالية:
    1- الاشتراكات والسيرفرات ليبيا اكس.
    2- الأسعار، المدة، والأكواد التجريبية.
    3- طرق الدفع.
    4- الدعم الفني والتفعيل.
    5- الأجهزة المدعومة.
    6- تنبيهات الأمان والثقة.

    ❌ لا ترد على أي استفسار لا يتعلق بـ IPTV أو خارج خدمات ليبيا إكس. بل تعتذر باحترام وتُشير إلى أنك مساعد رسمي لخدمة محددة فقط.
    ---

    **ما هو IPTV؟**  
    هو تطبيق يتم تحميله على أجهزة Android أو iPhone أو TV Box أو شاشات سمارت أندرويد أو أجهزة الكمبيوتر أو الرسيفرات التي تدعم iptv يوجد بها برنامج xtream iptv . يمكنك من خلال iptv مشاهدة قنوات رياضية و أفلام و مسلسلات و وباقات عالمية.
    ---

    ** السيرفرات والأسعار:**

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
      1- https://www.facebook.com/share/1Au4jF6o2n/   (الصفحه الرئيسة)
      2- https://www.facebook.com/share/1EeZhEbLjR/   (الصفحه الاحتياطية)
    ---

    **وقت التفعيل:**  
    يتم تفعيل الاشتراك عادة خلال 5 إلى 15 دقيقة بعد تأكيد الدفع.

    **خدمة العملاء:**  
    في حال وجود مشكلة، يرجى التواصل معنا عبر نفس الرقم اتصال عادي او واتساب أو مراسلتنا على بريد صفحة الفيسبوك.
    ---

    **تنبيه هام:** 
    الموزعين المعتمدين لدنيا
    1- المظلة و المضله و شركة المظلة و برنامج ايكارد و icard
    2- برنامج بن و bn , بن بلس و BN PLUS
    3- صفحاتنا على الفيسبوك او الواتساب فقط
    4- من خلال موقعنا على الويب

    ❗ الاشتراكات تتم فقط من خلال:
    - صفحات ليبيا اكس المذكورة في الأعلى فقط
    أو عن طريق الموزعين 1-نقاط البيع التابعه لي شركة المظلة Umbrella LTD او 2-تطبيق iCard
    او 3-تطبيق BN Plus او 4- موقعنا على الويب
    ❌ ولسنا مسؤولين عن أي كروت او اشتراكات من اي جهة غير معتمدنا لدينا .

    ---
    **جودة الخدمة:**  
    جميع الاشتراكات يتم تفعيلها من خلال أنظمتنا الرسمية لضمان الجودة والثبات.

    ---
    **اللغة:**  
    استخدم اللغة العربية دائمًا إلا إذا تم سؤالك باللغة الإنجليزية، فترد بها فقط لاتخلط الكلام عربي و انجليزي ابدا.

    دائما اجعل الروابط تكون في سطر منفرد لكي تعمل في المحادثه

    دائما تأكد من انك ترسل رقم الهاتف صحيح و من روابط انها تشتغل و تكون في سطر منفرد

    """
        }
    ]

# إنشاء متغير خاص لتخزين المحادثة الحالية بين المستخدم والمساعد
if "chat" not in st.session_state:
    st.session_state.chat = []

# ----------------------------------------------------------------------------------------------------------------------#
# تهيئة تنسيقات CSS لتعديل شكل الواجهة: حجم النص، تموضع صندوق الإدخال، وتنسيق الحقول
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
            line-height: 5.2;
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

# ----------------------------------------------------------------------------------------------------------------------#
# عرض الشعار والعنوان الرئيسي للموقع
col_logo, col_title, col_features = st.columns([20, 20, 20])  # تقسيم الصفحة إلى 3 أعمدة

# العمود الأول: عرض شعار ليبيا إكس
with col_logo:
    st.markdown(
        """
        <div style='margin-top: -60px; text-align: left;'>
            <img src="https://raw.githubusercontent.com/almezo/Libya-X/main/Libya_X_CHATBOT/libyax_logo.png" width="100">
        </div>
        """,
        unsafe_allow_html=True
    )

# العمود الثاني: عنوان الموقع الترحيبي
with col_title:
    st.markdown("""
        <div style='text-align: center; margin-top: -50px;'>
            <h3><span style='color:green;'>مرحباً بك </span> في <span style='color:red;'> ليبيا اكس </span><h3> المنصة الرائدة في بيع اشتراكات <h3><b style='color:red;'>IP</b>T<b style='color:green;'>V</b></h3>
        </div>
    """, unsafe_allow_html=True)

# العمود الثالث: عرض مميزات المنصة
with col_features:
    st.markdown("""
        <div dir="rtl" style="text-align: right; margin-top: -50px;">
            <ul>
                <li>موزع معتمد في ليبيا</li>
                <li>باقات قنوات فضائية</li>
                <li>باقات أفلام ومسلسلات عالمية</li>
                <li>اشتراكات شهرية وسنوية بأسعار منافسة</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# خط فاصل
st.markdown("<hr>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------#
# عرض سجل المحادثة السابقة داخل صندوق قابل للتمرير
st.markdown("<h4 style='text-align: center;'>📜 سجل المحادثة</h4>", unsafe_allow_html=True)
st.markdown("<div class='chat-history'>", unsafe_allow_html=True)

# تكرار وعرض جميع الرسائل السابقة بين المستخدم والمساعد
for speaker, msg in st.session_state.chat:
    align = "right" if speaker == "أنت" else "right"  # جعل كل النصوص تظهر في اليمين
    st.markdown(f"<div dir='rtl' style='text-align: {align}; padding: 20px 20px;'><b>{speaker}:</b> {msg}</div>",
                unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------#
# إنشاء واجهة إدخال الرسائل من المستخدم في الأسفل بشكل ثابت
st.markdown("<div class='chat-input-container'>", unsafe_allow_html=True)
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2, col3 = st.columns([60, 4, 7])  # تقسيم الصف إلى ثلاثة أعمدة (نص، إرسال، مسح)
    user_input = col1.text_input(label="", placeholder="اكتب استفسارك هنا... 💬")  # مربع إدخال نص
    send_clicked = col2.form_submit_button("إرسال 📨")  # زر الإرسال
    clear_clicked = col3.form_submit_button("مسح السجل المحادثه 🗑️")  # زر المسح
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------------------------------------------#
# إذا تم الضغط على زر "مسح"، يتم إعادة تهيئة المحادثة
if clear_clicked:
    st.session_state.chat.clear()
    st.session_state.messages = [
        {"role": "system", "content": "أنت مساعد ذكي باسم ليبيا اكس Libya X. رد باحترافية وباللغة العربية أو الإنجليزية إذا أُرسلت لك، وكن ودودًا وواضحًا حول الاشتراكات، الأسعار، طرق الدفع، والدعم الفني."}
    ]
    st.rerun()  # إعادة تحميل الصفحة

# ----------------------------------------------------------------------------------------------------------------------#
# إذا أرسل المستخدم رسالة جديدة
if send_clicked and user_input.strip():
    msg = user_input.strip()  # إزالة الفراغات الزائدة
    st.session_state.messages.append({"role": "user", "content": msg})  # حفظ رسالة المستخدم
    st.session_state.chat.append(("أنت", msg))  # عرضها في سجل الدردشة

    # إظهار رسالة "جاري التوليد..." أثناء الانتظار
    with st.spinner("🤖 يتم توليد الرد بواسطة الذكاء الاصطناعي..."):
        reply = client.chat.completions.create(
            model="llama3-70b-8192",  # اسم النموذج المستخدم - يمكن تغييره إلى gpt-4o
            messages=st.session_state.messages,  # إرسال جميع الرسائل السابقة
            temperature=0.7  # تحديد درجة الإبداع في الرد
        ).choices[0].message.content  # استخراج النص الناتج من الرد

    # حفظ الرد في السجل
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.chat.append(("ليبيا إكس", reply))
    st.rerun() # تحديث الصفحة تلقائيًا بعد الرد
