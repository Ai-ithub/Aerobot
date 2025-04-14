<!-- import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
from scipy.signal import savgol_filter

# تنظیمات اولیه
np.random.seed(42)
random.seed(42)
num_samples = 1000
start_time = datetime.now()

## 1. داده‌های زمانی
timestamps = [start_time + timedelta(seconds=i) for i in range(num_samples)]

## 2. داده‌های موقعیت و ارتفاع
# شبیه‌سازی مسیر پرواز: ابتدا کاهش ارتفاع، سپس انتقال به فاز کروز
altitude = np.concatenate([
    np.linspace(500, 100, 300),  # کاهش ارتفاع با پاراشوت
    np.linspace(100, 80, 100),   # انتقال فاز
    np.linspace(80, 75, 600)     # فاز کروز
])

# اضافه کردن نویز طبیعی
altitude += np.random.normal(0, 0.5, num_samples)

# مختصات GPS (شبیه‌سازی یک مسیر دایره‌ای)
lat = 35.6892 + 0.001 * np.sin(np.linspace(0, 2*np.pi, num_samples))
lon = 51.3890 + 0.001 * np.cos(np.linspace(0, 2*np.pi, num_samples))

## 3. داده‌های محیطی
pressure = 1013.25 * np.exp(-altitude / 8000)  # مدل فشار جوی
pressure += np.random.normal(0, 0.1, num_samples)

temperature = 15 - 0.0065 * altitude + np.random.normal(0, 0.3, num_samples)

## 4. داده‌های وضعیت پرواز
# زوایای پرواز
pitch = np.concatenate([
    np.random.normal(-5, 1, 300),  # فاز کاهش ارتفاع
    np.linspace(-5, 2, 100),       # انتقال فاز
    np.random.normal(2, 0.5, 600)  # فاز کروز
])

roll = np.random.normal(0, 0.5, num_samples)
yaw = np.linspace(0, 360, num_samples) % 360

# سرعت هوا
airspeed = np.concatenate([
    np.linspace(30, 15, 300),
    np.linspace(15, 12, 100),
    np.full(600, 12)
]) + np.random.normal(0, 0.3, num_samples)

## 5. داده‌های کنترل
# وضعیت بال (0: بسته, 1: باز)
wing_status = np.concatenate([np.zeros(300), np.ones(700)])

# وضعیت سروو موتورها
servo1 = np.concatenate([
    np.full(300, 90),
    np.linspace(90, 110, 100),
    np.random.normal(110, 2, 600)
])

servo2 = np.concatenate([
    np.full(300, 90),
    np.linspace(90, 70, 100),
    np.random.normal(70, 2, 600)
])

## 6. داده‌های سیستم
battery_voltage = np.linspace(8.4, 7.2, num_samples) + np.random.normal(0, 0.05, num_samples)
cpu_temp = np.random.normal(45, 2, num_samples)

## 7. پردازش سیگنال‌ها برای واقعی‌تر شدن
def smooth(data, window=11):
    return savgol_filter(data, window, 3)

altitude = smooth(altitude)
pressure = smooth(pressure)
airspeed = smooth(airspeed)

## ایجاد DataFrame
data = pd.DataFrame({
    'timestamp': timestamps,
    'latitude': lat,
    'longitude': lon,
    'altitude_m': altitude,
    'pressure_hPa': pressure,
    'temperature_C': temperature,
    'pitch_deg': pitch,
    'roll_deg': roll,
    'yaw_deg': yaw,
    'airspeed_mps': airspeed,
    'wing_status': wing_status,
    'servo1_angle': servo1,
    'servo2_angle': servo2,
    'battery_voltage': battery_voltage,
    'cpu_temp_C': cpu_temp,
    'flight_phase': np.concatenate([
        ['descent']*300,
        ['transition']*100,
        ['cruise']*600
    ])
})

## ذخیره داده‌ها
data.to_csv('cansat_flight_data_1000.csv', index=False)
print("1000 داده پروازی با موفقیت تولید و ذخیره شد!") -->