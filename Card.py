class CardClass:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.image_filename = f"Cards/{color}_{value}.png"
        
    def __repr__(self):
        return f"{self.color} {self.value}"
    
    def getImage(self):
        return "./images/{}_{}.png".format(self.color, self.value)
    
    def playable(self, other):
        return (
            self._color == other.color or
            self.card_type == other.card_type or
            other.color == 'black'
        )