from app.util.generate_spec import generate_spec

def test_generate_spec():
  class T:
    '''
    my:
      test:
        {T__k}
    blah: bleh
    '''
    def k():
      '''
      blue:
        bla: {T__l__j}
      '''
      pass
    class l:
      def j():
        '''
        blop: pop
        '''
        pass
  assert generate_spec(T) == {
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

def test_generate_spec_test_api():
  from ..api import TestAPI
  generate_spec(TestAPI)
