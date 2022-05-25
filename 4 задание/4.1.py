class FoodInfo:
    
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        
    def get_proteins(self):
        return self.proteins
    
    def get_fats(self):
        return self.fats
    
    def get_carbohydrates(self):
        return self.carbohydrates
    
     def get_carbohydrates(self):
        return self.carbohydrates

    def get_kcalories(self):
        return 4 * self.get_proteins() + 9 * self.get_fats() + 4 * self.get_carbohydrates()

