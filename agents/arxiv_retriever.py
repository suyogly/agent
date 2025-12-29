from arxiv import Client, Search, SortCriterion

client = Client()

def arxiv_search(query):
    search = Search(
        query=query,
        max_results=10,
        sort_by=SortCriterion.Relevance
    )

    res = client.results(search)

    for r in res:
        return r.title, r.pdf_url, r.authors, r.published