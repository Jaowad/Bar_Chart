import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 15, 25, 30]

# Create a bar chart
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')

# Show the plot
plt.show()

#vertical bar chart
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()

#Horizontal Bar chart
objects = ('A', 'B', 'C')
y_pos = np.arange(len(objects))
performance = [10,9,5]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos,objects)
plt.xlabel('Value')
plt.title('Horizontal bar Chart')

plt.show()