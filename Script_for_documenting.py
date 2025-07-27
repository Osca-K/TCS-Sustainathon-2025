#Script_for all the graphs on the main docs

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


##UNEMPLOYMENT RATE OVER THE YEARS IN SOUTH AFRICA

# Data extracted from the graph 
years = [2000, 2000.5, 2001, 2001.5, 2002, 2002.5, 2003, 2003.5, 2004, 2004.5, 2005, 2005.5, 2006, 2006.5, 2007, 2007.5, 2008, 2008.5, 2009, 2009.5, 2010, 2010.5, 2011, 2011.5, 2012, 2012.5, 2013, 2013.5, 2014, 2014.5, 2015, 2015.5, 2016, 2016.5, 2017, 2017.5, 2018, 2018.5, 2019, 2019.5, 2020, 2020.5, 2021, 2021.5, 2022, 2022.25, 2022.5, 2022.75, 2023, 2023.25]
values = [25.5, 29.5, 31.0, 29.0, 28.0, 26.5, 26.0, 25.0, 23.5, 23.0, 22.5, 22.0, 21.5, 22.0, 22.5, 23.5, 24.5, 25.0, 25.5, 24.5, 25.0, 24.0, 25.0, 24.5, 25.0, 24.5, 25.0, 25.5, 26.0, 25.0, 25.5, 26.5, 27.0, 27.5, 27.0, 27.5, 27.0, 27.5, 28.0, 29.0, 30.0, 23.5, 31.0, 32.5, 34.5, 35.0, 34.5, 33.5, 33.0, 32.5]
# The scraped data from the https://take-profit.org/en/statistics/unemployment-rate/south-africa/

plt.rcParams['font.family'] = "Times New Roman"
plt.rcParams['font.size'] = 12


plt.figure(figsize=(7, 4)) 
plt.plot(years, values, marker='o', markersize=3, linestyle='-', color='skyblue')
# plt.title('Title')
plt.xlabel('Year')
plt.ylabel('Unemplyment Rate (%)')
# plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.yticks(range(20, 37, 2))
plt.tight_layout()
plt.gca().set_ylim(20, 36)
plt.savefig('unemployment_rate_graph.png', dpi=300, bbox_inches='tight')

plt.show()



## HARVESTED AREA BY CROP


import matplotlib.pyplot as plt


#Sraped data from the https://www.statista.com/statistics/1310097/south-africa-main-crops-by-production-volume/
crops = [
    "Maize", "Soybeans", "Sunflower seed",  "Wheat",  "Sugar cane", "Rapeseed", "Grapes", "Barley", "Potatoes", "Beans, dry"
]

harvested_area_thousand_hectares = [
    3001.8, 925.3, 670.7,566.8, 258.4,123.51, 117.39,101.0, 66.9,42.9
]

plt.rcParams['font.family'] = "Times New Roman"
plt.rcParams['font.size'] = 12



plt.figure(figsize=(5, 3))
plt.barh(crops, harvested_area_thousand_hectares, color='cornflowerblue')



plt.gca().invert_yaxis()
plt.xlabel('Harvested area in thousand hectares')
plt.title('Harvested Area by Crop')

# Labelling the bars with their values
for index, value in enumerate(harvested_area_thousand_hectares):
    
    plt.text(value + 30, index, str(value), va='center', fontsize=10)

plt.grid(axis='x', linestyle=':', alpha=0.7) 
plt.tight_layout() 

plt.savefig('harvested_area_by_crop.png', dpi=300, bbox_inches='tight')
plt.show()


# CONSUMPTION OF MAIN CROPS IN SOUTH AFRICA 
# Website where the data was scrapts https://www.statista.com/statistics/1135184/consumption-of-processed-maize-in-south-africa/

periods = [
    "2001/2002", "2002/2003", "2003/2004", "2004/2005", "2005/2006",
    "2006/2007", "2007/2008", "2008/2009", "2009/2010", "2010/2011",
    "2011/2012", "2012/2013", "2013/2014", "2014/2015", "2015/2016",
    "2016/2017", "2017/2018", "2018/2019", "2019/2020"
]

total_consumption = [
    3900, 3700, 3700, 3750, 3850,
    3800, 3800, 4520, 4470, 4520,
    4520, 4500, 4600, 4850, 4700,
    4800, 5000, 5100, 5180
]


plt.rcParams['font.family'] = "Times New Roman"
plt.rcParams['font.size'] = 12

plt.figure(figsize=(6, 4))
plt.plot(periods, total_consumption, marker='o', markersize=5, linestyle='-', color='cornflowerblue')
plt.xticks(rotation=90)  # Changed from 45 to 90 for vertical labels
plt.xlabel('Period')
plt.ylabel('Total Consumption (in 1,000 tons)') 
# plt.title('Total Consumption of Processed Maize in South Africa')
# plt.grid(True, linestyle='--', alpha=0.7)       
plt.tight_layout()
plt.savefig('total_consumption_maize.png', dpi=300, bbox_inches='tight')
plt.show()


#Food Insecurity From https://sagrainmag.co.za/2024/10/02/sa-produces-enough-food-still-people-are-starving/#:~:text=In%20stark%20contrast%20to%20this,individuals)%20experience%20severe%20food%20insecurity.



# Data [Sourced from the article]
categories = ['Food Insecure', 'Severely Food Insecure']
percentages = [25.8, 11.4]
population_millions = [15.3, 6.8]

fig, ax = plt.subplots(figsize=(8, 6))


bars = ax.bar(categories, population_millions, color=["#f461a6", "#d93b13"])


for bar, percent in zip(bars, percentages):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.3,
            f'{percent}%\n({height}M)', ha='center', fontsize=10)

ax.set_title('Food Insecurity in South Africa (2022)', fontsize=14)
ax.set_ylabel('Population (millions)', fontsize=12)
ax.set_ylim(0, max(population_millions) + 3)
ax.set_facecolor('white')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()


plt.savefig('food_insecurity_sa.png') 
plt.show()

