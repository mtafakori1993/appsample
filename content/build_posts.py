#!/usr/bin/env python3
"""Builds the six portfolio posts (3 projects x FA/EN) as block-editor HTML.

Reads media.json (uploaded attachment ids/urls) and writes posts.json.
No credentials are used or stored here.
"""
import json, sys, html

MEDIA = json.load(open(sys.argv[1] if len(sys.argv) > 1 else 'media.json'))
E = html.escape


def p(t): return f'<!-- wp:paragraph -->\n<p>{t}</p>\n<!-- /wp:paragraph -->\n\n'
def h2(t): return f'<!-- wp:heading -->\n<h2>{t}</h2>\n<!-- /wp:heading -->\n\n'
def h3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3>{t}</h3>\n<!-- /wp:heading -->\n\n'
def ul(items): return '<!-- wp:list -->\n<ul class="wp-block-list">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>\n<!-- /wp:list -->\n\n'
def raw(t): return f'<!-- wp:html -->\n{t}\n<!-- /wp:html -->\n\n'


def figure(url, alt, accent):
    return (f'<figure style="margin:0"><img src="{url}" alt="{E(alt)}" loading="lazy" '
            f'style="width:100%;height:auto;display:block;border-radius:18px;border:1px solid {accent}33;'
            f'box-shadow:0 18px 40px -18px rgba(0,0,0,.5)"/></figure>')


def gallery(imgs, accent, cols=260):
    return raw(f'<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax({cols}px,1fr));gap:16px;margin-block:24px">'
               + ''.join(figure(u, a, accent) for u, a in imgs) + '</div>')


def notice(text, accent, rtl=True):
    side = 'right' if rtl else 'left'
    return raw(f'<div style="margin-block:20px;padding:16px 20px;border-radius:14px;background:{accent}14;'
               f'border:1px solid {accent}55;border-{side}:4px solid {accent};line-height:1.9">{text}</div>')


def techgrid(cats, accent):
    cards = ''
    for title, items in cats:
        chips = ''.join(f'<span style="display:inline-block;margin:3px;padding:4px 12px;border-radius:999px;'
                        f'border:1px solid {accent}66;font-size:.92em">{E(i)}</span>' for i in items)
        cards += (f'<div style="padding:16px 18px;border-radius:16px;border:1px solid {accent}33;background:{accent}0d">'
                  f'<strong style="display:block;margin-bottom:8px">{E(title)}</strong>{chips}</div>')
    return raw(f'<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-block:20px">{cards}</div>')


def url(proj, name): return MEDIA[f'{proj}-{name}.webp']['url']


PROJECTS = {}

# --------------------------------------------------------------------- VISTA
A = '#B8924A'
vp = 'vista-estate'
vimgs_fa = [
    (url(vp, 'mobile-home'), 'صفحه اصلی اپلیکیشن اندروید ویستا با جست‌وجوی املاک لوکس تهران، فیلتر محله و ملک منتخب'),
    (url(vp, 'mobile-detail'), 'صفحه جزئیات ملک با گالری تصاویر، مشخصات، امکانات، نقشه‌ی واحد و دکمه‌ی درخواست بازدید'),
    (url(vp, 'web-dashboard'), 'پیشخوان وب آژانس املاک با موجودی املاک، بازدیدهای پیش‌رو و مسیر سرنخ‌ها'),
]
vimgs_en = [
    (url(vp, 'mobile-home'), 'VISTA Estate Android home screen with luxury Tehran listings, neighborhood filters and a featured property'),
    (url(vp, 'mobile-detail'), 'Property detail screen with gallery, specifications, amenities, floor plan and a viewing-request button'),
    (url(vp, 'web-dashboard'), 'Agency web workspace with property inventory, upcoming viewings and a lead pipeline'),
]

