#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import logging
import random
from argparse import ArgumentParser

from chibi.file import Chibi_path
from chibi.config import basic_config, load as load_config

from chibi_dl.site import Site

from chibi_dl_elasticsearch.site.nhentai import Nhentai
from chibi_dl_elasticsearch.config import prepare


parser = ArgumentParser(
    description="descargar datos de mangas y animes",
    fromfile_prefix_chars='@'
)

parser.add_argument(
    "sites", nargs='+', metavar="site",
    help="urls de las series que se quieren descargar" )

parser.add_argument(
    "--log_level", dest="log_level", default="INFO",
    help="nivel de log",
)

parser.add_argument(
    "--config_site", type=Chibi_path, dest="config_site",
    help="python, yaml o json archivo con el usuario y password de cada sitio"
)


def main():
    args = parser.parse_args()
    basic_config( args.log_level )

    if args.config_site:
        load_config( args.config_site )

    prepare()

    proccessors = [ Nhentai() ]

    for site in args.sites:
        for proccesor in proccessors:
            if proccesor.append( site ):
                break

    for proccesor in proccessors:
        for item in proccesor:
            item.to_es()
