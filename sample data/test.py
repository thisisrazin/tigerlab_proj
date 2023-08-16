import pandas as pd

filename='sample data/results.csv'
headers=['teamOne', 'teamOneScore', 'teamTwo' ,'teamTwoScore']
df=pd.read_csv(filename, names=headers)
rankingDict={}
for index, row in df.iterrows():
    if row['teamOne'] not in rankingDict: rankingDict.update({row['teamOne']: 0})
    if row['teamTwo'] not in rankingDict: rankingDict.update({row['teamTwo']: 0})

    if row['teamOneScore']>row['teamTwoScore']: rankingDict[row['teamOne']]+=3
    if row['teamOneScore']<row['teamTwoScore']: rankingDict[row['teamTwo']]+=3
    if row['teamOneScore']==row['teamTwoScore']:
        rankingDict[row['teamOne']]+=1
        rankingDict[row['teamTwo']]+=1

rankingTuple=list(rankingDict.items())
sortedRankingTuple=sorted(rankingTuple, key=lambda x: (-x[1], x[0]))
sortedRankingDict=dict((x, y) for x, y in sortedRankingTuple)
print(sortedRankingDict)