vista_fa = (
    p('<strong>پلتفرم کشف ملک و مدیریت آژانس برای املاک لوکس تهران؛ اپلیکیشن اندروید برای خریداران و فضای کاری وب برای مشاوران</strong>')
    + notice('<strong>وضعیت پروژه:</strong> ویستا یک <strong>مفهوم محصول و نمونه‌کار طراحی</strong> از تفکر پردازان است؛ برای مشتری واقعی ساخته یا مستقر نشده است. تصاویر این صفحه، طراحی‌های رابط کاربری با <strong>داده‌های نمایشی</strong> هستند (املاک، قیمت‌ها و نام‌ها فرضی‌اند) و از یک سامانه‌ی در حال اجرا گرفته نشده‌اند.', A)
    + p('ویستا برای یک آژانس املاک بوتیک فرضی با تمرکز بر ملک‌های لوکس مسکونی در تهران طراحی شده است. هدف این است که تجربه‌ی خریدار شبیه یک کاتالوگ منتخب باشد، نه یک آگهی‌نامه‌ی عمومی؛ و در همان زمان، مشاوران و مدیر آژانس ابزار منظمی برای موجودی ملک، سرنخ‌ها و بازدیدها داشته باشند.')
    + gallery([vimgs_fa[0]], A, 420)
    + h2('مسئله‌ی کسب‌وکار')
    + p('در بازار املاک لوکس، مشتری انتظار تصویر باکیفیت، اطلاعات دقیق و پاسخ سریع مشاور را دارد؛ اما بسیاری از آژانس‌ها هنوز موجودی خود را در پیام‌رسان‌ها، جدول‌های پراکنده و دفترچه‌ی یادداشت نگه می‌دارند. نتیجه این است که وضعیت ملک (موجود، رزرو، فروخته‌شده) هم‌زمان در چند جا متفاوت است، پیگیری سرنخ‌ها فراموش می‌شود و هماهنگی بازدید به رفت‌وبرگشت‌های طولانی می‌انجامد.')
    + h2('راهکار پیشنهادی')
    + p('دو سطح تجربه روی یک پایگاه داده‌ی مشترک: یک اپلیکیشن اندروید برای کاوش و درخواست بازدید، و یک فضای کاری وب برای مدیریت موجودی، سرنخ‌ها و تقویم بازدیدها. هر تغییر وضعیت ملک در فضای کاری، بلافاصله در اپلیکیشن دیده می‌شود.')
    + h2('کاربران هدف')
    + ul(['<strong>خریداران و مستأجران:</strong> جست‌وجوی ملک برای خرید، اجاره و رهن و اجاره، ذخیره، مقایسه و درخواست بازدید',
          '<strong>مالکان:</strong> ثبت ملک با نظارت مشاور و پیگیری وضعیت آگهی',
          '<strong>مشاوران املاک:</strong> مدیریت ملک‌ها، مشتریان بالقوه و برنامه‌ی بازدید',
          '<strong>مدیر آژانس:</strong> نظارت بر موجودی، سرنخ‌ها و عملکرد آگهی‌ها'])
    + h2('قابلیت‌های محصول')
    + h3('اپلیکیشن اندروید (خریداران)')
    + ul(['فید کاوش با عکس بزرگ و کارت‌های ملک، منتخب‌های مشاور و اطلاعات محله',
          'جست‌وجوی خرید، اجاره و رهن و اجاره با فیلتر محله، قیمت، متراژ، تعداد خواب، سن بنا و امکانات',
          'صفحه‌ی ملک با گالری تصاویر، پیش‌نمایش نقشه‌ی واحد، مشخصات فنی و موقعیت روی نقشه',
          'ذخیره و مقایسه‌ی ملک‌ها',
          'درخواست بازدید، تماس با مشاور مسئول و پیگیری وضعیت درخواست‌ها'])
    + h3('فضای کاری وب (مشاوران و مدیر)')
    + ul(['موجودی ملک با وضعیت آگهی (فعال، رزرو‌شده، در انتظار تأیید، پیش‌نویس) و افزودن و ویرایش ملک',
          'ثبت پرسش‌ها و پیگیری مشتریان بالقوه در مسیر سرنخ‌ها با یادآوری اقدام بعدی',
          'مدیریت تقویم بازدیدها و تأیید درخواست‌ها',
          'خلاصه‌ی عملکرد آگهی‌ها (بازدید آگهی، درخواست بازدید)',
          'دسترسی نقش‌محور برای مشاور و مدیر آژانس'])
    + gallery(vimgs_fa, A)
    + h2('تجربه‌ی کاربری و تصمیم‌های طراحی')
    + ul(['<strong>عکس‌محور و کم‌شلوغ:</strong> کارت‌های بزرگ، نوشتار کوتاه و اطلاعات کلیدی (قیمت، متراژ، خواب) در یک نگاه',
          '<strong>راست‌چین واقعی:</strong> چیدمان، آیکن‌ها، اعداد فارسی و فونت وزیرمتن برای محیط فارسی طراحی شده‌اند',
          '<strong>یک اقدام اصلی در هر صفحه:</strong> در صفحه‌ی ملک، دکمه‌ی «درخواست بازدید» همیشه در دسترس است',
          '<strong>فضای کاری مشاوران:</strong> جدول موجودی، تقویم بازدید و مسیر سرنخ‌ها کنار هم، تا مشاور برای کار روزانه به چند صفحه نرود',
          '<strong>پیکربندی رنگ:</strong> زمینه‌ی تیره‌ی آبی‌سبز برند تفکر پردازان با لهجه‌ی طلایی برای حس منتخب و لوکس'])
    + h2('معماری فنی پیشنهادی')
    + p('معماری هدف یک <strong>ماژولار مونولیت</strong> با Go است که با مرزهای روشن بین ماژول‌ها، هم برای تیم کوچک ساده می‌ماند و هم بعداً قابل تفکیک است.')
    + ul(['<strong>ماژول‌ها:</strong> ملک و رسانه، جست‌وجو، سرنخ‌ها، بازدیدها، کاربران و نقش‌ها، اعلان‌ها',
          '<strong>مدل داده (خلاصه):</strong> properties، property_media، listings (فروش / اجاره / رهن و اجاره)، neighborhoods، amenities، leads، viewings، consultants، users و activity_log',
          '<strong>جست‌وجوی مکانی:</strong> PostgreSQL با PostGIS برای فیلتر محله و فاصله، در جایی که پرسش جغرافیایی واقعاً لازم است',
          '<strong>رسانه:</strong> تصاویر در فضای ذخیره‌سازی سازگار با S3 با نسخه‌های کوچک‌شده برای موبایل',
          '<strong>API:</strong> REST با مستندات OpenAPI؛ API مشتری و API فضای کاری از هم جدا هستند',
          '<strong>کش:</strong> Redis برای نتایج جست‌وجوی پرتکرار، در صورت نیاز'])
    + h2('فناوری‌ها')
    + p('فهرست زیر <strong>معماری پیشنهادی</strong> است؛ در نمونه‌ی فعلی تنها طراحی رابط کاربری و نمونه‌ی HTML/CSS ساخته شده است.')
    + techgrid([('موبایل', ['Kotlin', 'Jetpack Compose', 'Material 3', 'Navigation Compose', 'Coroutines و Flow', 'Retrofit یا Ktor Client']),
                ('وب', ['Next.js (App Router)', 'TypeScript']),
                ('بک‌اند', ['Go', 'Chi یا Gin', 'REST API', 'OpenAPI']),
                ('داده و زیرساخت', ['PostgreSQL + PostGIS', 'Redis', 'ذخیره‌سازی سازگار با S3', 'Docker', 'CI/CD', 'لاگ ساخت‌یافته و پایش'])], A)
    + h2('امنیت و مقیاس‌پذیری')
    + ul(['احراز هویت مبتنی بر نشست یا توکن کوتاه‌مدت و کنترل دسترسی نقش‌محور (مشاور / مدیر) که در سرور اعمال می‌شود',
          'اعتبارسنجی ورودی، محدودیت نرخ درخواست و ثبت رویدادهای مهم برای پیگیری',
          'اطلاعات تماس مالکان فقط برای نقش‌های مجاز نمایش داده شود',
          'مقیاس‌پذیری: ایندکس‌گذاری جست‌وجو، کش نتایج پرتکرار، تصاویر بهینه با CDN و تفکیک تدریجی ماژول‌ها در صورت رشد'])
    + h2('وضعیت و محدودیت‌ها')
    + p('آنچه انجام شده: تعریف محصول، طراحی سه صفحه‌ی اصلی (صفحه‌ی خانه و صفحه‌ی ملک در اندروید، پیشخوان وب) و نمونه‌ی HTML/CSS آن‌ها با متن واقعی فارسی؛ عکس‌های ملک با ابزار هوش مصنوعی تولید شده‌اند و ملک واقعی نیستند.')
    + p('آنچه ساخته نشده: اپلیکیشن اندروید، وب‌اپ Next.js، سرویس Go، پایگاه داده و استقرار. هیچ مشتری، فروش یا آماری برای این محصول گزارش نمی‌شود.')
    + h2('نقشه‌ی راه')
    + ul(['ساخت MVP: کاوش و جست‌وجو، صفحه‌ی ملک و درخواست بازدید',
          'فضای کاری وب برای موجودی و سرنخ‌ها',
          'اعلان‌ها (پیام کوتاه و اعلان اپلیکیشن) برای یادآوری بازدیدها',
          'ابزار مقایسه‌ی پیشرفته و تور مجازی ملک',
          'گزارش‌های عملکرد و برچسب‌گذاری منبع سرنخ‌ها'])
    + h2('مشخصات پروژه')
    + ul(['نوع: مفهوم محصول و نمونه‌کار طراحی (بدون مشتری و استقرار واقعی)',
          'حوزه: فناوری املاک (PropTech) · پلتفرم‌ها: اندروید و وب · زبان: فارسی با چیدمان راست‌چین',
          'داده‌ها: نمایشی و فرضی',
          'طراحی و توسعه: تفکر پردازان — <a href="https://tafakorpardazan.ir">tafakorpardazan.ir</a>'])
)

