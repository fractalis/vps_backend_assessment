# VPS Backend Assessment for Scott Rallya

## Overview

This backend assessment was implemented in Python utilizing the requests module to fetch
Starships from the SWAPI located at https://swapi.dev and the associated pilots with the
starship and then prints out the starship name and the pilot names, if any, to the screen
in a tabular format. 

## Technical Details

This solution was implemented using Python 3.9 utilizing Docker and Docker Compose.

## Features

This solution utilizes the following Python features:

* Dataclasses
* Type hinting
* Iterators

## Implementation Details

 The bulk of the functionality is implemented in the SWAPIClient class, specifically, the fetch_starships method. 
 It fetches the list of Starships from the SWAPI, paginating through the results and adding the next page of 
 results to the list of URLs to query, querying until no additional pages are found. It then constructs a 
 StarshipCollection class and passes in an array of Starship dataclasses to the the constructor and returns 
 the StarshipCollection to the caller of the method.

 The caller of the method, found in app.py, then calls a method on the Starship model class to fetch all the pilots
 associated with the specified Starship. This method simply iterates through the list of Pilots and fetches each individual
 People resource, yielding the result back to the caller of the method for further processing.

## Known Issues and Additional Considerations

 The data model was implemented in all strings. The API had a number of different formats for various types of data for the
 various fields, and in an effort to not spend too much time on this particular assessment I opted to not implement specific
 data types for the fields that could have been set to a different data type. For example, 'n/a' and 'unknown' are valid values
 for a field that could have been declared as int. This would have required additional consideration to have implemented proper
 data types for these fields and I opted to not spend the time implementing this functionality in this version. I'd be more than
 happy to implement this functionality in a future version if needed.

 ## Instructions to Run

 The best method for running this is to utilize docker-compose. Simply running `docker-compose run vps` is enough to build the docker
 image and run the command to fetch the Starships and associated Pilots. If `docker-compose` is not installed, then run the following commands:

 `docker build --tag vps_backend_assessment:0.1 .`
 `docker run vps_backend_assessment:0.1`

 After some time the output of the command will be displayed to the screen, similar to the following:

 ```
 Ship Name: Trade Federation cruiser
	Pilots:
		Obi-Wan Kenobi
		Anakin Skywalker
Ship Name: Theta-class T-2c shuttle
Ship Name: Republic attack cruiser
Ship Name: Naboo star skiff
	Pilots:
		Obi-Wan Kenobi
		Padmé Amidala
Ship Name: Jedi Interceptor
	Pilots:
		Obi-Wan Kenobi
		Anakin Skywalker
Ship Name: arc-170
Ship Name: Banking clan frigte
Ship Name: Belbullab-22 starfighter
	Pilots:
		Obi-Wan Kenobi
		Grievous
Ship Name: V-wing
```

## Instructions to Run tests

To run the tests, simply execute `nosetests` at the command prompt after installing the requirements with `pip install -r requirements.txt`