
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_excel("C:/Users/Sneha/Desktop/python_project2/hepatitisCdata.xlsx")
print(data.info())
print(data.describe())
data.fillna(0, inplace=True)
print(data.info())
df=pd.DataFrame({'Age':data['Age'],'Albumin':data['ALB'],'Alkaline Phosphatase':data['ALP'],'Alanine Aminotransferase':data['ALT'],'Aspartate Aminotransferase':data['AST'],'Bilirubin':data['BIL'],'Cholinesterase':data['CHE'],'Cholesterol':data['CHOL'],'Creatinine':data['CREA'],'Gamma-Glutamyl Transferase':data['GGT'],'Total Protein':data['PROT']})  
corr=df.corr()
print(corr)
plt.figure(figsize=(10,6))
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title("Correlation of all the blood test")
plt.show()
'''Objective 1->To find out which blood tests change the most as Hepatitis C becomes more serious,
and how those test results look in patients with cirrhosis.'''

# Cleaning column names
data.columns = data.columns.str.strip()

# Print unique categories to see disease stages
print("Disease categories:", data['Category'].unique())

# Focus on main liver test results
tests = ['ALT', 'AST', 'BIL']

# Group by disease category and calculate mean values
grouped_means = data.groupby('Category')[tests].mean()

# Plot
grouped_means.plot(kind='bar', figsize=(10,6))
plt.title('Average ALT, AST, BIL Values by Disease Stage')
plt.ylabel('Average Test Value')

plt.grid(True)
plt.tight_layout()
plt.show()