vista_en = (
    p('<strong>A property discovery and agency management platform for luxury homes in Tehran: an Android app for buyers and a web workspace for agents</strong>')
    + notice('<strong>Project status:</strong> VISTA Estate is a <strong>product concept and design portfolio piece</strong> by Tafakor Pardazan. It was not built or deployed for a client. The images on this page are interface designs with <strong>demonstration data</strong> (properties, prices and names are fictional), not screenshots of a running system.', A, False)
    + p('VISTA Estate is designed for a fictional boutique agency that specializes in high-end residential property in Tehran. Buyers should feel they are browsing a curated catalog rather than a general classifieds site, while consultants and the agency manager get one structured place for inventory, leads and viewings.')
    + gallery([vimgs_en[0]], A, 420)
    + h2('The business problem')
    + p('In luxury real estate, clients expect strong photography, accurate details and quick answers. Many agencies still track inventory in chat apps and scattered spreadsheets, so listing status drifts between sources, follow-ups are missed, and scheduling a viewing takes too many back-and-forth messages.')
    + h2('Proposed solution')
    + p('Two experiences on one shared data layer: an Android app for browsing and requesting viewings, and a web workspace for managing inventory, leads and the viewing calendar. When a consultant changes a listing status, the app reflects it.')
    + h2('Target users')
    + ul(['<strong>Buyers and tenants:</strong> search to buy, rent or take a mortgage-style rental (rahn and ejare), save, compare and request viewings',
          '<strong>Property owners:</strong> list a property under consultant supervision and follow its status',
          '<strong>Consultants:</strong> manage listings, prospective buyers and the viewing schedule',
          '<strong>Agency manager:</strong> oversee inventory, pipeline and listing performance'])
    + h2('Product capabilities')
    + h3('Android app (buyers)')
    + ul(['Discovery feed with large photography, consultant picks and neighborhood information',
          'Search for sale, rent and mortgage rental with filters for neighborhood, price, area, bedrooms, building age and amenities',
          'Property page with gallery, floor-plan preview, specifications and map location',
          'Save and compare properties',
          'Request a viewing, contact the assigned consultant and follow the request status'])
    + h3('Web workspace (agents and manager)')
    + ul(['Property inventory with listing status (active, reserved, pending approval, draft) and add or edit property records',
          'Inquiry tracking and a lead pipeline with next-action reminders',
          'Viewing calendar with approval of requests',
          'Listing-performance summaries (listing views, viewing requests)',
          'Role-based access for consultants and the agency manager'])
    + gallery(vimgs_en, A)
    + h2('UX and design decisions')
    + ul(['<strong>Photo-led and calm:</strong> large cards, short copy, and key facts (price, area, bedrooms) visible at a glance',
          '<strong>Genuine RTL:</strong> layout, icons, Persian numerals and the Vazirmatn typeface are designed for Persian first',
          '<strong>One primary action per screen:</strong> the property page keeps "request a viewing" within reach',
          '<strong>Agent workspace:</strong> inventory table, viewing calendar and lead pipeline sit together so daily work does not require hopping between pages',
          '<strong>Palette:</strong> Tafakor Pardazan deep teal with a gold accent for a curated, premium feel'])
    + h2('Proposed technical architecture')
    + p('The target is a <strong>modular monolith</strong> in Go with clear module boundaries, simple for a small team now and splittable later.')
    + ul(['<strong>Modules:</strong> properties and media, search, leads, viewings, users and roles, notifications',
          '<strong>Data model (summary):</strong> properties, property_media, listings (sale / rent / mortgage rental), neighborhoods, amenities, leads, viewings, consultants, users and activity_log',
          '<strong>Geospatial search:</strong> PostgreSQL with PostGIS for neighborhood and distance filters, only where geographic queries justify it',
          '<strong>Media:</strong> images in S3-compatible object storage with resized variants for mobile',
          '<strong>API:</strong> REST documented with OpenAPI; the customer API and the workspace API are kept separate',
          '<strong>Caching:</strong> Redis for frequent search results, if needed'])
    + h2('Technology stack')
    + p('The list below is the <strong>proposed architecture</strong>. In the current portfolio piece only the interface design and an HTML/CSS prototype exist.')
    + techgrid([('Mobile', ['Kotlin', 'Jetpack Compose', 'Material 3', 'Navigation Compose', 'Coroutines and Flow', 'Retrofit or Ktor Client']),
                ('Web', ['Next.js (App Router)', 'TypeScript']),
                ('Backend', ['Go', 'Chi or Gin', 'REST API', 'OpenAPI']),
                ('Data and infrastructure', ['PostgreSQL + PostGIS', 'Redis', 'S3-compatible storage', 'Docker', 'CI/CD', 'Structured logs and monitoring'])], A)
    + h2('Security and scalability')
    + ul(['Session or short-lived token authentication with role-based authorization enforced on the server (consultant / manager)',
          'Input validation, rate limiting and audit events for important actions',
          "Owners' contact details visible only to authorized roles",
          'Scalability: search indexing, caching of hot queries, optimized images behind a CDN, and gradual module extraction if load requires it'])
    + h2('Status and limitations')
    + p('What exists: product definition, three core screens (Android home and property detail, web workspace) and an HTML/CSS prototype of each with real Persian text. Property photographs were generated with an AI image model and do not depict real listings.')
    + p('What does not exist: the Android app, the Next.js app, the Go service, the database and any deployment. No clients, sales or metrics are claimed for this product.')
    + h2('Roadmap')
    + ul(['Build the MVP: discovery, search, property page and viewing requests',
          'Web workspace for inventory and leads',
          'Notifications (SMS and in-app) for viewing reminders',
          'Advanced comparison and virtual property tours',
          'Performance reports and lead-source attribution'])
    + h2('Project details')
    + ul(['Type: product concept and design portfolio piece (no real client or deployment)',
          'Domain: PropTech · Platforms: Android and web · Language: Persian with RTL layout',
          'Data: demonstration data only',
          'Designed and developed by Tafakor Pardazan — <a href="https://tafakorpardazan.ir/en/home/">tafakorpardazan.ir</a>'])
)

PROJECTS['vista'] = dict(
    accent=A, media_key=vp, featured='mobile-home',
    fa=dict(title='ویستا (VISTA Estate)؛ پلتفرم هوشمند املاک لوکس تهران', slug='vista-estate', content=vista_fa,
            excerpt='نمونه‌کار طراحی ویستا، پلتفرم کشف ملک و مدیریت آژانس برای املاک لوکس تهران با اپلیکیشن اندروید و فضای کاری وب؛ مفهوم محصول از تفکر پردازان.'),
    en=dict(title='VISTA Estate: Luxury Property Discovery and Agency Platform', slug='vista-estate-luxury-real-estate-platform', content=vista_en,
            excerpt='A Tafakor Pardazan product concept: VISTA Estate, an Android app and web workspace for luxury real estate in Tehran, with property discovery and lead management.'),
)

# ------------------------------------------------------------------ HR PORTAL
B = '#3FB25A'
hp = 'met-explorers-hr-portal'
himgs_fa = [
    (url(hp, 'mobile-home'), 'داشبورد کارمند در اپلیکیشن اندروید پرتال منابع انسانی کاوشگران فناوری خاورمیانه با ثبت ورود و خروج، شیفت بعدی و مانده‌ی مرخصی'),
    (url(hp, 'mobile-leave-request'), 'درخواست مرخصی با تقویم شمسی، مانده‌ی مرخصی و مسیر تأیید مدیر مستقیم و منابع انسانی'),
    (url(hp, 'web-dashboard'), 'داشبورد وب منابع انسانی با دفترچه‌ی کارکنان، صف تأیید، استثناهای حضور و غیاب، دپارتمان‌ها و برنامه‌ریزی شیفت'),
]
himgs_en = [
    (url(hp, 'mobile-home'), 'Employee dashboard in the Android app of the Middle East Technology Explorers HR portal with check-in and out, next shift and leave balance'),
    (url(hp, 'mobile-leave-request'), 'Leave request with a Jalali calendar, leave balance and an approval path through the line manager and HR'),
    (url(hp, 'web-dashboard'), 'HR web dashboard with employee directory, approval queue, attendance exceptions, departments and shift planning'),
]

