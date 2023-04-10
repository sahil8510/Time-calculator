def add_time(start, duration, day=""):
    lst=start.split()
    a=lst[0].split(":")
    hr1=a[0]
    min1=a[1]
    ampm=lst[1]
    
    b=duration.split(":")
    hr2=b[0]
    min2=b[1]
    hr11=int(hr1)+int(hr2)
    count=0
    
   
    if int(min1)+int(min2)>60:
        finm=(int(min1)+int(min2))-60
        hr11=hr11+1
    else:
        finm=int(min1)+int(min2)
        hr11=hr11

       
    while hr11>=12:
        if hr11>12:
            hr11=hr11-12
            if ampm=="AM":
               ampm="PM"
            elif ampm=="PM":
                ampm='AM'
                count=count+1
            
        elif hr11==12:
            hr11=hr11
            if ampm=="AM":
                ampm="PM"
            elif ampm=="PM":
                ampm='AM'
                count=count+1
            break       
    ndays=None
    if count==0:
        ndays=""
    elif count==1:
        ndays=" (next day)"
    elif count>1:
        ndays=f" ({count} days later)"

    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    finday=""
    for i in days:
       count1=count
       
       fincount=days.index(i)+count1
       while fincount>6:
          difcount=fincount-7
          fincount=0+difcount 

       if i==day.capitalize():
           finday=f", {days[fincount]}"
    
      
   
    hrmn=(str(hr11)+":"+str(finm).zfill(2))
    new_time=hrmn+" "+ampm+finday+str((ndays))

    
    return new_time

print(add_time("8:16 PM", "466:02", "tuesday"))







