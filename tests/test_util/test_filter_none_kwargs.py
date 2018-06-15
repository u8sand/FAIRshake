from app.util.filter_none_kwargs import filter_none_kwargs

def test_filter_none_kwargs():
  assert filter_none_kwargs(a=None, b='c') == {'b': 'c'}
  assert filter_none_kwargs({'a': None, 'b': 'c'}, d=None, e='c') == {'b': 'c', 'e': 'c'}
