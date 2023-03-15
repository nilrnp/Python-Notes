import csv

# implementation of a dictionary
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            # ord gets asci value
            h += ord(char)
        return h % 100

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key,value)
                found = True
                break

            if not found:
               self.arr[h].append((key,value))


    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]


if __name__ == '__main__':
    # implementing dictionary using class
    """
    t = HashTable()
    t["march"] = 6
    t["april"] = 7
    print(t.arr)
    """


    # implementing dictionary normally
    """
    h = {'a':1,'b':2,'c':3}
    print(h.keys())
    print(h.values())
    h['d'] = 4
    h['e'] = 4
    print(h.items())
    """

    # Exercises
    #nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    # 1) What was the average temperature in first week of Jan
    # 2) What was the maximum temperature in first 10 days of Jan
    weather_list = []

    with open('nyc_weather.csv', 'r') as file:
        next(file)
        for line in file:
            results = line.split(',')
            temp = int(results[1].strip())
            weather_list.append(temp)

    print(weather_list)
    # 1
    print(sum(weather_list[0:7])/7)
    # 2
    print(max(weather_list[0:10]))
    file.close()

    #nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    # (a) What was the temperature on Jan 9?
    # (b) What was the temperature on Jan 4?
    weather_dictionary = {}
    with open('nyc_weather.csv', 'r') as file2:
        next(file2)
        for line in file2:
            results = line.split(',')
            date = results[0]
            temp = int(results[1].strip())
            weather_dictionary[date] = temp
    # a
    print(weather_dictionary["Jan 9"])
    # b
    print(weather_dictionary["Jan 4"])