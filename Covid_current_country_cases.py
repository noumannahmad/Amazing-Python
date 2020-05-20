#get current cases of countries using python

#First You need to install pip install covid-19
#Now import the libaray
from covid import  Covid
covid=Covid()
pakistan=covid.get_status_by_country_name("pakistan")
data={
    key : pakistan[key]
    for key in pakistan.keys() and {'confirmed','active','deaths',
                                 'recovered'}
}
print(data)
#you can get information of any particular county by passing name and id