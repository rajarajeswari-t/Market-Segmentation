import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mcdonalds = pd.read_csv('/content/drive/MyDrive/mcdonalds.csv')

#convert visit frequency to numeric
visit_frequency_mapping = {
    "Never": 0,
    "Once a week": 1,
    "Once a month": 2,
    "Once a year": 3,
    "More than once a week":4,
    "Every three months":5
}

mcdonalds['VisitFrequencyNumeric'] = mcdonalds['VisitFrequency'].map(visit_frequency_mapping)
print(mcdonalds['VisitFrequencyNumeric'].head())

# Assuming k4 is a column in the dataset representing the segment membership
visit = mcdonalds.groupby('k4')['VisitFrequencyNumeric'].mean()
like = mcdonalds.groupby('k4')['Like.n'].mean()

mcdonalds['Female'] = (mcdonalds['Gender'] == 'Female').astype(int)
female = mcdonalds.groupby('k4')['Female'].mean()

plt.figure(figsize=(10, 6))
bubble_size = 10 * female
plt.scatter(visit, like, s=bubble_size, alpha=0.5)

# Add text labels for each segment
for i in range(len(visit)):
    plt.text(visit.iloc[i], like.iloc[i], str(visit.index[i]+1), fontsize=12, ha='center', va='center')

plt.xlim(2, 4.5)
plt.ylim(-3, 3)
plt.xlabel('Visit Frequency')
plt.ylabel('Liking (Like.n)')
plt.title('Segment Evaluation Plot')
plt.show()
