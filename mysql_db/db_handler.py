import json
import mysql.connector

def insert_data_db(host, port, user, password, database):
    # Load JSON file (single object)
    with open('gene_info.json', 'r') as f:
        gene = json.load(f)

    # Connect to MySQL
    conn = mysql.connector.connect(
       # host='localhost',
       # port=3306,
       # user='alumno',
       # password='Pce@6ooAdH',
       # database='SIC2025Grupo11'  
        
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        auth_plugin='mysql_native_password'
    )

    cursor = conn.cursor()

    # Insert the data
    cursor.execute("""
        INSERT INTO SIC2025Grupo11.Gen (Gene_ID, Gene_Symbol, Description, Chromosome_Location, Taxonomy_ID, Summary)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        gene['Gene_ID'],
        gene['Gene_Symbol'],
        gene['Description'],
        gene['Chromosome_Location'],
        gene['Taxonomy_ID'],
        gene['Summary']
    ))

    # Commit and close
    conn.commit()
    cursor.close()
    conn.close()
