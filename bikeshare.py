import time
import pandas as pd
import calendar as cld


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']
day_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (1.chicago, 2.new york city, 3.washington)
    i = 0
    while(i not in range(1,4)):
        try:
            i = int(input("Please select cities \n 1.chicago\n 2.new york city\n 3.washington\n "))
        except ValueError:
            print("Please select valid City from the list")
    
    city = list(CITY_DATA.keys())[i-1]
    #get user input for month (all, january, february, ... , june)
    i=0
    
    while(i not in range(1,8)):
        try:
            i = int(input("Please select month\n 1.all\n 2.january\n 3.february\n 4.march\n 5.april\n 6.may\n 7.june\n "))
        except ValueError:
            print("Please select valid month from the list")
    month = MONTHS[i-1]
    #get user input for day of week (all, monday, tuesday, ... sunday)

    i=0
    while(i not in range(1,9)):
        try:
            i = int(input("Please select day\n 1.all\n 2.monday\n 3.tuesday\n 4.wednesday\n 5.thrusday\n 6.friday\n 7.saturday\n 8.sunday\n "))
        except ValueError:
            print("Please select valid month from the list")    
    
    day = day_of_week[i-1]
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
    #load raw dataset for given city
    df = pd.read_csv(CITY_DATA[city])
    # Extract month, day and hour from startime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    #filter according to month
    if month != 'all':
        month = MONTHS.index(month)
        #filter by MONTHS
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #Common month in data set
    print('Common Month: {}'.format(cld.month_name[df['month'].mode()[0]]))
    #Common day in dataset
    print('Day: {}'.format(df['day'].mode()[0]))
    #common start time in data set
    print("Common Start: {}:00hrs".format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    #Most Common Start Station
    print("Most Common Start Station: {}".format(df['Start Station'].value_counts().idxmax()))
    #Most Common End Station
    print("Most Common End Station: {}".format(df['End Station'].value_counts().idxmax()))
    #Most Frequent Combination of start and end station
    most_freq_combination = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    print('\nMost Commonly used combination of Start station and End station: \n{}'.format(most_freq_combination.value_counts().idxmax())) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #Total travel time duration for the the selected data filter
    total_travel_time_duration = df['Trip Duration'].sum()
    tt_time_duration = total_travel_time_duration
    day = tt_time_duration // (24*3600)
    tt_time_duration %=(24*3600)
    hr = tt_time_duration //3600
    tt_time_duration %=3600
    mins = tt_time_duration // 60
    tt_time_duration %=60
    secs = tt_time_duration
    print('\nTotal Travel time {} days {} hour {} mins {} secs'.format(day,hr,mins,secs))
    
    #Mean or Average travel time for selected data filter
    mean_travel_time_duration = df['Trip Duration'].mean()
    mt_time_duration = mean_travel_time_duration
    day = mt_time_duration // (24*3600)
    tt_time_duration %=(24*3600)
    hr = mt_time_duration //3600
    mt_time_duration %=3600
    mins = mt_time_duration // 60
    mt_time_duration %=60
    secs = mt_time_duration
    
    print('\nMean Travel time {} days {} hour {} mins {} secs'.format(day,hr,mins,secs))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #dispaly types of users
    users = dict(df['User Type'].value_counts())
    
    for k,v in users.items():
        print("\nNumber of {} are {}\n".format(k,v))
    
    #display the gender in data set
    if 'Gender'in df.columns:
        gender = dict(df['Gender'].value_counts())
        for k,v in gender.items():
            print("\nNumber of {} are {}\n".format(k,v))
        
    #Min-Max of date of birth inside data set
    if 'Birth Year'in df.columns:
        earliest_yr = df['Birth Year'].min()
        recent_yr = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].value_counts().idxmax()
        print('\n Oldest Birth Year {}\n Youngest Birth year {}\n Common Birth Year {}\n'.format(earliest_yr,recent_yr,most_common_birth_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
