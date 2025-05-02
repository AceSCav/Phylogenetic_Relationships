# Phylogenetic_Relationships

This project performs an automated phylogenetic analysis of nucleotide sequences retrieved from NCBI. The pipeline includes sequence alignment, concatenation, phylogenetic inference (maximum likelihood, maximum parsimony, and Bayesian), and formatting for visualization.

---

## 🔧 Requirements

### Software and Tools
- [MAFFT v7.505](https://mafft.cbrc.jp/alignment/software/) – Multiple sequence alignment.
- [ModelTest-NG v0.1.7](https://github.com/ddarriba/modeltest) – Substitution model selection.
- [RAxML-NG v1.2.2](https://github.com/amkozlov/raxml-ng) – Maximum likelihood phylogenetic inference.
- [MPBoot](https://github.com/dominik-kubanek/mpboot) – Maximum parsimony inference.
- [MrBayes](http://nbisweden.github.io/MrBayes/) – Bayesian phylogenetic inference.
- [FigTree v1.4.4](http://tree.bio.ed.ac.uk/software/figtree/) – Phylogenetic tree visualization.
- [FASTA2NEX](https://github.com/Rendrick27/FASTA2NEX) – FASTA to NEXUS converter.  
  > *Note:* The original code was modified to better fit the workflow of this pipeline. The adapted version is available in this repository.
- [Concatenate Fasta Tool](https://github.com/StarGazerNex/Phylogeny/blob/main/Code/concatenate_fasta) – Concatenate multiple FASTA files.

### Python Libraries
- `Biopython`
- `pandas`

Install with:
```bash
pip install biopython pandas
```
or 
```bash
micromamba install -n myenv biopython pandas -c conda-forge
```

---

## 📂 Pipeline Structure

### 1. Download and Align Sequences
```bash
python3 Fasta_Entrez.py 'nucleotide' 'ACC_RANGE[accn]' 1000
mv algn_*.fasta algn_NAME.fasta
```

### 2. Convert Sequence IDs to Names
```bash
python3 names_converter.py algn_NAME.fasta ids_names.csv
mv algn_NAME_mod.fasta algn_NAME.fasta
```

### 3. Concatenate FASTA Files
```bash
mkdir concat_seq
cp algn_*.fasta ./concat_seq/
python3 Concatenate.py concat_seq/ concat_os.fasta
rm -rf concat_seq/
```

### 4. Maximum Parsimony Inference (MPBoot)
```bash
mpboot -s algn_NAME.fasta -pre max_parsimony_NAME -bb 4000
```

### 5. Evolutionary Model Selection (ModelTest-NG)
```bash
modeltest-ng -i algn_NAME.fasta
```

### 6. Maximum Likelihood Inference (RAxML-NG)
```bash
raxml-ng --msa algn_NAME.fasta --model MODEL --prefix NAME --threads 5 --seed 2
raxml-ng --bootstrap --msa algn_NAME.fasta --model MODEL --prefix NAME --seed 2 --threads 5
raxml-ng --support --tree NAME.raxml.bestTree --bs-trees NAME.raxml.bootstraps --prefix NAME --threads 5
```

### 7. Convert to NEXUS Format
```bash
python3 fasta2nex.py algn_NAME.fasta > algn_NAME.nexus
```

### 8. Bayesian Inference (MrBayes)
```bash
mb -i algn_NAME.nexus
```

---

## Notes
- Replace `NAME` with actual dataset names such as `adh1`, `os1283`, `os9971`, `os17357`, etc.
- The evolutionary models used in RAxML-NG must be chosen based on the output from `modeltest-ng`.
- It is recommended to execute each block using shell scripts or within a controlled environment (e.g., Micromamba).

---

## Collaborators
Aleff Cavalcante  
Alexandre Soares  
Ana Fernando  
Ravi Silva  

## Credits
[Rendrick Carreira](https://github.com/Rendrick27) for providing the code to transform FASTA to NEXUS
