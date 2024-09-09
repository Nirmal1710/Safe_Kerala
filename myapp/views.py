from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Max
from django.forms.models import model_to_dict
from myapp.models import *
from datetime import time, datetime
from django.core.serializers import serialize
import cv2
import face_recognition
import base64
import os

date_today=datetime.now().date()

def login(request):
    return render(request,"loginindex.html")

def login1(request):
    return render(request,"loginindex.html")


def login_post(request):

    uname =request.POST['textfield']
    password=request.POST['textfield2']
    qry=Login.objects.filter(username=uname,password=password)
    if qry.exists():
        res=Login.objects.get(username=uname,password=password)
        request.session['lid']=res.id
        if res.type == 'admin':
            return render(request,"admin/home.html")
        elif res.type == 'police':
            return render(request,"police_station/home.html")
        else:
            return HttpResponse('''<script>alert("Invalid");window.location='/myapp/'</script>''')
    else:
        return HttpResponse('''<script>alert("Invalid");window.location='/myapp/'</script>''')

def changepassword(request):
    return render(request,"admin/changepassword.html")


def change_pswrdpost(request):
    curp = request.POST['textfield']
    newp = request.POST['textfield2']
    cnfp = request.POST['textfield3']
    qry = Login.objects.filter(id=request.session['lid'], password=curp)
    if qry.exists():
        if newp==cnfp:
            Login.objects.filter(id=request.session['lid'], password=curp).update(password=newp)
            return HttpResponse('''<script>alert('Password Changed Success');window.location='/myapp/'</script>''')
        else:
            return HttpResponse('''<script>alert('Password Mismatch!');window.location='/myapp/changepassword'</script>''')
    else:
        return HttpResponse('''<script>alert('Current password must be valid!');window.location='/myapp/changepassword'</script>''')


def addpolice(request):
    return render(request,"admin/addpolice.html")


def addpolice_post(request):
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    district=request.POST['textfield7']
    pincode=request.POST['textfield6']
    import random

    rr=str(random.randint(0000,10000))
    ll=Login()
    ll.username=email
    ll.password=rr
    ll.type="police"
    ll.save()

    pp=PoliceStation()
    pp.LOGIN_id=ll.id
    pp.station_name=name
    pp.email=email
    pp.phone=phone
    pp.place=place
    pp.post=post
    pp.district=district
    pp.pincode=pincode
    pp.save()
    return HttpResponse("<script>alert('Information added successfully');window.location='/myapp/addpolice'</script>")


def viewpolice(request):
    res=PoliceStation.objects.all()
    return render(request,"admin/viewpolice.html",{'data':res})


# def searchpolice(request):
#     name=request.POST['textfield']
#     res=PoliceStation.objects.filter(station_name__icontains=name)
#     return render("admin/viewpolice.html",{'data':res})
def searchpolice(request):
    name = request.POST['textfield']
    res = PoliceStation.objects.filter(station_name__icontains=name)
    return render(request, "admin/viewpolice.html", {'data': res})

def deletepolice(request,id):
    PoliceStation.objects.filter(id=id).delete()
    return viewpolice(request)

def editpolice(request,id):
    res = PoliceStation.objects.get(id=id)
    return render(request,"admin/editpolice.html",{'data':res})

def editpolice_post(request):

    pid=request.POST['p_id']
    sname=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    place=request.POST['textfield4']
    post=request.POST['textfield5']
    district=request.POST['select']
    pin=request.POST['textfield6']
    PoliceStation.objects.filter(id=pid).update(station_name=sname,email=email,phone=phone,place=place,post=post,district=district,pincode=pin)

    return HttpResponse("<script>alert('Info updated successfully');window.location='/myapp/viewpolice'</script>")


def addnotification(request):
    return render(request,"admin/addnotification.html")

def addnotification_post(request):
    notification=request.POST['textarea']
    nn=Notification()
    nn.date=date_today
    nn.notification=notification
    nn.save()
    return HttpResponse("<script>alert('Info added successfully');window.location='/myapp/addnotification'</script>")

def viewnotification(request):
    res=Notification.objects.all()
    return render(request,"admin/viewnotification.html",{"data":res})

def searchnotification(request):

    date1=request.POST['textfield']
    date2=request.POST['textfield2']
    res = Notification.objects.filter(date__range=(date1, date2))
    print(res)
    return  render(request,"admin/viewnotification.html",{"data":res})


def deletenotification(request,id):
    Notification.objects.filter(id=id).delete()
    return viewnotification(request)


def editnotification(request,id):
    res=Notification.objects.get(id=id)
    return render(request,"admin/editnotification.html",{"data":res})


def editnotification_post(request):

    nid=request.POST['N_id']
    noti=request.POST['textarea']
    Notification.objects.filter(id=nid).update(notification=noti)

    return HttpResponse("<script>alert('Information updated successfully');window.location='/myapp/viewnotification'</script>")

def viewlabour1(request):
    res=Labour.objects.filter(status="pending")
    return render(request,"admin/viewlabour1.html", {"data":res})


def aaprovelabor(request,id):
    newnumber=0
    ff = Labour.objects.filter(status='Approved').aggregate(m=Max('idcard_no'))
    if ff["m"] is  None:
        newnumber = "00000001"
        print(newnumber)
    else:
        number=ff["m"]
        if str(number)=="0":
            newnumber="00000001"
            print(newnumber)
        else:
            new = int(number) + 1
            newnumber = str(new)
            print(newnumber,"-----------")

            if len(newnumber)==1:
                newnumber="0000000"+newnumber
            elif len(newnumber)==2:
                newnumber="000000"+newnumber
            elif len(newnumber)==3:
                newnumber="00000"+newnumber
            elif len(newnumber)==4:
                newnumber="0000"+newnumber
            elif len(newnumber)==5:
                newnumber="000"+newnumber
            elif len(newnumber)==6:
                newnumber="00"+newnumber
            elif len(newnumber) == 7:
                newnumber = "0" + newnumber
            elif len(newnumber) == 8:
                newnumber =  newnumber
            else:
                newnumber=newnumber
    Labour.objects.filter(id=id).update(status='Approved',idcard_no=newnumber)
    v=generateqr(id)
    return viewlabour1(request)

