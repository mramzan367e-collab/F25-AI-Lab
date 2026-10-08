"""A* audit on the supplied directed campus graph; deterministic tie-breaking."""
import heapq
G={"S":[("A",1),("B",4)],"A":[("C",2)],"B":[("G",5)],"C":[("G",3)],"G":[]}
H={"S":5,"A":4,"B":4,"C":2,"G":0}
TRUE={"S":6,"A":5,"B":5,"C":3,"G":0}
def search(h):
 pq=[(h["S"],0,0,"S",("S",))];best={"S":0};seq=0;trace=[];expanded=[]
 while pq:
  f,g,_,u,path=heapq.heappop(pq)
  if g!=best.get(u):continue
  trace.append((u,g,h[u],f))
  if u=="G":return g,list(path),trace,expanded
  expanded.append(u)
  for v,w in G[u]:
   ng=g+w
   if ng<best.get(v,float('inf')):
    best[v]=ng;seq+=1;heapq.heappush(pq,(ng+h[v],ng,seq,v,path+(v,)))
 return None,None,trace,expanded
print("Heuristic admissibility/consistency audit")
for n in H: print(f"{n}: h={H[n]}, true_remaining={TRUE[n]}, admissible={H[n]<=TRUE[n]}")
for u,edges in G.items():
 for v,w in edges: print(f"edge {u}->{v}: {H[u]} <= {w}+{H[v]} is {H[u]<=w+H[v]}")
for label,h in (("A*",H),("UCS (h=0)",{n:0 for n in H}),("A* overestimate h(C)=10",{**H,"C":10})):
 cost,path,trace,expanded=search(h)
 sum_cost=sum(next(w for v,w in G[a] if v==b) for a,b in zip(path,path[1:]))
 print(f"{label}: path={path}, cost={cost}, independent_sum={sum_cost}, processed={[x[0] for x in trace]}, expanded={expanded}, expansion_count={len(expanded)}")
 print("  g,h,f trace:",trace)
