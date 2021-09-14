filenames = ['train.from', 'train.to']
with open('NewTrain.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
