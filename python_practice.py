"""counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")




for county in counties:
    print(county)




counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


for county, value in counties_dict.items():
    #print(county+" county has " + str(value) +" registered voters.")
    print(f"{county} county has {value} registered voters.")
  
"""

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    #print(county_dict)
    for county, voters in county_dict.values():
        
        print(f"{county} County has {voters} registered voters.")

