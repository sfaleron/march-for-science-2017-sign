
Overview
========

Takes a two layer 22x17 inch landscape SVG and creates eight letter-sized tiles that fit neatly onto a 24x18 substrate, such as a sheet of corrugated plastic. The nams of the layers are not relevant, but are always referenced as "front" and "back" on the command line.

single sided signs can be done, but it's a little half-baked. use "back" on the command line. defaults are still two-sided. any remaining "front" content will remain (separately) in the output directory and zip file unless manually removed. better support for single-layer SVGs may show up in the future. or not.

obtain tiles
============

In case you only want the tiles, the latest release, with tiles and previews only can be downloaded from:

https://github.com/sfaleron/marchsign2017/releases/


tweak/mold to your will and rebuild
-----------------------------------

update the copyleft statement (there's a makefile for this, at least) if you change the text or otherwise make significant changes. you can even fork the repository to make it easy to share with others, if that suits you.

This works on Linux, and presumably the various BSDs. I would guess that MacOS and Cygwin also, but that seems less certain.

dependencies (not including dependencies-of-dependencies; I'll let you package manager figure that out): python (recent v2 or v3), inkscape, pdftk, mutool, imagemagick, ghostscript, xpdf/poppler...

if I discover that I've missed any, I'll update this list. it is a long list, but they are pretty standard on a desktop installation with document processing tools included, except the more graphics-oriented packages and mutool.

python build.py [front] [back] | sh

only the first two parameters are used. not specifying any sides will invoke a default of both. invalid parameters are ignored. if the first two are equal, only one pass is made. if parameters are provided but none are valid, the default is invoked.

the rest
========

get some generic 24x18 in corrugated plastic sign board, probably any of the big box hardware stores will work, or someplace that specializes in signage.

might want to do a test print of either side in b/w to check that the margins work out, since printers aren't going to all line up the same way.

attach with double sticky tape, thumbtacks, or whatever floats your boat.

final note
==========

I intend to make an unnecessarily elaborate mounting system just for kicks, but you can also hold overhead, or it at chest height, flipping every once in a while to expose both sides.

Perhaps not in time for the intended event. It's easily updatable for future uses, though!
