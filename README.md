# Predicting-the-price-of-Bitcoin

#hosh.py
Predicting the price of Bitcoin
This code uses the Coingecko API to get the price data for Bitcoin over the past 10 days, and then uses that data to train a neural network to predict the next day's price. The neural network is a simple feedforward network with two hidden layers, and it is trained using mean squared error as the loss function and the Adam optimizer. Once the model is trained, it is used to predict the next day's price, and the minimum and maximum predicted prices are printed out, with a buffer of +/- 10 USD. Note that this is just an example and the actual accuracy of the prediction will depend on many factors and cannot be guaranteed.

===================================================================================
این کد از API Coingecko برای دریافت داده‌های قیمت بیت کوین در طول ۱۰ روز گذشته استفاده می‌کند و سپس از این داده‌ها برای آموزش یک شبکه عصبی برای پیش‌بینی قیمت روز بعد بیت کوین استفاده می‌شود. شبکه عصبی از دو لایه پنهان با تابع فعال‌سازی relu تشکیل شده است و با استفاده از خطای میانگین مربعات به عنوان تابع خطای و بهینه‌ساز Adam آموزش داده می‌شود. پس از آموزش مدل، برای پیش‌بینی قیمت روز بعد از آن استفاده می‌شود و حداقل و حداکثر قیمت‌های پیش‌بینی شده برای روز بعد با بافر +/- ۱۰ دلار چاپ می‌شوند. توجه داشته باشید که این فقط یک مثال است و دقت پیش‌بینی واقعی بستگی به عوامل مختلفی دارد و قابل تضمین نیست.

======================================================================================

#hosh2.py

این کد از API Coingecko برای دریافت داده‌های قیمت بیت کوین در طول ۳۰ روز گذشته استفاده می‌کند و سپس از این داده‌ها برای آموزش یک شبکه عصبی با استفاده از TensorFlow استفاده می‌شود. شبکه عصبی یک شبکه دو لایه پنهان با تابع فعال‌سازی relu و یک لایه خروجی است. شبکه عصبی با استفاده از خطای میانگین مربعات به عنوان تابع خطای و بهینه‌ساز Adam آموزش داده می‌شود. پس از آموزش مدل، برای پیش‌بینی قیمت بیت کوین در هفت روز بعد، از مدل استفاده می‌شود. برای هفت روز بعد، قیمت بیت کوین با استفاده از مدل پیش‌بینی می‌شود و سپس حداقل و حداکثر قیمت‌های پیش‌بینی شده برای هر روز با بافر +/- ۵٪ از قیمت پیش‌بینی شده چاپ می‌شوند. 

توجه داشته باشید که این پیش‌بینی‌ها فقط بر اساس داده‌های قبلی قیمت بیت کوین است و نمی‌تواند دقیقاً قیمت واقعی آینده را پیش‌بینی کند.

برای اجرای این کد، باید کتابخانه‌های requests، numpy و TensorFlow نصب شده باشد.

================================================================================

i wish some buddy complete this code

