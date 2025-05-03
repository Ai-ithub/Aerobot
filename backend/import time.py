import time
import random
import math
import matplotlib.pyplot as plt

# ------------ تنظیمات اولیه ------------
initial_altitude = 300.0   # متر
target_drop = 30.0         # متر
min_cruise_altitude = initial_altitude - target_drop
drop_phase_completed = False

# ------------ PID پارامترها برای کنترل ارتفاع ------------
Kp_altitude = 1.5
Ki_altitude = 0.0
Kd_altitude = 0.8

# ------------ متغیرها ------------
current_altitude = initial_altitude
error_altitude = 0.0
previous_error_altitude = 0.0
integral_altitude = 0.0
output_altitude = 0.0

# ------------ برای شبیه سازی مسیر ------------
yaw_angle = 0  # درجه
yaw_trajectory = []
altitude_trajectory = []

# ------------ توابع اصلی ------------
def read_altitude_sensor():
    global current_altitude, drop_phase_completed
    if not drop_phase_completed:
        current_altitude -= random.uniform(0.3, 0.8)  # افت آرام
    else:
        current_altitude -= random.uniform(0.0, 0.05)  # تقریباً ثابت در فاز کروز
    if current_altitude < 0:
        current_altitude = 0
    return current_altitude

def control_altitude_drop(dt):
    global error_altitude, previous_error_altitude, integral_altitude, output_altitude
    
    error_altitude = min_cruise_altitude - current_altitude
    integral_altitude += error_altitude * dt
    derivative_altitude = (error_altitude - previous_error_altitude) / dt
    
    output_altitude = (Kp_altitude * error_altitude) + (Ki_altitude * integral_altitude) + (Kd_altitude * derivative_altitude)
    previous_error_altitude = error_altitude

    # در گلایدر واقعی این خروجی به زاویه Pitch تبدیل می‌شه
    pitch_command = max(min(90 + output_altitude, 120), 60)  # بین 60 تا 120 درجه
    print(f"[DROP] Altitude: {current_altitude:.2f} m | Pitch Cmd: {pitch_command:.1f}")

def control_circular_flight():
    global yaw_angle
    yaw_angle = (yaw_angle + 3) % 360  # هر سیکل 3 درجه چرخش به راست
    print(f"[CIRCULAR] Yaw Angle: {yaw_angle:.1f} degrees")

# ------------ حلقه اصلی شبیه سازی ------------
dt = 0.1  # زمان نمونه برداری (100 میلی‌ثانیه)

import time
import random
import math
import matplotlib.pyplot as plt

# ------------ تنظیمات اولیه ------------
initial_altitude = 300.0   # متر
target_drop = 30.0         # متر
min_cruise_altitude = initial_altitude - target_drop
drop_phase_completed = False

# ------------ PID پارامترها برای کنترل ارتفاع ------------
Kp_altitude = 1.5
Ki_altitude = 0.0
Kd_altitude = 0.8

# ------------ متغیرها ------------
current_altitude = initial_altitude
error_altitude = 0.0
previous_error_altitude = 0.0
integral_altitude = 0.0
output_altitude = 0.0

# ------------ برای شبیه سازی مسیر ------------
yaw_angle = 0  # درجه
yaw_trajectory = []
altitude_trajectory = []

# ------------ توابع اصلی ------------
def read_altitude_sensor():
    global current_altitude, drop_phase_completed
    if not drop_phase_completed:
        current_altitude -= random.uniform(0.3, 0.8)  # افت آرام
    else:
        current_altitude -= random.uniform(0.0, 0.05)  # تقریباً ثابت در فاز کروز
    if current_altitude < 0:
        current_altitude = 0
    return current_altitude

def control_altitude_drop(dt):
    global error_altitude, previous_error_altitude, integral_altitude, output_altitude
    
    error_altitude = min_cruise_altitude - current_altitude
    integral_altitude += error_altitude * dt
    derivative_altitude = (error_altitude - previous_error_altitude) / dt
    
    output_altitude = (Kp_altitude * error_altitude) + (Ki_altitude * integral_altitude) + (Kd_altitude * derivative_altitude)
    previous_error_altitude = error_altitude

    # در گلایدر واقعی این خروجی به زاویه Pitch تبدیل می‌شه
    pitch_command = max(min(90 + output_altitude, 120), 60)  # بین 60 تا 120 درجه
    print(f"[DROP] Altitude: {current_altitude:.2f} m | Pitch Cmd: {pitch_command:.1f}")

def control_circular_flight():
    global yaw_angle
    yaw_angle = (yaw_angle + 3) % 360  # هر سیکل 3 درجه چرخش به راست
    print(f"[CIRCULAR] Yaw Angle: {yaw_angle:.1f} degrees")

# ------------ حلقه اصلی شبیه سازی ------------
dt = 0.1  # زمان نمونه برداری (100 میلی‌ثانیه)

for i in range(1000):
    current_altitude = read_altitude_sensor()

    if not drop_phase_completed:
        control_altitude_drop(dt)
        if current_altitude <= min_cruise_altitude:
            drop_phase_completed = True
            print("\n>> Drop Phase Completed! Starting Circular Flight...\n")
    else:
        control_circular_flight()
    
    # ذخیره برای رسم نمودار
    yaw_trajectory.append(math.radians(yaw_angle))
    altitude_trajectory.append(current_altitude)
    
    time.sleep(dt)

# ------------ ترسیم نمودار ------------
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(altitude_trajectory)
plt.title('Altitude Over Time')
plt.xlabel('Time (ticks)')
plt.ylabel('Altitude (m)')

plt.subplot(1,2,2)
plt.polar(yaw_trajectory, range(len(yaw_trajectory)))
plt.title('Circular Flight Path (Simulated)')

plt.tight_layout()
plt.show()