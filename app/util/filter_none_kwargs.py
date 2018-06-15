def filter_none_kwargs(__={}, **kwargs):
  return {
    k: v
    for k, v in dict(__, **kwargs).items()
    if v is not None
  }
