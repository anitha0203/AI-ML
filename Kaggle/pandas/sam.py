import pandas as pd

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')


print(ingredients)

# reviews.rename(columns={'points': 'score'})
# reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})
# reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')


# canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
# british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")

# pd.concat([canadian_youtube, british_youtube])