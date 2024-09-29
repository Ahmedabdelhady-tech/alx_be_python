from datetime import datetime, timedelta
# Part 1: Display the Current Date and Time

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current data and time : {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_data():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_data = datetime.now()
    future_date = current_data + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%y-%m-%d")
    print(f"futuer date : {formatted_future_date}")

if __name__=="__main__":
    display_current_datetime()
    calculate_future_data()
