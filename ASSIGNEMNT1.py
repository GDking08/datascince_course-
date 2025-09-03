#!/usr/bin/env python
# coding: utf-8

# In[17]:


import os
os.chdir(r"E:\data_preprocess\csvs")
cwd = os.getcwd()
print("Path =",cwd)


# In[2]:


import pandas as pd

# Load CSV file
df = pd.read_csv("twit.csv")

# structure
print(df.head())      
print(df.info())      
print(df.shape)     


# In[9]:


# Custom delimiter and missing header
df = pd.read_csv("bio_data3.csv", delimiter=";", header=None)

print(df.head())


# In[15]:


import pandas as pd

# Create a dictionary of data
data = { 
    "Name": ["Giri", "Viswa", "Kalidasan", "Sharmila"],
    "Age": [21, 22, 25, 20],
    "City": ["Salem", "Madurai", "Chennai", "Pondicherry"]
}


df = pd.DataFrame(data)
df.to_csv("output.csv", index=False)

print("DataFrame exported to output.csv (no index column)")


# In[8]:


import os

path = "E:\data_preprocess\csvs"
all_files = []

for f in os.listdir(path):
    if f.endswith(".csv"):
        all_files.append(os.path.join(path, f))

print(all_files)


# In[18]:


import pandas as pd

# New rows you want to append
new_rows = pd.DataFrame({
    "First Name": ["Giri", "Viswa", "Kalidasan"],
    "Last Name": ["M", "S", "R"],   # just placeholders, can be real
    "Email": ["giri@example.com", "viswa@example.com", "kalidasan@example.com"],
    "Phone": ["9876543210", "9876543211", "9876543212"],
    "Gender": ["Male", "Male", "Male"],
    "Age": [28, 30, 32],
    "Job Title": ["Data Analyst", "Software Engineer", "Project Manager"],
    "Years Of Experience": [3, 5, 8],
    "Salary": [50000, 75000, 120000],
    "Department": ["Analytics", "IT", "Management"]
})

# Append to existing CSV
new_rows.to_csv("employees.csv", mode="a", header=False, index=False)

print(" New rows appended to employees.csv")


# In[14]:


import os
import pandas as pd

# Path to folder
path = r"E:\data_preprocess\csvs"

# Collect all CSV file paths

all_files = []
for f in os.listdir(path):
    if f.endswith(".csv"):
        all_files.append(os.path.join(path, f))

# Read and concatenate with safe parsing
dfs = []
for file in all_files:
    try:
        df = pd.read_csv(file, on_bad_lines="skip")   # skip problematic rows
        dfs.append(df)
        print(f" Loaded {file} with columns: {df.shape[1]} cols")
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Merge even if columns differ
final_df = pd.concat(dfs, ignore_index=True, sort=False)

print(final_df.head())
print("Shape:", final_df.shape)

