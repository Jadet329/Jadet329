def main():
    time_str = input("what time is it? ")
    time_float = convert(time_str)
    if 7.0 <= time_float <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_float <= 13.0:
        print("lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("dinner time")

def convert(time):
    hours_str, minutes_str = time.split(":")
    hours = float(hours_str)
    minutes = float(minutes_str) / 60
    return hours + minutes

if __name__ == "__main__":
    main()
