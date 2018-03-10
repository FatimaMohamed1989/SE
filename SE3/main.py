'''
Created on 9 Mar 2018

@author: user
'''

import light_tester
 
def main(filename, N):
    import parser
    light_tester.Light_Tester(N);
    theParser= parser.FileParser("");
    instructions = theParser.parse_file(filename);
    for cmd in instructions:
        light_tester().apply(cmd);
        print(light_tester().count())
if __name__ == '__main__':
    main("filename",6)