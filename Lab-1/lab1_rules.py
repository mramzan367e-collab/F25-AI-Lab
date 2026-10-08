"""Transparent policy prototype; all criteria are synthetic teaching assumptions."""
def decide(score, documents_complete, gpa_eligible, deadline_met):
    if not documents_complete: return "Hold", "required documents incomplete"
    if score < 70: return "Hold", "score below 70 threshold"
    if not gpa_eligible: return "Hold", "GPA eligibility condition failed"
    if not deadline_met: return "Hold", "deadline condition failed"
    return "Review", "all screening conditions passed; human review required"
cases=[
 ("pass",80,True,True,True,"Review"),
 ("GPA failure",80,True,False,True,"Hold"),
 ("deadline failure",80,True,True,False,"Hold"),
 ("threshold boundary",70,True,True,True,"Review"),
]
print("case | inputs(score,docs,gpa,deadline) | expected | actual | reason | PASS")
for name,s,d,g,t,expected in cases:
 actual,reason=decide(s,d,g,t)
 print(f"{name} | ({s},{d},{g},{t}) | {expected} | {actual} | {reason} | {expected==actual}")
