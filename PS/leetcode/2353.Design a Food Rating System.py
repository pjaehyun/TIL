class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_ratings = defaultdict(int)
        self.food_cuisine = defaultdict(str)
        self.cuisine_food_rank = defaultdict(list)

        for i in range(len(foods)):
            self.food_ratings[foods[i]] = ratings[i]
            self.food_cuisine[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_food_rank[cuisines[i]], (-ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_ratings[food] = newRating

        cuisine = self.food_cuisine[food]
        heapq.heappush(self.cuisine_food_rank[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest = self.cuisine_food_rank[cuisine][0]

        while self.food_ratings[highest[1]] != -highest[0]:
            heapq.heappop(self.cuisine_food_rank[cuisine])
            highest = self.cuisine_food_rank[cuisine][0]
        return highest[1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)