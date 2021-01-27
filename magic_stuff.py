import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/noahgift/food/master/data/features.en.openfoodfacts.org.products.csv"
)
df.drop(
    ["Unnamed: 0", "exceeded", "g_sum", "energy_100g"], axis=1, inplace=True
)  # drop two rows we don't need
df = df.drop(df.index[[1, 11877]])  # drop outlier
df.rename(index=str, columns={"reconstructed_energy": "energy_100g"}, inplace=True)
print(df.head())
