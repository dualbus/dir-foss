#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import glob
import pprint
import sys
import textwrap
import yaml
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

def U(k,h):
    return k in h and h[k] and h[k] is not None

def render_rst(group):
    print group['nombre']
    print len(group['nombre'])*'='
    if U('comentario', group):
        print
        print textwrap.fill(group['comentario'])
    if U('direccion', group):
        print
        print u"Dirección"
        print "---------"
        pprint.pprint(group['direccion'])
    if U('contacto', group):
        print
        print "Contacto"
        print "--------"
        print
        for k, v in sorted(group['contacto'].iteritems()):
            print "    * %s: %s" % (k, v)
    if U('presencia', group):
        print
        print "Presencia"
        print "---------"
        print
        for k, v in sorted(group['presencia'].iteritems()):
            print "    * %s: %s" % (k, v)

    pprint.pprint(group)

with open("/dev/stdin") as fp:
    reader = codecs.getreader('utf8')(fp)
    group = yaml.load(reader)
    if 'activo' in group and group['activo']:
        render_rst(group)
