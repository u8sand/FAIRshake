
def answer_value(value: str):
  try:
    return float(value)
  except:
    return 1 if value != '' else 0
