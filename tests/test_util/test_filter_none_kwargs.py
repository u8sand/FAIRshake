from app.util.filter_none_kwargs import filter_none_kwargs

def test_filter_none_kwargs():
  assert filter_none_kwargs(a=None, b='c') == {'b': 'c'}
