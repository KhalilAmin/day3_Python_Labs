city = ""
max_rent = 0
min_beds = 0


def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed == True:
        print(f"Welcome to GC Property Management! Looking up listing in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month....")
    else:
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month...")

def apt_search2(city, max_rent, min_beds = 2, pets_allowed = True):
    if pets_allowed == True:
        print(f"Welcome to GC Property Management! Looking up listing in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month....")
    else:
        print(f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month...")

apt_search1("Charlotte", 1500, 2, True)
apt_search1("Charlotte", 1500, 2, False)

apt_search2("Miami", 4500)
apt_search2("Miami", 4500, 1)
apt_search2("Miami", 4500, pets_allowed=False)

plus_one_hundred = lambda plus_one_hundred : plus_one_hundred +100
print(plus_one_hundred(5))

square_num = lambda square_num : square_num **2
print(square_num(3))

concatenate = lambda concatenate : "- " + concatenate
print(concatenate('hello'))

divide_by_three = lambda divide_by_three : divide_by_three / 3
print(divide_by_three(9))


