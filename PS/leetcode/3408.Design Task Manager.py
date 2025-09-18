class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_prio_map = defaultdict(int)
        self.task_user_map = defaultdict(int)
        self.t_hq = []
        for task in tasks:
            u, t, p = task
            self.task_prio_map[t] = p
            self.task_user_map[t] = u
            heappush(self.t_hq, (-p, -t))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_prio_map[taskId] = priority
        self.task_user_map[taskId] = userId
        heappush(self.t_hq, (-priority, -taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_prio_map[taskId] = newPriority
        heappush(self.t_hq, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        self.task_prio_map[taskId] = -1

    def execTop(self) -> int:
        while True:
            if not self.t_hq:
                return -1
            pt = heappop(self.t_hq)
            p, t = -pt[0], -pt[1]
            if self.task_prio_map[t] == p:
                break
        self.task_prio_map[t] = -1
        return self.task_user_map[t]