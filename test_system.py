from llm_evaluator import evaluate_answer
from predict_salary import predict_salary


role = "web_developer"
task = "Explain how to center a div."
answer = "We can use display flex, justify-content center and align-items center."

print("--- AI is Evaluating... ---")
result = evaluate_answer(role, task, answer_text=answer)

if "scores" in result:
    print(f"AI Scores: {result['scores']}")
    
    # Salary predict karo
    salary = predict_salary(role, result['scores'])
    print(f"\n--- Result ---")
    print(f"Predicted Salary: {salary} LPA")
    print(f"Suggestion: {result['suggestion']}")
else:
    print("AI Evaluation Failed:", result)