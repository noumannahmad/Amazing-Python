#First import the liabary name pip install covid-19

from covid import Covid

covid= Covid()


def covid_worldwide():
    print(covid.get_total_active_cases())
    print(covid.get_total_confirmed_cases())
    print(covid.get_total_recovered())
    print(covid.get_total_deaths())

covid_worldwide()


#the is the Currnet cases worldwide --next we will get the cases county by county


#So stay conected Bye