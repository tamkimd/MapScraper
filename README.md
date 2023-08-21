**Google Maps Scraper**

This tool is used to scrape information from Google Maps without **API KEY**, such as places, distances, star and reviews

**Usage**

To scrape places, use the `PlaceScraper` class. The following code shows how to scrape places for the search term "Trường Đại học duy tân , đà nẵng":

```
from mapcraper import PlaceScraper

search_term = "Trường Đại học duy tân , đà nẵng"
places = PlaceScraper(search_term).extract_places()

for place in places:
    print(place)
```

The output : ```{'Location': 'Duy Tan University, 254 Nguyễn Văn Linh, Thạc Gián, Thanh Khê, Đà Nẵng 550000', 'Reviews': '563 reviews', 'Star Rating': 4.1}
{'Location': 'Duy Tân University, 3 Quang Trung, Hải Châu 1, Hải Châu, Đà Nẵng 550000', 'Reviews': '266 reviews', 'Star Rating': 4.1}```

To scrape the distance between two places, use the `DistanceScraper` class. The following code shows how to scrape the distance between Big C Da Nang and Galaxy Cinema Da Nang:

```
from mapcraper import DistanceScraper

place_a = "GO!(Big C) ,Đà Nẵng "
place_b = "Galaxy Cinema, Đà Nẵng "

bigc_galaxy = DistanceScraper(place_a=place_a, place_b=place_b)
distance = bigc_galaxy.extract_distance()

print(f"distance from {place_a} to {place_b} : {distance}")
```

The output : ```distance from GO!(Big C) ,Đà Nẵng  to Galaxy Cinema, Đà Nẵng  : 3.5 km```

**Requirements**

beautifulsoup4

## Installation

To run the Django backend locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/tamkimd/Mapcraper.git
   git clone https://github.com/tamkimd/MapScraper.git
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```
