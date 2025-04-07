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

'''Objective 2->To compare blood test results between male and female patients and find out if gender has any effect on Hepatitis C.'''
data = data.drop('Patient id', axis=1)

# Separate male and female patients and get average test values
grouped_by_sex = data.groupby('Sex').mean(numeric_only=True)

# Plotting

grouped_by_sex.T.plot(kind='bar',figsize=(10,6), colormap='Pastel1')
plt.title('Average Test Values by Gender')
plt.ylabel('Average Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Sex', labels=['Female', 'Male'])
plt.tight_layout()
plt.show()
'''Objective 3-> "To find out if any patients have test results that are much higher or lower than others,
and understand what that might say about their health condition'''
test_columns = ['ALB', 'ALP', 'ALT', 'AST', 'BIL', 'CHE', 'CHOL', 'CREA', 'GGT', 'PROT']

# Plot boxplots for each test
plt.figure(figsize=(15, 8))
sns.boxplot(data=data[test_columns], orient='h', palette='Set2')
plt.title("Boxplot of Test Results to Detect Outliers")
plt.xlabel("Value")
plt.tight_layout()
plt.show()
'''Objective 4->To analyze how average clinical test values vary across different age groups and investigate
whether older patients are more likely to show signs of abnormal liver function based on routine blood test results'''
# Assuming 'data' is your cleaned DataFrame
bins = [0, 30, 50, 70, 100]
labels = ['Young (<30)', 'Middle (30-50)', 'Senior (50-70)', 'Elderly (70+)']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels)
test_columns = ['ALB', 'ALP', 'ALT', 'AST', 'BIL', 'CHE', 'CHOL', 'CREA', 'GGT', 'PROT']

avg_by_age_group = data.groupby('AgeGroup', observed=True)[test_columns].mean().reset_index()
print(avg_by_age_group)
plt.figure(figsize=(14, 7))

# Melt the dataframe so we can plot with seaborn
melted_df = avg_by_age_group.melt(id_vars='AgeGroup', var_name='Test', value_name='Average Value')

sns.lineplot(data=melted_df, x='AgeGroup', y='Average Value', hue='Test', marker='o')

plt.title('Average Clinical Test Values Across Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Average Test Value')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.show()
'''Objective 5->To compare the distribution of clinical test values and explore
whether certain tests show more variability among patients.'''
test_std = data[test_columns].std().sort_values(ascending=False)

# Convert to a DataFrame for plotting
std_df = test_std.reset_index()
std_df.columns = ['Test', 'Standard Deviation']

# Plot as bar chart
plt.figure(figsize=(12, 6))
sns.barplot(data=std_df, x='Test', y='Standard Deviation', hue='Test', palette='viridis', legend=False)
plt.title('Variability of Clinical Test Results Among Patients')
plt.ylabel('Standard Deviation')
plt.xlabel('Clinical Test')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
'''Objective 6->To understand the distribution of patients across different Hepatitis C disease stages or categories using a pie chart.'''
category_counts = data['Category'].value_counts()

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
plt.title('Distribution of Patients Across Hepatitis C Stages')

# Add legend (shows category names)
plt.legend(category_counts.index, title="Disease Stage", loc="best")
plt.axis('equal')  # To make the pie chart round
plt.show()
