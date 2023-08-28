import pandas as pd
file=pd.read_csv("Pandas\ds_salaries.csv")
print(file)
print(file.rename(columns={'salary_in_usd':'salary_in_dollars'}))
#rename() lets you rename index or column values by specifying a index or column keyword parameter, respectively
print(file.rename(index={0: 'firstEntry', 1: 'secondEntry'}))
print(file.rename_axis("serial", axis='rows').rename_axis("fields", axis='columns'))
'''canadian_youtube = pd.read_csv("../input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("../input/youtube-new/GBvideos.csv")
    #concat() function concates 2 same files
print(pd.concat([canadian_youtube, british_youtube]))'''

'''left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
    #join() lets you combine different DataFrame objects which have an index in common. 
left.join(right, lsuffix='_CAN', rsuffix='_UK')'''