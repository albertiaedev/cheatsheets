#SEABORN CHEATSHEET


#Basic step to creating plots with Seaborn:
  1. Prepare the data.
  2. Control figure aesthetics.
  3. Plot with Seaborn
  4. Further customize your plots.
  5. Show your plot.
#Example:

#Import the libraries to use
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('df') #step 1
sns.set_style('whitegrid') #step 2
g = sns.lmplot(x="column_X",y="column_Y",data=df,aspect=2) #step 3
g = (g.set_axis_labels("label_X","label_Y")).set(xlim=(0,10),ylim=(0,100))) #step 3
plt.title('title') #step 4
plt.show(g) #step 5
