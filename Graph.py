import pygal

if __name__ == "__main__":
  print('Computing Monte-Carlo...')
  monte_carlo = MonteCarlo()
  monte_carlo.run(10000)
  print('done')
