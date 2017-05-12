#!/usr/bin/python

import sys, getopt
import os

def file_link(input_file, output_file = None, modifier = None, fragment_view = None):
    lines = input_file.readlines()
    type = ''
    typelist = []
    for line in lines:
        if (line.find('<') != -1):
            possible_type = line.split('<')[1].split(' ')[0].replace('<', '').replace('\n', '')
            if (possible_type.find('/') == -1):
                type = possible_type

        if (line.find('android:id=') != -1):
            if (type == 'fragment'):
                print '======================================== WARNING ========================================'
                print "there is a fragment in your code that wasn't linked: {0}".format(
                    line.split('id/')[1].split('"')[0])
                print '=========================================================================================\n\n'
            else:
                typelist.append((type, line.split('id/')[1].split('"')[0]))

    for type, id in typelist:
        if (output_file != None):
            if (modifier != None):
                output_file.write(modifier + ' ')
            output_file.write(type + ' ' + id + ';\n')
        else:
            if (modifier != None):
                sys.stdout.write(modifier + ' ')
            print(type + ' ' + id + ';')

    if (output_file != None):
        output_file.write('\n\n')
    else:
        print '\n\n'

    for type, id in typelist:
        if (output_file != None):
            if (fragment_view != None):
                output_file.write(id + ' = ({0}) {1}.findViewById(R.id.{2});'.format(type, fragment_view, id) + '\n')
            else:
                output_file.write(id + ' = ({0}) findViewById(R.id.{1});'.format(type, id) + '\n')
        else:
            if (fragment_view != None):
                print(id + ' = ({0}) {1}.findViewById(R.id.{2});'.format(type, fragment_view, id))
            else:
                print(id + ' = ({0}) findViewById(R.id.{1});'.format(type, id))



def main(argv):

    if(len(argv) == 0):
        print('missing arguments')
        sys.exit(0)

    output_file = None
    input_file = None
    fragment_view = None
    modifier = None
    directory = None

    try:
        opts, args = getopt.getopt(argv, "hi:o:m:f:a:")
    except getopt.GetoptError:
        print 'android_id_linker.py -i <inputfile> -o <outputfile>'
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print 'android_id_linker.py -i <inputfile> -o <outputfile> -m <modifier> -f <fragment view>'
            sys.exit()
        elif opt == '-i':
            input_file = open(arg)
        elif opt in '-o':
            output_file = open(arg, 'w')
        elif opt == '-m':
            modifier = arg
        elif opt == '-f':
            fragment_view = arg
        elif opt == '-a':
            directory = arg

    if(directory == None and input_file == None):
        print 'missing input file'
        sys.exit(2)

    if(directory != None):
        for filename in os.listdir(directory):
            if(filename.find('.xml') != -1):
                if(output_file == None):
                    print '======================================== FILE : {0} ========================================'.format(filename)
                    file_link(open(directory + '/' + filename), output_file, modifier, fragment_view)
                    print '\n\n'
                else :
                    output_file.write('======================================== FILE : {0} ========================================\n'.format(filename))
                    file_link(open(directory + '/' + filename), output_file, modifier, fragment_view)
                    output_file.write('\n\n')

    print '======================================== FINISHED ========================================'

    # file_link(input_file, output_file, modifier, fragment_view)



if __name__ == "__main__":
    main(sys.argv[1:])