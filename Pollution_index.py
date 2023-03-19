index_rises = input ("Enter The daily hazard index : ")
index =float (index_rises)
if index > 275:
    print ("second stage smog alert")
elif index > 200:
    print ("first stage smog alert")
elif index > 100:
    print ("unhealthful")

