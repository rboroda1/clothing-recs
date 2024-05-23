import csv
from collections import Counter


# function to recommend clothes
def recommendClothes(temp, precip):
    dataSet = []
    margin = 4
    while(dataSet == []):
        with open("data.csv") as csvfile:
            # change contents to floats
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:  # each row is a list
                if(row[0] != 'temperature'):
                    if(int(row[0]) > (temp-margin) and int(row[0]) < (temp+margin)):
                        if(row[1] == precip):
                            dataSet.append(row)
        margin += 3  # widens margin and repeats until dataSet isn't empty

    # make lists of tops and bottoms
    tops = []
    bottoms = []
    for day in dataSet:
        tops.append(day[2])
        bottoms.append(day[3])

    def most_frequent(List):
        occurence_count = Counter(List)
        return occurence_count.most_common(1)[0][0]

    print('You should wear a', most_frequent(
        tops), 'and', most_frequent(bottoms))


# function to turn Kelvin temp into Fahrenheit
def kelvinToFahrenheit(kelvins):
    fahrenheit = (kelvins - 273.15) * 9/5 + 32
    return fahrenheit


# function to check for precipitation
def raining(weatherStatus):
    precipitation = 'no'
    if("rain" in weatherStatus.lower()):
        precipitation = 'yes'
    if("shower" in weatherStatus.lower()):
        precipitation = 'yes'
    if("hail" in weatherStatus.lower()):
        precipitation = 'yes'
    if("snow" in weatherStatus.lower()):
        precipitation = 'yes'
    if("sleet" in weatherStatus.lower()):
        precipitation = 'yes'
    if("drizzle" in weatherStatus.lower()):
        precipitation = 'yes'
    if("storm" in weatherStatus.lower()):
        precipitation = 'yes'
    if("blizzard" in weatherStatus.lower()):
        precipitation = 'yes'
    return precipitation
