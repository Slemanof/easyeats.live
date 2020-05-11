from gmplot import gmplot
import maps_googleV2

apikey = "AIzaSyCwR7HL2a3L3WDsBUF3HY-wRkHXWYIFLco"
gmap = gmplot.GoogleMapPlotter.from_geocode("Prague", apikey)

top_attraction_lats, top_attraction_lons = zip(*maps_googleV2.get_res_coord())
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=15, marker=False)

gmap.draw("my_map.html")