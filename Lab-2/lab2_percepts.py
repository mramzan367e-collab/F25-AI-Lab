"""Stateful classroom controller: simulation only, no hardware access."""
class ClassroomAgent:
    def __init__(self): self.previous_mode=None
    @staticmethod
    def target(temp,occupied):
        if not occupied: return "ECO"
        if temp>26: return "COOL"
        if temp<20: return "WARM"
        return "IDLE"
    def act(self,temp,occupied):
        previous=self.previous_mode
        target=self.target(temp,occupied)
        send=target!=previous
        self.previous_mode=target
        return previous,target,send
percepts=[(29,True),(29,True),(20,True),(26,True),(19,True),(29,False)]
agent=ClassroomAgent()
print("step | previous | percept(temp,occupied) | target | command")
for i,p in enumerate(percepts,1):
 prev,target,send=agent.act(*p)
 print(f"{i} | {prev or 'NONE'} | {p} | {target} | {'SEND' if send else 'NO COMMAND'}")
