# Pystation-api
Package to use playstation store api to retrive info from a games with a json format.
## How to use 
```Python
from pystationapi import Playstation
playstationapi= Playstation()
playstationapi.to_json_from_category(Playstation.SALES,3)#first parameter is the category for the search, the second parameter is the number of results
```
### Enumeration

There is 2 enumeration one in Playstation Object composite from that:

```Python
from pystationapi import Playstation
playstationapi= Playstation()
Playstation.SALES #Game in sales in the store
Playstation.PS4_GAMES# filter only plastation 4 games
Playstation.PS5_GAMES# filter only plastation 5 games
Playstation.PS_PLUS# filter only plastation plus offers games
Playstation.EA_GAMES# filter only EA games

```

### Enumeration 2
In this class PlaystationEnum there is filter to use inside filterBy this functionality is predisposed but have not implemented yet
this is the value of enumeration:
```Python
    FACET_NAME_OPTION_TYPE = 'storeDisplayClassification'
    FACET_NAME_OPTION_PRICE = 'webBasePrice'
    FACET_NAME_OPTION_GENRE = 'productGenres'
    FACET_NAME_OPTION_PLATFORMPS4 = 'targetPlatforms'
    FACET_NAME_OPTION_PLATFORMPS5 = 'targetPlatforms'
    FACET_NAME_OPTION_RELEASE_DATE = 'productReleaseDate'
    FACET_NAME_OPTION_PLAYSTATION_VR = 'productVrCompatibility'
    FACET_NAME_OPTION_AGE_RATING = 'ageRating'

    SORTING_OPTION_BEST_SELLING = 'sales30' 
    SORTING_OPTION_MOST_DOWNLOADED = 'downloads30'
    SORTING_OPTION_PRODUCT_NAME = 'productName'
    SORTING_OPTION_RELEASE_DATE = 'productReleaseDate'
    SORTING_OPTION_WEB_BASE_PRICE = 'webBasePrice'

    #values type first facet option

    FACET_NAME_OPTION_TYPE_FULL_GAME = 'FULL_GAME'
    FACET_NAME_OPTION_TYPE_GAME_BUNDLE = 'GAME_BUNDLE'
    FACET_NAME_OPTION_TYPE_OTHER = 'OTHER'
    FACET_NAME_OPTION_TYPE_CHARACTER = 'CHARACTER'
    FACET_NAME_OPTION_TYPE_ADD_ON_PACK = 'ADD-ON_PACK'
    FACET_NAME_OPTION_TYPE_LEVEL = 'LEVEL'
    FACET_NAME_OPTION_TYPE_BUNDLE = 'BUNDLE'
    FACET_NAME_OPTION_TYPE_MAP = 'MAP'
    FACET_NAME_OPTION_TYPE_PREMIUM_EDITION = 'PREMIUM_EDITION'
    FACET_NAME_OPTION_TYPE_ITEM = 'ITEM'
    FACET_NAME_OPTION_TYPE_SEASON_PASS = 'SEASON_PASS'
    FACET_NAME_OPTION_TYPE_VEHICLE = 'VEHICLE'

    #value type second facet option

    FACET_NAME_OPTION_PRICE_0_99 = '0-99'
    FACET_NAME_OPTION_PRICE_100_199 = '100-199'
    FACET_NAME_OPTION_PRICE_200_499 = '200-499'
    FACET_NAME_OPTION_PRICE_500_999 = '500-999'
    FACET_NAME_OPTION_PRICE_1000_1999 = '1000-1999'
    FACET_NAME_OPTION_PRICE_2000_2999 = '2000-2999'
    FACET_NAME_OPTION_PRICE_3000_3999 = '3000-3999'
    FACET_NAME_OPTION_PRICE_4000_4999 = '4000-4999'
    FACET_NAME_OPTION_PRICE_5000_ = '5000-'

    #value type third facet option

    FACET_NAME_OPTION_GENRE_ADVENTURE = 'ADVENTURE'
    FACET_NAME_OPTION_GENRE_ROLE_PLAYING_GAMES = 'ROLE_PLAYING_GAMES'
    FACET_NAME_OPTION_GENRE_HORROR = 'HORROR'
    FACET_NAME_OPTION_GENRE_SHOOTER = 'SHOOTER'
    FACET_NAME_OPTION_GENRE_ARCADE = 'ARCADE'
    FACET_NAME_OPTION_GENRE_UNIQUE = 'UNIQUE'
    FACET_NAME_OPTION_GENRE_RACING = 'RACING'
    FACET_NAME_OPTION_GENRE_PUZZLE = 'PUZZLE'
    FACET_NAME_OPTION_GENRE_SPORTS = 'SPORTS'
    FACET_NAME_OPTION_GENRE_FIGHTING = 'FIGHTING'
    FACET_NAME_OPTION_GENRE_SIMULATION = 'SIMULATION'
    FACET_NAME_OPTION_GENRE_STRATEGY = 'STRATEGY'
    FACET_NAME_OPTION_GENRE_CASUAL = 'CASUAL'
    FACET_NAME_OPTION_GENRE_FAMILY = 'FAMILY'
    FACET_NAME_OPTION_GENRE_MUSIC_RHYTHM = 'MUSIC/RHYTHM'
    FACET_NAME_OPTION_GENRE_PARTY = 'PARTY'
    FACET_NAME_OPTION_GENRE_EDUCATIONAL = 'EDUCATIONAL'
    FACET_NAME_OPTION_GENRE_FITNESS = 'FITNESS'
    FACET_NAME_OPTION_GENRE_BRAIN_TRAINING = 'BRAIN_TRAINING'
    FACET_NAME_OPTION_GENRE_SIMULATOR = 'SIMULATOR'

    # fourth facet values

    FACET_NAME_OPTION_PLATFORMPS4_VALUE = 'PS4'
    FACET_NAME_OPTION_PLATFORMPS5_VALUE = 'PS5'

    # fiveth facet values

    FACET_NAME_OPTION_RELEASE_DATE_JUST_RELEASED = 'last_thirty_days'

    #sixth facet values

    FACET_NAME_OPTION_PLAYSTATION_VR_REQUIRED = 'REQUIRED'
    FACET_NAME_OPTION_PLAYSTATION_VR_OPTIONAL = 'OPTIONAL'

    #seveth facet values

    FACET_NAME_OPTION_AGE_RATING_PEGI_3 = 'PEGI_3'
    FACET_NAME_OPTION_AGE_RATING_PEGI_7 = 'PEGI_7'
    FACET_NAME_OPTION_AGE_RATING_PEGI_12 = 'PEGI_12'
    FACET_NAME_OPTION_AGE_RATING_PEGI_16 = 'PEGI_16'
    FACET_NAME_OPTION_AGE_RATING_PEGI_18 = 'PEGI_18'


```