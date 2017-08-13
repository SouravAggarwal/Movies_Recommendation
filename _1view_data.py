import pandas
import os
import webbrowser

data_table = pandas.read_csv("SampleMovieData/ratings.csv")
html = data_table[0:20].to_html()
with open('data.html','w') as f:
    f.write(html)

full_filename = os.path.abspath("data.html")
print(full_filename)
#open file in web browser