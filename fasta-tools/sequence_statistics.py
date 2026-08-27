def sequence_statistics(sequence):
  sequence=sequence.upper().replace(",", "").replace("/n", "")
  a_count = sequence.count("A")
  t_count = sequence.count("T")
  g_count = sequence.count("G")
  c_count = sequence.count("C")
  n_count = sequence.count("n")
  seq_length = len(sequence)
  if seq_length > 0:
    gc_percent = ((g_count + c_count)/seq_length) * 100
    at_percent = ((a_count + t_count)/seq_length) * 100
  else:
    gc_percent = 0
    at_percent = 0
  return {
    "Length": seq_length,
        "A": a_count,
        "T": t_count,
        "G": g_count,
        "C": c_count,
        "N": n_count,
        "GC_content": gc_content,
        "AT_content": at_content
  }
dna = "ATGCTCGCGTAGCTGACGTGATGCTGATA"
result = sequence_statistics(dna)
for statistiics, Value in result.items():
  if statistic in ["GC_content", "AT_content"]:
        print(f"{statistic}: {value:.2f}%")
    else:
        print(f"{statistic}: {value}")
  
