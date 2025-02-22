#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Data exploration and ingest
import pandas as pd
df = pd.read_csv("C:/Users/91957/Downloads/Indicators_of_Anxiety_or_Depression_Based_on_Reported_Frequency_of_Symptoms_During_Last_7_Days (1).csv")


# In[2]:


df.head()


# In[3]:


print(df.info())


# In[4]:


print(df.describe())


# In[ ]:





# In[5]:


#data cleaning and transformation


# In[6]:


#Removing Duplicate Rows
df.drop_duplicates()


# In[7]:


original_count = len(df)  # Number of rows before removing duplicates

df = df.drop_duplicates()  # Remove duplicate rows

new_count = len(df)  # Number of rows after removing duplicates
deleted_rows = original_count - new_count  # Calculate the number of rows deleted

print(f"Number of duplicate rows deleted: {deleted_rows}")


# In[ ]:





# In[8]:


original_count = len(df)  # Number of rows before removing rows with missing values

df = df.dropna()  # Remove rows with missing values

new_count = len(df)  # Number of rows after removal
deleted_rows = original_count - new_count  # Calculate the number of rows deleted

print(f"Number of rows deleted due to missing values: {deleted_rows}")


# In[ ]:





# In[9]:


# Convert columns to datetime
df['Time Period Start Date'] = pd.to_datetime(df['Time Period Start Date'])
df['Time Period End Date'] = pd.to_datetime(df['Time Period End Date'])

# Print the head of the changed columns
print("First few entries of the date columns:")
print(df[['Time Period Start Date', 'Time Period End Date']].head())


# In[ ]:





# In[10]:


df = df.rename(columns={'Low CI': 'Lower Confidence Interval', 'High CI': 'Upper Confidence Interval'})

# Print the head of the renamed columns
print("First few entries of the renamed columns:")
print(df[['Lower Confidence Interval', 'Upper Confidence Interval']].head())


# In[ ]:





# In[11]:


# Define columns to drop
columns_to_drop = ['Phase', 'Time Period', 'Time Period Label']

# Drop the columns
df = df.drop(columns=columns_to_drop)

# Print the names of the deleted columns
print("Deleted columns:")
print(columns_to_drop)


# In[12]:


# Drop the 'Confidence Interval' column
df.drop(columns=['Confidence Interval'], inplace=True)
# Print the name of the dropped column
print("Dropped column: 'Confidence Interval'")


# In[13]:


df.to_csv('Manohar_cleaned_data.csv', index=False)


# In[14]:


df = pd.read_csv("C:/Users/91957/Downloads/Manohar_cleaned_data.csv")


# In[15]:


df.head()


# In[16]:


# Calculate summary statistics 
summary_stats = df.describe()
# Print the summary statistics
print(summary_stats)


# In[18]:


# Calculate summary statistics for the 'Value' column
value_stats = df['Value_nn'].describe()
print("Summary statistics for the 'Value' column:")
print(value_stats)


# In[20]:


# Visualize the distribution of 'Value'
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.hist(df['Value_nn'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Value')
plt.xlabel('Value_nn')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[21]:


# Scatter plot for anxiety vs. depression symptoms
plt.figure(figsize=(8, 6))
plt.scatter(df['Value_nn'], df['Lower_Confidence_Interval'], color='skyblue', label='Lower CI')
plt.scatter(df['Value_nn'], df['Upper_Confidence_Interval'], color='orange', label='Upper CI')
plt.title('Scatter Plot of Anxiety vs. Depression Symptoms')
plt.xlabel('Value_nn')
plt.ylabel('Confidence_Interval')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# In[ ]:





# In[23]:


import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Ensure your 'Time Period Start Date' is in datetime format
df['Time_Period_Start_Date'] = pd.to_datetime(df['Time_Period_Start_Date'])

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Time_Period_Start_Date', y='Value_nn', hue='Indicator')

plt.title('Frequency of Anxiety and Depression Symptoms Over Time')
plt.xlabel('Time Period Start Date')
plt.ylabel('Value')


ax = plt.gca() 
ax.xaxis.set_major_locator(mdates.AutoDateLocator())  
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Set the display format to Year-Month

plt.xticks(rotation=45)  # Rotate labels for better legibility
plt.tight_layout()  

plt.show()


# In[ ]:





# In[24]:


df_subset = df[['Value_nn', 'Lower_Confidence_Interval', 'Upper_Confidence_Interval']]


# In[26]:


# Calculate the correlation matrix
correlation_matrix = df_subset.corr()
#sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')  
plt.title('Correlation Matrix')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