hr_fa = (
    p('<strong>پلتفرم خودخدمتی کارکنان و مدیریت نیروی انسانی با برند شرکت کاوشگران فناوری خاورمیانه؛ اپلیکیشن اندروید و پرتال وب</strong>')
    + notice('<strong>وضعیت پروژه:</strong> این صفحه یک <strong>مفهوم محصول و نمونه‌کار طراحی</strong> است که با نام و هویت بصری شرکت کاوشگران فناوری خاورمیانه ارائه شده؛ سامانه‌ای مستقر یا در حال استفاده نیست و گزارش آماری یا نتیجه‌ی کسب‌وکاری برای آن ارائه نمی‌شود. تصاویر، <strong>طراحی‌های رابط کاربری با نام‌ها و داده‌های فرضی</strong> هستند.', B)
    + p('پرتال منابع انسانی کاوشگران فناوری خاورمیانه برای یک شرکت فناوری چنددپارتمانی طراحی شده است؛ جایی که کارمندان باید حضور، شیفت، مرخصی و فیش حقوقی خود را در یک اپلیکیشن ببینند و مدیران و کارشناسان منابع انسانی درخواست‌ها و استثناها را در یک پرتال وب مدیریت کنند. هدف، پوشش چرخه‌ی کار روزمره‌ی کارمند است، نه فقط یک دستگاه ثبت ورود و خروج.')
    + gallery([himgs_fa[0]], B, 420)
    + h2('نیازمندی‌های کسب‌وکار')
    + p('در سازمان‌هایی با چند دپارتمان، درخواست مرخصی و اضافه‌کار معمولاً از طریق پیام‌رسان یا کاغذ جمع می‌شود. تأیید مدیر در جایی ثبت نمی‌شود، منابع انسانی استثناهای حضور را دیر می‌فهمد و آماده‌سازی حقوق به فایل‌های پراکنده وابسته است. این پروژه یک مسیر واحد، قابل پیگیری و ممیزی‌پذیر برای این کارها پیشنهاد می‌کند.')
    + h2('کاربران و نقش‌ها')
    + ul(['<strong>کارمند:</strong> حضور، شیفت، درخواست‌ها، فیش حقوقی، اطلاعیه‌ها و پروفایل',
          '<strong>مدیر مستقیم:</strong> بررسی و تأیید درخواست‌های تیم',
          '<strong>کارشناس منابع انسانی:</strong> پرونده‌ی کارکنان، استثناهای حضور، اسناد و ساختار سازمانی',
          '<strong>مسئول حقوق و دستمزد:</strong> آماده‌سازی و خروجی گرفتن از اطلاعات حقوق',
          '<strong>مدیر سامانه:</strong> نقش‌ها، دسترسی‌ها و گزارش ممیزی'])
    + h2('قابلیت‌های محصول')
    + h3('اپلیکیشن اندروید (کارمند)')
    + ul(['صفحه‌ی اصلی شخصی: وضعیت حضور امروز، ساعت کارکرد، شیفت بعدی، مانده‌ی مرخصی و اعلان‌ها',
          'ثبت ورود و خروج با بررسی محدوده‌ی مکانی مجاز',
          'تقویم شیفت و کار',
          'درخواست مرخصی (روزانه و ساعتی)، اضافه‌کار و مأموریت با تقویم شمسی',
          'پیگیری وضعیت درخواست‌ها و مسیر تأیید',
          'دسترسی به فیش‌ها و اسناد حقوقی و اطلاعیه‌های داخلی',
          'پروفایل و اطلاعات استخدامی'])
    + h3('پرتال وب (مدیران و منابع انسانی)')
    + ul(['نمای کلی سازمان: کارمندان فعال، حاضرین، مرخصی و مأموریت',
          'دفترچه‌ی کارکنان با دپارتمان، سمت، وضعیت و مدیر مستقیم',
          'استثناهای حضور و غیاب مانند خروج ثبت‌نشده و تأخیر',
          'صف تأیید مرخصی، اضافه‌کار و مأموریت',
          'برنامه‌ریزی و تخصیص شیفت',
          'مدیریت اسناد کارکنان و آماده‌سازی خروجی حقوق',
          'گزارش ممیزی اقدامات مهم مدیریتی',
          'کنترل دسترسی برای کارمند، مدیر، منابع انسانی و حقوق و دستمزد'])
    + gallery(himgs_fa, B)
    + h2('تجربه‌ی کاربری و تصمیم‌های طراحی')
    + ul(['<strong>اقدام اصلی روز، اول صفحه:</strong> کارت حضور با وضعیت، ساعت کارکرد و دکمه‌ی ورود یا خروج',
          '<strong>تقویم شمسی و هفته‌ی ایرانی:</strong> هفته از شنبه شروع می‌شود و جمعه تعطیل مشخص شده است',
          '<strong>شفافیت مسیر تأیید:</strong> کارمند پیش از ارسال می‌بیند درخواست او برای چه کسانی ارسال می‌شود',
          '<strong>پرتال مدیران:</strong> هر فهرست یک کار روشن دارد: تأیید، بررسی استثنا یا برنامه‌ریزی شیفت',
          '<strong>هویت بصری:</strong> نشان قطب‌نمایی برای نام «کاوشگران» و پالت آبی‌سبز با لهجه‌ی سبز روشن'])
    + h2('معماری فنی پیشنهادی')
    + p('سرویس Go با ماژول‌های جدا برای کارکنان، حضور و غیاب، مرخصی، شیفت، اسناد حقوقی، اعلان‌ها و رویدادهای ممیزی، روی PostgreSQL؛ به‌همراه صف کار پس‌زمینه برای اعلان‌ها، کارهای زمان‌بندی‌شده و خروجی‌ها.')
    + ul(['<strong>حضور و غیاب:</strong> زمان‌ها به‌صورت UTC ذخیره و بر اساس منطقه‌ی زمانی Asia/Tehran و تقویم شمسی نمایش داده می‌شوند؛ درخواست‌های ثبت تکراری با کلید یکتا رد می‌شوند',
          '<strong>گردش تأیید:</strong> ماشین حالت برای هر نوع درخواست (ثبت، تأیید مدیر، تأیید منابع انسانی، نتیجه) با ثبت تاریخچه',
          '<strong>اسناد حقوقی:</strong> فایل‌ها در ذخیره‌ساز خصوصی نگهداری و فقط پس از بررسی دسترسی و با لینک کوتاه‌مدت امضاشده تحویل داده می‌شوند؛ هیچ آدرس عمومی ندارند',
          '<strong>ممیزی:</strong> هر اقدام حساس (تغییر نقش، تأیید، دسترسی به سند) با شناسه‌ی کاربر و زمان ثبت می‌شود',
          '<strong>API:</strong> REST با مستندات OpenAPI و مجوزدهی نقش‌محور در سرور'])
    + h2('فناوری‌ها')
    + p('فهرست زیر <strong>معماری پیشنهادی</strong> است؛ در نمونه‌ی فعلی تنها طراحی رابط کاربری و نمونه‌ی HTML/CSS ساخته شده است.')
    + techgrid([('اندروید', ['Kotlin', 'Jetpack Compose', 'Material 3', 'Navigation Compose', 'Coroutines و Flow', 'Room (ذخیره‌ی محلی مناسب)', 'Retrofit یا Ktor Client']),
                ('وب', ['Next.js (App Router)', 'TypeScript', 'رابط واکنش‌گرا با پشتیبانی RTL و LTR']),
                ('بک‌اند', ['Go', 'REST API', 'OpenAPI', 'ماژول‌های کارکنان، حضور، مرخصی، شیفت و اعلان']),
                ('داده و زیرساخت', ['PostgreSQL', 'صف کار پس‌زمینه', 'Docker', 'CI/CD', 'لاگ ساخت‌یافته و پایش', 'پشتیبان‌گیری'])], B)
    + h2('امنیت و حریم خصوصی')
    + ul(['اطلاعات کارکنان فقط برای کاربران مجاز و بر اساس نقش و دپارتمان در دسترس است؛ کنترل دسترسی در سرور اعمال می‌شود',
          'فیش‌ها و اسناد حقوقی از مسیر آدرس عمومی ارائه نمی‌شوند',
          'اقدامات حساس قابل ممیزی هستند',
          'محاسبه‌ی اضافه‌کار و حقوق در این طرح <strong>مطابق قانون کار ادعا نمی‌شود</strong>؛ هر قاعده‌ی محاسباتی باید پیش از استفاده با کارشناس حقوقی و حسابداری شرکت صحت‌سنجی و تست شود'])
    + h2('وضعیت و محدودیت‌ها')
    + p('آنچه انجام شده: تعریف محصول، طراحی سه صفحه‌ی اصلی (داشبورد کارمند، درخواست مرخصی با تقویم و پرتال منابع انسانی) و نمونه‌ی HTML/CSS آن‌ها با نام‌ها و داده‌های فرضی.')
    + p('آنچه ساخته نشده: اپلیکیشن اندروید، پرتال Next.js، سرویس Go، پایگاه داده، محاسبات حقوق و استقرار. این صفحه ادعای استقرار یا همکاری تجاری با هیچ سازمانی ندارد.')
    + h2('نقشه‌ی راه')
    + ul(['MVP: حضور و غیاب، مرخصی و صف تأیید',
          'شیفت‌بندی و تقویم کاری',
          'اسناد کارکنان و فیش حقوقی با دسترسی کنترل‌شده',
          'خروجی آماده‌سازی حقوق با قواعد صحت‌سنجی‌شده',
          'اتصال به تقویم رسمی تعطیلات و سامانه‌های داخلی سازمان'])
    + h2('مشخصات پروژه')
    + ul(['نوع: مفهوم محصول و نمونه‌کار طراحی با هویت برند شرکت کاوشگران فناوری خاورمیانه (بدون استقرار و گزارش نتیجه‌ی واقعی)',
          'حوزه: فناوری منابع انسانی (HRTech) · پلتفرم‌ها: اندروید و وب · زبان: فارسی راست‌چین با پشتیبانی انگلیسی',
          'داده‌ها: نام‌ها و رکوردهای فرضی',
          'طراحی و توسعه: تفکر پردازان — <a href="https://tafakorpardazan.ir">tafakorpardazan.ir</a>'])
)

