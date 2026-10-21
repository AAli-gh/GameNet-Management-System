# GameNet-Management-System


یک سیستم کامل و حرفه‌ای برای **مدیریت گیم‌نت (GameNet Management System)** طراحی و پیاده‌سازی کن.

این پروژه باید در نسخه اول **کاملاً Local** باشد و داخل شبکه داخلی گیم‌نت اجرا شود. معماری پروژه باید به شکلی باشد که در آینده بتوان Cloud و دسترسی از راه دور را بدون بازنویسی کامل سیستم اضافه کرد.

## هدف پروژه

ساخت یک پنل مدیریتی مدرن برای صاحب یا مدیر گیم‌نت که بتواند تمام سیستم‌های گیم‌نت، مشتری‌ها، جلسات بازی، رزروها، درآمد، فروشگاه و وضعیت لحظه‌ای کامپیوترها را از یک پنل مدیریت کند.

---

# 1. تکنولوژی

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- Recharts برای نمودارها
- طراحی کاملاً Responsive

### Backend
- Python
- FastAPI
- REST API
- WebSocket برای اطلاعات Real-Time

### Database
- PostgreSQL

### PC Agent
یک Agent سبک با Python طراحی کن که روی کامپیوترهای گیم‌نت اجرا شود و بتواند با Backend ارتباط برقرار کند.

Agent باید امکان دریافت وضعیت سیستم و در آینده اجرای دستورات مدیریتی را داشته باشد.

---

# 2. معماری

معماری کلی:

Admin Panel
↓
Next.js
↓
FastAPI
↓
PostgreSQL

و برای سیستم‌های گیم‌نت:

FastAPI
↓
WebSocket
↓
GameNet Agent
↓
PCهای گیم‌نت

هر PC باید یک شناسه منحصر به فرد داشته باشد.

مثلاً:

PC-01
PC-02
PC-03
PC-04

---

# 3. داشبورد اصلی

یک Dashboard حرفه‌ای و مدرن طراحی کن.

در بالای صفحه کارت‌های آماری نمایش داده شود:

- تعداد کل سیستم‌ها
- سیستم‌های آزاد
- سیستم‌های در حال استفاده
- سیستم‌های رزرو شده
- سیستم‌های دارای مشکل
- کاربران حاضر
- درآمد امروز
- درآمد ماه جاری

همچنین:

### نمودار درآمد
نمایش درآمد:
- روزانه
- هفتگی
- ماهانه

### نمودار استفاده از سیستم‌ها

نمایش میزان استفاده از PCها.

### جلسات فعال

لیست جلسات در حال اجرا:

PC
کاربر
زمان شروع
زمان سپری‌شده
زمان باقی‌مانده
هزینه فعلی
وضعیت

---

# 4. مدیریت سیستم‌ها

یک صفحه کامل برای مدیریت PCهای گیم‌نت بساز.

سیستم‌ها به شکل Card نمایش داده شوند.

هر کارت شامل:

- نام سیستم
- شماره سیستم
- وضعیت
- نام کاربر
- زمان باقی‌مانده
- هزینه فعلی
- بازی در حال اجرا
- CPU Usage
- RAM Usage
- GPU Usage
- Network Status

وضعیت‌ها:

🟢 Available
🔵 In Use
🟡 Reserved
🔴 Error
⚫ Offline

امکان Filter و Search وجود داشته باشد.

مثلاً:

All
Available
In Use
Reserved
Offline
Error

---

# 5. مدیریت جلسه بازی

امکان ایجاد Session جدید:

- انتخاب PC
- انتخاب مشتری
- انتخاب نوع تعرفه
- انتخاب مدت زمان
- شروع Session

در Session فعال:

- Start Time
- Duration
- Remaining Time
- Current Cost

امکانات:

- Pause
- Resume
- Extend Time
- End Session
- Change PC
- Add Discount

وقتی زمان تمام شد، سیستم باید هشدار دهد.

---

# 6. سیستم تعرفه

امکان تعریف تعرفه‌های مختلف:

مثلاً:

Normal
VIP
Night
Weekend

امکان تعیین قیمت بر اساس:

- ساعت
- نیم ساعت
- بازه زمانی
- نوع سیستم

مثلاً:

PC Normal:
60,000 تومان / ساعت

PC VIP:
100,000 تومان / ساعت

