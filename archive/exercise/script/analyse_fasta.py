#!/usr/bin/env python3

import sys 

def nucl_freq(seq):
  if not isinstance(seq, str):
    raise TypeError("Input must be a string.")
  valid_nucl = {"A", "T", "C", "G"}
  seq_nucl = set(seq)
  if seq_nucl.difference(valid_nucl) != set():
    raise ValueError("Input string must only contain characters A, C, T or G.")
    
  n = len(seq)
  freq = dict()
  for nucl in valid_nucl:
    freq[nucl] = seq.count(nucl)/n
  return freq 

def analyse_fasta(input_file, output_file):
  freq = {}
  
  with open(input_file, 'r') as input:
    for line in input:
      if line.startswith(">"):
        sequence_name = line.strip()[1:]
      else: 
        current_sequence = line.strip()
        freq[sequence_name] = nucl_freq(current_sequence)

  with open(output_file, 'w') as output:
    output.write("Seq A T C G\n")
    for key, value in freq.items():
      output.write(f"{key} {value.get('A')} {value.get('T')} {value.get('C')} {value.get('G')}\n")

  return None


if __name__ == "__main__":  
  if len(sys.argv) != 3:
    print("Usage: python analyse_fasta.py path/to/fasta path/to/output/file")
  else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    analyse_fasta(input_file, output_file)
