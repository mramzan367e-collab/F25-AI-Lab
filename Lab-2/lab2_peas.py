"""PEAS design notes are in Lab2_Report.docx; this file prints environment classifications."""
systems={
 "Delivery robot":{"observability":"Partially observable","reason":"occluded pedestrians and unobserved obstacles","transition":"Stochastic in the real world; deterministic only in a fixed simulator"},
 "LLM student-support agent":{"observability":"Partially observable","reason":"limited context and no access to private records by assumption","transition":"Stochastic output generation and uncertain user/tool outcomes"}}
for name,details in systems.items():
 print(f"{name}: {details['observability']}; {details['transition']}. {details['reason']}.")
