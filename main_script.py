
import argparse

from p_acquisition import m_acquisition

def argument_parser():
    parser = argparse.ArgumentParser(description='specify input file and api key...')
    parser.add_argument("-p", "--path", type=str, help='specify companies list file...', required=True)
    parser.add_argument("-k", "--key", type=str, help='specify Quandl API key...', required=True)
    args = parser.parse_args()


def main(args):
    print('Hola bb - Starting pipeline')
    #df = pd.DataFrame ({'a':[1,2,3], 'b': [4,5,6]})
    m_acquisition.get_tickers(args.path)
    print('Pipeline finished')



if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)
    print(f'my path is {arguments.path}')
    print(f'my key is {arguments.key}')



