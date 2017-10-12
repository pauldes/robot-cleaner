import pygal
from MonteCarlo import MonteCarlo

if __name__ == "__main__":

  EPISODE_LENGTH = 100
  INFINITE_LIMIT = 100

  print('Computing Monte-Carlo...')
  monte_carlo = MonteCarlo()
  monte_carlo_performances = monte_carlo.run(INFINITE_LIMIT,EPISODE_LENGTH)
  print('done')

  print('Drawing graph...')
  graph = pygal.Line()
  graph.title = 'Performance evolution'
  graph.x_title = 'Iteration'
  graph.y_title = 'Performance'
  graph.x_labels = map(str, range(0,INFINITE_LIMIT))

  graph.add('Monte-Carlo',monte_carlo_performances)

  graph.render_to_file('graph_rendering.svg')
  print('done')



