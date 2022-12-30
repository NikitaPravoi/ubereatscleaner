import pandas as pd

df = pd.read_excel('stg_uber_eats_price.xlsx')
# r"[^\w\s,&'?’\"--()/]"mg

df['Category'].replace(to_replace=r"[^\w\s,’&()-\?\"\']", value='', regex=True)
df['Category'].replace(to_replace=r"[\t]", value='', regex=True)
df['Category'].replace(to_replace=r"\s+$", value='', regex=True)
# print(df['Category'].unique())
df['Price(£)'].replace(to_replace=r"B\xa0", value='', regex=True)
df['Price(£)'].replace(to_replace=r"^[^\d]", value='0.', regex=True)

df['Item'].replace(to_replace=r"[^\w\s,’&()-\?\"\']", value='', regex=True)
df['Item'].replace(to_replace=r"®", value='', regex=True)
df['Item'].replace(to_replace=r"[\t]", value='', regex=True)
df['Item'].replace(to_replace=r"\s+$", value='', regex=True)


print(df['Item'].unique())