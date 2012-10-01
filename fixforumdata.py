"""
Usage :
fixforumdata.py <path-to-data>

For example :
<path-to-data> : products/ploneboard_anyxmlimport/inputxml/afpy_zope_forum_zope.data
"""

import re
import os
import sys


#TODO: test libxml2.parseFile(source)

def fix_data(source):
    patterns = ['\x1b.*?m', "\x0b", "\x07"]
    source_file = file(source)
    data = source_file.read()
    source_file.close()
    res = []
    for pattern in patterns:
        res += [(m.start(), pattern) for m in re.finditer(pattern, data)]
    if len(res) == 0:
        print "Your data is already cleaned.\nNothing to do."
        return
    print "%s patterns to fix found" % len(res)
    cleaned_data = data
    for pattern in patterns:
        cleaned_data = re.sub(pattern, '', cleaned_data)
    source_parts = source.split('/')
    source_filename_parts = source_parts[-1].split('.')
    source_new_path = os.path.join('/'.join(source_parts[:-1]),
                                   "%s_old.%s" % (source_filename_parts[0],
                                                  source_filename_parts[1]))
    os.rename(source, source_new_path)
    target = open(source, 'w')
    target.write(cleaned_data)
    target.close()
    print "%s is cleaned now !" % source
    print "(Note: your old data was saved in %s)" % source_new_path
    print "Done"


def main():
    if len(sys.argv) < 2:
        print 'You have to specify the path to the target data to fix'
        sys.exit(1)
    source = sys.argv[1]
    if not os.path.isfile(source):
        print 'No file found here : %s' % source
        sys.exit(2)
    fix_data(source)


if __name__ == '__main__':
    main()
