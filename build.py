
### Copyright 2017 Christopher Fuller
###
### Licensed under the Apache License, Version 2.0 (the "License");
### you may not use this file except in compliance with the License.
### You may obtain a copy of the License at
###
###     http://www.apache.org/licenses/LICENSE-2.0
###
### Unless required by applicable law or agreed to in writing, software
### distributed under the License is distributed on an "AS IS" BASIS,
### WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
### See the License for the specific language governing permissions and
### limitations under the License.
############################################################################
############################################################################


# sorry, just not a fan of Bash/Makefile programming
# also, not tested in Python v3, but that'll get fixed soon

# expects to be run from project's root

# decent command line validation, but could still blow up messily
# if the input SVG isn't Just So.

SVG = 'src/sign.svg'

import sys

from string import Template

import xml.etree.ElementTree as ET

TMPLS = {
   'outer'  : [ Template(s) if s else None for s in (
      'inkscape -Cj -i $id -y 255 --export-pdf=tmp/${name}1.pdf $svg',
      'mutool poster -x 2 -y 2 tmp/${name}1.pdf tmp/tiles.pdf',
      'pdftk tmp/tiles.pdf burst output tmp/tile%d1.pdf',
      'pdftk tmp/tile21.pdf background src/copyleft.pdf output tmp/tile22.pdf',
      '',
      'pdftk tmp/tile14.pdf tmp/tile25.pdf tmp/tile34.pdf tmp/tile44.pdf cat output output/${name}.pdf',
      'pdfnup --nup 2x2 --outfile tmp/${name}2.pdf tmp/tile11.pdf tmp/tile22.pdf tmp/tile31.pdf tmp/tile41.pdf',
      'convert tmp/${name}2.pdf -geometry 440x340 output/${name}.png',
      'zip -n .png output/sign.zip output/${name}.pdf output/${name}.png',
   ) ],

   'inner_why_not_this_work' : [ Template(s) for s in (
      './pdfScale.sh -s 0.9 tmp/tile${i}${j}.pdf tmp/tile${i}${k}.pdf',
   ) ],

   'inner'  : [ Template(s) for s in (
      'pdftk  tmp/tile${i}${j}.pdf rotate 1east output tmp/tile${i}${k}.pdf',
      'pdf2ps tmp/tile${i}${k}.pdf tmp/tile${i}${k}.ps',
      'pstops -p letter "@0.9(0.425in,0.55in)" tmp/tile${i}${k}.ps tmp/tile${i}${m}.ps',
      'ps2pdf tmp/tile${i}${m}.ps tmp/tile${i}${m}.pdf',
      'pdftk  tmp/tile${i}${m}.pdf rotate 1west output tmp/tile${i}${n}.pdf'
   ) ]
}

#TMPLS['outer'][1] = Template('mutool poster -x 2 -y 2 tmp/${name}.pdf tmp/tiles.pdf')
#TMPLS['outer'][1] = Template('pdfposter     -p2x2Let  tmp/${name}.pdf tmp/tiles.pdf')

def nonsplz(s):
   t = ''
   for c in s[::-1]:
      if c == '}':
         break
      else:
         t = c+t

   return t


if __name__ == '__main__':

   argv  = sys.argv[1:]

   sides_in = argv[:2]
   sides    = []

   while sides_in:
      if sides_in[-1] in ('front', 'back'):
         sides.append(sides_in[-1])

      sides_in.pop()

   if len(sides) == 2 and sides[0] == sides[1]:
      sides.pop()

   if not sides:
      sides = ('front', 'back')

   tree = ET.parse(SVG)
   root = tree.getroot()

   IDs = [ e.attrib['id'] for e in root.iter() if nonsplz(e.tag) == 'g' ]

   layers = dict(zip(('back', 'front'), IDs))
   kwargs = dict(svg=SVG)

   print 'mkdir -p tmp'

   for name in sides:
      kwargs['name'] = name
      kwargs[  'id'] = layers[name]
      for tplo in TMPLS['outer']:
         if tplo:
            print tplo.substitute(**kwargs)
         else:
            for i,j,k,m,n in zip(
               (1,2,3,4), (1,2,1,1), (2,3,2,2), (3,4,3,3), (4,5,4,4) ):
               for tpli in TMPLS['inner']:
                  print tpli.substitute(i=i, j=j, k=k, m=m, n=n)


   print 'rm -f tmp/*'
