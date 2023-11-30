import pandas as pd
import re

# dictionary of state names to abbreviations
state_abbreviations = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington DC': 'DC', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

df = pd.read_csv('data/2018-climate-all.csv')

# remove duplicates
df.drop_duplicates(subset=['Username', 'Content'], inplace=True)

def get_state(location):
    if not isinstance(location, str):
        return None
    
    # check for DC first
    if re.search(r'\b(Washington DC|DC|D\.C)\b', location, re.IGNORECASE):
        return 'Washington DC'

    for state, abbrev in state_abbreviations.items():
        pattern = rf'\b({re.escape(state)}|{re.escape(abbrev)})\b'
        if re.search(pattern, location, re.IGNORECASE):
            return state
        
    return None

df['User Location (State)'] = df['User Location'].apply(get_state)

# filter rows where 'User Location (State)' is not blank
filtered_df = df[df['User Location (State)'].notna() & (df['User Location (State)'] != '')]

filtered_df.to_csv('data/2018-climate-usa.csv', index=False)
