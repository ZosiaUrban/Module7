airports = {}
while True:
    action = input("To fetch airport click 1, to add airport click 2, to quit click enter: ")


    def fetch(icao, airports):
        if icao in airports:
            print(f"Airport Name: {airports[icao]}")
        else:
            print("Airport not found.")
    def add(airports):
        name = input("Enter airport name: ")
        icao = input("Enter airport ICAO: ")
        if icao in airports:
            print("Airport already exists.")
        else:
            airports[icao] = name
            print("Airport added successfully!")

    if action == "1":
        icao = input("Enter airport ICAO: ")
        fetch(icao, airports)
    elif action == "2":
        add(airports)
    elif action == "":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
