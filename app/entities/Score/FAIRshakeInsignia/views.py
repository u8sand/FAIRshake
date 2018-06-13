from .util import build_insignia_svg

kinds = {}
def register_kind(kind):
  def register_kind_decorator(func):
    global kinds
    kinds[kind] = func
    return func
  return register_kind_decorator

@register_kind('application/json')
def application_json(scores):
  return (
    scores,
    200,
  )

@register_kind('text/html')
def text_html(scores):
  return (
    '<svg viewBox="0 0 1 1">%s</svg>' % (
      ''.join(build_insignia_svg(scores))
    ),
    201,
  )

@register_kind('')
def unknown_kind(scores):
  return (
    '',
    401,
  )
