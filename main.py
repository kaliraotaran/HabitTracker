import pandas as pd
from tabulate import tabulate
from datetime import datetime
from habittracker import track_habit, Habit

def main():
    habits: list[Habit] =[
        track_habit('coffee', datetime(2023, 6,6,8), cost=5, minutes_used= 5),
        track_habit('NETFLIX', datetime(2023, 6,10,9), cost=15, minutes_used= 80)

    ]


    df = pd.DataFrame(habits)
    print(tabulate(df, headers='keys', tablefmt='psql'))

if __name__ =='__main__':
    main()