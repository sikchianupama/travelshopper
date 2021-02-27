# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%matplotlib inline
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from lightfm import LightFM


item_dataset=pd.read_csv('/Users/a0g00e6/Downloads/items.csv')


#Converting the format of Genre column to a list and then appending to the new list
Tag=[]
Tags={}
for num in range(0,len(item_dataset)):
    key=item_dataset.iloc[num]['itemNbr']
    value=item_dataset.iloc[num]['tags'].split(',')
    Tags[key]=value
    Tag.append(value)

    
#Making a new column in our original Dataset         
item_dataset['tagArray']=Tag

#print(item_dataset.head(5))


item_dataset = item_dataset.sort_values('rating', ascending=False).head(5)


s = item_dataset.apply(lambda x: pd.Series(x['tagArray']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'tag'
gen_item_dataset = item_dataset.drop('tagArray', axis=1).join(s)


#print(gen_item_dataset.head(5))


location_dataset=pd.read_csv('/Users/a0g00e6/Downloads/location_tags.csv')


#Converting the format of Genre column to a list and then appending to the new list
Tag=[]
Tags={}
for num in range(0,len(location_dataset)):
    key=location_dataset.iloc[num]['location_id']
    value=location_dataset.iloc[num]['tags'].split(',')
    Tags[key]=value
    Tag.append(value)

    
#Making a new column in our original Dataset         
location_dataset['tagArray']=Tag

#print(location_dataset.head(5))


def get_tags_from_location(location):
    df = location_dataset[location_dataset['city']==location]
    return df['tagArray']



def build_chart(location, percentile=0.85):
    tagArray=get_tags_from_location(location)
    tagArray = list(tagArray)
    result=pd.DataFrame() 
    for tag in tagArray[0]:
        qualified=gen_item_dataset[gen_item_dataset['tag'] == tag]
        qualified=qualified.sort_values('rating',ascending=False).head(5)
        result = result.append(qualified[['itemNbr','itemDesc','brand','price','rating']].drop_duplicates()).drop_duplicates()
        
    result=result.sort_values('rating',ascending=False).head(5)
    return result


purchase_dataset=pd.read_csv('/Users/a0g00e6/Downloads/purchase.csv')
#purchase_dataset=purchase_dataset[purchase_dataset.itemNbr.isin(items['itemNbr'].to_list())]
        
user_item_purchase = pd.pivot_table(purchase_dataset, index='userId', columns='itemNbr', values='rating')

# fill missing values with 0
user_item_purchase = user_item_purchase.fillna(0)

user_item_purchase.head(10)

# convert to csr matrix
user_item_purchase_csr = csr_matrix(user_item_purchase.values)
user_item_purchase_csr

user_id = list(user_item_purchase.index)
user_dict = {}
counter = 0 
for i in user_id:
    user_dict[i] = counter
    counter += 1




model = LightFM(loss='warp',
                random_state=2016,
                learning_rate=0.90,
                no_components=150,
                user_alpha=0.000005)

model = model.fit(user_item_purchase_csr,
                  epochs=100,
                  num_threads=16, verbose=False)


def sample_recommendation_user(model, user_item_purchase, user_id, user_dict,location, threshold = 0,nrec_items = 5, show = True):
    items=build_chart(location)
    item_dict ={}
    df = items[['itemNbr','itemDesc']].sort_values('itemDesc', ascending=False).reset_index()

    for i in range(df.shape[0]):
        item_dict[(df.loc[i,'itemNbr'])] = df.loc[i,'itemDesc']
    
    items=items[['itemNbr','rating']]
        
    items_selected_transformed = pd.get_dummies(items, columns = ['rating'])
    items_selected_transformed = items_selected_transformed.sort_values('itemNbr').reset_index().drop('index', axis=1)
    items_csr = csr_matrix(items_selected_transformed.drop('itemNbr', axis=1).values)

    user_item_purchase=user_item_purchase.loc[:,user_item_purchase.columns.isin(items['itemNbr'].to_list())]

    n_users, n_items = user_item_purchase.shape
    user_x = user_dict[user_id]
    scores = pd.Series(model.predict(user_x,np.arange(n_items), item_features=items_csr))
    scores.index = user_item_purchase.columns
    scores = list(pd.Series(scores.sort_values(ascending=False).index))
    known_items = list(pd.Series(user_item_purchase.loc[user_id,:] \
                                 [user_item_purchase.loc[user_id,:] > threshold].index).sort_values(ascending=False))
    scores = [x for x in scores if x not in known_items]
    return_score_list = scores[0:nrec_items]
    known_items = list(pd.Series(known_items).apply(lambda x: item_dict[x]))
    scores = list(pd.Series(scores).apply(lambda x: item_dict[x]))
    print(scores)


sample_recommendation_user(model, user_item_purchase, 'a124', user_dict, 'Ladakh')

def recommend(userId, location, model):
    result = pd.DataFrame()

    return result    
    
















