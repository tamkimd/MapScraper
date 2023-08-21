import requests
from bs4 import BeautifulSoup
import urllib.parse
import json


class ScraperBase():
    """
    Base class for web scraping.
    """

    def __init__(self):
        self.base_url = "https://www.google.com/maps"
        self.url = self.base_url

    def get_soup(self):
        """
        Get BeautifulSoup object from the URL.
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            return soup
        except Exception as e:
            return f"Error processing get_soup: {str(e)}"

    def get_app_init_state(self):
        """
        Get the app initialization state script content.
        """
        try:
            script_tags = self.get_soup().find_all("script")

            for script_tag in script_tags:
                script_content = script_tag.get_text()

                if "window.APP_INITIALIZATION_STATE" in script_content:
                    start_index = script_content.find(
                        "window.APP_INITIALIZATION_STATE")
                    end_index = script_content.find("];", start_index) + 1
                    return script_content[start_index:end_index]
        except Exception as e:
            return f"Error processing get_app_init_state: {str(e)}"


class PlaceScraper(ScraperBase):
    """
    Scrapes places based on a search term.
    """

    def __init__(self, search_term):
        super().__init__()
        self.search_term = urllib.parse.quote(search_term)
        self.url = f"{self.base_url}/search/{self.search_term}"
        self.app_init_state = self.get_app_init_state()

    def extract_places(self):
        """
        Extract and return a list of dictionaries containing places'information.
        """

        try:
            app_init_data = json.loads(
                self.app_init_state.split("=")[1].strip())
            places = json.loads(app_init_data[3][2][5:])[0][1]
            place_info_list = []
            if len(places) >= 1:
                places = places[1:]

            for id, place in enumerate(places):
                try:
                    place_info = self.get_place_info(place, id)
                    place_info_list.append(place_info)
                except Exception as e:
                    return f"Error processing place {id}: {str(e)}"

            return place_info_list
        except Exception as e:
            return f"Error processing extract_places: {str(e)}"

    def get_place_info(self, place, place_id):
        try:
            location = self.get_location(place)
            reviews_data, star_rating = self.get_reviews_and_star(place)

            place_info = {
                "Location": location,
                "Reviews": reviews_data,
                "Star Rating": star_rating
            }
            return place_info

        except Exception as e:
            return f"Error processing place {place_id + 1}: {str(e)}"

    def get_reviews_and_star(self, place):
        try:
            place_data = place[14]
            if place_data[4] is not None:
                reviews_data = place_data[4][3][1]
                star_rating = place_data[4][7]
                return reviews_data, star_rating
            return None, None
        except Exception as e:
            return f"Error processing reviews and star: {str(e)}"

    def get_location(self, place):
        try:
            place_data = place[14]
            location = place_data[18]
            return location
        except Exception as e:
            return f"Error processing location: {str(e)}"


class DistanceScraper(ScraperBase):
    """
    Scrapes Distance from a place to b place
    """

    def __init__(self, place_a, place_b):
        super().__init__()
        self.place_a = urllib.parse.quote(place_a)
        self.place_b = urllib.parse.quote(place_b)
        self.url = f"{self.base_url}/dir/{self.place_a}/{self.place_b}"
        self.app_init_state = self.get_app_init_state()

    def extract_distance(self):
        """
        Extract and return distance from a place to b place
        """

        try:
            app_init_data = json.loads(
                self.app_init_state.split("=")[1].strip())[3][4][5:]
            data = json.loads(app_init_data)[0][1][0][0]
            distance = data[2][1]
            return distance

        except Exception as e:
            return f"Error processing extract_distance: {str(e)}"


