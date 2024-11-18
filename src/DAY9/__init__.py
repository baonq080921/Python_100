capitals = {
    "France": 9,
    "Germany": 10,


}

highest_capital =[(key,value) for key,value in capitals.items()]
print(max(highest_capital))

# empty_dictionary = {}
#
# capitals["Spanish"] = "Barcelona"
# empty_dictionary = capitals
# print(empty_dictionary)



#Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "Dijon"],
#     "Germany": ["Berlin", "Stuttgart"]
# }

# nested_list = ["A","B",["C","D"]]
travel_log = {
    "France": {
        'num_times_visited': 8,
        'city_visited': ['Paris', 'Dijon','Lille']
    },
    "Germany": {
        'num_times_visited': 5,
        'city_visited': ['Berlin', 'Hamburg','Stugratt']
    },
}
#print Sturggart:
# print(travel_log['Germany']['city_visited'][2])
