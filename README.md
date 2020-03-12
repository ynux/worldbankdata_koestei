## Visualize some World Bank Data on a Map

Project for coursera class

### Data

from the [World Bank Data](https://data.worldbank.org/)

in csv format, with metadata
[GDP (current US$)](http://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.CD?downloadformat=csv)
[Population, total](http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv)
[Refugee population by country or territory of origin](http://api.worldbank.org/v2/en/indicator/SM.POP.REFG.OR?downloadformat=csv)
[Refugee population by country or territory of asylum](http://api.worldbank.org/v2/en/indicator/SM.POP.REFG?downloadformat=csv)

### How to get this on a Map?

I won't put shapes - too much work for this project. But let's get a lat lon, also from the world bank. We have country codes, 3 letters, 
https://datahelpdesk.worldbank.org/knowledgebase/articles/898590-country-api-queries
Get lat lon for all 304 countries with `curl -L http://api.worldbank.org/v2/country?per_page=500 > countries_500.xml
`



