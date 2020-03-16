#!/usr/bin/env python3
import sys
import fileinput
import json
from elasticsearch_dsl import Document, field, InnerDoc
from elasticsearch_dsl.connections import connections
import logging


logger = logging.getLogger( 'chibi_dl_elasticsearch.models.nhentai' )


connections.configure(
    default={
        'host': 'waifus',
        'port': 80
    } )


from elasticsearch_dsl import analyzer, tokenizer

tag = analyzer(
    'tag',
    tokenizer=tokenizer( 'trigram', 'nGram', min_gram=3, max_gram=3 ),
    filter=[ "lowercase", ],
)

titles = analyzer(
    'titles',
    tokenizer=tokenizer( 'trigram', 'nGram', min_gram=3, max_gram=5 ),
    filter=[ "lowercase", ],
)

titles_space = analyzer(
    'titles_space',
    tokenizer='whitespace',
    filter=[ "lowercase", ],
)


class Tag( InnerDoc ):
    artists = field.Text(
        analyzer=tag, multi=True,
        fields={ 'keyword': field.Keyword( multi=True ) } )
    categories = field.Text(
        analyzer=tag, multi=True,
        fields={ 'keyword': field.Keyword( multi=True ) } )
    characters = field.Text(
        analyzer=tag, multi=True,
        fields={ 'keyword': field.Keyword( multi=True ) } )
    groups = field.Text(
        analyzer=tag, multi=True,
        fields={ 'keyword': field.Keyword( multi=True ) } )
    languages = field.Text(
        analyzer=tag, multi=True,
        fields={ 'keyword': field.Keyword( multi=True ) } )
    parodies = field.Text(
        analyzer=tag, multi=True,
        fields={ 'keyword': field.Keyword( multi=True ) } )
    tags = field.Text(
        analyzer=tag, multi=True,
        fields={ 'keyword': field.Keyword( multi=True ) } )


class Manga( Document ):
    title = field.Text()
    title= field.Text(
        analyzer=titles, multi=True,
        fields={
            'space': field.Text( analyzer=titles_space, multi=True ),
            'keyword': field.Keyword( multi=True ),
        } )
    tags = field.Object( Tag )
    upload_at = field.Date()
    scan_at = field.Date()

    url = field.Keyword()
    cover_url = field.Keyword()
    images_urls = field.Keyword( multi=True )
    images_len = field.Integer()

    class Index:
        name = 'nhentai__mangas'
        settings = { 'number_of_shards': 2, 'number_of_replicas': 1 }

    @classmethod
    def url_is_scaned( cls, url ):
        logger.info( f"buscando manga {url}" )
        if cls.search().filter( "term", url=url ).count() > 0:
            return True
        return False
