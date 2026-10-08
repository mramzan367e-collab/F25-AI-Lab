"""Synthetic scholarship-screening comparison; not a trained predictor."""
def symbolic(score, complete):
    return "Review" if complete and score >= 70 else "Hold"
def threshold(probability):
    return "Review" if probability >= 0.70 else "Hold"
cases=[("complete_high",82,True,.81),("complete_low",68,True,.74),("incomplete_high",91,False,.88),("boundary",70,True,.70)]
print("case | score | complete | supplied_probability | symbolic | threshold | disagreement")
for name,score,complete,p in cases:
    a,b=symbolic(score,complete),threshold(p)
    print(f"{name} | {score} | {complete} | {p:.2f} | {a} | {b} | {a!=b}")
