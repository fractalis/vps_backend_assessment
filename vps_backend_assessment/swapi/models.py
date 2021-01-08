from dataclasses import dataclass
from datetime import datetime
from typing import List

from .utilities import fetch

import dateutil.parser
import ujson as json

@dataclass
class Starship:
    """
        A dataclass to represent a Starship

        Attributes
        ----------

        name : str
            Name of the starship
        model : str
            Model of the starship
        manufacturer : str
            Manufacturer of the starship
        cost_in_credits : str
            Cost of the starship in credits
        length : str
            Length of the starship (varying measurements)
        max_atmosphereing_speed : str
            Max speed of starship in atmosphere (n/a if ship can't fly in atmosphere)
        crew : str
            Range of the crew members that maintain the ship
        cargo_capacity : str
            Cargo capacity of the starship
        consumables : str
            Length of time that the ship can sustain before refueling consumables
        hyperdrive_rating : str
            The rating of the hyperdrive of the ship
        MGLT : str
            Speed of the ship in Megalight Per Hour
        starship_class : str
            Class of the Starship
        pilots : List[str]
            URL List of the pilots who've piloted the ship
        films : List[str]
            URL list of the films the ship has appeared in
        created : datetime
            Datetime this entry was created
        edited : datetime
            Datetime this entry was edited
        url : str
            The URL to this entry
    """
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str
    pilots: List[str]
    films: List[str]
    created: datetime
    edited: datetime
    url: str

    def __post_init__(self):
        """Initializes fields post init so they're the proper data type"""
        if type(self.created) is str:
            self.created = dateutil.parser.parse(self.created)
        if type(self.edited) is str:
            self.edited = dateutil.parser.parse(self.edited)

    def fetch_pilots(self):
        """Fetches the People object for each pilot in the pilots collection"""
        for pilot in self.pilots:
            # Fetch the Pilot Data
            resp = fetch(pilot)

            json_data = json.loads(resp.content)

            # Construct a People object out of the JSON data
            pilot = People(**json_data)

            yield pilot

@dataclass
class People:
    """
        A dataclass to represent a Person

        Attributes:
        --------------
        name : str
            Name of the person
        height : str
            Height of the in centimeters
        mass : str
            Mass of the person in kilograms
        hair_color : str
            Hair color of the person
        skin_color : str
            Skin color of the person
        eye_color : str
            Eye color of the person
        birth_year : str
            The birth year of the person, using the in-universe standard of BBY or ABY (Before the Battle of Yavin or After the Battle of Yavin)
        gender : str
            Gender of the person
        homeworld : str
            URL of a planet resource - planet this person was born on or inhabits
        films : List[str]
            List of URLS that this person has been in
        species : List[str]
            List of species URLs that this perosn belongs to
        starships : List[str]
            List of starship URLs that this person has piloted
        vehicles : List[str]
            List of vehicle URLs that this person has pilot
        created : datetime
            The ISO 8601 date format of the time this resource was created
        edited : datetime
            The ISO 8601 date format of the time this resource was edited
        url : str
            The URL of this People resource
    """
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]
    created: datetime
    edited: datetime
    url: str

    def __post_init__(self):
        """Initializes fields post init so they're the proper data type"""
        if type(self.created) is str:
            self.created = dateutil.parser.parse(self.created)
        if type(self.edited) is str:
            self.edited = dateutil.parser.parse(self.edited)


class BaseCollection(object):
    """
        Represents a collection of items
    """

    def __init__(self):
        self.items = []

    def length(self):
        """Return the length of the collection"""
        return len(self.items)

    def iter(self):
        """Acts as an iterator for the collection and yields each item in the collection"""
        for item in self.items:
            yield item

class StarshipCollection(BaseCollection):
    """
        Represents a collection of Starships
    """
    def __init__(self, starships):
        super(StarshipCollection, self).__init__()
        for starship in starships:
            self.items.append(starship)
    
        

