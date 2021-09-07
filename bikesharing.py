import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    bikecities = {'chicago', 'new york city', 'washington'}
    bikemonth = {'all', 'january', 'february', 'march',' april', 'may', 'june'}
    bikedays = {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('For which city would you like to get information about US bikeshare data?')
    city = input('Please enter for which city you want to know more about. \n city: ').lower()
    while city not in bikecities:
        print('Sorry, we either have no information, about that city or you spelled the city wrong. The cities we have are: chicago, new york city and washington')
        city = input('Please reenter the city you want to look at. \n city: ').lower()
    else:
        print('Thank you, we will no provide you information about', city)
    month = input('Now please enter the month of the year for which you seek information.The bikesharing is available from January to June. if you want to know the most frequent time for all the month type: "all". \n month: ').lower()
    while month not in bikemonth:
        print('Sorry, we either have no information, about that month or you spelled the month wrong. The bikesharing is available from January to June. if you want to know the most frequent time for all the month type: "all".')
        month = input('Please reenter the month you want to look at.\n month: ').lower()
    else: 
        print('Thank you, we will no provide you information about', month)
    day = input('And last please enter the day of the week you want to know more about. If you want the information for all the days type: "all". \n day: ').lower()
    while day not in bikedays:
        print('Sorry, I guess you spelled the "day of the week" wrong.')
        day = input('Please reenter the day you want to look at. \n day: ').lower()
    else: 
        print('Thank you, we will now provide you information about', day)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

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
        df = df[df['day'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['month'] =  df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most popular month is: ', popular_month)

    # TO DO: display the most common day of week
    df['day'] =  df['Start Time'].dt.day_name()
    popular_day = df['day'].mode()[0]
    print('The most popular day is: ', popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] =  df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour of the day is: ', popular_hour, 'o\' clock')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: ', start_station)
    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is: ', end_station)
    # TO DO: display most frequent combination of start station and end station trip
    station_combination = df['Start Station'] + df['End Station']
    common_combination = max(station_combination)
    print('The most common stationcombination is: ', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print('The total Duration is:', total_duration, 'seconds.')

    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    print('The mean Duration is:', average_duration, 'seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('The earlies birth year was: ', df['Birth Year'].min(),'\n', 'The latest birth year was: ', df['Birth Year'].max(),'\n', 'The average birth year was: ', df['Birth Year'].median() )
    else:
        print('Birth Year stats cannot be calculated because Gender does not appear in the dataframe')
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    temp = ['','','']
    temp = get_filters()
    df = load_data(temp[0],temp[1],temp[2])
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no?\n')
    start_loc = 0
    while view_data.lower() == 'yes':
        print(df.iloc[:5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        break
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    while restart.lower() == 'yes':
        temp = get_filters()
        df = load_data(temp[0],temp[1],temp[2])
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        break
    print('Goodbye')
        
if __name__ == "__main__":
	main() 