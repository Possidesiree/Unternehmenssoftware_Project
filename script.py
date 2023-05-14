# Importing necessary libraries
import pandas as pd
import numpy as np

# Reading in data from a CSV file
data = pd.read_csv('Stress.csv')

#Remove duplicate rows
#data.drop_duplicates()
#After cleaning and preprocessing your data, you can save
#data.to_csv('cleaned_dataset.csv', index=False)



#1. type of  data.label: 1= stress; 0= no stress
np_label=np.array(data.label)
# print(type(np_label))
# print(np_label)
# print(type(data.label))
#individuals who are not stressed
stress_counts= data['label'].value_counts
print(stress_counts)
counts= data.label.value_counts()
print(np.mean(np_label))
print(np.median(np_label))
# print the result// the most people are stressed
if counts[0] > counts[1]:
    print("The most frequent value is 0 (no stress)")
else:
    print("The most frequent value is 1 (stress)")

# Number of Person with stress level 1
stress = (data['label'] == 1).sum()

print("Number of Person with stress level 1:", stress)
#Number of Person without stress
total_label= len(np_label)
no_stress= total_label-stress
print("Number of Person with stress level 0:", no_stress)

#2. type of confidence level-->0-1
#print(data.confidence)
#np_confidence=np.array(data.confidence)
#print(np_confidence)


#3. Reason of stress: Subreddit
# get the frequency count of each reason
reason_counts = data['subreddit'].value_counts()

# sort the results in descending order
reason_counts = reason_counts.sort_values(ascending=False)

# print the most common reason: is post-traumatic stress disorder
print("The most common reason for stress is:", reason_counts.index[0])
#print the number of ptsd
ptsd = (data['subreddit'] == 'ptsd').sum()
print(ptsd)