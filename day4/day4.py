import re

with open('data.txt', 'r') as f:
    data = f.read()

pp_strings = data.strip().split('\n\n')

def format_strings(s):
    res = {}
    field_list = s.replace(' ', '\n').split('\n')
    for field in field_list:
        k, v = field.split(':')
        res[k] = v
    return res

# Part 1
valid_count = 0
for s in pp_strings:
    pp = format_strings(s)
    if len(pp) == 8 or (len(pp) == 7 and pp.get('cid') is None):
        valid_count += 1
print(valid_count)

# Part 2
pats = {
    'byr': re.compile(r'^((1)|2)(?(2)9|0)(?(2)[2-9]|0)(?(2)\d|[0,1,2])$'),
    'iyr': re.compile(r'^20((2)|1)(?(2)0|\d)$'),
    'eyr': re.compile(r'^20((3)|2)(?(2)0|\d)$'),
    'hgt': re.compile(r'^((59|[6]\d|7[0-6])|1[5-8]\d|19[0-3])(?(2)in|cm)$'),
    'hcl': re.compile(r'^#[0-9a-f]{6}$'),
    'ecl': re.compile(r'^amb|blu|brn|gry|grn|hzl|oth$'),
    'pid': re.compile(r'^\d{9}$'),
    'cid': re.compile(r'.*')
}
def validate(pp):
    pp['cid'] = pp.get('cid', '')
    if pp.keys() != pats.keys():
        return False

    for k in pp:
        m = re.match(pats[k], pp[k])
        if not m:
            return False
    return True

valid_count_2 = 0
for s in pp_strings:
    pp = format_strings(s)
    if validate(pp):
        valid_count_2 += 1
print(valid_count_2)