hr_en = (
    p('<strong>An employee self-service and workforce management platform branded for Middle East Technology Explorers: an Android app and a web portal</strong>')
    + notice('<strong>Project status:</strong> this is a <strong>product concept and design portfolio piece</strong> presented with the name and visual identity of Middle East Technology Explorers. It is not a deployed or in-use system, and no statistics or business results are claimed. The images are <strong>interface designs with fictional names and data</strong>.', B, False)
    + p('The Middle East Technology Explorers HR Portal is designed for a multi-department technology company. Employees see attendance, shifts, leave and payslips in one app; managers and HR specialists handle requests and exceptions in a web portal. The aim is the full daily employee lifecycle, not just a clock-in device.')
    + gallery([himgs_en[0]], B, 420)
    + h2('Business requirements')
    + p('In organizations with several departments, leave and overtime requests often travel through chat apps or paper. Manager approvals are not recorded anywhere, HR learns about attendance exceptions late, and payroll preparation depends on scattered files. This project proposes one trackable, auditable path for those tasks.')
    + h2('Users and roles')
    + ul(['<strong>Employee:</strong> attendance, shifts, requests, payslips, announcements and profile',
          '<strong>Line manager:</strong> review and approve team requests',
          '<strong>HR specialist:</strong> employee records, attendance exceptions, documents and organization structure',
          '<strong>Payroll administrator:</strong> prepare and export payroll data',
          '<strong>System administrator:</strong> roles, permissions and the audit log'])
    + h2('Product capabilities')
    + h3('Android app (employees)')
    + ul(['Personal home: today\'s attendance, hours worked, next shift, leave balance and notifications',
          'Check-in and check-out with an allowed-location check',
          'Shift and work calendar',
          'Leave (daily and hourly), overtime and business-trip requests with a Jalali calendar',
          'Request tracking and approval path',
          'Payslips, payroll documents and internal announcements',
          'Profile and employment information'])
    + h3('Web portal (managers and HR)')
    + ul(['Organization overview: active employees, present today, leave and missions',
          'Employee directory with department, role, status and line manager',
          'Attendance exceptions such as missing check-outs and late arrivals',
          'Approval queue for leave, overtime and business trips',
          'Shift planning and assignment',
          'Employee document management and payroll export preparation',
          'Audit trail for important administrative actions',
          'Role-based access for employees, managers, HR and payroll administrators'])
    + gallery(himgs_en, B)
    + h2('UX and design decisions')
    + ul(['<strong>The main action first:</strong> an attendance card with status, hours worked and the check-in or check-out button',
          '<strong>Jalali calendar and the Iranian week:</strong> the week starts on Saturday and Friday is marked as the weekend',
          '<strong>Transparent approval path:</strong> before submitting, employees see who the request goes to',
          '<strong>Manager portal:</strong> every list has one clear job: approve, review an exception, or plan a shift',
          '<strong>Visual identity:</strong> a compass mark for the "Explorers" name and a teal palette with a light-green accent'])
    + h2('Proposed technical architecture')
    + p('A Go service with separate modules for employees, attendance, leave, shifts, payroll documents, notifications and audit events on PostgreSQL, plus a background job runner for notifications, scheduled tasks and exports.')
    + ul(['<strong>Attendance:</strong> timestamps stored in UTC and displayed in the Asia/Tehran zone and Jalali calendar; duplicate submissions are rejected with idempotency keys',
          '<strong>Approval workflow:</strong> a state machine per request type (submitted, manager approval, HR approval, outcome) with recorded history',
          '<strong>Payroll documents:</strong> kept in private storage and delivered only after an authorization check through short-lived signed links; they have no public URL',
          '<strong>Audit:</strong> every sensitive action (role change, approval, document access) is recorded with user and time',
          '<strong>API:</strong> REST documented with OpenAPI and role-based authorization enforced on the server'])
    + h2('Technology stack')
    + p('The list below is the <strong>proposed architecture</strong>. In the current portfolio piece only the interface design and an HTML/CSS prototype exist.')
    + techgrid([('Android', ['Kotlin', 'Jetpack Compose', 'Material 3', 'Navigation Compose', 'Coroutines and Flow', 'Room (where local persistence fits)', 'Retrofit or Ktor Client']),
                ('Web', ['Next.js (App Router)', 'TypeScript', 'Responsive RTL and LTR interface']),
                ('Backend', ['Go', 'REST API', 'OpenAPI', 'Modules: employees, attendance, leave, shifts, notifications']),
                ('Data and infrastructure', ['PostgreSQL', 'Background job runner', 'Docker', 'CI/CD', 'Structured logs and monitoring', 'Backups'])], B)
    + h2('Security and privacy')
    + ul(['Employee data is available only to authorized users by role and department, with access control enforced on the server',
          'Payslips and payroll documents are never served from public asset URLs',
          'Sensitive actions are auditable',
          'Overtime and payroll calculations are <strong>not presented as legally compliant</strong>; any calculation rule must be validated and tested with the company\'s legal and accounting specialists before use'])
    + h2('Status and limitations')
    + p('What exists: product definition, three core screens (employee dashboard, leave request with calendar, and the HR portal) and an HTML/CSS prototype of each using fictional names and data.')
    + p('What does not exist: the Android app, the Next.js portal, the Go service, the database, payroll calculations and any deployment. This page makes no claim of deployment or a commercial engagement with any organization.')
    + h2('Roadmap')
    + ul(['MVP: attendance, leave and the approval queue',
          'Shift scheduling and the work calendar',
          'Employee documents and payslips with controlled access',
          'Payroll export with validated rules',
          'Integration with the official holiday calendar and internal systems'])
    + h2('Project details')
    + ul(['Type: product concept and design portfolio piece with the brand identity of Middle East Technology Explorers (no deployment or real results reported)',
          'Domain: HRTech · Platforms: Android and web · Language: Persian RTL with English support',
          'Data: fictional names and records',
          'Designed and developed by Tafakor Pardazan — <a href="https://tafakorpardazan.ir/en/home/">tafakorpardazan.ir</a>'])
)

