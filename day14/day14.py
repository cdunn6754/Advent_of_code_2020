import os, re
with open(f'{os.getcwd()}/day14/data.txt', 'r') as f:
    data = f.read()

# data = """
# mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
# """
# part 2
# data = """
# mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# """

instructions = []
for i in data.strip().split('\n'):
    ins, mag = i.split(' = ')
    instructions.append((ins, mag))

def apply_mask(dec, mask):
    bin_string = bin(dec)[2:].zfill(36)
    res = []
    for mc, c in zip(mask, bin_string):
        if mc == 'X':
            res.append(c)
            continue
        res.append(mc)
    return int(''.join(res), base=2)

memory = {}
mask = None
mem_pat = re.compile(r'mem\[(\d+)\]')

# Part 1
for ins, mag in instructions:
    if ins.startswith('mask'):
        mask = mag
        continue
    loc = int(re.findall(mem_pat, ins)[0])
    memory[loc] = apply_mask(int(mag), mask)

print("Part 1:", sum(memory.values()))


# Part 2

def apply_mask_2(dec, mask):
    bin_string = bin(dec)[2:].zfill(36)
    res = []
    for mc, c in zip(mask, bin_string):
        if mc == 'X':
            res.append('X')
        elif mc == '0':
            res.append(c)
        else:
            res.append('1')
    return ''.join(res)

def get_bin_list(bin_template):
    """Get rid of them Xes, bin_template is a binary string with X wildcards in it."""
    if len(bin_template) == 0:
        return [[]]
    bin_template = list(bin_template)
    masks = []
    for idx, c in enumerate(bin_template):
        if c != 'X':
            continue
        # Figure out all the combinations for the list from idx + 1 on
        smaller_results = get_bin_list(bin_template[idx+1:])

        for smaller in smaller_results:
            masks.append(bin_template[0:idx] + ['0'] + smaller)
            masks.append(bin_template[0:idx] + ['1'] + smaller)
        # Pretty wierd, only need to worry about the first x
        break
    else:
        return [bin_template]
    return masks

def get_nums_list(location_dec, mask):
    location_template = apply_mask_2(location_dec, mask)
    bin_list = get_bin_list(location_template)
    return [int(''.join(bin_s), 2) for bin_s in bin_list]

memory = {}
mask = None

for ins, mag in instructions:
    if ins.startswith('mask'):
        mask = mag
        continue
    location_dec = int(re.findall(mem_pat, ins)[0])
    locations = get_nums_list(location_dec, mask)
    for location in locations:
        memory[location] = int(mag)
print("Part 2:", sum(memory.values()))
