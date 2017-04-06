ants_far = open('ants-far.csv', 'r', encoding='utf-8')
ants_middle = open('ants-middle.csv', 'r', encoding='utf-8')
ants_near = open('ants-near.csv', 'r', encoding='utf-8')
ants_avg = open('ants-avg.csv', 'w', encoding='utf-8')

af = ants_far.readline()
am = ants_middle.readline()
an = ants_near.readline()

while len(af) != 0 :
    count = 0
    if af[1] == '\t' :
        count = int(af[2:]) + int(am[2:]) + int(am[3:])
    else :
        count = int(af[3:]) + int(am[3:]) + int(am[3:])
    ants_avg.write(str(count/3)+'\n')    
    af = ants_far.readline()
    am = ants_middle.readline()
    an = ants_near.readline()

ants_far.close()
ants_middle.close()
ants_near.close()
ants_avg.close()
