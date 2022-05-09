import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    dataset = pd.read_csv('adult.data.csv', sep = ",", skip_blank_lines=True)
    
    df = pd.DataFrame(dataset)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    
    race_count = df['race'].value_counts()

    # What is the average age of men?

    men = df.query('sex == "Male"')
  
    average_age_men = (men['age'].sum() / men['age'].count()).round(1) 

    # What is the percentage of people who have a Bachelor's degree?
    
    degrees = df['education'].value_counts(normalize=True)
  
    percentage_bachelors = (degrees.loc['Bachelors'] * 100).round(1)
    
  
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    educ1 = df[['education', 'salary']]

    high_education = educ1[((educ1['education'] == 'Bachelors') | (educ1['education'] == 'Masters') | (educ1['education'] == 'Doctorate'))]
  
    high_education_hs = educ1[((educ1['salary'] == '>50K') & ((educ1['education'] == 'Bachelors') | (educ1['education'] == 'Masters') | (educ1['education'] == 'Doctorate')))]
  
   # percentage with salary >50K
  
    higher_education_rich = ((high_education_hs['education'].count() / high_education['education'].count()) *100).round(1)
   
    # What percentage of people without advanced education make more than 50K?
  
    w_high_education = educ1[~((educ1['education'] == 'Bachelors') | (educ1['education'] == 'Masters') | (educ1['education'] == 'Doctorate'))]

    w_high_education_hs = educ1[((educ1['salary'] == '>50K') & (~((educ1['education'] == 'Bachelors') | (educ1['education'] == 'Masters') | (educ1['education'] == 'Doctorate'))))]
  
    
    lower_education_rich = ((w_high_education_hs['education'].count() / w_high_education['education'].count()) *100).round(1)  

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
  
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    num_min_workers = df[(df['hours-per-week'] == 1)]['hours-per-week'].count()
  
    rich_percentage = (( df[ ((df['hours-per-week'] == 1) & (df['salary'] == '>50K')) ]['hours-per-week'].count() / num_min_workers) * 100).round(1)

    # What country has the highest percentage of people that earn >50K?

    country_salaries = df[['native-country', 'salary']]
    
    country_s_total = country_salaries['native-country'].value_counts().drop(index='?')
    
    countries_hs1 = country_salaries[(df['salary'] == '>50K')]
    countries_hs2 = (countries_hs1['native-country'].value_counts()).drop(index='?')

    ratio = (countries_hs2 / country_s_total *100).round(1).sort_values(ascending = False).dropna()
    
    country_1 = (ratio[0:1].index).tolist()
    country_1 = ''.join(country_1)
    highest_earning_country = country_1

    #print(highest_earning_country)
  
    highest_earning_country_percentage = ratio.max()
  
    # Identify the most popular occupation for those who earn >50K in India.

    world1 = df[['native-country', 'occupation', 'salary']]
  
    india_top = world1[(world1['salary'] == '>50K') & (world1['native-country'] == 'India')]
  
    india_top = india_top['occupation'].value_counts()
    x_india =(india_top[0:1].index).tolist()
    x_india = ''.join(x_india)
    top_IN_occupation = x_india
  
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)
      
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
