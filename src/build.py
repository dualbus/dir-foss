#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import glob
import sys
import textwrap
import yaml
sys.stdout = codecs.getwriter('utf8')(sys.stdout)

def U(k,h):
    return k in h and h[k] and h[k] is not None
def Ptree(t, indent=4):
    def C(x):
        return isinstance(x, dict) or isinstance(x, list)

    if isinstance(t, dict):
        items = sorted(t.iteritems())
    elif isinstance(t, list):
        items = enumerate(t)
    else:
        raise Exception

    for k, v in items:
        if v is None:
            print '%s* %s:' % (' '*indent, k)
        elif isinstance(v, bool):
            print '%s* %s: %s' % (' '*indent, k, [u'sí', 'no'][v])
        elif C(v):
            print '%s* %s:' % (' '*indent, k)
            Ptree(v, indent+4)
        else:
            print '%s* %s: %s' % (' '*indent, k, v)

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
        print
        Ptree(group['direccion'])
    if U('contacto', group):
        print
        print "Contacto"
        print "--------"
        print
        Ptree(group['contacto'])
    if U('presencia', group):
        print
        print "Presencia"
        print "---------"
        print
        Ptree(group['presencia'])

with open("/dev/stdin") as fp:
    reader = codecs.getreader('utf8')(fp)
    group = yaml.load(reader)
    if 'activo' in group and group['activo']:
        render_rst(group)
