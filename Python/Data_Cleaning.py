#Cleaning product_dirty file
import pandas as pd
df =  pd.read_csv("products_dirty.csv")
df
df.rename(columns={'cogs': 'Direct cost'},inplace=True)
df.drop_duplicates(inplace=True)
df = df.dropna(subset=['category_id', 'price'])
df.to_csv('product_clean_data.csv' , index = False)

#Cleaning Shipping_dirty File
import pandas as pd
df = pd.read_csv('shipping.csv')
df
df.rename(columns={'shipping providers':'Delivery_Services'},inplace =True)
df.drop_duplicates(inplace = True)
df['return_date'] = df['return_date'].fillna('Not Applicable')
df.to_csv('shipping_clean_data.csv' , index = False)

#Cleaning inventory_dirty file
import pandas as pd
df = pd.read_csv('inventory_dirty.csv')
df
df['last_stock_date'] = pd.to_datetime(df['last_stock_date'], format='mixed', dayfirst=True)
df.drop_duplicates(inplace=True)
df.to_csv('inventory_clean_data.csv' , index=False)

#Cleaning customers_dirty file
import pandas as pd 
df = pd.read_csv('customers_dirty.csv')
df
df['Name'] = df['first_name'] + ' ' + df['last_name']
df.drop(['first_name', 'last_name'], axis=1,inplace=True)
df['state'] = df['state'].str.strip().str.title()
df.to_csv('customer_clean_data.csv' , index=False)

#Cleaning orders_dirty file
import pandas as pd
df = pd.read_csv("orders_dirty.csv")
df
df.drop_duplicates(inplace = True)
df['order_status'] = df['order_status'].str.strip().str.title()
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed', dayfirst=True)
median_value = df['order_date'].median()
df['order_date'] = df['order_date'].fillna(median_value)
df.to_csv('orders_clean_data.csv' , index=False)

#Cleaning order_items_dirty file
import pandas as pd
df = pd.read_csv('order_items_dirty.csv')
df
df.drop_duplicates(inplace=True)
df['price_per_unit'].isna().sum()
df['price_per_unit'] = df['price_per_unit'].fillna(df['price_per_unit'].mean())
df.to_csv('order_items_clean_data.csv' , index=False)


