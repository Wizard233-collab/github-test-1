# conditional expression = one line shortcut for if statement(X if condition else Y)
user_role = "guest"

access_level = "Allowed" if user_role == "admin" else "Not allowed"
print(access_level)