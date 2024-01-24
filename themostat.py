actual_temp = 0
desired_temp = 0

def heating_cooling(actual_temp, desired_temp):
    thermostat = "y"
    while thermostat == "y":
        actual_temp = int(input("What is the current temp?: "))
        desired_temp = int(input("What is the desired temp?: "))
        if actual_temp < desired_temp:
            print("Run heat")
        elif actual_temp > desired_temp:
            print("Run A/C")
        else:
            print("Standby")
        thermostat = input("Do you want to change the temp again? (y/n): ")

heating_cooling(actual_temp, desired_temp)