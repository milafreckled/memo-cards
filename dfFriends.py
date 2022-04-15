import pandas as pd
import numpy as np

np.datetime64("2018-01-01")
cast = [['Rachel Green', np.datetime64("1969-02-11"), 'Los Angeles', 52],
        ['Monica Geller', np.datetime64("1964-06-15"), 'Birmingham', 57],
        ['Phoebe Buffay', np.datetime64("1963-07-30"),'Los Angeles', 58],
        ['Joey Tribbiani', np.datetime64("1967-07-25"), 'Newton', 54],
        ['Chandler Ping', np.datetime64("1969-08-19"), 'Williamstown', 52],
        ['Ross Geller', np.datetime64("1966-11-02"), 'Queens', 55]]
index = ['Jennifer Aniston', 'Courtney Cox', 'Lisa Kudrow', 'Matthew LeBlanc', 'Matthew Perry', 'David Schwimmer']
dfFriends = pd.DataFrame(cast, index=index, columns=['Character', 'Birth date', 'Place of birth', 'Age'])
# 29/11/2021
locked = dfFriends.loc[:, ('Character', 'Birth date')]
dfAt = dfFriends.at['Matthew LeBlanc', 'Character']
dfIAt = dfFriends.iat[1, 2]
dfIloc = dfFriends.iloc[:, lambda df:[0, 2]]
dfNdim = dfFriends.ndim
print(dfFriends)
print('-'*20)
print(dfNdim)
# print(dfFriends.head())