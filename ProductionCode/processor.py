"""Helper functions for loading and filtering UFO sightings data."""


def load_data(filepath="Data/UFO_Sightings.csv"):
    """Load dummy UFO sighting data as a list of dictionaries."""
    return [
        {
            'datetime': '01/01/1999 22:00',
            'city': 'los angeles',
            'state': 'ca',
            'country': 'us',
            'shape': 'circle',
            'duration (seconds)': '60',
            'comments': 'Bright light in the sky'
        },
        {
            'datetime': '03/15/1999 21:30',
            'city': 'seattle',
            'state': 'wa',
            'country': 'us',
            'shape': 'triangle',
            'duration (seconds)': '30',
            'comments': 'Triangle craft hovered silently'
        },
        {
            'datetime': '07/04/2000 20:45',
            'city': 'phoenix',
            'state': 'az',
            'country': 'us',
            'shape': 'fireball',
            'duration (seconds)': '45',
            'comments': 'Fireball moving fast in sky'
        },
        {
            'datetime': '10/31/2001 19:10',
            'city': 'chicago',
            'state': 'il',
            'country': 'us',
            'shape': 'cigar',
            'duration (seconds)': '25',
            'comments': 'Cigar-shaped object glowing orange'
        },
        {
            'datetime': '12/12/1999 18:00',
            'city': 'new york',
            'state': 'ny',
            'country': 'us',
            'shape': 'oval',
            'duration (seconds)': '40',
            'comments': 'Oval object over Central Park'
        }
    ]

def display_results(results):
    """Display search results."""
    if not results:
        print("No sightings found matching your query, please try again with different parameters.")
        return    
    for row in results:
        print(row)

def filter_sightings_by_year(data,year):
    """Filter data data by year."""
    results = []
    for row in data:
        try:
            row_year = int(row['datetime'].split('/')[2].split()[0])
            if row_year == year:
                results.append(row)
        except (IndexError, ValueError):
            continue
    return results

def filter_by_shape(data, shape):
    """filter data to match the given shape."""
    results = []
    shape = shape.strip().lower()
    for row in data:
        row_shape = row['shape'].strip().lower()
        if row_shape == shape:
            results.append(row)
    return results

def get_sightings_by_shape(shape):
    """Get sightings by given shape."""
    data = load_data()
    return filter_by_shape(data, shape)

def get_sightings_by_year(year):
    """Get sightings by given year."""
    data = load_data()
    return filter_sightings_by_year(data,year)