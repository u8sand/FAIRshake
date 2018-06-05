from app.util.generate_spec import generate_spec

def test_generate_spec():
  class T:
    '''
    my:
      test:
        {T__k}
    blah: bleh
    '''
    def k(self):
      '''
      blue:
        bla: {T__l}
      '''
      pass
    def l(self):
      '''
      blop: pop
      '''
      pass
  assert generate_spec(T.__doc__, dict(T=T)) == {
    'my': {
      'test': {
        'blue': {
          'bla': {
            'blop': 'pop',
          },
        },
      },
    },
    'blah': 'bleh',
  }
