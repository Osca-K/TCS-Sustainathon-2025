
#Script_for all the graphs on the main docs

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# Data extracted from the graph 
years = [2000, 2000.5, 2001, 2001.5, 2002, 2002.5, 2003, 2003.5, 2004, 2004.5, 2005, 2005.5, 2006, 2006.5, 2007, 2007.5, 2008, 2008.5, 2009, 2009.5, 2010, 2010.5, 2011, 2011.5, 2012, 2012.5, 2013, 2013.5, 2014, 2014.5, 2015, 2015.5, 2016, 2016.5, 2017, 2017.5, 2018, 2018.5, 2019, 2019.5, 2020, 2020.5, 2021, 2021.5, 2022, 2022.25, 2022.5, 2022.75, 2023, 2023.25]
values = [25.5, 29.5, 31.0, 29.0, 28.0, 26.5, 26.0, 25.0, 23.5, 23.0, 22.5, 22.0, 21.5, 22.0, 22.5, 23.5, 24.5, 25.0, 25.5, 24.5, 25.0, 24.0, 25.0, 24.5, 25.0, 24.5, 25.0, 25.5, 26.0, 25.0, 25.5, 26.5, 27.0, 27.5, 27.0, 27.5, 27.0, 27.5, 28.0, 29.0, 30.0, 23.5, 31.0, 32.5, 34.5, 35.0, 34.5, 33.5, 33.0, 32.5]


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
