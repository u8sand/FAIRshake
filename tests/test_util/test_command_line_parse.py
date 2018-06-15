from app.util.command_line_parse import parse

def test_parse():
  assert parse(
    ['a', '10', '--c=d', 'true', '--g=["h", "i"]', '--j=false']
  ) == (
    ['a', 10, True,], {'c': 'd', 'g': ['h', 'i'], 'j': False,}
  )