def generateqr(labourid):
    import qrcode
    img = qrcode.make(labourid)
    type(img)  # qrcode.image.pil.PilImage
    from datetime import datetime  
    p="C:\\Users\\nirma\\OneDrive\\Documents\\project\\SafeKeralamain\\SafeKerala[1]\\SafeKerala\\media\\qrcodes\\"
    s=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    img.save(p+s)
    s="/static/qrcodes/"+ s
    return "ok"

def rejectlabor(request,id):
    Login.objects.filter(id=id).update(type='Reject')
    Labour.objects.filter(LOGIN_id=id).update(status='Reject')
    return viewlabour1(request)


def viewlabour(request):
    res=Labour.objects.filter(status='Approved')
    return render(request,"admin/view labour.html",{"data":res})


def viewcriminallist(request):
    res=Criminal.objects.all()
    return render(request,"admin/view criminal list.html",{"data":res})


def searchcriminal(request):
    name=request.POST['textfield']
    res = Criminal.objects.filter(name__icontains=name)
    return render(request, "admin/view criminal list.html", {"data": res})


def viewcomplaint(request):
    res=Complaints.objects.all()
    return render(request,"admin/viewcomplaint.html",{"data":res})


def viewfeedback(request):
    res=Feedback.objects.all()
    return render(request,"admin/view feedback.html",{"data":res})


def searchfeedback(request):
    name=request.POST["textfield"]
    res = Feedback.objects.filter(USER__name__icontains=name)
    return render(request, "admin/view feedback.html", {"data": res})


def home1(request):
    return  render(request,"police_station/home.html")


def addcriminallist(request):
    return render(request,"police_station/addcriminallist.html")


def addcriminallist_post(request):
    name=request.POST['textfield']
    gender=request.POST['radio']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    district=request.POST['textfield4']
    state=request.POST['textfield5']
    dob=request.POST['textfield6']
    photo1=request.FILES['fileField']
    photo2=request.FILES['fileField2']
    adar=request.POST['textfield7']
    fprint=request.FILES['fileField3']

    from datetime import datetime

    d1 = "criminals/criminal1/"+datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
    fs1 = FileSystemStorage()
    fs1.save(d1, photo1)
    path1 = fs1.url(d1)

    d2 = "criminals/criminal2/" + datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
    fs2 = FileSystemStorage()
    fs2.save(d2, photo2)
    path2 = fs2.url(d2)

    # d3 = "criminals/criminal2/" + datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
    d3 = "criminals/finger/" + datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
    fs3 = FileSystemStorage()
    fs3.save(d3, fprint)
    path3 = fs3.url(d3)

    cc=Criminal()
    cc.name=name
    cc.photo1=path1
    cc.photo2=path2
    cc.gender=gender
    cc.place=place
    cc.district=district
    cc.state=state
    cc.post=post
    cc.dob=dob
    cc.adarcard=adar
    cc.fingerprint=path3
    cc.save()
    return HttpResponse("<script>alert('Information added successfully');window.location='/myapp/addcriminallist'</script>")


def viewcriminal1(request):
    res=Criminal.objects.all()
    return render(request,"police_station/viewcriminallist.html",{"data":res})


def searchcriminal1(request):
    name=request.POST['textfield']
    res = Criminal.objects.filter(name__icontains=name)
    return render(request, "police_station/viewcriminallist.html", {"data": res})

def deletecriminal(request,id):
    Criminal.objects.filter(id=id).delete()
    return viewcriminal1(request)


def editcriminallist(request,id):
    res=Criminal.objects.get(id=id)
    return  render(request,"police_station/editcriminallist.html", {"data": res})



def editcriminallist_post(request):
    cid=request.POST['c_id']
    name=request.POST['textfield']
    gender=request.POST['radio']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    district=request.POST['text']
    state=request.POST['textfield4']
    dob=request.POST['textfield5']

    adar=request.POST['textfield7']

    cc = Criminal.objects.get(id=cid)
    cc.name = name
    cc.gender = gender
    cc.place = place
    cc.district = district
    cc.state = state
    cc.post = post
    cc.dob = dob
    cc.adarcard = adar

    from datetime import datetime
    if 'fileField' in request.FILES:
        ph1 = request.FILES['fileField']
        if ph1.name != "":
            from datetime import datetime
            d1 = "criminals/criminal1/" + datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
            fs1 = FileSystemStorage()
            fs1.save(d1, ph1)
            path1 = fs1.url(d1)
            cc.photo1 = path1
    if 'fileField2' in request.FILES:
        ph1 = request.FILES['fileField2']
        if ph1.name != "":
            from datetime import datetime
            d1 = "criminals/criminal2/" + datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
            fs1 = FileSystemStorage()
            fs1.save(d1, ph1)
            path1 = fs1.url(d1)
            cc.photo2 = path1
    if 'fileField3' in request.FILES:
        ph1 = request.FILES['fileField3']
        if ph1.name != "":
            from datetime import datetime
            d1 = "criminals/finger/" + datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
            fs1 = FileSystemStorage()
            fs1.save(d1, ph1)
            path1 = fs1.url(d1)
            cc.fingerprint = path1
    cc.save()
    return viewcriminal1(request)


def addlabour(request):
    return render(request,"police_station/addlabour.html")


