import requests
import xml.etree.ElementTree as ET
import json

def fetch_gene_info(gene_id, output_file='gene_info.json'):
    # Endpoint base
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    # Parameters
    params = {
        "db": "gene",
        "id": gene_id,
        "retmode": "xml"
    }

    # API Request
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error in petition:", response.status_code)
        return

    # Parse XML
    root = ET.fromstring(response.text)
    
    # XML Data
    gene_data = {}
    gene = root.find(".//Entrezgene")
    if gene is not None:
        gene_data['Gene_ID'] = int(gene.findtext(".//Gene-track_geneid"))
        gene_data['Gene_Symbol'] = gene.findtext(".//Gene-ref_locus", default="None")
        gene_data['Description'] = gene.findtext(".//Gene-ref_desc", default="None")
        # gene_data['Organism'] = gene.findtext(".//Org-ref_taxname")
        gene_data['Chromosome_Location'] = gene.findtext(".//Gene-ref_maploc", default="None")
        taxonomy_id = gene.findtext(".//Org-ref_db/Dbtag[Dbtag_db='taxon']/Dbtag_tag/Object-id/Object-id_id")
        gene_data['Taxonomy_ID'] = int(taxonomy_id) if taxonomy_id else None
        gene_data['Summary'] = gene.findtext(".//Entrezgene_summary", default="None")
    
    # Save as json
    with open(output_file, "w", encoding='utf-8') as f:
        json.dump(gene_data, f, indent=4, ensure_ascii=False)
    
    print(f"Datos guardados en {output_file}")

'''
gene_ID = input('Gene ID from NCBI gene database: ')

# Asks gene ID
fetch_gene_info(gene_ID)
'''