PROJECTS['hr'] = dict(
    accent=B, media_key=hp, featured='mobile-home',
    fa=dict(title='پرتال منابع انسانی کاوشگران فناوری خاورمیانه', slug='met-explorers-hr-portal', content=hr_fa,
            excerpt='نمونه‌کار طراحی پرتال منابع انسانی شرکت کاوشگران فناوری خاورمیانه: اپلیکیشن اندروید کارکنان و پرتال وب برای حضور، شیفت، مرخصی و تأیید درخواست‌ها؛ مفهوم محصول از تفکر پردازان.'),
    en=dict(title='Middle East Technology Explorers — Human Resources Portal', slug='middle-east-technology-explorers-hr-portal', content=hr_en,
            excerpt='A Tafakor Pardazan product concept: an Android app and web portal for attendance, shifts, leave and approvals, branded for Middle East Technology Explorers.'),
)

# ------------------------------------------------------------------- SAFFRON
C = '#E8A92D'
sp = 'saffron-table'
simgs_fa = [
    (url(sp, 'mobile-home'), 'صفحه اصلی اپلیکیشن اندروید سفران با دسته‌بندی منو، پیشنهاد سرآشپز و باشگاه مشتریان'),
    (url(sp, 'mobile-detail-cart'), 'صفحه‌ی غذا با انتخاب اندازه و افزودنی‌ها و سبد خرید با کد تخفیف و جمع‌بندی مبلغ'),
    (url(sp, 'web-dashboard'), 'داشبورد آشپزخانه با صف سفارش‌ها بر اساس وضعیت، موجودی منو، فروش ساعتی و پرفروش‌ها'),
]
simgs_en = [
    (url(sp, 'mobile-home'), 'SAFFRON Table Android home screen with menu categories, chef picks and a loyalty club'),
    (url(sp, 'mobile-detail-cart'), 'Dish screen with portion and add-on selection, and a cart with discount code and price breakdown'),
    (url(sp, 'web-dashboard'), 'Kitchen dashboard with orders by status, menu availability, hourly sales and best sellers'),
]