def addlabour_post(request):
    name=request.POST['textfield']
    gender=request.POST['radio']
    dob=request.POST['textfield2']
    maritalstatus=request.POST['textfield3']
    nplace=request.POST['textfield4']
    ncity=request.POST['textfield5']
    nstate=request.POST['textfield6']
    npin=request.POST['textfield7']
    cplace=request.POST['textfield8']
    cdistrict=request.POST['textfield9']
    idmark1=request.POST['textfield10']
    idmark2=request.POST['textfield11']
    photo1=request.FILES['fileField']
    adar=request.POST['adar']
    fprint=request.FILES['fileField2']
    jj = request.POST['j']
    phone=request.POST['textfield12']
    email=request.POST['textfield13']
    status='pending'
    from datetime import datetime
    dop=datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
    d1 = "labours/labour/" + dop
    fs1 = FileSystemStorage()
    fs1.save(d1, photo1)
    path1 = fs1.url(d1)

    res = Criminal.objects.all()

    print(res)

    knownimage = []
    knownids = []


    for i in res:
        s = i.photo1

        s = s.replace("/media/criminals/criminal1/", "")
        # pth = "D:\\Corezone\\2024-2025\\Kottayam\\Safe\\SafeKerala\\media\\criminals\\criminal1\\" + s
        pth = "C:\\Users\\nirma\\OneDrive\\Documents\\project\\SafeKeralamain\\SafeKerala[1]\\SafeKerala\\media\\criminals\\criminal1\\" + s
        
        picture_of_me = face_recognition.load_image_file(pth)
        print(pth)
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
        print(my_face_encoding)
        knownimage.append(my_face_encoding)
        knownids.append(i.id)
    x="C:\\Users\\nirma\\OneDrive\\Documents\\project\\SafeKeralamain\\SafeKerala[1]\\SafeKerala\\media\\labours\\labour\\"+dop
    picture_of_others = face_recognition.load_image_file(x)
    # print(pth)
    others_face_encoding = face_recognition.face_encodings(picture_of_others)

    totface = len(others_face_encoding)

    print("aaaaa", totface)
    l = 0
    for i in range(0, totface):


        print("inside check")
        res = face_recognition.compare_faces(knownimage, others_face_encoding[i], tolerance=0.45)
        print(res, "helllo")


        for j in res:
            if j == True:
                print(knownids[l], "found")
                res=Criminal.objects.get(id=knownids[l])
                return render(request,'admin/view_criminal.html',{"data":res})
                # return '''<script>alert('Criminal case registered')</script>'''
            l += 1

    d2= "labours/sign/" + dop
    fs2 = FileSystemStorage()
    fs2.save(d2, fprint)
    path2 = fs2.url(d2)

    ll = Login()
    ll.username = email
    ll.password = phone
    ll.type = "labour"
    ll.save()

    lab=Labour()
    lab.labourname=name
    lab.gender=gender
    lab.dob=dob
    lab.marital_status=maritalstatus
    lab.native_place=nplace
    lab.native_city=ncity
    lab.native_state=nstate
    lab.native_pin=npin
    lab.photo=path1
    lab.current_place=cplace
    lab.current_district=cdistrict
    lab.identification_mark1=idmark1
    lab.identification_mark2=idmark2
    lab.adarcard=adar
    lab.fingerprint=path2
    lab.job_type=jj
    lab.phone=phone
    lab.email=email
    lab.status=status
    lab.LOGIN_id=ll.id
    lab.save()

    return HttpResponse(
        "<script>alert('Information added successfully');window.location='/myapp/addlabour'</script>")


def viewlabour1(request):
    res=Labour.objects.filter(status='pending')
    return render(request,"police_station/viewlabour.html",{"data":res})


def viewapprovedlabour(request):
    res=Labour.objects.filter(status="Approved")
    return render(request,"police_station/viewapprovedlabours.html",{"data":res})

def blocklabor(request,id):
    res = Labour.objects.filter(id=id).update(status="Approved")
    return viewapprovedlabour(request)


def deletelabour(request,id):
    Labour.objects.filter(id=id).delete()
    return viewlabour1(request)


def editlabour(request,id):
    res = Labour.objects.get(id=id)
    return render(request,"police_station/editlabour.html",{"data":res})



def editlabour_post(request):
    laid=request.POST['la_id']
    name = request.POST['textfield']
    gender = request.POST['radio']
    dob = request.POST['textfield2']
    maritalstatus = request.POST['textfield3']
    nplace = request.POST['textfield4']
    ncity = request.POST['textfield5']
    nstate = request.POST['textfield6']
    npin = request.POST['textfield7']
    cplace = request.POST['textfield8']
    cdistrict = request.POST['textfield9']
    idmark1 = request.POST['textfield10']
    idmark2 = request.POST['textfield11']
    adar=request.POST['textfield12']
    j = request.POST['j']
    phone=request.POST['textfield12']
    lab = Labour.objects.get(id=laid)
    lab.labourname = name
    lab.gender = gender
    lab.dob = dob
    lab.marital_status = maritalstatus
    lab.native_place = nplace
    lab.native_city = ncity
    lab.native_state = nstate
    lab.native_pin = npin
    lab.current_place = cplace
    lab.current_district = cdistrict
    lab.identification_mark1 = idmark1
    lab.identification_mark2 = idmark2
    lab.adarcard = adar
    lab.job_type = j
    lab.phone = phone

    if 'fileField' in request.FILES:
        photo1 = request.FILES['fileField']
        if photo1.name !="":
            from datetime import datetime
            dop = datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
            d1 = "labours/labour/" + dop
            fs1 = FileSystemStorage()
            fs1.save(d1, photo1)
            path1 = fs1.url(d1)
            lab.photo = path1
    if 'fileField2' in request.FILES:
        fprint = request.files['fileField2']
        if fprint.name !="":
            from datetime import datetime
            dop = datetime.now().strftime('%Y%d%m%H%M%S') + '.jpg'
            d2 = "labours/sign/" + dop
            fs2 = FileSystemStorage()
            fs2.save(d2, fprint)
            path2 = fs2.url(d1)
            lab.fingerprint = path2

    lab.save()
    return HttpResponse(
        "<script>alert('Information added successfully');window.location='/myapp/viewlabour1'</script>")


def viewcomplaint1(request):
    
    res=Complaints.objects.all()
    print(res,'/////////////////////////////////')
    return render(request,"police_station/viewcomplaint.html",{'data':res})



def addreply(request,id):
    if 'button' in request.POST:
        reply=request.POST['textarea']
        ob = Complaints.objects.get(id = id )
        ob.reply = reply
        ob.status="done"
        ob.save()
        return HttpResponse('''<script>alert('Replied');window.location='/myapp/viewcomplaint1'</script>''')
        
    return  render(request,"police_station/addreply.html")


def addreply_post(request):
    # comid=request.POST['cid']
    reply=request.POST['textarea']
    Complaints.objects.filter(id = request.session['lid']).update(status='Done',reply=reply)
    return viewcomplaint1(request)


