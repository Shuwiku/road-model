class Road:

    def __init__(self, next_roads, road_id, road_points):
        self._next_roads = next_roads
        self._road_id = road_id
        self._road_points = road_points

    @property
    def next_roads(self):
        return self._next_roads

    @property
    def road_id(self):
        return self._road_id

    @property
    def road_points(self):
        return self._road_points
