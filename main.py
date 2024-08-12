import folium
import webbrowser


class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
        self.my_map = folium.Map(location = self.center, zoom_start = self.zoom_start)

    def show_map(self):
        self.my_map.save("map.html")
        webbrowser.open("map.html")

    def add_marker(self, coords):
        folium.Marker((coords)).add_to(self.my_map)
        pass


coords = [4.813246876760088, -75.68723409291646]
map = Map(center = coords, zoom_start = 10)
marker_coords = (4.813246876760088, -75.68723409291646)
map.add_marker(marker_coords)
sorrento_coords = (4.432348824759994, -75.7331965378849)
map.add_marker(sorrento_coords)


map.show_map()