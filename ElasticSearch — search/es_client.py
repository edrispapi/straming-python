"""Connecting to Elasticsearch for course search"""
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def search_courses(query):
    res = es.search(index="courses", body={
        "query": {"match": {"title": query}}
    })
    return res['hits']['hits']
