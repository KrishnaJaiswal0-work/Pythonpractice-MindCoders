import matplotlib.pyplot as plt

# Data 
places = ['Bholaram','Silicon City','Bharwarkua','Vijay Nagar','Nehru Nagar']
students = [1200,2500,980,870,650]
colors = ["#00A2FF",'#4CAf50','#FF9800','#9C2780','#F44336']


# Bar Chart - comparing categories
plt.figure(figsize=(9,5))
bars = plt.bar(places, students, color = colors,edgecolor = 'white',linewidth=1.5 )
plt.title('Students Enrolled per Places')
plt.xlabel('Places in Indore')
plt.ylabel('Number of Students')

for bar,val in zip(bars, students):
    plt.text(bar.get_x()+bar.get_width()/2, val+30,str(val),ha='center', fontweight='bold')

plt.tight_layout()
plt.show()