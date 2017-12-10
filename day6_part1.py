with open('input_d6.txt', 'rU') as f:
  mem_banks = f.read().split('\t')

mem_banks = map(int, mem_banks)
seen_configs = [mem_banks[:]]
count = 0
same_config = False
print mem_banks


def redistribute(num_times, memory_banks, index_start):
  mem_banks_copy = memory_banks[:]
  mem_banks_copy[index_start] = 0
  for i in range(1, num_times + 1):
    mem_banks_copy[(index_start+i) % len(mem_banks_copy)] += 1
  return mem_banks_copy


while same_config == False:

  largest = max(seen_configs[-1])
  index_largest = seen_configs[-1].index(largest)

  new_config = redistribute(largest, seen_configs[-1], index_largest)

  count += 1


  if new_config in seen_configs:
    same_config = True
    break
  else:
    seen_configs.append(new_config)

print count
