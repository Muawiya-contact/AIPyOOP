def refactor_code(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
    result = evaluate_code(code)
    print("\nFeedback:", result['feedback'])
    print("Suggestions:")
    for s in result['suggestions']:
        print(f"- {s}")
    print("Code Score:", result['score'])
