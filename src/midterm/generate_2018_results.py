import pandas as pd
import numpy as np

def load_senate():
    df = pd.read_csv('../data/2018-senate.csv')
    grps = df.groupby(['state_po'])
    d = []
    for name, group in grps:
        location = ''
        year = ''
        cand1_actual = 0
        cand2_actual = 0
        
        for index, row in group.iterrows():
            location = row.state_po
            year = row.year
            if((row.party == 'democrat' or row.party == 'democratic-farmer-labor') or (row.party == 'democratic-npl' or row.candidate == 'Bernie Sanders')):
                if(cand1_actual != 0 and row.state_po == 'CA'):
                    cand2_actual = 100 * (row.candidatevotes/row.totalvotes)
                else:
                    cand1_actual = 100*(row.candidatevotes/row.totalvotes)
            elif(row.party == 'republican'):
                cand2_actual = 100*(row.candidatevotes/row.totalvotes)
            elif((cand2_actual == 0) or (cand2_actual < 100*(row.candidatevotes/row.totalvotes))):
                cand2_actual = 100*(row.candidatevotes/row.totalvotes)

        d.append(np.array([location, year, 'Sen-G', 'Sen-G', 'Democrat', 'Republican', '11/6/2018', cand1_actual, cand2_actual]))
    
    columns = ['location', 'year', 'type_simple', 'type_detail', 'cand1_name', 'cand2_name', 'electiondate', 'cand1_actual', 'cand2_actual']
    elx = pd.DataFrame(data=d, columns=columns)
    return elx

def load_house():
    df = pd.read_csv('../data/2018-house.csv')
    grps = df.groupby(['state_po', 'district'])
    
    d= []

    for name, group in grps:
        location = ''
        year = ''
        cand1_actual = 0
        cand2_actual = 0

        for index, row in group.iterrows():
            location = row.state_po + '-' + str(row.district)
            year = row.year
            if((row.party == 'democrat' or row.party == 'democratic-farmer-labor') or row.party == 'democratic-npl'):
                cand1_actual = 100*(row.candidatevotes/row.totalvotes)
            elif(row.party == 'republican'):
                cand2_actual = 100*(row.candidatevotes/row.totalvotes)
                
        d.append(np.array([location, year, 'House-G', 'House-G', 'Democrat', 'Republican', '11/6/2018', cand1_actual, cand2_actual]))
    columns = ['location', 'year', 'type_simple', 'type_detail', 'cand1_name', 'cand2_name', 'electiondate', 'cand1_actual', 'cand2_actual']
    elx = pd.DataFrame(data=d, columns=columns)
    return elx

def generate_results():
    df1 = load_house()
    df2 = load_senate()
    df1.to_csv('../out/utility/house.csv')
    df2.to_csv('../out/utility/senate.csv')
