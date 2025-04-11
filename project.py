
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
