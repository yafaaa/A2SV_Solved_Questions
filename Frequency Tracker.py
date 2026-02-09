class FrequencyTracker:

    def __init__(self):
        self.main = dict()
        self.sub = dict()

    def add(self, number: int) -> None:
        if number in self.main:
            self.sub[self.main[number]]-=1
            if self.sub[self.main[number]]==0:
                del self.sub[self.main[number]]
        self.main[number] = self.main.get(number, 0)+1
        self.sub[self.main[number]] = self.sub.get(self.main[number],0)+1

    def deleteOne(self, number: int) -> None:
        if number in self.main:
            self.sub[self.main[number]]-=1
            if self.main[number]-1!=0:
                self.sub[self.main[number]-1] = self.sub.get(self.main[number]-1,0)+1
            if self.sub[self.main[number]]==0:
                del self.sub[self.main[number]]

            self.main[number]-=1
            if self.main[number]==0:
                del self.main[number]
            
        
    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.sub



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
