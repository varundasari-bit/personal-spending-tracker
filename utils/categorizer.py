def categorize(text):
    text = text.lower()
    
    if any(word in text for word in ["pizza","food","restaurant","burger"]):
        return "Food"
    elif any(word in text for word in ["uber","bus","train","fuel"]):
        return "Travel"
    elif any(word in text for word in ["amazon","shopping","clothes"]):
        return "Shopping"
    elif any(word in text for word in ["rent","electricity","bill"]):
        return "Bills"
    else:
        return "Other"
