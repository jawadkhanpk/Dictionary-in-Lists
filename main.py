

#Dictionary in List

capitals ={
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list in a Dictionary
travel_log = [
    {
        "country": "France",
        "visits": 2,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# task is to write a function that will allow new countries to be added to the travel_log

def add_new_country(coutry_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = coutry_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2 , ["Moscow", "Saint Petersburg"])
print(travel_log)