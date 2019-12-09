import heapq
class astar:
    def __init__(self, initial, trans_f, estimate_f = lambda x:0):
        self.initial_state = initial
        self.trans_func = trans_f
        self.estimate_func = estimate_f
    def run(self, target_state):
        visited = dict()
        queue = []
        def get_path():
            state = target_state
            path = []
            while state != None:
                path.append(state)
                state = visited[state]
            return path
        initial_est = self.estimate_func(self.initial_state)
        heapq.heappush(queue, (initial_est, 0, self.initial_state, None))
        while queue:
            rank, cost, state, ancestor = heapq.heappop(queue)
            if state in visited: continue
            visited[state] = ancestor
            if state == target_state: return (cost, get_path())
            transitions = self.trans_func(state)
            for next_state, next_cost in transitions:
                new_cost = cost + next_cost
                new_rank = new_cost + self.estimate_func(next_state)
                heapq.heappush(queue, (new_rank, new_cost, next_state, state))