تعرفه‌ها باید از داخل پنل قابل تغییر باشند.

---

# 7. مشتری‌ها

صفحه مدیریت مشتری‌ها:

- نام
- شماره تلفن
- شناسه
- تاریخ عضویت
- مجموع زمان بازی
- مجموع هزینه
- آخرین مراجعه
- موجودی کیف پول

صفحه جزئیات مشتری:

- تاریخچه Sessions
- پرداخت‌ها
- رزروها
- خریدهای فروشگاه
- مجموع هزینه
- امتیاز وفاداری

---

# 8. رزرو سیستم

یک سیستم Reservation کامل طراحی کن.

امکان:

- انتخاب PC
- انتخاب مشتری
- انتخاب تاریخ
- انتخاب ساعت شروع
- تعیین مدت
- ثبت رزرو

نمایش رزروها به شکل Calendar.

وضعیت رزرو:

Pending
Confirmed
Completed
Cancelled

در صورت نزدیک شدن زمان رزرو، هشدار نمایش داده شود.

---

# 9. مدیریت بازی‌ها

صفحه Games:

- نام بازی
- نسخه
- وضعیت نصب
- سیستم‌های دارای بازی
- حجم بازی
- آخرین Update

مثلاً:

CS2
Valorant
GTA V
FC 26
Call of Duty
Minecraft

امکان مشخص کردن اینکه هر بازی روی کدام PC نصب است.

---

# 10. فروشگاه / کافی‌شاپ

یک سیستم فروش ساده داخل پنل ایجاد کن.

محصولات:

- نوشیدنی
- چیپس
- شکلات
- ساندویچ
- سایر محصولات

هر محصول:

- نام
- قیمت
- موجودی
- دسته‌بندی

امکان ثبت سفارش برای مشتری.

مثلاً:

PC-04
Customer: Ali

Order:
Coca Cola × 1
Chips × 1

Total:
120,000 تومان

هزینه سفارش به حساب Session اضافه شود.

---

# 11. حسابداری

صفحه Finance ایجاد کن.

نمایش:

- درآمد امروز
- درآمد هفته
- درآمد ماه
- درآمد Sessionها
- درآمد فروشگاه
- تخفیف‌ها
- هزینه‌ها
- سود خالص

گزارش‌ها قابل Filter باشند.

---

# 12. گزارش‌ها

صفحه Reports:

### گزارش سیستم‌ها
- پربازده‌ترین PC
- کم‌استفاده‌ترین PC
- بیشترین زمان استفاده

### گزارش مشتری‌ها
- بهترین مشتری‌ها
- بیشترین هزینه
- بیشترین زمان بازی

### گزارش بازی‌ها
- محبوب‌ترین بازی‌ها
- بیشترین استفاده

### گزارش مالی
- درآمد روزانه
- درآمد هفتگی
- درآمد ماهانه

---

# 13. PC Agent

یک Agent با Python ایجاد کن.

Agent باید بتواند:

- اتصال به Server
- ارسال وضعیت PC
- CPU Usage
- RAM Usage
- GPU Usage
- Disk Usage
- Network Status
- Online/Offline Status

را گزارش کند.

معماری Agent را طوری طراحی کن که در آینده بتوان قابلیت‌های زیر را اضافه کرد:

- Lock PC
- Shutdown
- Restart
- Send Message
- Launch Game
- Close Game
- محدود کردن دسترسی کاربر

Agent باید با یک Device Token امن به Server متصل شود.

---

# 14. Real-Time

وضعیت سیستم‌ها باید Real-Time باشد.

اگر مثلاً:

PC-04

از Available به In Use تغییر کرد، بدون Refresh کردن صفحه وضعیت Dashboard و صفحه Systems تغییر کند.

از WebSocket استفاده کن.

---

# 15. Authentication

سیستم Login ایجاد کن.

Roleها:

Admin
Manager
Operator

هر Role سطح دسترسی متفاوت داشته باشد.

مثلاً:

Admin:
دسترسی کامل

Manager:
مدیریت سیستم‌ها، مشتری‌ها و گزارش‌ها

Operator:
شروع و پایان Session و ثبت فروش

---

# 16. طراحی UI

ظاهر پروژه باید حرفه‌ای و مخصوص Gaming باشد.

سبک:

Dark Gaming
Modern
Futuristic
Minimal
Glassmorphism

