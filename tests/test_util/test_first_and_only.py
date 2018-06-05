from app.util.first_and_only import first, first_and_only

def test_first():
  assert first([1, 2]) == 1

def test_first_and_only():
  assert first_and_only([1]) == 1

  try:
    first_and_only([])
    assert "Doesn't raise when empty."
  except:
    pass

  try:
    first_and_only([1, 2])
    assert "Doesn't raise when more than one."
  except:
    pass
