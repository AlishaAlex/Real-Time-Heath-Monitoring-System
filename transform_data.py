import pandas as pd

def transform_data():
    df = pd.read_csv('data/covid_data_raw.csv')

    # Clean and enrich data
    df['mortality_rate'] = (df['deaths'] / df['cases']) * 100
    df['recovery_rate'] = (df['recovered'] / df['cases']) * 100

    df = df[['date', 'country', 'cases', 'todayCases', 'deaths', 'todayDeaths',
             'recovered', 'active', 'mortality_rate', 'recovery_rate']]
    df.to_csv('data/covid_data_transformed.csv', index=False)
    print("Data transformed and saved to covid_data_transformed.csv")

if __name__ == "__main__":
    transform_data()
