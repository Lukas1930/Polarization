
def calc_thres(PP, PA, PAV):
    party_agree = []
    for party in PP:
        #print(party)
        memb_agree = []
        for member1 in PP.get(party):
            for member2 in set(PP.get(party)):
                if member1 != member2:
                    common = set(PAV.get(member1)) & set(PAV.get(member2)) # how many votes do they agree on 
                
                    common2 = set(PA.get(member1)) & set(PA.get(member2)) # how many same bills have they voted on

                    if len(common) != 0: # if they have at least one vote thats the same, (too avoid divide by 0)
                    
                        percentage = len(common) / len(common2)
                        memb_agree.append(percentage)
                    else:
                        memb_agree.append(0)
        if len(memb_agree) != 0:
            avgMemb = sum(memb_agree)/len(memb_agree)
            #std_dev = statistics.stdev(memb_agree) if len(memb_agree) > 1 else 0  # Avoid error for single-member case
            avg_plus_std = avgMemb# + std_dev # Compute the sum of average and standard deviation
            party_agree.append(avg_plus_std)
            #print(avg_plus_std)
        #else:
            #print(party) # party where there is only one member
            #print('1')
            #party_agree.append(1)
    
    #avgParty = sum(party_agree)/len(party_agree)
    #print(max(party_agree))
    return party_agree

def edgelist_calc(PA, PAV, threshold):
    edgelist=[]
    for i in PAV: # person 1

        for j in PAV: # for loop for person 2

            if i != j: # checks they are not the same

                common = set(PAV.get(i)) & set(PAV.get(j)) # how many votes do they agree on 
                
                common2 = set(PA.get(i)) & set(PA.get(j)) # how many same bills have they voted on

                if len(common) != 0: # if they have at least one vote thats the same, (too avoid divide by 0)
                    
                    percentage = len(common) / len(common2)
                    if percentage > threshold:
                        edgelist.append((i,j))
                

    return list(set(edgelist))

def calc_inter_edges(PP, PA, PAV):
    inter_party_agree = []  # Stores agreement percentages for different-party members
    parties = list(PP.keys())  # Get the list of parties

    # Take all possible member combinations between the two parties
    party1, party2 = parties[0], parties[1]

    for member1 in PP.get(party1, []):  # Iterate over members of Party 1
        for member2 in PP.get(party2, []):  # Iterate over members of Party 2
            common = set(PAV.get(member1, [])) & set(PAV.get(member2, []))  # Common votes
            common2 = set(PA.get(member1, [])) & set(PA.get(member2, []))  # Common bills

            if len(common) != 0 :  # Avoid division by zero
                percentage = len(common) / len(common2)
                inter_party_agree.append((member1, member2, percentage))
    max_percentage = max(inter_party_agree, key=lambda x: x[2])[2]

    # Get all (member1, member2) pairs with the max percentage
    edgelist = [(m1, m2) for m1, m2, perc in inter_party_agree if perc == max_percentage]

    return edgelist   

def dict_create(data, personid, partyid, voteid, vote_cast, name=None):
    PA = {}          #<<-------------- Person, Afstemning
    for _, row in data.iterrows():
        
        if row[personid] not in PA:
            PA[row[personid]] = [(row[voteid])]
        else:
            PA[row[personid]].append((row[voteid]))

    PAV = {}          #<<-------------- Person, Afstemning, Vote
    for _, row in data.iterrows():
        
        if row[personid] not in PAV:
            PAV[row[personid]] = [(row[voteid],row[vote_cast])]
        else:
            PAV[row[personid]].append((row[voteid],row[vote_cast]))
    
    PAVP = {}          #<<-------------- Person, Afstemning, Vote, Party
    if name != None:
        for _, row in data.iterrows():
            if row[personid] not in PAVP:
                PAVP[row[personid]] = [(row[voteid],row[vote_cast],row[partyid],row[name])]
            else:
                PAVP[row[personid]].append((row[voteid],row[vote_cast],row[partyid],row[name]))
    else:        #<<-------------- Person, Afstemning, Vote, Party
        for _, row in data.iterrows():
            if row[personid] not in PAVP:
                PAVP[row[personid]] = [(row[voteid],row[vote_cast],row[partyid])]
            else:
                PAVP[row[personid]].append((row[voteid],row[vote_cast],row[partyid]))
    
    PP = {}          #<<-------------- Party, Person
    for _, row in data.iterrows():
        if row[partyid] not in PP:
            PP[row[partyid]] = [(row[personid])]
        elif row[personid] not in PP.get(row[partyid]):
            PP[row[partyid]].append((row[personid]))

    return PA, PAV, PAVP, PP