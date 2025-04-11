import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
file_path="C:/Users/Sneha/Desktop/python project/retail_sales_dataset.xlsx"
data = pd.read_excel(file_path, sheet_name='retail_sales_dataset')
print(data.head(5))
data.info()
print(data.describe())
corr=data['Age'].corr(data['Total Amount'])
print("COrrelation:",corr)
corr1=data['Age'].corr(data['Quantity'])
print(corr1)
#Objective 1->How does customer age and gender influence their purchasing behaviour?
bins=[18,25,35,45,65,100]
labels=["18-25","26-35","36-45","46-65","65+"]
data["Age Group"] = pd.cut(data["Age"], bins=bins, labels=labels, right=False)
age_gender_spending=data.groupby(['Age Group','Gender'],observed=True)['Total Amount'].mean()
plt.figure(figsize=(8,6))
sns.barplot(x=age_gender_spending.index.get_level_values(0),  
            y=age_gender_spending.values, hue=age_gender_spending.index.get_level_values(1), 
            palette="coolwarm",errorbar=None)
plt.show()
#Objective 2->Which product categories hold the highest appeal among customers?

category_sales=data.groupby("Product Category")["Total Amount"].sum().reset_index()
category_sales = category_sales.sort_values(by="Total Amount", ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(data=category_sales, x="Total Amount", y="Product Category",hue="Product Category", palette="viridis")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product Category")
plt.title("Top Selling Product Categories")
#plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()

#Objective 3-> What is the relationships between age,spending and product preferences?

plt.figure(figsize=(10,6))
sns.scatterplot(data=data, 
                x="Age", 
                y="Total Amount", 
                hue="Product Category",   
                size="Total Amount",  
                sizes=(10, 300), 
                alpha=0.7,  
                palette="Set2")

plt.title("Relationship Between Age, Spending, and Product Preferences")
plt.xlabel("Age")
plt.ylabel("Total Spending ($)")
plt.legend(title="Product Category", bbox_to_anchor=(1,1)) 
plt.show()

#Objective 4-> : Analyze how shopping varies over time (daily, weekly, monthly),What are the peak shopping days of the week? (Do people shop more on weekends?)


# Ensure Date column is in datetime format
data["Date"] = pd.to_datetime(data["Date"])

# Aggregate sales data monthly
monthly_sales = data.groupby(data["Date"].dt.to_period("M"))["Total Amount"].sum().reset_index()

# Convert 'Date' period to string, then back to datetime (Seaborn needs datetime)
monthly_sales["Date"] = monthly_sales["Date"].astype(str)  # Convert period to string
monthly_sales["Date"] = pd.to_datetime(monthly_sales["Date"])  # Convert back to datetime

# Plot the monthly trend
plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_sales, x="Date", y="Total Amount", marker="o")
plt.title("Monthly Shopping Trends")
plt.xticks(rotation=45)
plt.show()

#Objective 5-> : How does gender affect shopping trends?
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Total Amount', data=data
            )
plt.title("Customer Spending Behavior by Gender")
plt.xlabel("Gender")
plt.ylabel("Total Spending")
plt.show()  