def viewnotification1(request):
    res=Notification.objects.all()
    return render(request,"police_station/viewnotification.html",{"data":res})


def viewfeedback1(request):
    res=Feedback.objects.all()
    return render(request,"police_station/viewfeedback.html",{"data":res})


def searchfeedback1(request):
    date1 = request.POST['textfield']
    date2 = request.POST['textfield2']
    res = Feedback.objects.filter(date__range=(date1, date2))
    return render(request,"police_station/viewfeedback.html",{"data":res})

def changepassword1(request):
    return render(request,"police_station/changepassword.html")


def change_pswrdpost1(request):
    curp = request.POST['textfield']
    newp = request.POST['textfield2']
    cnfp = request.POST['textfield3']
    qry = Login.objects.filter(id=request.session['lid'], password=curp)
    if qry.exists():
        if newp==cnfp:
            Login.objects.filter(id=request.session['lid'], password=curp).update(password=newp)
            return HttpResponse('''<script>alert('Password Changed Success');window.location='/myapp/'</script>''')
        else:
            return HttpResponse('''<script>alert('Password Mismatch!');window.location='/myapp/changepassword1'</script>''')
    else:
        return HttpResponse('''<script>alert('Current password must be valid!');window.location='/myapp/changepassword1'</script>''')

# -------------------------android password ----------------------------------------#


def and_login(request):
    username=request.POST["username"]
    password=request.POST["password"]

    qry = Login.objects.filter(username=username, password=password)
    if qry.exists():
        res = Login.objects.get(username=username, password=password)
       
        if res.type == 'user':
            return JsonResponse({'status':"ok", 'lid':res.id, 'type':'user'})
        elif (res.type == 'labour'):

            return JsonResponse({'status': "ok", 'lid': res.id, 'type': 'labour'})
        else:
            return JsonResponse({'status':"no"})
    else:
        return JsonResponse({'status':"no"})


def and_signup(request):
    name=request.POST["name"]
    email=request.POST["email"]
    phone=request.POST["phone"]
    gender=request.POST["gender"]
    photo=request.POST["photo"]
    place=request.POST["place"]
    post=request.POST["post"]
    district=request.POST["district"]
    pincode=request.POST["pincode"]
    password=request.POST["password"]
    import random
    import time
    import base64

    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(photo)
    # fh = open("D:\\Corezone\\2024-2025\\Kottayam\\Safe\\SafeKerala\\media\\user\\" + timestr + ".jpg", "wb")
    fh = open("C:\\Users\\nirma\\OneDrive\\Documents\\project\\SafeKeralamain\\SafeKerala[1]\\SafeKerala\\media\\user\\" + timestr + ".jpg", "wb")
    
    path = "/media/user/" + timestr + ".jpg"
    fh.write(a)
    fh.close()
    rr = str(random.randint(0000, 10000))
    ll = Login()
    ll.username = email
    ll.password = password
    ll.type = "user"
    ll.save()

    uu=User()
    uu.LOGIN_id=ll.id
    uu.name=name
    uu.email=email
    uu.phone=phone
    uu.gender=gender
    uu.photo=path
    uu.place=place
    uu.post=post
    uu.district=district
    uu.pincode=pincode
    uu.save()
    return JsonResponse({'status':"ok"})

def and_changepassword(request):
    curp=request.POST["oldpassword"]
    newp=request.POST["newpassword"]
    cnfp=request.POST["cnfmpassword"]
    lid=request.POST["lid"]
    qry = Login.objects.filter(id=lid, password=curp)
    if qry.exists():
        if newp == cnfp:
            Login.objects.filter(id=lid, password=curp).update(password=newp)
            return JsonResponse({'status':"ok"})
        else:
            return JsonResponse({'status': "no"})
    else:
        return JsonResponse({'status': "no"})


def and_labchangepassword(request):
    curp=request.POST["oldpassword"]
    newp=request.POST["newpassword"]
    cnfp=request.POST["cnfmpassword"]
    lid=request.POST["lid"]
    qry = Login.objects.filter(id=lid, password=curp)
    if qry.exists():
        if newp == cnfp:
            Login.objects.filter(id=lid, password=curp).update(password=newp)
            return JsonResponse({'status':"ok"})
        else:
            return JsonResponse({'status': "no"})
    else:
        return JsonResponse({'status': "no"})


def and_viewprofile(request):
    lid = request.POST['lid']
    qry = User.objects.get(LOGIN_id=lid)
    res_dict = model_to_dict(qry)
    return JsonResponse({'status': 'ok', 'data': res_dict})



def and_edit_prof(request):
    lid = request.POST['lid']

    res =User.objects.get(LOGIN_id=lid)
    user_json = serialize('json', [res])
    return JsonResponse({'status': 'ok', 'data': user_json})


