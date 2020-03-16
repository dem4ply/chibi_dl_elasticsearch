#!/usr/bin/env python3
import sys
import fileinput
import json
from elasticsearch_dsl import Document, field, InnerDoc
from elasticsearch_dsl.connections import connections
from chibi.config import configuration


def prepare():
    connections.configure( **configuration.elasticsearch.connections )
    from chibi_dl_elasticsearch.models.nhentai import Manga
    if not Manga._index.exists():
        Manga.init()
