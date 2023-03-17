# -*- coding: utf-8 -*-
"""ViS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OnhiQN2AoZmDlAUF_z9YhRXhgfepKYeR
"""

import pandas as pd
import statistics
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

exam = pd.read_csv('exams.csv')
exam.head()

gender = exam['gender']
race = exam['race/ethnicity']
education = exam['parental level of education']
lunch = exam['lunch']
test = exam['test preparation course']
math = exam['math score']
reading = exam['reading score']
writing = exam['writing score']

fig = plt.figure(figsize = (100, 10))
ax = plt.axes(projection ="3d")
ax.scatter3D(math,reading,writing,color="green")
plt.title('Scatter plot podataka rezultata testa iz matematike, čitanja i pisanja', fontweight = 'bold')
ax.set_xlabel('Matematika',fontweight ='bold')
ax.set_ylabel('Čitanje',fontweight ='bold')
ax.set_zlabel('Pisanje',fontweight ='bold')

plt.show()

print("\n\n\n\n")

plt.hist(math, bins = 20)
plt.title('Histogram vrijednosti testa iz matematike', fontweight = 'bold')
plt.show()

print("\n\n")

plt.boxplot(math)
plt.title('Boxplot vrijednosti testa iz matematike', fontweight = 'bold')
plt.show()

print("\n\n\n\n")

plt.hist(reading, bins = 20)
plt.title('Histogram vrijednosti testa iz čitanja', fontweight = 'bold')
plt.show()

print("\n\n")

plt.boxplot(reading)
plt.title('Boxplot vrijednosti testa iz čitanja', fontweight = 'bold')
plt.show()


print("\n\n\n\n")

plt.hist(writing, bins = 20)
plt.title('Histogram vrijednosti testa iz pisanja', fontweight = 'bold')
plt.show()


print("\n\n")

plt.boxplot(writing)
plt.title('Boxplot vrijednosti testa iz pisanja', fontweight = 'bold')
plt.show()
