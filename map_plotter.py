from gmplot import gmplot
import maps_googleV2

gmap = gmplot.GoogleMapPlotter(50.0595854,14.3255415, 13)

top_attraction_lats, top_attraction_lons = zip(*maps_googleV2.get_res_coord())
gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=15, marker=False)

gmap.draw("my_map.html")