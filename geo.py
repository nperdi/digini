from Bio import Entrez

# Set your email here
Entrez.email = "nikosp@uoa.gr"

def search_geo(query, db="gds", retmax=10):
    """
    Search GEO database for ChIP-seq data.

    :param query: Search term
    :param db: Database to search in (default is 'gds')
    :param retmax: Maximum number of results to return
    :return: List of GEO IDs
    """
    # Search GEO
    handle = Entrez.esearch(db=db, term=query, retmax=retmax)
    record = Entrez.read(handle)
    handle.close()

    # Get list of GEO IDs
    geo_ids = record["IdList"]
    return geo_ids

def fetch_geo_summaries(geo_ids, db="gds"):
    """
    Fetch summaries for a list of GEO IDs.

    :param geo_ids: List of GEO IDs
    :param db: Database to search in (default is 'gds')
    :return: List of summaries
    """
    # Fetch summaries
    handle = Entrez.esummary(db=db, id=",".join(geo_ids))
    records = Entrez.read(handle)
    handle.close()

    summaries = []
    for record in records:
        summaries.append({
            "GEO ID": record["Id"],
            "Title": record["title"],
            "Summary": record["summary"],
            "Organism": record["taxon"],
        })
    return summaries

# Example usage
if __name__ == "__main__":
    search_term = "ChIP-seq"
    print("geo_ids")
    geo_ids = search_geo(search_term)
    print("fetch_geo_summaries")
    summaries = fetch_geo_summaries(geo_ids)

    for summary in summaries:
        print(f"GEO ID: {summary['GEO ID']}")
        print(f"Title: {summary['Title']}")
        print(f"Summary: {summary['Summary']}")
        print(f"Organism: {summary['Organism']}")
        print("-" * 40)