sf_fa = (
    p('<strong>پلتفرم سفارش مستقیم برای یک رستوران ایرانی؛ اپلیکیشن اندروید، وب‌سایت سفارش و داشبورد آشپزخانه با هویت برند اختصاصی</strong>')
    + notice('<strong>وضعیت پروژه:</strong> سفران یک <strong>مفهوم محصول و نمونه‌کار طراحی</strong> برای یک رستوران فرضی است. رستوران، منو، قیمت‌ها و سفارش‌های نمایش‌داده‌شده <strong>نمونه و فرضی</strong> هستند و پرداخت در این طرح <strong>شبیه‌سازی</strong> می‌شود؛ هیچ پرداخت واقعی انجام نمی‌شود.', C)
    + p('سفران برای رستورانی طراحی شده که می‌خواهد سفارش آنلاین را در کانال اختصاصی خودش داشته باشد، نه صرفاً به‌عنوان یک گزینه میان رستوران‌های دیگر در یک بازارگاه. تمرکز، تجربه‌ی برند، منوی دقیق و گردش کار روشن آشپزخانه است.')
    + gallery([simgs_fa[0]], C, 420)
    + h2('مدل کسب‌وکار سفارش مستقیم')
    + p('رستوران‌ها در بازارگاه‌های سفارش غذا با کمیسیون، رقابت قیمتی و محدودیت در ارتباط با مشتری روبه‌رو هستند. کانال سفارش مستقیم به رستوران اجازه می‌دهد منو، قیمت و تجربه‌ی خود را کنترل کند، با مشتری ارتباط مستقیم داشته باشد و باشگاه مشتریان بسازد. در این طرح، کانال مستقیم مکمل کانال‌های دیگر دیده شده است.')
    + h2('کاربران')
    + ul(['<strong>مشتری:</strong> انتخاب غذا، سفارش ارسال یا تحویل حضوری، پیگیری و تاریخچه‌ی سفارش',
          '<strong>مدیر رستوران:</strong> منو، قیمت، تخفیف، مناطق ارسال، ساعات کاری و گزارش فروش',
          '<strong>کارکنان آشپزخانه:</strong> مشاهده‌ی صف سفارش و تغییر وضعیت آماده‌سازی',
          '<strong>مسئول سفارش‌ها:</strong> پذیرش یا رد سفارش، هماهنگی ارسال و پیگیری لغو و بازپرداخت'])
    + h2('سفر مشتری')
    + ul(['ورود به صفحه‌ی اصلی با عکس غذا، دسته‌های کباب، خوراک، پیش‌غذا، نوشیدنی و دسر',
          'صفحه‌ی غذا: مواد تشکیل‌دهنده، انتخاب اندازه‌ی پرس و افزودنی‌ها',
          'سبد خرید: ویرایش هر قلم، انتخاب ارسال یا تحویل حضوری، آدرس و توضیحات تحویل، کد تخفیف',
          'ثبت سفارش و پیگیری با خط زمانی وضعیت',
          'تاریخچه‌ی سفارش‌ها و امتیازهای باشگاه مشتریان'])
    + h2('گردش کار آشپزخانه و وضعیت سفارش')
    + p('هر سفارش از یک ماشین حالت مشخص عبور می‌کند تا پذیرش، آماده‌سازی، ارسال، تحویل، لغو و بازپرداخت با هم اشتباه گرفته نشوند:')
    + ul(['<strong>جدید ← پذیرفته‌شده یا ردشده</strong> (رد با ثبت دلیل)',
          '<strong>پذیرفته‌شده ← در حال آماده‌سازی ← آماده</strong>',
          '<strong>آماده ← ارسال‌شده ← تحویل‌شده</strong> (برای ارسال) یا <strong>آماده ← تحویل به مشتری</strong> (برای تحویل حضوری)',
          '<strong>لغوشده</strong> با دلیل، و در صورت پرداخت‌شده بودن، <strong>بازپرداخت در انتظار ← بازپرداخت‌شده</strong>'])
    + gallery(simgs_fa, C)
    + h2('قابلیت‌های محصول')
    + ul(['اپلیکیشن اندروید مشتری با منوی دسته‌بندی‌شده، سفارش سفارشی‌سازی‌شده و باشگاه مشتریان',
          'وب‌سایت برند با منو، جست‌وجو، سبد خرید، تسویه و صفحه‌ی وضعیت سفارش',
          'صف سفارش ورودی با پذیرش یا رد و تغییر وضعیت آماده‌سازی و تحویل',
          'مدیریت منو و موجودی: خاموش و روشن کردن غذا هنگام تمام شدن',
          'پیکربندی قیمت، کد تخفیف، مناطق ارسال و ساعات کاری',
          'خلاصه‌ی فروش و پرفروش‌ترین غذاها'])
    + h2('تجربه‌ی کاربری و هویت بصری')
    + ul(['<strong>تصویر غذا در مرکز:</strong> زمینه‌ی تیره‌ی گرم با لهجه‌ی زعفرانی تا غذا بدرخشد',
          '<strong>سفارش با کمترین قدم:</strong> دکمه‌ی افزودن در کارت غذا و سبد با جمع‌بندی شفاف',
          '<strong>جمع مبلغ قابل‌اتکا:</strong> جمع اقلام، تخفیف، هزینه‌ی ارسال و مبلغ نهایی همیشه از یک محاسبه‌ی سمت سرور می‌آیند',
          '<strong>داشبورد آشپزخانه:</strong> ستون‌های وضعیت و کارت‌های سفارش با زمان انتظار، برای خواندن سریع در محیط شلوغ'])
    + h2('معماری فنی پیشنهادی')
    + p('یک <strong>ماژولار مونولیت</strong> با Go روی PostgreSQL، با ماژول‌های منو، سبد و قیمت‌گذاری، سفارش، پرداخت، اعلان و گزارش.')
    + ul(['<strong>محاسبه‌ی مبلغ:</strong> مبلغ‌ها به‌صورت عدد صحیح تومان نگهداری می‌شوند. مبلغ نهایی = Σ (تعداد × (قیمت پایه + افزودنی‌ها)) − تخفیف + هزینه‌ی ارسال؛ در یک تابع سمت سرور محاسبه می‌شود و کلاینت فقط نمایش می‌دهد',
          '<strong>لایه‌ی پرداخت:</strong> یک رابط PaymentProvider (مجوز، تأیید، بازپرداخت) با کلید تکراری‌نشدن (idempotency) و یک پیاده‌سازی <strong>شبیه‌سازی‌شده / سندباکس</strong> برای نمونه؛ اتصال به درگاه واقعی در آینده بدون تغییر منطق سفارش',
          '<strong>پایگاه داده (خلاصه):</strong> menu_items، modifiers، carts، orders، order_items، order_events، discounts، delivery_zones، customers، loyalty_ledger',
          '<strong>اعلان‌ها:</strong> رویدادهای سفارش در پایگاه داده (الگوی outbox) و ارسال آن‌ها به اعلان اپلیکیشن، پیام کوتاه و نمایشگر آشپزخانه',
          '<strong>سبد موقت:</strong> Redis برای سبد و کدهای تخفیف در صورت نیاز',
          '<strong>تصاویر غذا:</strong> ذخیره‌سازی سازگار با S3',
          '<strong>نسخه‌ی برند اختصاصی برای رستوران‌های دیگر:</strong> رنگ، لوگو، منو و مناطق ارسال به‌صورت تنظیمات هر مستأجر (tenant) تا همین محصول برای رستوران‌های دیگر نیز قابل استفاده باشد'])
    + h2('فناوری‌ها')
    + p('فهرست زیر <strong>معماری پیشنهادی</strong> است؛ در نمونه‌ی فعلی تنها طراحی رابط کاربری و نمونه‌ی HTML/CSS ساخته شده است.')
    + techgrid([('موبایل', ['Kotlin', 'Jetpack Compose', 'Material 3', 'Navigation Compose', 'Coroutines و Flow', 'Retrofit یا Ktor Client']),
                ('وب', ['Next.js (App Router)', 'TypeScript', 'صفحات سمت سرور برای منو و SEO']),
                ('بک‌اند', ['Go', 'REST API', 'OpenAPI', 'رابط PaymentProvider']),
                ('داده و زیرساخت', ['PostgreSQL', 'Redis', 'ذخیره‌سازی سازگار با S3', 'اعلان‌های Push', 'Docker', 'CI/CD', 'لاگ ساخت‌یافته، پایش و پشتیبان‌گیری'])], C)
    + h2('امنیت و کارایی')
    + ul(['قیمت و تخفیف همیشه در سرور محاسبه می‌شود تا دست‌کاری مبلغ در کلاینت اثری نداشته باشد',
          'دسترسی نقش‌محور برای مدیر، آشپزخانه و مسئول سفارش',
          'رویدادهای سفارش، لغو و بازپرداخت ثبت و قابل پیگیری هستند',
          'اطلاعات پرداخت کارت در سامانه نگهداری نمی‌شود؛ پرداخت از طریق درگاه انجام می‌شود',
          'کش منو و تصاویر بهینه برای زمان بارگذاری کوتاه'])
    + h2('وضعیت و محدودیت‌ها')
    + p('آنچه انجام شده: تعریف محصول، طراحی سه صفحه‌ی اصلی (صفحه‌ی خانه و صفحه‌ی غذا همراه با سبد در اندروید، داشبورد آشپزخانه) و نمونه‌ی HTML/CSS آن‌ها. عکس غذاها با ابزار هوش مصنوعی تولید شده است و منو و قیمت‌ها نمونه هستند.')
    + p('آنچه ساخته نشده: اپلیکیشن، وب‌سایت، سرویس Go، پایگاه داده، درگاه پرداخت و استقرار. تسویه‌ی نشان‌داده‌شده در طراحی، <strong>شبیه‌سازی</strong> است و هیچ پرداخت واقعی را نشان نمی‌دهد.')
    + h2('نقشه‌ی راه')
    + ul(['MVP: منو، سبد، تسویه‌ی سندباکس و صف سفارش آشپزخانه',
          'اتصال به درگاه پرداخت واقعی',
          'پیگیری لحظه‌ای ارسال و اعلان‌های Push',
          'باشگاه مشتریان با امتیاز و پاداش',
          'نسخه‌ی برند اختصاصی (white-label) برای چند رستوران'])
    + h2('مشخصات پروژه')
    + ul(['نوع: مفهوم محصول و نمونه‌کار طراحی (بدون مشتری و استقرار واقعی)',
          'حوزه: تجارت رستورانی (FoodTech) · پلتفرم‌ها: اندروید و وب · زبان: فارسی راست‌چین',
          'داده‌ها: منو و قیمت‌های نمونه · پرداخت: شبیه‌سازی‌شده',
          'طراحی و توسعه: تفکر پردازان — <a href="https://tafakorpardazan.ir">tafakorpardazan.ir</a>'])
)

