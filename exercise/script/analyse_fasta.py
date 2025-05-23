#!/usr/bin/env python3

import sys 

def nucl_freq(seq):
  valid_nucl = ["A", "T", "C", "G"]

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
