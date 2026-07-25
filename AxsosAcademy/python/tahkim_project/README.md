# دار التحكيم الشرعي — مشروع Django

مشروع Django كامل لمنصة تحكيم شرعي: تقديم قضايا للعامة، نشر الأحكام، وحجز جلسات استشارة
مع خيار الدفع عبر واتساب أو الدفع الإلكتروني (Stripe).

## هيكل المشروع

```
tahkim_project/
├── manage.py
├── requirements.txt
├── tahkim_project/        ← إعدادات المشروع (settings.py, urls.py)
└── arbitration/           ← التطبيق الرئيسي
    ├── models.py          ← نموذجا: Case (قضية) و Booking (حجز)
    ├── admin.py           ← لوحة تحكم المحكّم (تُستخدم لوحة Django الجاهزة)
    ├── forms.py
    ├── views.py
    ├── urls.py
    ├── templates/arbitration/   ← ملفات HTML
    └── static/arbitration/
        ├── css/style.css  ← التنسيق (خشب + زيتوني فاتح عتيق + أبيض)
        └── js/main.js
```

## خطوات التشغيل (لأول مرة)

1. تأكد من تثبيت Python 3.10 أو أحدث.
2. من داخل مجلد المشروع، أنشئ بيئة افتراضية وفعّلها:
   ```
   python -m venv venv
   source venv/bin/activate      # على ماك/لينكس
   venv\Scripts\activate         # على ويندوز
   ```
3. ثبّت المتطلبات:
   ```
   pip install -r requirements.txt
   ```
4. أنشئ قاعدة بيانات PostgreSQL (محلياً أو عبر مزوّد استضافة مثل Railway أو Render أو Supabase)،
   ثم انسخ ملف `.env.example` إلى ملف جديد اسمه `.env` وعبّئ بياناتها:
   ```
   cp .env.example .env
   ```
   وافتح `.env` وضع فيه اسم القاعدة، اسم المستخدم، كلمة السر، والعنوان (Host) والمنفذ (Port)
   التي يعطيك إياها مزوّد الاستضافة.
5. أنشئ جداول قاعدة البيانات:
   ```
   python manage.py migrate
   ```
6. أنشئ حساب المحكّم (المدير) الذي سيدخل للوحة الإدارة:
   ```
   python manage.py createsuperuser
   ```
7. شغّل السيرفر المحلي:
   ```
   python manage.py runserver
   ```
8. افتح المتصفح على `http://127.0.0.1:8000` للموقع، أو `http://127.0.0.1:8000/admin/` للوحة المحكّم.

## إعدادات تحتاج تعديلها قبل النشر الفعلي

في ملف `tahkim_project/settings.py`:
- `SECRET_KEY`: غيّره لمفتاح سري جديد.
- `DEBUG = False` عند النشر.
- `ALLOWED_HOSTS`: ضع دومين الموقع الفعلي بدلاً من `"*"`.
- `WHATSAPP_NUMBER`: رقم واتساب المحكّم.
- `STRIPE_PAYMENT_LINK`: رابط الدفع من Stripe Payment Links (اتركه فارغاً حتى يصبح جاهزاً).
- `DATABASES`: مضبوطة الآن على PostgreSQL (وليس SQLite)، وتُقرأ بياناتها من ملف `.env` — لا تعدّلها مباشرة بالكود.

## لوحة إدارة المحكّم

لا حاجة لبناء لوحة تحكم يدوياً — تم استخدام لوحة Django الإدارية الجاهزة والآمنة على `/admin/`،
وهي تسمح للمحكّم بـ:
- مراجعة القضايا الجديدة وكتابة نص الحكم ونشره (تغيير الحالة إلى "صدر الحكم").
- إدارة الحجوزات (تأكيد / إلغاء / تحديد كمدفوع) مباشرة من القائمة دون فتح كل حجز.

## النشر على الإنترنت (استضافة Render — الأسهل للمبتدئين)

المشروع جاهز الآن للنشر الفعلي (فيه `Procfile`، `gunicorn`، `whitenoise` لخدمة ملفات
CSS/JS، وكل الإعدادات الحساسة تُقرأ من متغيرات بيئة بدل أن تكون مكتوبة بالكود).

### 1. ارفعي المشروع على GitHub
1. أنشئي حساب مجاني على https://github.com إذا ما عندك.
2. أنشئي مستودع (Repository) جديد فاضٍ.
3. من الـ Terminal، داخل مجلد المشروع:
   ```
   git init
   git add .
   git commit -m "أول نسخة من المشروع"
   git branch -M main
   git remote add origin رابط_المستودع_من_GitHub
   git push -u origin main
   ```
   (لاحظي: ملف `.env` **لن يُرفع** تلقائياً لأنه محمي — هذا مقصود ومهم لحمايته).

### 2. أنشئي حساب على Render
1. افتحي https://render.com وسجّلي دخول بحساب GitHub.
2. اضغطي **New** → **Web Service**.
3. اختاري مستودع المشروع الذي رفعتيه.
4. Render سيكتشف تلقائياً أنه مشروع Python.
5. **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
6. **Start Command**: `gunicorn tahkim_project.wsgi`

### 3. أضيفي متغيرات البيئة (بدل ملف .env)
من صفحة الخدمة على Render → تبويب **Environment** → أضيفي نفس القيم الموجودة بملف
`.env` عندك، بالإضافة إلى:
```
SECRET_KEY=مفتاح_سري_جديد_تولّديه
DEBUG=False
ALLOWED_HOSTS=your-app-name.onrender.com
```

### 4. بعد أول نشر ناجح
من تبويب **Shell** بلوحة Render، شغّلي مرة واحدة:
```
python manage.py migrate
python manage.py createsuperuser
```

بعدها موقعك يصير شغالاً فعلياً على رابط عام مثل:
`https://your-app-name.onrender.com`

### بدائل أخرى
Railway وPythonAnywhere بديلان جيدان أيضاً بخطوات مشابهة. إذا واجهتِ صعوبة بأي
خطوة من هذه، يُفضّل الاستعانة بمطوّر لإتمام النشر النهائي (الدومين المخصص، شهادة
SSL، وربط PayPal بوضع Live الحقيقي).