def and_editprofile(request):

    uid = request.POST["uid"]
    name = request.POST["name"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    gender = request.POST["gender"]
    place = request.POST["place"]
    post = request.POST["post"]
    district = request.POST["district"]
    pincode = request.POST["pincode"]
    uu = User.objects.get(LOGIN_id=uid)

    uu.name = name
    uu.email = email
    uu.phone = phone
    uu.gender = gender

    uu.place = place
    uu.post = post
    uu.district = district
    uu.pincode = pincode

    photo = request.POST["photo"]
    if photo != "no":
        timestr = time.strftime("%Y%m%d-%H%M%S")
        a = base64.b64decode(photo)
        path = f"/media/user/{timestr}.jpg"
        with open(f"/path/to/static/user/{timestr}.jpg", "wb") as fh:
            fh.write(a)
            uu.photo = path
    uu.save()
    return JsonResponse({'status': 'ok'})


def and_sendcomplaint(request):
    if request.method == 'POST':
        userlid = request.POST["lid"]
        print(userlid)
        complaint = request.POST["complaint"]
        cc=Complaints()
        cc.USER_id=userlid
        cc.complaint=complaint
        cc.reply="pending"
        cc.status="pending"
        cc.date=date_today
        cc.save()

        return JsonResponse({'status': 'ok'})


def and_sendfeedback(request):
    userlid = request.POST["lid"]
    complaint = request.POST["complaint"]
    ff=Feedback()
    ff.date=date_today
    ff.USER.LOGIN_id=userlid
    ff.feedback=complaint
    ff.save()
    return JsonResponse({'status': 'ok'})


from django.utils import timezone

# def payment(request):
#     userlid = request.POST["lid"]
#     print(userlid,"uuuuuuuu")
#     request_id = request.POST["request_id"]
#     print(request_id,"rrrrrr")
#     payment_amount = request.POST['payment']
#     print(payment_amount,"amount")
#     if ff.REQUEST.work_status=="Work Finished":
#         ff = Payment()
#         ff.USER_id = userlid  
#         ff.REQUEST_id = request_id
#         ff.payment = payment_amount
#         ff.date = timezone.now()
#         ff.save()

#     return JsonResponse({'status': 'ok'})


def payment(request):
    userlid = request.POST["lid"]
    print(userlid, "uuuuuuuu")
    request_id = request.POST["request_id"]
    print(request_id, "rrrrrr")
    payment_amount = request.POST['payment']
    print(payment_amount, "amount")
    request_obj = Request.objects.get(id=request_id)
    if request_obj.work_status == "Work Finished":
        ff = Payments()
        ff.USER = User.objects.get(LOGIN_id=userlid)
        ff.REQUEST_id = request_id
        ff.payment = payment_amount
        ff.date = timezone.now()
        ff.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Work not approved'})




def and_view_reply(request):
    userlid=request.POST["lid"]
    res=Complaints.objects.filter(USER_id=userlid)

    user_json = []
    for i in res:
        user_json.append({"reply":i.reply,
                          "complaint":i.complaint,
                          "date":i.date
                          })
    return JsonResponse({'status': 'ok', 'data': user_json})


def and_labview_reply(request):
    userlid = request.POST["lid"]
    res = Complaints.objects.filter(USER_id=userlid)

    user_json = serialize('json', [res])
    return JsonResponse({'status': 'ok', 'data': user_json})


def and_view_labour(request):
    lid = request.POST["lid"]
    res = User.objects.filter(LOGIN_id=lid)
    print(res)
    if res.exists():
        res=Labour.objects.filter(current_district=res[0].district,status="Approved")
    else:
        res = Labour.objects.filter( status="Approved")
    user_json = []
    for i in res:
        user_json.append({
            "labour_id":i.pk,
            "login_id":i.LOGIN.id,
            "labourname":i.labourname,
            "gender":i.gender,
            "dob":i.dob,
            "marital_status":i.marital_status,
            "native_place":i.native_place,
            "native_city":i.native_city,
            "native_state":i.native_state,
            "native_pin":i.native_pin,
            "photo":i.photo,
            "current_place":i.current_place,
            "current_district":i.current_district,
            "idcard_no":i.adarcard,
            "job_type":i.job_type,
            "phone":i.phone,
            "status":i.status,
            "con_lid":"0",
            "email":i.email
        })
    print(user_json)
    return JsonResponse({'status': 'ok', 'data': user_json})



def and_view_labour_by_id(request):
    id=request.POST["labour_id"]
    print(id,'/////lab')
    res = Labour.objects.filter(id=id)
    user_json = []
    for i in res:
        user_json.append({
            "labour_id":i.pk,
            "login_id":i.LOGIN.id,
            "labourname":i.labourname,
            "gender":i.gender,
            "dob":i.dob,
            "marital_status":i.marital_status,
            "native_place":i.native_place,
            "native_city":i.native_city,
            "native_state":i.native_state,
            "native_pin":i.native_pin,
            "photo":i.photo,
            "current_place":i.current_place,
            "current_district":i.current_district,
            "idcard_no":i.adarcard,
            "job_type":i.job_type,
            "phone":i.phone,
            "status":i.status,
            "con_lid":"0",
            "email":i.email
        })
    print(user_json)
    return JsonResponse({'status': 'ok', 'data': user_json})


# def and_view_labour_search(request):
#     name=request.POST["name"]
#     res = Labour.objects.filter(labourname__icontains=name)
#     user_json = []
#     for i in res:
#         user_json.append({
#             "labour_id":i.pk,
#             "login_id":i.LOGIN.id,
#             "labourname":i.labourname,
#             "gender":i.gender,
#             "dob":i.dob,
#             "marital_status":i.marital_status,
#             "native_place":i.native_place,
#             "native_city":i.native_city, 
#             "native_state":i.native_state,
#             "native_pin":i.native_pin,
#             "photo":i.photo,
#             "current_place":i.current_place,
#             "current_district":i.current_district,
#             "idcard_no":i.adarcard,
#             "job_type":i.job_type,
#             "phone":i.phone,
#             "status":i.status,
#             "con_lid":"0",
#             "email":i.email
#         })
#     print(user_json)
#     return JsonResponse({'status': 'ok', 'data': user_json})

def and_view_labour_search(request):
    # Get the search parameter from POST request
    district = request.POST.get("current_district","")
    
    # Filter Labour objects by current_district
    res = Labour.objects.filter(current_district__icontains=district)
    
    # Prepare the data to return as JSON
    user_json = []
    for i in res:
        user_json.append({
            "labour_id": i.pk,
            "login_id": i.LOGIN.id,
            "labourname": i.labourname,
            "gender": i.gender,
            "dob": i.dob,
            "marital_status": i.marital_status,
            "native_place": i.native_place,
            "native_city": i.native_city,
            "native_state": i.native_state,
            "native_pin": i.native_pin,
            "photo": i.photo,
            "current_place": i.current_place,
            "current_district": i.current_district,
            "idcard_no": i.adarcard,
            "job_type": i.job_type,
            "phone": i.phone,
            "status": i.status,
            "con_lid": "0",
            "email": i.email
        })
    #print(user_json)
    # Return JSON response
    return JsonResponse({'status': 'ok', 'data': user_json})


# def and_sendrequest(request):
#     userlid=request.POST["lid"]
#     labourlid=request.POST["llid"]
#     worktype=request.POST["worktype"]
#     dis=request.POST["discription"]
#     location=request.POST["location"]
#     rr=Request()
#     rr.USER=User.objects.get(LOGIN_id=userlid)
#     rr.WORKER=Labour.objects.get(LOGIN_id=labourlid)
#     rr.work_type=worktype
#     rr.description=dis
#     rr.location=location
#     rr.date=date_today
#     rr.time=datetime.now().time()
#     rr.type="Labours"
#     rr.save()
#     return JsonResponse({'status': 'ok'})

from django.utils.dateformat import DateFormat
from datetime import datetime, timedelta
def and_sendrequest(request):
    userlid = request.POST["lid"]
    labourlid = request.POST["llid"]
    worktype = request.POST["worktype"]
    dis = request.POST["discription"]
    location = request.POST["location"]
    
    date_today = datetime.today().date()
    
    labour = Labour.objects.get(LOGIN_id=labourlid)
    
    # Check if the labour is already booked today with status "Approve" and work_status not "Work Finished"
    existing_requests = Request.objects.filter(WORKER=labour, date=date_today)
    
    if existing_requests.exists() and not existing_requests.filter(status='Approve', work_status='Work Finished').exists():
        return JsonResponse({'status': 'error', 'message': 'Labourer is already booked today and work is not approved and finished.'})
    
    rr = Request()
    rr.USER = User.objects.get(LOGIN_id=userlid)
    rr.WORKER = labour
    rr.work_type = worktype
    rr.description = dis
    rr.location = location
    rr.date = date_today
    rr.time = datetime.now().time()
    rr.type = "Labours"
    rr.save()
    
    return JsonResponse({'status': 'ok'})




















#
# @app.route('/and_viewemployee',methods=['post'])
# def and_viewemployee():
#     id=request.form["clid"]
#     lid = request.form["lid"]
#     qry = "SELECT `district` FROM `user` WHERE `user_lid`='" + lid + "'"
#     db = Db()
#     res = db.selectOne(qry)
#     if res is not None:
#         db = Db()
#         qry = "SELECT * FROM `labour` WHERE `con_lid`='" + id + "' and current_district='"+str(res["district"])+"' and status='Approved'"
#         res  = db.select(qry)
#     else:
#         db=Db()
#         qry="SELECT * FROM `labour` WHERE `con_lid`='"+id+"'and status='Approved'  "
#         res=db.select(qry)
#     return jsonify(status="ok",data=res)
#
# @app.route('/and_viewemployee_search',methods=['post'])
# def and_viewemployee_search():
#     id=request.form["clid"]
#     lid = request.form["lid"]
#     name=request.form["name"]
#     qry = "SELECT `district` FROM `user` WHERE `user_lid`='" + lid + "'"
#     db = Db()
#     res = db.selectOne(qry)
#     if res is not None:
#         db = Db()
#         qry = "SELECT * FROM `labour` WHERE `con_lid`='" + id + "' and current_district='"+str(res["district"])+"' and status='Approved' and (labourname like '%"+name+"%' or idcard_no like '%"+name+"%')"
#         res  = db.select(qry)
#     else:
#         db=Db()
#         qry="SELECT * FROM `labour` WHERE `con_lid`='"+id+"' and status='Approved'  "
#         res=db.select(qry)
#     return jsonify(status="ok",data=res)
#
#
# @app.route('/and_searchemployee',methods=['post'])
# def and_searchemployee():
#     name = request.form["name"]
#     db = Db()
#     qry = "SELECT * FROM `labour` where current_place like '%" + name + "%' or job_type like '%" + name + "%'"
#     res = db.select(qry)
#     return jsonify(status=['post'])
#
#
#
# @app.route('/and_sendrequest1',methods=['post'])
# def and_sendrequest1():
#     userlid = request.form["lid"]
#     labourlid = request.form["llid"]
#     worktype = request.form["worktype"]
#     dis = request.form["discription"]
#
#     location = request.form["location"]
#     db = Db()
#     qry = "INSERT INTO `request`(`user_id`,`labourr_lid`,`work_type`,`discription`,`location`,`date`,`time`,`type`) VALUES ('" + userlid + "','" + labourlid + "','" + worktype + "','" + dis + "','" + location + "',CURDATE(),CURTIME(),'Labours')"
#     res = db.insert(qry)
#     return jsonify(status="ok")
#
#
#
#
# @app.route('/and_viewwageplan',methods=['post'])
# def and_viewwageplan():
#     db=Db()
#     qry="SELECT * FROM `job_wage` ;"
#     res=db.select(qry)
#     return jsonify(status="ok",data=res)
#

def and_view_skill(request):
    llid=request.POST["llid"]
    qq=Labour.objects.get(LOGIN_id=llid).id
    res=Skill.objects.filter(WORKER_id=qq)
    ll=[]
    for i in res:
        ll.append({"skill_id":i.id,"skill_type":i.skill_type,"labour_id":i.WORKER.pk})
    return JsonResponse({'status': 'ok', 'data': ll})


#
# @app.route('/and_send_reviewtocontractor',methods=['post'])
# def send_reviewtocontractor():
#     db=Db()
#     ulid = request.form["lid"]
#     aid = request.form["llid"]
#     rating = request.form["rating"]
#     review = request.form["review"]
#     qry = "INSERT INTO `review`(`rating`,`review`,`date`,`user_lid`,`about_id`,`type`) VALUES('" + rating + "','" + review + "',curdate(),'" + ulid + "','" + aid + "','contractor')"
#     res = db.insert(qry)
#     return jsonify(status="ok")
#
# @app.route('/and_view_reviewcustom',methods=['post'])
# def view_reviewcustom():
#     db=Db()
#     qry="SELECT * FROM review "
#     res=db.select(qry)
#     return jsonify(status="ok",data=res)
#
#

def send_reviewtoworker(request):
    ulid = request.POST["lid"]
    aid = request.POST["llid"]
    rating = request.POST["rating"]
    review = request.POST["review"]
    rr=Review()
    rr.rating = rating
    rr.review = review
    rr.date = date_today
    rr.USER = User.objects.get(LOGIN_id=ulid)
    rr.WORKER = Labour.objects.get(LOGIN_id=aid)
    rr.type = "worker"
    rr.save()
    
    return JsonResponse({'status': 'ok'})


#
#
# # --------------------------------------------- android labour

def and_lab_signup(request):
    lname=request.POST["name"]
    gender=request.POST["gender"]
    dob=request.POST["ldob"]
    phone=request.POST["phone"]
    mail=request.POST["email"]
    photo=request.POST["lphoto"]
    mstatus=request.POST["mstatus"]
    nativeplace=request.POST["nplace"]
    nativecity=request.POST["ncity"]
    nativestate=request.POST["nstate"]
    nativepin=request.POST["npin"]
    curplace=request.POST["curplace"]
    curdis=request.POST["curdis"]
    idmark1=request.POST["idmark1"]
    idmark2=request.POST["idmark2"]
    adharcard=request.POST["adharcard"]
    imgfingerprint=request.POST["imf"]
    jobtype=request.POST["jobtype"]
    password=request.POST["password"]

    import random
    import time
    import base64

    timestr = time.strftime("%Y%m%d=%H%M%S")
    print(timestr)
    a = base64.b64decode(photo)
    # fh = open("D:\\Corezone\\2024-2025\\Kottayam\\Safe\\SafeKerala\\media\\labours\\labour\\"+timestr+".jpg",'wb')
    fh = open("C:\\Users\\nirma\\OneDrive\\Documents\\project\\SafeKeralamain\\SafeKerala[1]\\SafeKerala\\media\\labours\\labour\\"+timestr+".jpg",'wb')
    
    path="/media/labours/labour/" + timestr + ".jpg"

    fh.write(a)
    fh.close()

    timestr = time.strftime("%Y,%m,%d=%H%M%S")
    print(timestr)
    b = base64.b64decode(imgfingerprint)
    fp = open("C:\\Users\\nirma\\OneDrive\\Documents\\project\\SafeKeralamain\\SafeKerala[1]\\SafeKerala\\media\\labours\\sign\\"+timestr+".jpg",'wb')
    path2="/media/labours/sign/" + timestr + ".jpg"

    fp.write(b)
    fp.close()

    rr = str(random.randint(0000, 10000))

    ll=Login()
    ll.username=mail
    ll.password=password
    ll.type='labour'
    ll.save()

    lab = Labour()
    lab.labourname = lname
    lab.gender = gender
    lab.dob = dob
    lab.marital_status = mstatus
    lab.native_place = nativeplace
    lab.native_city = nativecity
    lab.native_state = nativestate
    lab.native_pin = nativepin
    lab.photo = path
    lab.current_place = curplace
    lab.current_district = curdis
    lab.identification_mark1 = idmark1
    lab.identification_mark2 = idmark2
    lab.adarcard = adharcard
    lab.fingerprint = path2
    lab.job_type = jobtype
    lab.phone = phone
    lab.email = mail
    lab.status = "pending"
    lab.LOGIN_id = ll.id
    lab.save()
    return JsonResponse({'status':"ok"})


def and_lab_changepassword(request):
        curp = request.POST["oldpassword"]
        newp = request.POST["newpassword"]
        cnfp = request.POST["cnfmpassword"]
        lid = request.POST["lid"]
        qry = Login.objects.filter(id=lid, password=curp)
        if qry.exists():
            if newp == cnfp:
                Login.objects.filter(id=lid, password=curp).update(password=newp)
                return JsonResponse({'status': "ok"})
            else:
                return JsonResponse({'status': "no"})
        else:
            return JsonResponse({'status': "no"})



def and_lab_viewprofile(request):
    lid=request.POST['lid']
    res=Labour.objects.get(LOGIN_id=lid)
    res_dict = model_to_dict(res)
    return JsonResponse({'status': 'ok', 'data': res_dict})



def and_lab_editpro(request):
    lid=request.POST['login']
    res = Labour.objects.get(LOGIN_id=lid)
    user_json = serialize('json', [res])
    return JsonResponse({'status': 'ok', 'data': user_json})


def and_lab_editprofile(request):
    labid=request.POST["labid"]
    name=request.form["lname"]
    gender=request.form["lgender"]
    dob=request.form["ldob"]
    phone=request.form["lphone"]
    email=request.form["lemail"]
    mstatus=request.form["lmstatus"]
    nplace=request.form["lnplace"]
    ncity=request.form["lncity"]
    nstate=request.form["lnstate"]
    npin=request.form["lnpin"]
    cplace=request.form["lcplace"]
    cdis=request.form["lcdis"]
    idm1=request.form["lidm1"]
    idm2=request.form["lidm2"]
    adhrcard=request.form["ladharcard"]
    jobtype=request.form["jobtype"]
    photo=request.form["photo"]
    fingerprint=request.form["fp"]
    lab = Labour.objects.get(id=labid)
    lab.labourname = name
    lab.gender = gender
    lab.dob = dob
    lab.marital_status = mstatus
    lab.native_place = nplace
    lab.native_city = ncity
    lab.native_state = nstate
    lab.native_pin = npin

    lab.current_place = cplace
    lab.current_district = cdis
    lab.identification_mark1 = idm1
    lab.identification_mark2 = idm2
    lab.adarcard = adhrcard

    lab.job_type = jobtype
    lab.phone = phone


    lab.save()
    if photo !="no":

        timestr = time.strftime("%Y%m%d-%H%M%S")
        print(timestr)
        a = base64.b64decode(photo)
        # fh = open("D:\\Corezone\\2024-2025\\Kottayam\\Safe\\SafeKerala\\media\\labours\\labour\\")
        fh = open("C:\\Users\\nirma\\OneDrive\\Documents\\project\\SafeKeralamain\\SafeKerala[1]\\SafeKerala\\media\\labours\\labour\\")
        
        path = "/static/labour/" + timestr + ".jpg"
        fh.write(a)
        fh.close()
        lab.photo=path

    if fingerprint !="no" :

        timestr = time.strftime("%Y%m%d-%H%M%S")
        print(timestr)
        b = base64.b64decode(fingerprint)
        fh1 = open("C:\\Users\\nirma\\OneDrive\\Documents\\project\\SafeKeralamain\\SafeKerala[1]\\SafeKerala\\media\\labours\\sign\\")
        path1 = "/static/laboursign" +timestr+ ".jpg"
        fh1.write(b)
        fh1.close()
        lab.fingerprint = path1

    lab.save()
    return JsonResponse({'status': 'ok'})



def and_lab_viewrequest(request):
    lid=request.POST["lid"]
    res=Request.objects.filter(WORKER__LOGIN_id=lid)
    ll=[]
    for i in res:
      ll.append({
          "request_id":i.pk,
          "name":i.USER.name,
          "phone":i.USER.phone,
          "labourr_lid":i.WORKER.LOGIN.pk,
          "work_type":i.work_type,
          "discription":i.description,
          "location":i.location,
          "date":i.date,
          "time":i.time,
          "type":i.type,
          "status":i.status,
          "work_status":i.work_status

      })
    print(ll)
    return JsonResponse({'status': 'ok', 'data': ll})

def and_cust_viewrequest(request):
    lid=request.POST["lid"]
    res=Request.objects.filter(USER__LOGIN_id=lid)
    ll=[]
    for i in res:
      ll.append({
          "request_id":i.pk,
          "labourname":i.WORKER.labourname,
          "phone":i.WORKER.phone,
          "labourr_lid":i.WORKER.LOGIN.pk,
          "work_type":i.work_type,
          "discription":i.description,
          "location":i.location,
          "date":i.date, 
          "time":i.time,
          "type":i.type,
          "status":i.status,
          "work_status":i.work_status
      })
    print(ll)
    return JsonResponse({'status': 'ok', 'data': ll})


def and_lab_editskill(request):
    laboulid=request.POST["skill_id"]
    skill=request.POST["skill"]
    dd=Skill.objects.filter(id=laboulid).update(skill_type=skill)
    return JsonResponse({'status': 'ok'})


def and_lab_addskill(request):
    laboulid=request.POST["lid"]
    skill=request.POST["skill"]
    ss=Skill()
    ss.skill_type=skill
    ss.WORKER=Labour.objects.get(LOGIN_id=laboulid)
    ss.save()

    return JsonResponse({'status': 'ok'})


def and_lab_viewskill(request):
    return JsonResponse({'status': 'ok'})









def and_lab_edit_skill(request):
    skillid=request.form['skill_id']
    res=Skill.objects.filter(id=skillid)
    return JsonResponse({'status': 'ok'})


def and_lab_editskilma(request):
    return JsonResponse({'status': 'ok'})
#
#
# @app.route('/and_lab_sendcomplaint',methods=['post'])
# def and_lab_sendcomplaint():
#     lid=request.form["lid"]
#     complaint=request.form["complaint"]
#     toid = request.form["toid"]
#     type = request.form["type"]
#     if type=="Contractor":
#         ty="lab_cont"
#     else:
#         ty="lab_user"
#
#     db=Db()
#     qry="INSERT INTO `complaints`(`date`,`complaint`,`reply`,`status`,`user_lid`,`login_id`,`con_lid`,type) VALUES (curdate(),'"+complaint+"','pending','pending','0','"+lid+"','"+toid+"','"+ty+"');"
#     res=db.insert(qry)
#     return jsonify(status="ok",data=res)
#
#
# @app.route('/and_lab_viewworkreview',methods=['post'])
# def and_lab_viewworkreview():
#     return jsonify(status="ok")
#
#
#
#
#
# @app.route('/and_view_type',methods=['post'])
# def and_view_type():
#     type=request.form["type"]
#     t=[]
#     if type=="Contractor":
#         db = Db()
#         qry = "SELECT * FROM `contractor` WHERE `status`='Approved' "
#         res = db.select(qry)
#         t=[]
#         for i in res:
#             t.append({"id":i["con_lid"],"name":i["name"],"phone":i["phone"]})
#     else:
#         db = Db()
#         qry = "SELECT * FROM user "
#         res = db.select(qry)
#         t = []
#         for i in res:
#             t.append({"id": i["user_lid"], "name": i["name"], "phone": i["phone"]})
#     return jsonify(status="ok",data=t)
#

def and_view_payment(request):
    # Assuming 'lid' is passed via POST data
    lid = request.POST.get("lid", "")

    # Fetching the specific Request IDs associated with the worker's login ID
    req_ids = Request.objects.filter(WORKER__LOGIN_id=lid).values_list('id', flat=True)

    
    # Query payments related to filtered requests
    payments = Payments.objects.filter(REQUEST__in=req_ids) # Using select_related to join USER table
    print(payments,'payments isssssssssssssssssssss')
    # Prepare the response data
    payment_data = []
    for payment in payments:
        payment_data.append({
            "username": payment.USER.name,  # Accessing the name of the user
            "amount": payment.payment,
        })

    return JsonResponse({'status': 'ok', 'data': payment_data})

def and_view_review(request):
    lid=request.POST["lid"]
    res=Review.objects.filter(WORKER=Labour.objects.get(LOGIN_id=lid),type='worker')
    ll=[]
    for i in res:
      ll.append({
          "rating":i.rating,
          "name":i.USER.name,
          "review":i.review,
          "date":i.date,
      })
    print(ll)
    return JsonResponse({'status': 'ok', 'data': ll})



def deleteskill(request):
    lid=request.POST["skill_id"]
    Skill.objects.filter(id=lid).delete()
    return JsonResponse({'status': "ok"})


def approve_request(request):
    id=request.POST["aid"]
    status='Approve'
    dd = Request.objects.filter(id=id).update(status=status)

    return JsonResponse({'status': "ok"})


def update_work_status(request):
    id = request.POST.get("aid")
    
    if not id:
        return JsonResponse({'status': "failed", 'message': "ID is required"})
    
    # Retrieve the request object with the given ID
    request_obj = Request.objects.filter(id=id).first()

    if request_obj and request_obj.status == "Approve":
        # Update the work status if the status is "Approve"
        request_obj.work_status = 'Work Finished'
        request_obj.save()
        return JsonResponse({'status': "ok"})
    else:
        # Return a failure response if the status is not "Approve" or the request does not exist
        return JsonResponse({'status': "failed", 'message': "Status not 'Approve' or request not found"})





def reject_request(request):
    id=request.POST["aid"]
    status='Reject'

    dd=Request.objects.filter(id=id).update(status=status)

    return JsonResponse({'status':"ok"})
