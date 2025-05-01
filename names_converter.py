import sys
import pandas as pd


def convert_names(sequence, df):
    id_map = {}
    for i, row in df.iterrows():
        for item in row[1:]: 
            id_map[str(item)] = row[0]  
    
    new_lines = []

    for line in sequence.splitlines():
        if line.startswith('>'):
            identifier = line[1:9].split()[0]
            if identifier in id_map:
                new_line = f">{id_map[identifier]}"
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    return "\n".join(new_lines)


if __name__ == "__main__":
    fasta_path = sys.argv[1]
    df = pd.read_csv(sys.argv[2], sep=',', header=None)

    with open(fasta_path) as f:
        sequence = f.read()
    new_content = convert_names(sequence, df)

    with open(fasta_path.replace(".fasta", "_mod.fasta"), 'w') as f:
        f.write(new_content)
