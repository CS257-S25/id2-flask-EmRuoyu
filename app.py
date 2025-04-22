"Flask API for UFO Sightings"
from flask import Flask
from ProductionCode.processor import get_sightings_by_year

app = Flask(__name__)

@app.route("/")
def home():
    """Home route with usage instructions."""
    return (
        "<h2>Welcome to the UFO Sightings API</h2>"
        "<p>Use the route <code>/year/&lt;year&gt;</code><br>"
        "to view sightings from a specific year.</p>"
        "<p>Example: <a href='/year/1999'>/year/1999</a></p>"
    )

@app.route("/year/<int:year>")
def sightings_by_year(year):
    """Return UFO sightings from the given year in HTML table format."""
    results = get_sightings_by_year(year)
    if not results:
        return f"<p>No sightings found for the year {year}.</p>"
    return render_results(year, results)

def render_results(year, results):
    """Render results in an HTML table."""
    table = table_constructor(results)
    return f"<h3>Sightings from {year}</h3>" + table

def table_constructor(results):
    """Construct an HTML table from the data."""
    header_row = "".join(f"<th>{key}</th>" for key in results[0].keys())
    table = "<table border='1'><tr>" + header_row + "</tr>"
    for row in results:
        data_row = "".join(f"<td>{val}</td>" for val in row.values())
        table += "<tr>" + data_row + "</tr>"
    table += "</table>"
    return table

if __name__ == "__main__":
    app.run()
