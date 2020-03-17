import time
import pandas as pd
import numpy as np

#This is the Bikeshare.py Project.  Users are asked for city and month inputs.
#Then the program provides a summary analysis of ride data.
#The final run shows the detail data file, if requested by the user.

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Which city would you like to explore - Chicago, Washington, or New York? ").lower()
    while True:
        if city == 'chicago':
            print(city.capitalize() + "...The Windy City. Great choice!")
            break
        if city == 'new york':
            print(city.capitalize() + "...The Big Apple. I Love NYC!")
            break
        if city == 'washington':
            print(city.capitalize() + "...Our nation's capital. USA!")
            break
        else:
            city = input ("Please choose one of these - Chicago, Washington, or New York: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("Which month would you like to see for " + city.capitalize() + "? Type ALL if you want to see everything: ").lower()
    while True:
        if month in months:
            print(month.capitalize() + ".  Awesome Sauce!")
            break
        else:
            month = input("Please enter only a month between January and June. Or type ALL if you want to see everything: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_of_week = ['sunday', 'monday', 'tuesday','wednesday','thursday', 'friday', 'saturday', 'all']
    day = input("Which day of the week do you want? Type ALL if you want to see everything: ").lower()
    while True:
        if day in days_of_week:
            print(day.capitalize() + ", best days ever!")
            break
        else:
            day = input("Please enter a day of the week. Or type ALL if you want to see everything: ").lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month, day of week, and hour of day from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour_of_day'] = df['Start Time'].dt.hour

    # combine the Start and End Stations to create a new column
    df['from_to_trip']= df['Start Station'] + " to " + df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def fifth_line (line_count):
    if line_count == 5:
            input('Press any key to continue...\n')
            line_count == 0
            return line_count


def time_stats(df, line_count):
    """Displays statistics on the most frequent times of travel."""
    from collections import Counter
    start_time = time.time()

    print('\nCalculating The Most Frequent Times of Travel...')
    line_count = 0

    # TO DO: display the most common month,the most common day of week & the most common start hour
    high_month = Counter(df['month']).most_common(1)[0][0] - 1
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    high_day = Counter(df['day_of_week']).most_common(1)[0][0]
    busy_hour = Counter(df['hour_of_day']).most_common(1)[0][0]

    print('High travel times are in '+ months[high_month] + ' on '+ high_day + 's at ' + str(busy_hour) + ':00.')
    line_count = line_count+1
    fifth_line(line_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    line_count = line_count+1
    fifth_line(line_count)

    print('-'*40)
    line_count = line_count+1
    input('Press any key to continue...\n')



def station_stats(df, line_count):
    """Displays statistics on the most popular stations and trip."""
    from collections import Counter
    start_time = time.time()

    print('Calculating The Most Popular Stations and Trip...')
    line_count = 0

    # TO DO: display most commonly used start station
    popular_start_station = Counter(df['Start Station']).most_common(1)[0][0]
    print('Starting Point: ' + popular_start_station)
    line_count = line_count+1
    fifth_line(line_count)

    # TO DO: display most commonly used end station
    popular_end_station = Counter(df['End Station']).most_common(1)[0][0]
    print('Ending Point: ' + popular_end_station)
    line_count = line_count+1
    fifth_line(line_count)

    # TO DO: display most frequent combination of start station and end station trip
    popular_round_trip = Counter(df['from_to_trip']).most_common(1)[0][0]
    print('Popular Round Trip: ' + popular_round_trip)
    line_count = line_count+1
    fifth_line(line_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    line_count = line_count+1
    fifth_line(line_count)

    print('-'*40)
    line_count = line_count+1
    input('Press any key to continue...\n')



def trip_duration_stats(df, line_count):
    """Displays statistics on the total and average trip duration."""
    start_time = time.time()

    print('Calculating Trip Duration...')
    line_count = 0

    # TO DO: display total travel time
    print (str(sum(df['Trip Duration'])) + ' seconds over all bikeshares')
    line_count = line_count+1
    fifth_line(line_count)

    # TO DO: display mean travel time
    print (str(sum(df['Trip Duration'])/len(df['Trip Duration'])) + ' seconds on average for one bikeshare trip')
    line_count = line_count+1
    fifth_line(line_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    line_count = line_count+1
    fifth_line(line_count)

    print('-'*40)
    input('Press any key to continue...\n')




def user_stats(df, line_count):
    """Displays statistics on bikeshare users."""
    import statistics
    from collections import Counter

    start_time = time.time()
    print('Calculating User Stats...')
    line_count = 0


    # TO DO: Display counts of user types
    # Remove any row that is blank in User Type
    df.dropna(subset = ["User Type"], inplace=True)
    for key, value in Counter(df['User Type']).items():
        print (key, " -> ", value)
        line_count = line_count+1
        fifth_line(line_count)

    # TO DO: Display counts of gender
    if "Gender" in df:
        for key, value in Counter(df['Gender']).items():
            if key == 'Male' or key == 'Female':
                print (key, " -> ", value)
                line_count = line_count+1
                fifth_line(line_count)

    # Check that the column Birth Year is in the data
    if "Birth Year" in df:
    # Remove any row that is not a number (NaN)
        df.dropna(subset = ["Birth Year"], inplace=True)
    # Change Birth Year float format to integer by rounding value to nearest integer
        year_of_birth = [round(x) for x in df['Birth Year']]
    # TO DO: Display earliest, most recent, and most common year of birth
        print('Oldest Rider Birth Year: ' + str(min(year_of_birth)))
        line_count = line_count+1
        fifth_line(line_count)

        print('Youngest Rider Birth Year: ' + str(max(year_of_birth)))
        line_count = line_count+1
        fifth_line(line_count)

        print('Most Frequent Rider Birth Year: ' + str(statistics.mode(year_of_birth)))
        line_count = line_count+1
        fifth_line(line_count)

    print("\nThis took %s seconds." % (time.time() - start_time))
    line_count = line_count+1
    fifth_line(line_count)

    print('-'*40)
    line_count = line_count+1
    input('Press any key to continue...\n')

def show_rawdata(df):
    get_lines = input('Would you like to view 5 rows of the raw data? Enter yes or no: ')
    line_one = 0
    line_five = 5
    while True:
        if get_lines.lower() in ['yes', 'y']:
            print(df.iloc[line_one:line_five])
            line_one=line_one+5
            line_five=line_five+5
        else:
            break
        get_lines = input('Want to see another 5 rows of the raw data? Enter yes or no: ')

def main():
    line_count = 0
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, line_count)
        station_stats(df, line_count)
        trip_duration_stats(df, line_count)
        user_stats(df, line_count)
        show_rawdata(df)

        restart = input('\n***END OF ANALYSIS***. Would you like to restart? ')
        if restart.lower() not in ['yes', 'y']:
            break

if __name__ == "__main__":
	main()
