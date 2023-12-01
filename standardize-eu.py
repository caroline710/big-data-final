import pandas as pd

city_to_country = {
    # Austria
    "Vienna": "Austria", "Graz": "Austria", "Linz": "Austria",
    # Belgium
    "Brussels": "Belgium", "Antwerp": "Belgium", "Ghent": "Belgium",
    # Bulgaria
    "Sofia": "Bulgaria", "Plovdiv": "Bulgaria", "Varna": "Bulgaria",
    # Croatia
    "Zagreb": "Croatia", "Split": "Croatia", "Rijeka": "Croatia",
    # Cyprus
    "Nicosia": "Cyprus", "Limassol": "Cyprus", "Larnaca": "Cyprus",
    # Czech Republic
    "Prague": "Czech Republic", "Brno": "Czech Republic", "Ostrava": "Czech Republic",
    # Denmark
    "Copenhagen": "Denmark", "Aarhus": "Denmark", "Odense": "Denmark",
    # Estonia
    "Tallinn": "Estonia", "Tartu": "Estonia", "Narva": "Estonia",
    # Finland
    "Helsinki": "Finland", "Espoo": "Finland", "Tampere": "Finland",
    # France
    "Paris": "France", "Marseille": "France", "Lyon": "France",
    # Germany
    "Berlin": "Germany", "Munich": "Germany", "Frankfurt": "Germany",
    # Greece
    "Athens": "Greece", "Thessaloniki": "Greece", "Patras": "Greece",
    # Hungary
    "Budapest": "Hungary", "Debrecen": "Hungary", "Szeged": "Hungary",
    # Ireland
    "Dublin": "Ireland", "Cork": "Ireland", "Limerick": "Ireland",
    # Italy
    "Rome": "Italy", "Milan": "Italy", "Naples": "Italy",
    # Latvia
    "Riga": "Latvia", "Daugavpils": "Latvia", "Liepāja": "Latvia",
    # Lithuania
    "Vilnius": "Lithuania", "Kaunas": "Lithuania", "Klaipėda": "Lithuania",
    # Luxembourg
    "Luxembourg": "Luxembourg",
    # Malta
    "Valletta": "Malta", "Birkirkara": "Malta", "Qormi": "Malta",
    # Netherlands
    "Amsterdam": "Netherlands", "Rotterdam": "Netherlands", "The Hague": "Netherlands",
    # Poland
    "Warsaw": "Poland", "Krakow": "Poland", "Lodz": "Poland",
    # Portugal
    "Lisbon": "Portugal", "Porto": "Portugal", "Vila Nova de Gaia": "Portugal",
    # Romania
    "Bucharest": "Romania", "Cluj-Napoca": "Romania", "Timisoara": "Romania",
    # Slovakia
    "Bratislava": "Slovakia", "Kosice": "Slovakia", "Prešov": "Slovakia",
    # Slovenia
    "Ljubljana": "Slovenia", "Maribor": "Slovenia", "Celje": "Slovenia",
    # Spain
    "Madrid": "Spain", "Barcelona": "Spain", "Valencia": "Spain",
    # Sweden
    "Stockholm": "Sweden", "Gothenburg": "Sweden", "Malmo": "Sweden",
}

eu_countries = ["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]

df = pd.read_csv('data/2020-climate-all.csv')

def get_eu_country(location):
  if not isinstance(location, str):
    return None
  
  # check for country first
  for country in eu_countries:
      if country in location:
          return country

  for city, country in city_to_country.items():
      if city in location:
          return country
  
  return None

df['Country'] = df['User Location'].apply(get_eu_country)

# filter rows where 'Country' is not blank
filtered_df = df[df['Country'].notna() & (df['Country'] != '')]

filtered_df.to_csv('data/2020-climate-eu.csv', index=False)