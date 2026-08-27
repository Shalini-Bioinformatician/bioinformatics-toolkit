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
        "GC_content": gc_percent,
        "AT_content": at_percent
  }
dna = "ATGCTCGCGTAGCTGACGTGATGCTGATA"
result = sequence_statistics(dna)
for statistics, Value in result.items():
    if statistics in ["GC_content", "AT_content"]:
        print(f"{statistics}: {Value:.2f}%")
    else:
        print(f"{statistics}: {Value}")
  
