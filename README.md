## Visualize some World Bank Data on a Map

Final Project for coursera course Object Oriented Programming in Java
by University of California San Diego.

### Data

from the [World Bank Data](https://data.worldbank.org/)

in csv format, with metadata
[GDP (current US$)](http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv)
[Population, total](http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv)
[Refugee population by country or territory of origin](http://api.worldbank.org/v2/en/indicator/SM.POP.REFG.OR?downloadformat=csv)
[Refugee population by country or territory of asylum](http://api.worldbank.org/v2/en/indicator/SM.POP.REFG?downloadformat=csv)

### How to get this on a Map?

The code for Life Expectancy already does this for me.
Remove first line of csv to make it clean csv. Add to data folder, refresh the folder in Eclipse. Find fields with country code, and with data. Remove quotes. The map already works (though the color scheme is not good for the number range, of course.)

But what really is interesting is refugee population per capita and GDP. The formula used within Germany to distribute asylum seekers over the Laender (regions; called Koenigssteiner Schluessel) is: `2/3*(proportion of tax revenue) + 1/3*(proportion of population)` We take the GDP instead of the tax revenue, because the tax systems vary too much internationally.

If this is the distribution key, we can define a contribution index like this (done for 2016 and OECD in [Refugee Datathon #5: International Data Sources, and an OECD wide „Königssteiner Schlüssel“](https://refugee-datathon-muc.de/?p=1158) )

We will ignore very small countries (population under 5 million - Lebanon only has 6 million and is a major receiving country, so 10 wouldn't do). We'll see if things work for small countries, we don't want to divide by zero.

The formula is:
```
expected refugee intake = (2/3 * GDP_country/GDP_world + 1/3*Pop_country/Pop_world)*Refugees_world
actual refuee intake = Refugees_country
```
Color according to actual / expected

GDP_world, Pop_world, Refugees_world are fixed integers

Get GDP_country, Pop_country, Refugees_country from csv - always the most recent possible. GDP and Pop don't vary too much. Still it would be instructive to see the year. We can tell from the index, but this is for later.