sf_en = (
    p('<strong>A direct-ordering platform for a Persian restaurant: an Android app, an ordering website and a kitchen dashboard with its own brand identity</strong>')
    + notice('<strong>Project status:</strong> SAFFRON Table is a <strong>product concept and design portfolio piece</strong> for a fictional restaurant. The restaurant, menu, prices and orders shown are <strong>illustrative sample data</strong>, and payment in this concept is <strong>simulated</strong>; no real payment is processed.', C, False)
    + p('SAFFRON Table is designed for a restaurant that wants online ordering on its own channel rather than as one listing among many in a marketplace. The focus is the brand experience, an accurate menu and a clear kitchen workflow.')
    + gallery([simgs_en[0]], C, 420)
    + h2('The direct-ordering business model')
    + p('On marketplaces, restaurants face commissions, price competition and limited access to their own customers. A direct channel lets the restaurant control its menu, pricing and experience, talk to its customers directly and build a loyalty club. In this concept the direct channel complements other channels.')
    + h2('Users')
    + ul(['<strong>Customers:</strong> pick dishes, order for delivery or pickup, track orders and view history',
          '<strong>Restaurant manager:</strong> menu, pricing, discounts, delivery zones, hours and sales reports',
          '<strong>Kitchen staff:</strong> see the order queue and update preparation status',
          '<strong>Order staff:</strong> accept or reject orders, coordinate dispatch and follow cancellations and refunds'])
    + h2('Customer journey')
    + ul(['Land on a home screen with food photography and the categories: kebab, mains, starters, drinks and desserts',
          'Dish page: ingredients, portion size and add-ons',
          'Cart: edit each line, choose delivery or pickup, address and delivery notes, discount code',
          'Place the order and track it on a status timeline',
          'Order history and loyalty points'])
    + h2('Kitchen workflow and order states')
    + p('Each order moves through an explicit state machine so acceptance, preparation, dispatch, delivery, cancellation and refund are never confused:')
    + ul(['<strong>New → accepted or rejected</strong> (rejection records a reason)',
          '<strong>Accepted → preparing → ready</strong>',
          '<strong>Ready → dispatched → delivered</strong> (delivery) or <strong>ready → handed to the customer</strong> (pickup)',
          '<strong>Cancelled</strong> with a reason and, if already paid, <strong>refund pending → refunded</strong>'])
    + gallery(simgs_en, C)
    + h2('Product capabilities')
    + ul(['Android customer app with a categorized menu, customizable orders and a loyalty club',
          'Branded website with menu, search, cart, checkout and an order-status page',
          'Incoming order queue with accept or reject and preparation and handoff updates',
          'Menu and availability management: switch a dish off when it runs out',
          'Pricing, discount codes, delivery zones and operating hours',
          'Sales summary and best-selling dishes'])
    + h2('UX and visual identity')
    + ul(['<strong>Food at the center:</strong> a warm dark canvas with a saffron accent so the dishes glow',
          '<strong>Fewest steps to order:</strong> an add button on every dish card and a cart with a transparent breakdown',
          '<strong>Reliable totals:</strong> items, discount, delivery fee and final total always come from one server-side calculation',
          '<strong>Kitchen dashboard:</strong> status columns and order cards with waiting time, readable at a glance in a busy kitchen'])
    + h2('Proposed technical architecture')
    + p('A Go <strong>modular monolith</strong> on PostgreSQL, with modules for menu, cart and pricing, orders, payments, notifications and reporting.')
    + ul(['<strong>Totals:</strong> amounts are stored as integer toman. Total = Σ (quantity × (base price + add-ons)) − discount + delivery fee, computed in one server-side function; clients only display it',
          '<strong>Payment layer:</strong> a PaymentProvider interface (authorize, capture, refund) with idempotency keys and a <strong>simulated / sandbox</strong> implementation for the demo; a real gateway can be added later without changing order logic',
          '<strong>Database (summary):</strong> menu_items, modifiers, carts, orders, order_items, order_events, discounts, delivery_zones, customers, loyalty_ledger',
          '<strong>Notifications:</strong> order events written to the database (outbox pattern) and dispatched as push notifications, SMS and updates to the kitchen display',
          '<strong>Temporary cart state:</strong> Redis for carts and discount codes, if needed',
          '<strong>Food photography:</strong> S3-compatible object storage',
          '<strong>White-label deployment:</strong> color, logo, menu and delivery zones as per-tenant configuration, so the same product can serve other restaurants'])
    + h2('Technology stack')
    + p('The list below is the <strong>proposed architecture</strong>. In the current portfolio piece only the interface design and an HTML/CSS prototype exist.')
    + techgrid([('Mobile', ['Kotlin', 'Jetpack Compose', 'Material 3', 'Navigation Compose', 'Coroutines and Flow', 'Retrofit or Ktor Client']),
                ('Web', ['Next.js (App Router)', 'TypeScript', 'Server-rendered menu pages for SEO']),
                ('Backend', ['Go', 'REST API', 'OpenAPI', 'PaymentProvider abstraction']),
                ('Data and infrastructure', ['PostgreSQL', 'Redis', 'S3-compatible storage', 'Push notifications', 'Docker', 'CI/CD', 'Structured logs, monitoring and backups'])], C)
    + h2('Security and performance')
    + ul(['Prices and discounts are always calculated on the server so tampering on a client has no effect',
          'Role-based access for manager, kitchen and order staff',
          'Order, cancellation and refund events are recorded and traceable',
          'Card details are never stored in the system; payment is handled by the gateway',
          'Cached menu data and optimized images for fast load times'])
    + h2('Status and limitations')
    + p('What exists: product definition, three core screens (Android home, dish page with cart, and the kitchen dashboard) and an HTML/CSS prototype of each. Food photographs were generated with an AI image model; the menu and prices are samples.')
    + p('What does not exist: the apps, the website, the Go service, the database, a payment gateway and any deployment. The checkout shown in the design is a <strong>simulation</strong> and does not represent a real payment.')
    + h2('Roadmap')
    + ul(['MVP: menu, cart, sandbox checkout and the kitchen order queue',
          'Connect a real payment gateway',
          'Live delivery tracking and push notifications',
          'Loyalty club with points and rewards',
          'White-label edition for multiple restaurants'])
    + h2('Project details')
    + ul(['Type: product concept and design portfolio piece (no real client or deployment)',
          'Domain: restaurant commerce (FoodTech) · Platforms: Android and web · Language: Persian RTL',
          'Data: sample menu and prices · Payment: simulated',
          'Designed and developed by Tafakor Pardazan — <a href="https://tafakorpardazan.ir/en/home/">tafakorpardazan.ir</a>'])
)

PROJECTS['saffron'] = dict(
    accent=C, media_key=sp, featured='mobile-home',
    fa=dict(title='سفران (SAFFRON Table)؛ سفارش آنلاین اختصاصی رستوران', slug='saffron-table', content=sf_fa,
            excerpt='نمونه‌کار طراحی سفران، پلتفرم سفارش مستقیم برای یک رستوران ایرانی با اپلیکیشن اندروید، وب‌سایت سفارش و داشبورد آشپزخانه؛ مفهوم محصول از تفکر پردازان.'),
    en=dict(title='SAFFRON Table: Direct Online Ordering for a Persian Restaurant', slug='saffron-table-restaurant-direct-ordering', content=sf_en,
            excerpt='A Tafakor Pardazan product concept: SAFFRON Table, an Android app, ordering website and kitchen dashboard for direct restaurant ordering with simulated payment.'),
)

json.dump(PROJECTS, open('posts.json', 'w'), ensure_ascii=False, indent=1)
print({k: (len(v['fa']['content']), len(v['en']['content'])) for k, v in PROJECTS.items()})
