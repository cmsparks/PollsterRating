import pandas as pd

def 3wk_as_dataframe():
    polls = pd.read_csv("../data/3week-midterm-polls.csv")
    governor_results = pd.read_csv('../data/governor_results.csv')
    house_results = pd.read_csv('../data/house_results.csv')
    senate_results = pd.read_csv('../data/senate_results.csv')
    

    columns = ["poll_id","race","location","type","pollster","partisan","poll_date","sample_size","c1","c1_pct","c2","c2_pct","c3_pct","poll_margin","electiondate","c1_real","c2_real","real_margin","error","bias"]
    formatted = pandas.DataFrame(columns=columns)

    for row in polls.itertuples():
        poll_result = parse_data(row)
        [row.Index, get_race_name(row), get_race_location(row), get_race_type(row), row.pollster, row.partisan, row.endDate, row.sampleSize, 



def get_race_type(row):
    if row.type == 'house':
        return 'HOUSE-G'
    elif row.type == 'senate':
        return 'SENATE-G'
    elif row.type == 'governor':
        return 'GOV-G'

def get_race_location(row):
    state = "national"
    if row.state != None:
        state = us_state_abbrev[row.state]

    row.

def get_race_name(row):
    



us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# thank you to @kinghelix and @trevormarburger for this idea
abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))
