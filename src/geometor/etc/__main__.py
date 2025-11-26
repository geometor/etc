import argparse
import os
import glob
from pathlib import Path
from .ingest import ingest_folder
from .parser import parse_center
from .transform import generate_rst_files

def main():
    parser = argparse.ArgumentParser(description="GEOMETOR ETC Pipeline")
    parser.add_argument('--input', '-i', default='etc/source', help="Input directory containing HTML files")
    parser.add_argument('--split-dir', '-s', default='etc/split', help="Directory to store split HTML files")
    parser.add_argument('--output', '-o', default='docsrc/centers', help="Output directory for RST files")
    parser.add_argument('--limit', '-l', type=int, default=0, help="Limit the number of entries to process (0 for all)")
    parser.add_argument('--skip-ingest', action='store_true', help="Skip the ingestion step")
    
    args = parser.parse_args()
    
    # 1. Ingest / Split
    if not args.skip_ingest:
        print(f"Splitting HTML files from {args.input} to {args.split_dir}...")
        ingest_folder(args.input, args.split_dir)
    else:
        print("Skipping ingestion step.")
    
    from .glossary import extract_glossary_terms, generate_glossary_rst
    
    # 1.5 Glossary
    print("Processing glossary...")
    glossary_file = os.path.join(args.input, "GLOSSARY, a support page for ENCYCLOPEDIA TRIANGLE CENTERS.html")
    glossary_terms = {}
    if os.path.exists(glossary_file):
        with open(glossary_file, 'r', encoding='utf-8') as f:
            glossary_content = f.read()
        glossary_terms = extract_glossary_terms(glossary_content)
        print(f"Found {len(glossary_terms)} glossary terms.")
        
        # Generate glossary.rst
        glossary_rst = generate_glossary_rst(glossary_terms)
        # Assuming output dir is docsrc/centers, we probably want glossary in docsrc/
        # But args.output is docsrc/centers. Let's assume docsrc is parent.
        docsrc_dir = os.path.dirname(args.output.rstrip('/'))
        glossary_output_path = os.path.join(docsrc_dir, "glossary.rst")
        with open(glossary_output_path, 'w', encoding='utf-8') as f:
            f.write(glossary_rst)
        print(f"Generated {glossary_output_path}")
    else:
        print(f"Glossary file not found at {glossary_file}")

    # 2. Parse
    print(f"Parsing files in {args.split_dir}...")
    # Filter for x-*.html to ensure we process the identified centers
    split_files = sorted(glob.glob(os.path.join(args.split_dir, 'x-*.html')))
    print(f"Found {len(split_files)} center files in split directory.")
    
    centers = []
    count = 0
    for file_path in split_files:
        if args.limit > 0 and count >= args.limit:
            break
            
        # print(f"Parsing {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        center_data = parse_center(content)
        if center_data:
            centers.append(center_data)
            count += 1
            print(f"Parsed {file_path} -> {center_data['key']}")
        else:
            print(f"Failed to parse {file_path}")

            
    print(f"Parsed {len(centers)} centers.")
    
    # 3. Transform
    print(f"Generating RST files in {args.output}...")
    generate_rst_files(centers, args.output, glossary_terms=list(glossary_terms.keys()))
    print("Done.")

if __name__ == '__main__':
    main()