dataset_infile = '/data/yfcc100m/yfcc100m_dataset'

def main():
  print('quantitatively estimate the number of broken images')

  t_line = 0
  with open(dataset_infile) as fin:
    for line in fin.readlines():
      t_line += 1
  print('%s contains %d lines in total' % (dataset_infile, t_line))

if __name__ == '__main__':
  main()