__author__ = "MAK"

from constants import SOURCE_MAP


def aggregate_source(factory, search_query):
    source_factory = factory(bool(search_query))
    source = source_factory.make_source_object()
    if search_query:
        source.prepare_payload(query=search_query)
    response = source.get_response()
    result = source.prepare_source_specific_response(response) if response else []
    return result


def aggregate_all(search_query):
    full_result = []
    for source, factory in SOURCE_MAP.items():
        result = aggregate_source(factory, search_query)
        full_result.extend(result)
    return full_result
