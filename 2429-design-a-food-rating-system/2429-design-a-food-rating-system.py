import heapq
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.d={}
        self.c={}
        for i in range(len(foods)):
            self.d[foods[i]]=[cuisines[i],ratings[i]]
            if cuisines[i] not in self.c:
                self.c[cuisines[i]]=[]
            heapq.heappush(self.c[cuisines[i]],(-ratings[i],foods[i]))
        
    def changeRating(self, food: str, newRating: int) -> None:
        self.d[food]=[self.d[food][0],newRating]
        heapq.heappush(self.c[self.d[food][0]],(-newRating,food))
        
    def highestRated(self, cuisine: str) -> str:
        x,y=heapq.heappop(self.c[cuisine])
        while self.d[y]!=[cuisine,-x]:
            x,y=heapq.heappop(self.c[cuisine])
        heapq.heappush(self.c[cuisine],(x,y))
        return y
        


        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)