ants_far = open('ants-far2.csv', 'r', encoding='utf-8')
ants_middle = open('ants-middle2.csv', 'r', encoding='utf-8')
ants_near = open('ants-near2.csv', 'r', encoding='utf-8')
ants_avg = open('ants-avg.csv', 'w', encoding='utf-8')

af = ants_far.readline()
af = af.split("\t")
am = ants_middle.readline()
am = am.split("\t")
an = ants_near.readline()
an = an.split("\t")


while af != [''] :
    count = 0
    print("af : ",af)
    count = int(af[1]) + int(am[1]) + int(an[1])
    ants_avg.write('{}\t'.format(af[0])+str(count/3)+'\n')    
    af = ants_far.readline()
    af = af.split("\t")
    am = ants_middle.readline()
    am = am.split("\t")
    an = ants_near.readline()
    an = an.split("\t")

#ants_avg.write('{}\t'.format(af[)+str(count/3)+'\n')    
ants_far.close()    
ants_middle.close()
ants_near.close()
ants_avg.close()
