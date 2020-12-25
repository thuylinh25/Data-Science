# read salries.csv as dataframe called sal
# check the head of the DataFrame
# Use the .info() method to find out how many entries there are
# what is the average BasePay
# What is the highest amount of OvertimePay in the dataset
# What is the job title of JOSEPH DRISCOLL
# How much does JOSEPH DRISCOLL make (including benefits)?
# What is the name of the higest paid person (including benefits)

import pandas as pd
sal = pd.read_csv('Salaries.csv')
# sal.head()
# sal.info()
# average_basepay = sal['BasePay'].mean(axis=0)
# highest_overtimepay = sal['OvertimePay'].max(axis=0)
# # jobtitle_JOSEPH = sal.loc[sal['EmployeeName']== 'JOSEPH DRISCOLL','JobTitle']
# jobtitle_JOSEPH = sal[sal['EmployeeName']== 'JOSEPH DRISCOLL','JobTitle']
# # salary_JOSEPH = sal.loc[sal['EmployeeName']== 'JOSEPH DRISCOLL','TotalPayBenefits']
# salary_JOSEPH = sal[sal['EmployeeName']== 'JOSEPH DRISCOLL','TotalPayBenefits']
# highest_paid_rate = sal['TotalPayBenefits'].max(axis=0)
# highest_paid_person = sal.loc[sal['TotalPayBenefits']== highest_paid_rate ,'EmployeeName']

# What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?
# What was the average (mean) BasePay of all employees per year? (2011-2014)?
# How many unique job titles are there?
# What are the top 5 most common jobs?
# How many Job Titles were represented by only one person in 2013? (e.g.Job Title with only one occurence in 2013?)
# How many people have the word Chief in their job title?
# Is there a correlation between length of the Job Title string and Salary?

lowest_TotalPayBenefits = sal['TotalPayBenefits'].min(axis=0)
# tiền lương âm
# for i in range(2011, 2015):
#     average_basepay = sal[sal['Year']==i]['BasePay'].mean()
#     print(average_basepay)
sal.groupby('Year')['BasePay'].mean()
sal['JobTitle'].value_counts().head(10)
sal['JobTitle'].value_counts(ascending=True).head(10)
sal['JobTitle'].value_counts().tail(10)
jobs=sal[sal['Year']==2013]['JobTitle'].value_counts()
sum(jobs==1)
jobs[jobs ==1].count()
sum(sal['JobTitle'].str.contains('Chief'))
