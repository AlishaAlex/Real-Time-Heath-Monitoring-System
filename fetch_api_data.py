import requests
import pandas as pd
import datetime

def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/countries/USA"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("API call failed with status code:", response.status_code)
    data = response.json()

    df = pd.DataFrame([{
        'date': datetime.date.today().isoformat(),
        'country': data['country'],
        'cases': data['cases'],
        'todayCases': data['todayCases'],
        'deaths': data['deaths'],
        'todayDeaths': data['todayDeaths'],
        'recovered': data['recovered'],
        'active': data['active']
    }])

    df.to_csv('data/covid_data_raw.csv', index=False)
    print("Data fetched and saved to covid_data_raw.csv")

if __name__ == "__main__":
    fetch_covid_data()
