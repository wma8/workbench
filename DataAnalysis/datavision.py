import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

reviews = pd.read_csv("/home/weikunma/Desktop/Datasets/winemag-data_first150k.csv",
index_col=0)
print(reviews.head(3))

a = reviews['province'].value_counts().head(10)
# plt.show(a)

# a = (a / len(reviews)).plot.bar()

# plt.show(a)

# b = reviews['points'].value_counts().sort_index().plot.area()
# plt.show(b)

pd.set_option('max_columns', None)
pokemon = pd.read_csv("/home/weikunma/Desktop/Datasets/Pokemon.csv")
print(pokemon.head(3))

# c = reviews[reviews['price'] < 100].sample(100).
# plot.scatter(x = 'price', y='points')


# c = reviews[reviews['price'] < 100].plot.hexbin(x='price', y='points', gridsize = 15)

# plt.show(c)
pokemon_state_legendary = pokemon.groupby(['Legendary', 'Generation']).mean()[['Attack', 'Defense']]
# plt.show(pokemon_state_legendary.plot.bar(stacked=True))

pokemon_stats_by_generation = pokemon.groupby('Generation').mean()[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
# plt.show(pokemon_stats_by_generation.plot.line())


# d = sns.jointplot(x='price', y='points', data=reviews[reviews['price'] < 100])
plt.show(sns.jointplot(x='price', y='points', data=reviews[reviews['price'] < 100], kind='hex', 
              gridsize=20))






