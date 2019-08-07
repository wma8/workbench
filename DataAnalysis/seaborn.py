import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
print("Setup Complete")

# filepath = '/home/weikunma/Desktop/Datasets/nyc-jobs.csv'
parks = '/home/weikunma/Desktop/Datasets/parks.csv'


# # ny_data = pd.read_csv(filepath)
# # print(ny_data.head())

parks_data = pd.read_csv(parks, index_col=['Park Code'])
# # print(parks_data.head(3))

# # print(parks_data.iloc[2])
# # print(parks_data.loc['BADL'])

print(parks_data.loc[['BADL', 'ARCH', 'ACAD']])

# print(parks_data['State'].head(3))

parks_data.columns = [col.replace(' ', '_').lower() for col
in parks_data.columns]
# print(parks_data.columns)

print(parks_data[['state', 'acres']][:3])

print(parks_data.state.iloc[2])

print(parks_data.state.iloc[[2]])

# boolean indexing
print((parks_data.state == 'UT').head(3))

# Give the subsets with state == UT
b = parks_data[parks_data.state == 'UT']
print(b.loc['ARCH'])

# logical operators
a = parks_data[ (parks_data.latitude > 60) | (parks_data.acres > 10**6)].head(3)
print(a)

parks_data[parks_data['park_name'].str.split().
apply(lambda x: len(x) == 3)].head(3)

parks_data[parks_data.state.isin(['WA', 'OR', 'CA'])].head()

print(parks_data.iat[1,1])






