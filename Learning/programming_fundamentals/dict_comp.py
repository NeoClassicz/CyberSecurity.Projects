import os
os.system('cls')

labels = ['first_name', 'last_name', 'favorite_food']
data = ['Breandan', 'King', 'pizza']

# results = [
#     (labels[index], data[index])
#     for index in range(0, len(labels))
# ]

# results = { labels[index]: data[index] for index in range (0, len(labels)) }

results = { label: datum for label, datum in zip(labels, data) }

print(results)