[app]
title = MyApp
package.name = myapp
package.domain = com.example

# تحديد مصدر الكود (المجلد الرئيسي)
source.dir = .

# تضمين الامتدادات الضرورية
source.include_exts = py,png,jpg,kv,atlas

# المتطلبات
requirements = python3,kivy
# إعدادات الأندرويد
android.api = 31
android.ndk = 23b
android.arch = arm64-v8a

# إضافة رقم إصدار التطبيق
version = 1.0.0
