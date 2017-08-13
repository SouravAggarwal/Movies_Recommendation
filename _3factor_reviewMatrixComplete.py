import pandas as pd
import numpy as np
import matrix_lowRankMatrixFactorization
#Load data from csv
raw_dataset_df= pd.read_csv("SampleMovieData/ratings.csv")
raw_dataset_df=raw_dataset_df.iloc[:50,:3]
#Convert the list of user ratings into matrix
#to build review matrix
ratings_df=pd.pivot_table(raw_dataset_df,index="userId",columns="movieId",aggfunc=np.max)

print(ratings_df)

#to replace nan with 0
ratings_df=ratings_df.fillna(value=0)

#Given Data
print(ratings_df)
print("-----------------------------------------")
#Matrix factorization: to find User and Movie attribute matirx
U,M= matrix_lowRankMatrixFactorization.matrix_factorization(np.array(ratings_df))
final_Output=np.round_((np.dot(U,M)),2)
#Output data
#print(final_Output)

#adding row and column in final_Output
col=ratings_df.columns.values
new_col=[]
for i in col:
    new_col.append(i[1])


predicted_Ratings=pd.DataFrame(final_Output,index=ratings_df.index.values,columns=new_col)
print(predicted_Ratings)



#output data in files
pand_ratings_df=pd.DataFrame(ratings_df)
html=pand_ratings_df.to_html(na_rep="")
with open('_3Given_Review.html','w') as f:
    f.write(html)
x=pd.DataFrame(ratings_df)
x.to_csv("_3Given_Review.csv")


pand_ratings_df=pd.DataFrame(predicted_Ratings)
html=pand_ratings_df.to_html(na_rep="")
with open('_3Output_Review.html','w') as f:
    f.write(html)

predicted_Ratings.to_csv("_3Output_Review.csv")