def is_safe_query(query):
    dangerous_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]

    query_upper = query.upper()
    
    for keyword in dangerous_keywords:
        if keyword in query_upper:
            return False

    return True
