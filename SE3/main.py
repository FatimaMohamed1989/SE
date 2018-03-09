'''
Created on 9 Mar 2018

@author: user
'''

from light_tester import light_tester
def main(filename, N):
    lights = light_tester(N).lights;
    
    instructions = parse_file(filename);
if __name__ == '__main__':
    pass