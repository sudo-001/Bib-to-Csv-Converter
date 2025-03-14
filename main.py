import bibtexparser
import csv

# Fonction pour lire le fichier .bib et le parser
def read_bib_file(bib_file):
    with open(bib_file, 'r') as file:
        bib_data = bibtexparser.load(file)
    return bib_data.entries

# Fonction pour écrire les données dans un fichier .csv
def write_csv_file(entries, output_csv):
    # Définir les en-têtes du CSV
    headers = ['ID', 'Author', 'Title', 'Journal', 'Volume', 'Issue', 'Year', 'DOI', 'ISSN', 'Abstract']
    
    with open(output_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        
        for entry in entries:
            # Extraire les informations pour chaque entrée .bib
            row = {
                'ID': entry.get('ID', ''),
                'Author': entry.get('author', ''),
                'Title': entry.get('title', ''),
                'Journal': entry.get('journal', ''),
                'Volume': entry.get('volume', ''),
                'Issue': entry.get('issue', ''),
                'Year': entry.get('year', ''),
                'DOI': entry.get('doi', ''),
                'ISSN': entry.get('issn', ''),
                'Abstract': entry.get('abstract', '')
            }
            writer.writerow(row)

# Nom du fichier .bib d'entrée et du fichier .csv de sortie
input_bib_file = '../dataset/export.bib'
output_csv_file = '../dataset/dataset.csv'

# Lire le fichier .bib, puis l'écrire dans le fichier .csv
entries = read_bib_file(input_bib_file)
write_csv_file(entries, output_csv_file)

print(f"Le fichier {input_bib_file} a été converti en {output_csv_file}")