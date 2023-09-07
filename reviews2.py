import pandas as pd
import zipfile

# Open zipped file as dataframe

# with zipfile.ZipFile('data\winemag-data-130k-v2.csv.zip', 'r') as zip_ref:
#     zip_ref.extract('winemag-data-130k-v2.csv', 'data')

df = pd.read_csv('data/winemag-data-130k-v2.csv', index_col=0)

reviews_per_country = df.country.value_counts()

review_points = df.groupby('country')['points'].mean().round(1)

reviews_merged = pd.DataFrame.merge(reviews_per_country, review_points, on='country', how='inner')

reviews_merged.to_csv('data/reviews-per-country.csv')