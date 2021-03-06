# house_puller

You will need to set these environment variables in advance before using this script:
```
EMAIL_ADDRESS (emails will be sent from this account over gmail)
EMAIL_PASSWORD 
RECEIVER_EMAIL_ADDRESS (emails will be received by this account)
```

Run the application in the background and every 4 hours it will give out updates to your email that you set as the RECEIVER
```
$ python3 house_puller.py &
```


```
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|Property                                         |Beds |Baths|price   |status              |open house               |
|=====================================================================================================================|
|                                                 |4    |2    |$799,000|New Listing         |08/08/2021               |
|3416 Waterman Court San Jose, California 95127   |     |     |        |                    |10:00AM-1:00PM           |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |3    |2    |$800,000|New Listing         |08/08/2021               |
|2227 Huran Drive San Jose, California 95122      |     |     |        |                    |1:00PM-4:00PM            |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |3    |2    |$849,000|List Price Decreased|08/08/2021               |
|3420 Buckner Drive San Jose, California 95127    |     |     |        |                    |1:00PM-4:00PM            |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |3    |$849,999|New Listing         |Not available for viewing|
|2430 Samoa Way San Jose, California 95122        |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |2    |$895,000|New Listing         |Not available for viewing|
|2248 Poplar Drive San Jose, California 95122     |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |3    |2    |$899,000|New Listing         |Not available for viewing|
|1244 Gainsville Avenue San Jose, California 95122|     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |3    |2    |$899,000|New Listing         |08/08/2021               |
|1343 Sylvia Drive San Jose, California 95121     |     |     |        |                    |2:00PM-5:00PM            |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |3    |2    |$899,888|New Listing         |Not available for viewing|
|2918 Via Encinitas San Jose, California 95132    |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |3    |$919,000|New Listing         |Not available for viewing|
|14380 Jerilyn Drive San Jose, California 95127   |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |3    |$929,000|New Listing         |Not available for viewing|
|956 Gerard Way San Jose, California 95127        |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |2    |$935,000|New Listing         |08/08/2021               |
|780 Kaufmann Court San Jose, California 95116    |     |     |        |                    |1:00PM-4:00PM            |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |2    |$939,000|New Listing         |Not available for viewing|
|592 Candlestick Way San Jose, California 95127   |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |3    |2    |$979,000|New Listing         |Not available for viewing|
|348 N 8th Street San Jose, California 95112      |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |5    |3    |$986,000|New Listing         |Not available for viewing|
|210 Sedona Place San Jose, California 95116      |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |5    |3    |$988,888|New Listing         |Not available for viewing|
|1270 Farringdon Drive San Jose, California 95127 |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |3    |2    |$995,000|New Listing         |08/08/2021               |
|449 N 18th Street San Jose, California 95112     |     |     |        |                    |1:00PM-4:00PM            |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |3    |2    |$998,000|New Listing         |08/08/2021               |
|5731 Arapaho Drive San Jose, California 95123    |     |     |        |                    |1:00PM-4:00PM            |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |2    |$998,000|New Listing         |Not available for viewing|
|5908 Sorrel Avenue San Jose, California 95123    |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |2    |$998,888|New Listing         |Not available for viewing|
|763 Stardust Lane San Jose, California 95123     |     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |2    |$999,000|New Listing         |Not available for viewing|
|1845 Arroyo De Platina San Jose, California 95116|     |     |        |                    |                         |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |2    |2    |$999,888|New Listing         |08/08/2021               |
|926 Dempsey Road Milpitas, California 95035      |     |     |        |                    |1:30PM-4:30PM            |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
|                                                 |4    |2    |$999,888|New Listing         |08/08/2021               |
|2966 Postwood Drive San Jose, California 95132   |     |     |        |                    |1:30PM-4:30PM            |
|-------------------------------------------------|-----|-----|--------|--------------------|-------------------------|
```
