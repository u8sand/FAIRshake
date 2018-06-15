def filter_none_kwargs(__={}, **kwargs):
  return dict({
    k: v
    for k, v in __.items()
    if v is not None
  }, **({} if kwargs == {} else filter_none_kwargs(kwargs)))
