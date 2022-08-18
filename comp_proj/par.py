import pickle
def fread():
    fin=open("comp_proj/participant.dat",'rb')
    try:
        while True:
            st_rec=pickle.load(fin)
            print(st_rec)
            
    except EOFError:
        fin.close()
fread()