import folium
import webbrowser
import pandas as pd


class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
        self.my_map = folium.Map(location=self.center, zoom_start=self.zoom_start)

    def show_map(self):
        self.my_map.save("map.html")
        webbrowser.open("map.html")

    def add_marker(self, coords, name, status):
        if status:
            color = "green"
        else:
            color = "red"
        folium.Marker(
            location=coords, popup=name, icon=folium.Icon(color=color)
        ).add_to(self.my_map)


def create_map(df):
    center_coords = [4.813246876760088, -75.68723409291646]
    my_map = Map(center=center_coords, zoom_start=10)
    for row in df.itertuples():
        coords = row.coordenadas.split(", ")
        my_map.add_marker(coords, row.viaje, row.completado)

    my_map.show_map()


def read_tsv(path):
    df = pd.read_csv(path, delimiter="\t")
    return df


if __name__ == "__main__":
    df_coords = read_tsv("src/viajes_100.tsv")
    create_map(df_coords)
