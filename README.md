**Google Maps Scraper**

This tool is used to scrape information from Google Maps without **API KEY**, such as places, distances, star and reviews

**Usage**

To scrape places, use the `PlaceScraper` class. The following code shows how to scrape places for the search term "KFC New York":

```
from mapcraper import PlaceScraper

search_term = "KFC New York"
places = PlaceScraper(search_term).extract_places()

for place in places:
    print(place)
```

The output : ```{'Location': 'KFC, 242 E 14th St, New York, NY 10003, United States', 'Reviews': '1,428 reviews', 'Star Rating': 3.4}
{'Location': 'KFC, 408 8th Ave, New York, NY 10001, United States', 'Reviews': '330 reviews', 'Star Rating': 3.3}
{'Location': 'KFC, 458 Utica Ave, Brooklyn, NY 11203, United States', 'Reviews': '964 reviews', 'Star Rating': 3.6}
{'Location': 'KFC, 3645 Broadway, New York, NY 10031, United States', 'Reviews': '525 reviews', 'Star Rating': 3.5}
{'Location': 'KFC, 1922 3rd Ave, New York, NY 10029, United States', 'Reviews': '918 reviews', 'Star Rating': 3.5}```

To scrape the distance between two KFC locations, you can use the DistanceScraper class. The following code shows how to calculate the distance between two KFC locations in New York:
```
from mapcraper import DistanceScraper

place_a = "KFC, 242 E 14th St, New York, NY 10003, United States"
place_b = "KFC, 408 8th Ave, New York, NY 10001, United States"

kfc_14th_kfc_8th = DistanceScraper(place_a=place_a, place_b=place_b)
distance = kfc_14th_kfc_8th.extract_distance()

print(f"distance from {place_a} to {place_b} : {distance}")
```

The output : ```distance from KFC, 242 E 14th St, New York, NY 10003, United States to KFC, 408 8th Ave, New York, NY 10001, United States : 1.8 miles```

**Requirements**

beautifulsoup4

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/tamkimd/MapScraper.git
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```
Alternatively, you can use a single command:
```
pip install git+https://github.com/tamkimd/MapScraper.git
```
