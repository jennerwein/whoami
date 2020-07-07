
def zeitdauer(time):

    def norm2(zahl):
        return(("00"+str(zahl))[-2:])

    gesamtzeit=time
    dauer=''
    # Tage
    days = time // (24 * 3600)
    if days == 1:
        dauer=dauer+str(days)+' day '
    if days > 1:
        dauer=dauer+str(days)+' days '
    #Stunden
    time = time % (24 * 3600)
    hours = time // 3600
    if hours == 1:
        dauer=dauer+str(hours)+' hour '
    if hours > 1:
        dauer=dauer+str(hours)+' hours '
    #Minuten
    time %= 3600
    minutes = time // 60
    if minutes >= 1:
        dauer=dauer+str(minutes)+' min '
    # Sekunden
    time %= 60
    seconds = time
    dauer=dauer+str(seconds)+' sec'
    
    ##### Testausdruck
    # print("d:h:m:s-> %d:%d:%d:%d" % (days, hours, minutes, seconds))

    return dauer

##############################################################################
if __name__ == '__main__':

    time = int(2*60*60+7)
    print(zeitdauer(time))
