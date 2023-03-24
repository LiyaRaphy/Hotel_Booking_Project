import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
df=pd.read_csv('hotel_bookings 2.csv')#load data

df.head()
df.tail(15) 
#prints the specified number of rows
df.shape 
#number of rows and columns
df.columns 
#name of all columns
df.info() 
#view the data type sof the table/columns

df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'])
#changing the colum to datetime format
df.info()
#checking the data type
df.describe(include ='object') 
#gets details of all columns that have datatype object.,include parameter specifies the datatype other than 
df.describe() 
#gets details of all numeric columns


for col in df.describe(include ='object').columns:
    print(col)
    print(df[col].unique())
    print(".."*50)
    #we get the column names that are object adattype and all unique column values of it.

df.isnull().sum()  
#shows number of missing values along with column_name
df.drop(['agent','company'],axis=1,inplace=True) 
#to remove any columns use axis=1 and to change the dataframe set inplace as True
df.dropna(inplace=True) 
#to remove rows with missing value we use this. 
df.isnull().sum()  
#to check any column have missing value or not
df.describe()  
#gives summary statistics of numeric columns
#finding out the outlier
df['adr'].plot(kind='box')   
#1 vanle is >5000 others are below 1000.so it is a outlier
df=df[df['adr']<5000]
#almost cleaned the data


#next we move to data analyse 
cancelled_percentage=df['is_canceled'].value_counts(normalize=True)  
#valuecounts written the category name how many time sit is present in column if use normalize =True it return in percentage
cancelled_percentage  
#0 means not cancelled
print(cancelled_percentage)
plt.figure(figsize=(5,4))
plt.title('Resevation status count')
plt.bar(['Not cancelled','cancelled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.7)
#in bar chart 1st list is the x values ,and next things is the df.here we need whole values not percentages so remove 
#normalize=True from above line of code
plt.show()
#next we need to view according to hotel type the cancellation.
#using countplot of seaborm


# figsize() takes two parameters- width and height (in inches). 
# By default the values for width and height are 6.4 and 4.8 respectively. 
plt.figure(figsize=(8,4))

#seaborn.countplot() method is used to Show the counts of observations in each categorical bin using bars.
# hue : (optional) This parameter take column name for colour encoding
# x, y: This parameter take names of variables in data or vector data, optional, Inputs for plotting long-form data.
'''palette : (optional) This parameter take palette name, list, or dict, 
    Colors to use for the different levels of the hue variable. 
    Should be something that can be interpreted by color_palette(), or
    a dictionary mapping hue levels to matplotlib colors.
    '''
ax1=sns.countplot(x='hotel',hue='is_canceled',data=df,palette='Blues')

# The Axes Class contains most of the figure elements: Axis, Tick, Line2D, Text, Polygon, etc., 
# and sets the coordinate system
# Axes.get_legend_handles_labels() function in axes module of matplotlib library is 
# used to return the handles and labels for legend.not take nay parameters.

legend_labels,_=ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title("Reservation status in different hotels",size=20)
plt.xlabel('Hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()

#Legend: A legend is an area describing the elements of the graph. In the Matplotlib library, 
#there’s a function called legend() which is used to Place a legend on the axes. 
#The attribute Loc in legend() is used to specify the location of the legend. 
#The default value of loc is loc=  “best” (upper left).

# The syntax to set the legend outside is as given below:
# matplotlib.pyplot.legend(bbox_to_anchor=(x,y)

#finding percentage of resort and city hotels cancellation
#so filter the data
resort_hotel=df[df['hotel']== 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)  #here ~28% gets cancelled
city_hotel=df[df['hotel']== 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)   #here ~41% gets cancelled


#now we will check any relation b/w price and cancellation
#use group by fubction

resort_hotel=resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel=city_hotel.groupby('reservation_status_date')[['adr']].mean()





#creating visulaization

plt.figure(figsize=(20,8))
plt.title("Average daily rate in city and resort hotel",fontsize=30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label="Resort Hotel")
plt.plot(city_hotel.index,city_hotel['adr'],label="city Hotel")
plt.legend(fontsize=20)
plt.show()

df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
ax1=sns.countplot(x='month',hue='is_canceled',data=df)
plt.xlabel('Month')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# plt.figure(figsize=(15,8))
# plt.title("ADR per month",fontsize=30)
# sns.barplot('month','adr',data=df[df['is_canceled'] == 1 ].groupby('month')[['adr']].sum().reset_index())
# plt.show()


cancelled_data=df[df['is_canceled'] == 1 ]
top_10_country=cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.title('Top 10 countries with reservation cancelld')
plt.pie(top_10_country,autopct='%.2f',labels=top_10_country.index)
plt.show()


df['market_segment'].value_counts()
df['market_segment'].value_counts(normalize=True)
cancelled_data['market_segment'].value_counts(normalize=True)





