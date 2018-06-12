from app.util.generate_spec import generate_spec

def test_generate_spec():
  class T:
    '''
    my:
      test:
        {T.k}
    blah: bleh
    '''
    def k(self):
      '''
      blue:
        bla: {T.l.j}
      '''
      pass
    class l(self):
      def j(self):
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