از رنگ‌های Neon به صورت کنترل‌شده استفاده کن.

رنگ اصلی پیشنهادی:
Neon Purple / Blue

پس‌زمینه:
Dark

UI نباید شلوغ باشد.

Sidebar سمت چپ داشته باشد.

ساختار Sidebar:

Dashboard
Systems
Sessions
Customers
Reservations
Games
Store
Finance
Reports
Settings

در پایین Sidebar:
Admin Profile
Logout

---

# 17. زبان

رابط کاربری اصلی فارسی باشد.

RTL را به صورت کامل پیاده‌سازی کن.

واحد پول:
تومان

تاریخ‌ها در UI:
شمسی

اما در Backend و Database از استانداردهای مناسب برای ذخیره DateTime استفاده کن.

---

# 18. Local Deployment

پروژه باید بتواند روی یک کامپیوتر داخل گیم‌نت اجرا شود.

پیشنهاد:

Docker Compose

شامل:

Frontend
Backend
PostgreSQL

و Agentها روی PCهای گیم‌نت اجرا شوند.

مدیر بتواند از سیستم‌های داخل شبکه با آدرس:

http://SERVER-IP

به پنل دسترسی داشته باشد.

سیستم نباید برای عملکرد اصلی خود به اینترنت وابسته باشد.

---

# 19. امنیت

موارد زیر را رعایت کن:

- Password Hashing
- JWT Authentication
- Role Based Access Control
- Device Token
- API Validation
- WebSocket Authentication
- Rate Limiting
- Secure Environment Variables
- Audit Logs

تمام عملیات مهم ثبت شوند.

مثلاً:

Admin
Started Session
PC-04
Time: 14:32

---

# 20. Database

Database Schema مناسب طراحی کن.

حداقل جداول:

users
roles
pcs
pc_status
customers
sessions
session_logs
tariffs
reservations
games
pc_games
products
orders
order_items
payments
expenses
notifications
audit_logs
devices

Relationshipها را اصولی طراحی کن.

---

# 21. Notifications

سیستم Notification ایجاد کن.

مثلاً:

⚠️ PC-04 آفلاین شد.

⏱️ زمان جلسه PC-02 رو به پایان است.

📅 رزرو PC-07 تا 15 دقیقه دیگر شروع می‌شود.

💰 پرداخت ثبت شد.

---

# 22. Dashboard UX

Dashboard باید در یک نگاه مهم‌ترین اطلاعات گیم‌نت را نشان دهد.

مدیر نباید برای دیدن وضعیت کلی مجبور به ورود به چند صفحه شود.

اولویت اطلاعات:

1. وضعیت سیستم‌ها
2. Sessions فعال
3. درآمد
4. رزروها
5. هشدارها

---

# 23. کیفیت کد

کد باید:

- Modular
- Clean
- Maintainable
- Type Safe
- Well Structured

باشد.

Frontend و Backend را کاملاً جدا نگه دار.

APIها را مستند کن.

از Environment Variables استفاده کن.

هیچ Password یا Secret را داخل Source Code قرار نده.

---

# 24. ساختار پروژه پیشنهادی

ساختار را مشابه این طراحی کن:

/gamenet
    /frontend
        /app
        /components
        /lib
        /hooks
        /types

    /backend
        /app
            /api
            /models
            /schemas
            /services
            /websocket
            /auth

    /agent
        /services
        /network
        /system

    /database

    docker-compose.yml

    README.md

---

# 25. مهم

قبل از پیاده‌سازی، ابتدا Architecture و Database Schema را طراحی کن.

بعد:

1. Backend
2. Database
3. Authentication
4. Frontend
5. Dashboard
6. Systems
7. Sessions
8. Customers
9. Reservations
10. Store
11. Finance
12. Reports
13. WebSocket
14. PC Agent

را مرحله‌به‌مرحله پیاده‌سازی کن.

در هر مرحله پروژه باید قابل اجرا باشد.

از ساخت Fake UI بدون Backend واقعی خودداری کن.

برای اطلاعات نمونه می‌توان Seed Data ایجاد کرد، ولی ساختار نهایی باید برای استفاده واقعی آماده باشد.

هدف نهایی:

یک **GameNet Management System حرفه‌ای، Local-First، Real-Time و قابل توسعه** که بتواند در یک گیم‌نت واقعی استفاده شود.
