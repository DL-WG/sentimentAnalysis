# Written by Jake Lever 03/2021
class Sentiment:
    def __init__(self, score, magnitude):
        self.score = score
        self.magnitude = magnitude

    def __str__(self):
        return 'Sentiment Score: {}. Magnitude: {}'.format(self.score, self.magnitude)