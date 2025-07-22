text='968-Maria, ( D@t@ Engineer ) ;;  27y  '

print(
    text.strip().
    replace("968","name").
    replace("-",": ").
    lower().
    replace(","," |").
    replace("("," role:").
    replace("@","a").
    replace(')',' | age').
    replace(";;",":").
    replace(' 27y','27y'))