import pygal
from MonteCarlo import MonteCarlo
from DynamicProgramming import DynamicProgramming

if __name__ == "__main__":

  EPISODE_LENGTH = 12
  INFINITE_LIMIT = 1000


  print('Computing Dynamic Programming...')
  d_p = DynamicProgramming()
  d_p_performance = d_p.main()
  d_p_performances = []
  d_p_performances.append(d_p_performance)
  for i in range(0,INFINITE_LIMIT-2):
    d_p_performances.append(None)
  d_p_performances.append(d_p_performance)
  print('done')

  print('Computing Monte-Carlo...')
  monte_carlo = MonteCarlo()
  monte_carlo_performances =  monte_carlo.run(INFINITE_LIMIT,EPISODE_LENGTH)
  print('done')

  print('Drawing graph...')
  graph = pygal.Line()
  graph.title = 'Performance evolution'
  graph.x_title = 'Iteration'
  graph.y_title = 'Performance'
  graph.x_labels = map(str, range(0,INFINITE_LIMIT))

  graph.add('Monte-Carlo',monte_carlo_performances)
  #graph.add('Dynamic Programming',d_p_performances)

  graph.render_to_file('graph_rendering.svg')
  print('done')



