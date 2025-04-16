#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df= pd.read_csv("C:/Users\\Paria\\Downloads\\flights_data.csv")
print(df.describe())


# In[3]:


df_cleaned = df.dropna()
len(df_cleaned)


# In[7]:


df_cleaned.head(10)


# # بررسی آماری داده‌های استخراج‌شده (میانگین، میانه، دامنه مقادیر)

# In[4]:


mean_values = df_cleaned.mean(numeric_only=True)
median_values = df_cleaned.median(numeric_only=True)
std_values = df_cleaned.std(numeric_only=True)

print("Mean Values:\n", mean_values)
print("Median Values:\n", median_values)
print("Standard Deviation:\n", std_values)


# In[5]:


df_cleaned.columns = ['ID', 'Flight', 'Country', 'Timestamp1', 'Timestamp2', 'Longitude', 'Latitude', 'Altitude']

numeric_columns = ['Longitude', 'Latitude', 'Altitude']

range_values = {}
for column in numeric_columns:
    max_value = df_cleaned[column].max()
    min_value = df_cleaned[column].min()
    range_values[column] = max_value - min_value

print("دامنه هر ستون:")
for column, range_value in range_values.items():
    print(f"{column}: {range_value}")


# # شناسایی داده‌های پرت با الگوریتم‌های تشخیص ناهنجاری

# In[10]:


def detect_outliers_iqr(data):
    q1 = data.quantile(0.25)
    q3 = data.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return data[(data < lower_bound) | (data > upper_bound)]

outliers = {}
for column in numeric_columns:
    outliers[column] = detect_outliers_iqr(df_cleaned[column])

print(" IQR داده‌های پرت شناسایی‌شده:")
for column, outlier_values in outliers.items():
    print(f"{column}: {outlier_values}")


# In[9]:


from scipy.stats import zscore

z_scores = df_cleaned[numeric_columns].apply(zscore)

outliers_zscore = (z_scores.abs() > 3)

print("داده‌های پرت شناسایی‌شده با Z-Score:")
for column in numeric_columns:
    print(f"{column}: {df_cleaned[column][outliers_zscore[column]]}")


# # مقایسه مقادیر پروازی با داده‌های تاریخی برای بررسی سازگاری

# In[ ]:




