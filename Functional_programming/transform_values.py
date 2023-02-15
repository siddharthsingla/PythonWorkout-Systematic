def transform_values(f1, f2, a_dict):
    return {key: f1(value) for key, value in a_dict.items() if f2(key, value)}