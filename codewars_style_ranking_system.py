class User():
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def up_rank(self):
        while self.progress >= 100:
            temp = self.progress - 100

            if self.rank == 8:
                self.progress = 0
                break
            
            elif self.rank == -1:
                self.rank += 2

            else:
                self.rank += 1

            self.progress = temp
    
    def inc_progress(self, task_rank):
        if task_rank < -8 or task_rank > 8:
            return ValueError

        if task_rank == self.rank:
            self.progress += 3
        
        if task_rank == self.rank - 1:
            self.progress += 1
        
        if task_rank == -1 and self.rank == 1:
            self.progress += 1

        if task_rank > self.rank:
            if self.rank < 0 and task_rank > 0:
                dif = task_rank - self.rank - 1
                self.progress += 10 * dif * dif
            else:
                dif = task_rank - self.rank
                self.progress += 10 * dif * dif

        self.up_rank()

user = User()
user.rank # => -8
user.progress # => 0
user.inc_progress(1)
user.inc_progress(1)
user.inc_progress(1)
user.inc_progress(1)
user.inc_progress(1)
user.inc_progress(2)
user.inc_progress(2)
user.rank # => -8
user.progress # => 0
user.inc_progress(-1)
user.rank # => -8
user.progress # => 21
user.inc_progress(3)
user.inc_progress(8)
user.progress # => 10
user.rank
user.inc_progress(1) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
            
        

        
    
