import pandas as pd
import numpy as np
import matrix_lowRankMatrixFactorization


class predictMovies_forUser:

    #Load data from csv
    movie_names=pd.read_csv("SampleMovieData/movies.csv")
    raw_dataset_df= pd.read_csv("SampleMovieData/ratings.csv")

    raw_dataset_df=raw_dataset_df.iloc[:500,:3]                        #Specify the no. of rows to get from file(100 for less data)

    def create_HTML_CSV(self,data,name):
        data_df = pd.DataFrame(data)
        html = data_df.to_html(na_rep="")
        with open('_4'+str(name)+'.html', 'w') as f:
            f.write(html)

        data.to_csv('_4'+str(name)+'.csv')


    def getAllPredicted_Ratings(self):
        #Convert the list of user ratings into matrix =>to build review matrix
        ratings_df=pd.pivot_table(self.raw_dataset_df,index="userId",columns="movieId",aggfunc=np.max)

        # Given Data
        self.create_HTML_CSV(ratings_df, "Given")

        #to replace nan with 0
        ratings_df=ratings_df.fillna(value=0)


        #Matrix factorization: to find User and Movie attribute matirx
        U,M= matrix_lowRankMatrixFactorization.matrix_factorization(np.array(ratings_df))
        Output=np.round_((np.dot(U,M)),2)
        #adding row and column in final_Output
        col=ratings_df.columns.values
        print(ratings_df.index.values)
        new_col=[]
        for i in col:
            new_col.append(i[1])
        predicted_Ratings=pd.DataFrame(Output,index=ratings_df.index.values,columns=new_col)

        #Predicted Ratings
        self.create_HTML_CSV(predicted_Ratings,"PredictedForAll")
        print("Predicted Ratings for All::")
        print(predicted_Ratings)
        print("------------------------------------")

        self.predictForUser(predicted_Ratings)

#----------------------------NEW Code (particular User Recommendation)-----------------



    def predictForUser(self,predicted_Ratings):

        print("Enter a UserId to get Top 10 Recommendations (user b/w 1 to 10 )")
        userId_toSearch=int(input())
        print("Movies already reviewed by user:"+str(userId_toSearch))

        Already_Reviewed_byUser=self.raw_dataset_df[self.raw_dataset_df['userId']==userId_toSearch]
        print(Already_Reviewed_byUser)
        PredictedRating_forGivenUser=(predicted_Ratings.T[userId_toSearch])
        All=PredictedRating_forGivenUser

        y = (np.setdiff1d(All.keys(), np.array(Already_Reviewed_byUser['movieId'])))
        zz = (self.movie_names.loc[np.sum(self.movie_names['movieId'].values == pd.DataFrame(y).values, axis=0) == 1])
        zz = np.array(zz)
        rating = np.array(All.loc[np.in1d(np.array(All.keys()), y)])
        zz = np.append(zz, rating.reshape(rating.shape[0], 1), axis=1)
        zz = pd.DataFrame(zz)
        final_Data=zz.sort_values(3, ascending=False)

        index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        final_forUser=pd.DataFrame(final_Data,index=index)
        final_forUser.columns=["MovieId","Movie Name","Genre","Predicted Rating for User "+str(userId_toSearch)]

        self.create_HTML_CSV(final_forUser,"Recommendation_User")
        print(type(final_Data))
        print(final_Data)
#xx=getData.getDatas(All_Predicted,Already_Reviewed_byUser)




if(__name__=="__main__"):
    predictMovies_forUser().getAllPredicted_Ratings()



