
# Emotion data
all_emotions = {'angry': 156, 'fear': 46, 'neutral': 20, 'happy': 89, 'sad': 1}


import matplotlib.pyplot as plt
# Extract emotion labels and values
emotions = list(all_emotions.keys())
values = list(all_emotions.values())

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(values, labels=emotions, autopct='%1.1f%%', startangle=140)
plt.title('Emotion Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Save the pie chart as an image file (e.g., PNG)
plt.savefig('rizzai/static/images/emotion_pie_chart')

# Display the pie chart
plt.show()