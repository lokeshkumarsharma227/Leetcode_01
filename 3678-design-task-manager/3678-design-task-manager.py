from sortedcontainers import SortedSet
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.taskPriorityMap = {}
        self.executionList = SortedSet()
        self.taskUserMap = {}

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskUserMap[taskId] = userId
        self.taskPriorityMap[taskId] = priority
        self.executionList.add((priority, taskId))               

    def edit(self, taskId: int, newPriority: int) -> None:
        currentPriority = self.taskPriorityMap[taskId]
        self.taskPriorityMap[taskId] = newPriority
        self.executionList.remove((currentPriority, taskId))
        self.executionList.add((newPriority, taskId))

    def rmv(self, taskId: int) -> None:
        priority = self.taskPriorityMap[taskId]

        if (priority, taskId) in self.executionList:
            self.executionList.remove((priority, taskId))

        del self.taskPriorityMap[taskId]
        del self.taskUserMap[taskId]
        
    def execTop(self) -> int:
        if len(self.executionList) == 0:
            return -1

        priority, taskId = self.executionList.pop(-1)

        userId = self.taskUserMap[taskId]
        self.rmv(taskId)
        return userId


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()