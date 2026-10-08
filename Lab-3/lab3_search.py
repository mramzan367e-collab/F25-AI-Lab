"""BFS, DFS, DLS, IDDFS and UCS on manual graph plus explicit weighted extension."""
from collections import deque
import heapq
GRAPH={"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":["G"],"F":[],"G":[]}
WEIGHTED={"A":[("B",1),("C",6)],"B":[("D",2),("E",1)],"C":[("F",2),("G",6)],"D":[],"E":[("G",1)],"F":[],"G":[]}
def bfs_trace(start,goal):
 q=deque([(start,[start])]); seen={start}; trace=[]
 while q:
  node,path=q.popleft(); trace.append(node)
  if node==goal:return path,trace
  for n in GRAPH[node]:
   if n not in seen: seen.add(n);q.append((n,path+[n]))
 return None,trace
def dfs_trace(start,goal):
 stack=[(start,[start])];seen=set();trace=[]
 while stack:
  node,path=stack.pop()
  if node in seen:continue
  seen.add(node);trace.append(node)
  if node==goal:return path,trace
  for n in reversed(GRAPH[node]):stack.append((n,path+[n]))
 return None,trace
def dls(start,goal,limit):
 trace=[]
 def visit(node,path,depth):
  trace.append(node)
  if node==goal:return "FOUND",path
  cutoff=False
  if depth<limit:
   for n in GRAPH[node]:
    if n not in path:
     status,result=visit(n,path+[n],depth+1)
     if status=="FOUND":return status,result
     cutoff |= status=="CUTOFF"
  else:
   cutoff=any(n not in path for n in GRAPH[node])
  return ("CUTOFF" if cutoff else "FAILURE"),None
 status,path=visit(start,[start],0);return status,path,trace
def iddfs(start,goal,max_depth):
 attempts=[]
 for limit in range(max_depth+1):
  status,path,trace=dls(start,goal,limit);attempts.append((limit,status,path,trace))
  if status=="FOUND":return path,attempts
 return None,attempts
def ucs(graph,start,goal):
 pq=[(0,0,start,[start])]; best={start:0}; trace=[]; serial=1
 while pq:
  cost,_,node,path=heapq.heappop(pq)
  if cost!=best.get(node):continue
  trace.append(node)
  if node==goal:return cost,path,trace
  for nxt,w in graph.get(node,[]):
   nc=cost+w
   if nc<best.get(nxt,float('inf')):
    best[nxt]=nc;heapq.heappush(pq,(nc,serial,nxt,path+[nxt]));serial+=1
 return None,None,trace
def bfs_weighted():
 q=deque([("A",["A"])]);seen={"A"}
 while q:
  n,p=q.popleft()
  if n=="G":return p
  for v,w in WEIGHTED[n]:
   if v not in seen:seen.add(v);q.append((v,p+[v]))
print("BFS",*bfs_trace("A","G"))
print("DFS",*dfs_trace("A","G"))
for limit in (1,2,3,4):
 status,path,trace=dls("A","G",limit);print(f"DLS limit={limit}: {status}; path={path}; visits={trace}")
 path,attempts=iddfs("A","G",limit);print(f"IDDFS max={limit}: path={path}; limits={[a[0] for a in attempts]}; statuses={[a[1] for a in attempts]}")
cost,path,trace=ucs(WEIGHTED,"A","G")
def path_cost(p):return sum(dict(WEIGHTED[a])[b] for a,b in zip(p,p[1:]))
bpath=bfs_weighted()
print("Weighted edges:",WEIGHTED)
print(f"BFS weighted route={bpath}, hops={len(bpath)-1}, cost={path_cost(bpath)}")
print(f"UCS route={path}, cost={cost}, independently_summed={path_cost(path)}, processing={trace}")
