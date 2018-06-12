import math as m

def nearest_sq(n):
  ''' Find the nearest square to build the insignia '''
  return m.ceil(m.sqrt(n))

def linearize(x1, y1, x2, y2, val):
  ''' Convert val from space x1,y1 into space x2,y2 '''
  return val * (y2 - y1) / (x2 - x1)

def build_insignia_svg(scores):
  ''' Construct the insignia with arbitrary scores and summaries
  
  This constructs a nested square where the outer square consists
  of square blocks corresponding to each score in scores and inner
  squares corresponding to each average in that particular score.
  
      1<n<=4 summaries in second score
        \/
  |--------|-------|
  |        |___|___|
  |        |   |   |
  |--------|-------|
  |--------|-------|
  |__|__|__|       | < 1 summary in 1st and fourth score
  |  |  |  |       | 
  |--------|-------|
    /\
  4<n<=9 summaries in third score
  
  Color is linarly chosen between Red (0) and Blue (1).
  '''
  scores_sq = nearest_sq(len(scores))
  for i, score in enumerate(scores):
    summary_sq = nearest_sq(len(score.summaries))
    for j, summary in enumerate(score.summaries):
      yield '<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="#{fill}" />'.format(
        x = (i % (scores_sq * summary_sq)) / (scores_sq * summary_sq),
        y = m.ceil(i % (scores_sq * summary_sq)) / (scores_sq * summary_sq),
        width = 1 / (scores_sq * summary_sq),
        height = 1 / (scores_sq * summary_sq),
        fill = linearize(0, 1, 0xff0000, 0x0000ff, score.average),
      )
