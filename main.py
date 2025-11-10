import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # كود HTML يعرض صفحة آمنة ومحايدة
    return """
    <html>
        <head><title>منصة الأبحاث الأمنية</title></head>
        <body>
            <h1>🔬 منصة الأبحاث الأمنية</h1>
            <p>منصة أكاديمية لإجراء الأبحاث في مجال الأمن السيبراني</p>
            <p>جامعة التقنية - قسم أمن المعلومات</p>
        </body>
    </html>
    """

@app.route('/health')
def health_check():
    # نقطة فحص صحة الخدمة (تستخدمها منصات الاستضافة)
    return {"status": "active", "service": "research-platform"}

if __name__ == "__main__":
    # الحصول على رقم البورت من متغيرات البيئة (تستخدمه Render)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
