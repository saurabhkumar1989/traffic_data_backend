def status(i,num_passe):
    barLength = 20 
    status = ""
    progress = (float(i)/(num_passe-1))
    block = int(round(barLength*progress))
    sys.stdout.write('\r')
    text = "[{0}] Tweets {1}% Saved.".format( "#"*block + "-"*(barLength-block), format(progress*100,".2f"),status)
    sys.stdout.write(text)
    sys.stdout.flush()