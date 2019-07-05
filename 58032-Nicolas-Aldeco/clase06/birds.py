class Bird(object):
    name = ''
    flightless = False
    extinct = False

    bird_speed = {
        'Ostrich': 15,
        'Chicken': 7,
        'Flamingo': 8,
        'Gold Finch': 12,
        'Bluejay': 10,
        'Robin': 14,
        'Hummingbird': 16,
    }

    def get_speed(self):
        if self.extinct:
            return -1  # we do not care about extinct bird speeds
        return self.bird_speed.get(self.name, -1)