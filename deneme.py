import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df1 = pd.read_csv('tmdb_5000_movies.csv')
df1.drop(['title'], axis=1, inplace=True)

tfidf = TfidfVectorizer(stop_words='english')
df1['overview'] = df1['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df1['overview'])

cosine_sim = linear_kernel(tfidf_matrix,tfidf_matrix)
indices = pd.Series(df1.index,index = df1['id']).drop_duplicates()

def get_recommendation(id,cosine_sim=cosine_sim):
    idx = indices[id]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores,key=lambda x:x[1],reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df1['id'].iloc[movie_indices].tolist()



