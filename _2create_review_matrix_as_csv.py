
import pandas as pd
import numpy as np

df = pd.read_csv("SampleMovieData/ratings.csv")
#print(df[:100]["userId","movieId","ratings"])

df=df.iloc[:100,:3]
print(df)
ratings_df=pd.pivot_table(df,index='userId',columns='movieId',aggfunc=np.max)



# x=ratings_df[:50].to_html("reviewed_matrix.html")
#to create html file





html=ratings_df.to_html(na_rep="")
with open('_2reviewed_matrix.html','w') as f:
    f.write(html)
# to create csv output
ratings_df.to_csv("_2reviewed_matrix.csv",na_rep="")

html2=df.to_html(na_rep="")
with open('_2RatingsFile.html','w') as f:
    f.write(html2)
