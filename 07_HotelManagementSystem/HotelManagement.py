from Hotel import Hotel
from User import User

def print_hotel_datas(hotels):
    for hotel in hotels:
        print(hotel)

def sort_hotel_by_name(hotels):
    return sorted(hotels, key=Hotel.get_name, reverse=False)

def sort_hotel_by_rating(hotels):
    return sorted(hotels, key=Hotel.get_rating, reverse=False)
    
def hotel_in_bangalore_location(hotels):
    for hotel in hotels:
        if hotel.get_location() == "Bangalore":
            print(hotel)

def sort_hotel_by_room(hotels):
    return sorted(hotels, key=Hotel.get_room, reverse=True)


def main():
    #initialize Hotel data
    hotel_1 = Hotel("H1", 4, "Bangalore", 5, 100)
    hotel_2 = Hotel("H2", 5, "Bangalore", 5, 200)
    hotel_3 = Hotel("H3", 6, "Munbai", 3, 100)

    #list contain all the hotel data
    hotels = [hotel_1, hotel_2, hotel_3]

    #initialialize User data
    user_1 = User("U1", 2, 1000)
    user_2 = User("U2", 3, 1200)
    user_3 = User("U3", 4, 1100)

    #list contain all the user data
    users = [user_1, user_2, user_3]

    #print hotel datas:
    print_hotel_datas(hotels)

    #sorted hotel by name
    print("\nsorted hotel by name:")
    sorted_hotel_by_name = sort_hotel_by_name(hotels)
    print_hotel_datas(sorted_hotel_by_name)

    #sorted hotel by rating
    print("\nsorted hotel by rating")
    sorted_hotel_by_rating = sort_hotel_by_rating(hotels)
    print_hotel_datas(sorted_hotel_by_rating)

    #print data for Bangalore location
    print("\nPrint hotel in Bangalore")
    hotel_in_bangalore_location(hotels)

    #sort hotel by maximun number of rooms Available
    print("\n hotel sorted by maximun number of rooms available")
    sorted_hotel_by_room = sort_hotel_by_room(hotels)
    print_hotel_datas(sorted_hotel_by_room)

    #print user booking datas
    print("\nuser's booking data")
    for user in users:
        print(user)


if __name__ == '__main__':
    main()
