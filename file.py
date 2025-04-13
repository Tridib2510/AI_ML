def countwords(filePath):
    word_count={}
    with open(filePath,'r')as file:
        for line in file:
            words=line.split()
            for c in words:
                c=c.lower().strip('')
                word_count[c]=word_count.get(c,0)+1
    return word_count

print(countwords('file.txt'))