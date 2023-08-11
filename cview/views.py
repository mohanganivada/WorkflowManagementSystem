from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mohan3658",
  database="vista2"
)
mycursor = mydb.cursor()


# Create your views here.

def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},context_instance=RequestContext(request))
    response.status_code = 500
    return response

def home(request):
    context={

    }
    return render(request,"home.html",context)

def authentication(request):
    return render(request,"authentication.html")



def registration(request):
    data=dict(request.POST)

    firstname = data['firstname'][0]
    lastname = data['lastname'][0]
    middlename = data['middlename'][0]
    email = data['email'][0]
    mobile = data['mobile'][0]
    alternateMobile = data['alternateMobile'][0]
    password = data['opassword'][0]
    
    
    imgSourceFail="https://cdn-icons-png.flaticon.com/512/5219/5219070.png"
    imgSourceSuccess="https://www.pngmart.com/files/22/Congratulations-PNG-Transparent.png"

    #if user is existing and try to create new account
    query = """SELECT * FROM tbl_user_master WHERE User_eMail=%s"""
    mycursor.execute(query,(email,))
    myresult = mycursor.fetchone()

    if myresult==None:
        query= "INSERT INTO tbl_user_master (User_Last_Name,User_First_Name,User_Middle_Name,User_eMail,User_Mobile_Number,User_Alternative_Number,user_password) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(query,(lastname,firstname,middlename,email,mobile,"9000001234",password))
        mydb.commit()
        context={
            'imgsrc':imgSourceSuccess
        }
        return render(request,'registration.html',context)

    context={
        'imgsrc':imgSourceFail,
        'error':"please enter new email or login with the existing email"
    }
    
    return render(request,'registration.html',context)

def user(request):
    if request.method == 'POST':
        data=dict(request.POST)
        email=data['email'][0]
        sql = "SELECT * FROM tbl_user_master WHERE User_eMail=%s"
        mycursor.execute(sql,(email,))
        user=mycursor.fetchone()
        mydb.commit()

        

        if(user==None):
            context={
                "error":"please register or enter valid details"
            }
            return render(request,"authentication.html",context)

        userId=user[0]
        userRole=user[2]

        #user login
        if(userRole==1):
            sql="SELECT resume_id,status_id FROM tbl_resume WHERE User_id=%s LIMIT 1"
            mycursor.execute(sql,(user[0],))
            result=mycursor.fetchone()
            context={
                'userId':user[0],
                'resume':result
            }
            return render(request, 'user.html',context)

        #editor login
        if(userRole==2):
            sql="select tbl_resume.Resume_Id,tbl_user_master.User_Id,tbl_user_master.User_First_Name,tbl_user_master.User_Last_Name, tbl_resume_status.Status_Description from tbl_user_master JOIN tbl_resume ON tbl_user_master.User_Id=tbl_resume.User_Id JOIN tbl_resume_status ON tbl_resume.Status_ID=tbl_resume_status.Status_Id WHERE Assign_to=%s AND tbl_resume.status_id != 3 AND tbl_resume.status_id !=7"
            mycursor.execute(sql,(userId,))
            resumes=mycursor.fetchall()
            mydb.commit()

            sql="select tbl_resume.Resume_Id,tbl_user_master.User_Id,tbl_user_master.User_First_Name,tbl_user_master.User_Last_Name, tbl_resume_status.Status_Description from tbl_user_master JOIN tbl_resume ON tbl_user_master.User_Id=tbl_resume.User_Id JOIN tbl_resume_status ON tbl_resume.Status_ID=tbl_resume_status.Status_Id WHERE Assign_to=%s AND tbl_resume.status_id = 3"
            mycursor.execute(sql,(userId,))
            acceptanceResumes=mycursor.fetchall()
            mydb.commit()

            #for counts of statuses
            sql="""truncate tbl_report1_temp"""
            mycursor.execute(sql)
            mydb.commit()
            sql="""INSERT into tbl_report1_temp (user_first_name,user_id,records_assigned,user_last_name,user_email,user_mobile,status_id,role_id)
                    ((SELECT c.User_first_Name,c.user_id,count(a.assign_to),c.user_last_name,c.user_email,c.user_mobile_number, a.status_id,c.user_role
                    from tbl_resume a, tbl_resume_status b, tbl_user_master c
                    where b.status_id = a.Status_ID and c.user_id = a.Assign_to
                    group by a.assign_to, a.status_id, b.Status_Description
                    ))"""
            mycursor.execute(sql)
            mydb.commit()

            sql="""insert into tbl_report1_temp (user_first_name, user_id,user_last_name,user_email,user_mobile,status_id,role_id)
                    (SELECT c.User_first_Name,c.user_id,c.user_last_name,c.user_email,c.user_mobile_number, 2 ,c.user_role
                    from  tbl_user_master c
                    where c.user_role = 2);"""
            mycursor.execute(sql)
            mydb.commit()

            sql="""SELECT
                    sum(CASE WHEN status_id = 1 THEN Records_assigned ELSE 0 END) AS "form filling",
                    sum(CASE WHEN status_id = 2 THEN Records_assigned ELSE 0 END) AS "pending for assignment",
                    sum(CASE WHEN status_id = 3 THEN Records_assigned ELSE 0 END) AS "pending for acceptance",
                    sum(CASE WHEN status_id = 4 THEN Records_assigned ELSE 0 END) aS "pending for editing",
                    sum(CASE WHEN status_id = 5 THEN Records_assigned ELSE 0 END) AS "editing in progress",
                    sum(CASE WHEN status_id = 6 THEN Records_assigned ELSE 0 END) AS "pending for review",
                    sum(CASE WHEN status_id = 7 THEN Records_assigned ELSE 0 END) AS "completed"
                    FROM tbl_report1_temp WHERE user_id=%s;""" % (userId)

            mycursor.execute(sql)
            summary=mycursor.fetchone()
            mydb.commit()

            context={
                'userId':userId,
                'resumes':resumes,
                'summary':summary,
                'acceptanceResumes':acceptanceResumes
            }
            return render(request,'editor.html',context)


        
        #super editor login
        if(userRole==3):
            sql="select tbl_resume.Resume_Id,tbl_user_master.User_Id,tbl_user_master.User_First_Name,tbl_user_master.User_Last_Name, tbl_user_master.User_eMail, tbl_user_master.User_Mobile_Number, tbl_resume_status.Status_Description from tbl_user_master JOIN tbl_resume ON tbl_user_master.User_Id=tbl_resume.User_Id JOIN tbl_resume_status ON tbl_resume.Status_ID=tbl_resume_status.Status_Id WHERE Assign_to=%s"
            mycursor.execute(sql,(userId,))
            resumes=mycursor.fetchall()
            mydb.commit()

            sql="""truncate tbl_report1_temp"""
            mycursor.execute(sql)
            mydb.commit()
            sql="""INSERT into tbl_report1_temp (user_first_name,user_id,records_assigned,user_last_name,user_email,user_mobile,status_id,role_id)
                    ((SELECT c.User_first_Name,c.user_id,count(a.assign_to),c.user_last_name,c.user_email,c.user_mobile_number, a.status_id,c.user_role
                    from tbl_resume a, tbl_resume_status b, tbl_user_master c
                    where b.status_id = a.Status_ID and c.user_id = a.Assign_to
                    group by a.assign_to, a.status_id, b.Status_Description
                    ))"""
            mycursor.execute(sql)
            mydb.commit()

            sql="""insert into tbl_report1_temp (user_first_name, user_id,user_last_name,user_email,user_mobile,status_id,role_id)
                    (SELECT c.User_first_Name,c.user_id,c.user_last_name,c.user_email,c.user_mobile_number, 2 ,c.user_role
                    from  tbl_user_master c
                    where c.user_role = 2);"""
            mycursor.execute(sql)
            mydb.commit()
            sql="""SELECT user_id,user_first_name, user_last_name, user_mobile, user_email, role_id,
                    sum(CASE WHEN status_id = 4 THEN Records_assigned ELSE 0 END) aS "pending for editing",
                    sum(CASE WHEN status_id = 5 THEN Records_assigned ELSE 0 END) AS "editing in progress",
                    sum(CASE WHEN status_id = 2 THEN Records_assigned ELSE 0 END) AS "pending for assignment",
                    sum(CASE WHEN status_id = 1 THEN Records_assigned ELSE 0 END) AS "form filling",
                    sum(CASE WHEN status_id = 3 THEN Records_assigned ELSE 0 END) AS "pending for acceptance",
                    sum(CASE WHEN status_id = 6 THEN Records_assigned ELSE 0 END) AS "pending for review",
                    sum(CASE WHEN status_id = 7 THEN Records_assigned ELSE 0 END) AS "completed"
                    FROM tbl_report1_temp
                    where role_id = 2
                    group by user_id,user_first_name,user_last_name, user_mobile, user_email,role_id"""
            mycursor.execute(sql)
            editors=mycursor.fetchall()
            mydb.commit()
            
            sql="""SELECT
                    sum(CASE WHEN status_id = 1 THEN Records_assigned ELSE 0 END) AS "form filling",
                    sum(CASE WHEN status_id = 2 THEN Records_assigned ELSE 0 END) AS "pending for assignment",
                    sum(CASE WHEN status_id = 3 THEN Records_assigned ELSE 0 END) AS "pending for acceptance",
                    sum(CASE WHEN status_id = 4 THEN Records_assigned ELSE 0 END) aS "pending for editing",
                    sum(CASE WHEN status_id = 5 THEN Records_assigned ELSE 0 END) AS "editing in progress",
                    sum(CASE WHEN status_id = 6 THEN Records_assigned ELSE 0 END) AS "pending for review",
                    sum(CASE WHEN status_id = 7 THEN Records_assigned ELSE 0 END) AS "completed"
                    FROM tbl_report1_temp;"""

            mycursor.execute(sql)
            summary=mycursor.fetchone()
            mydb.commit()

            sql="select tbl_resume.Resume_Id,tbl_user_master.User_First_Name,tbl_user_master.User_Last_Name, tbl_user_master.User_Mobile_Number,tbl_resume.Assign_to, tbl_resume_status.Status_Description from tbl_user_master JOIN tbl_resume ON tbl_user_master.User_Id=tbl_resume.User_Id JOIN tbl_resume_status ON tbl_resume.Status_ID=tbl_resume_status.Status_Id"
            mycursor.execute(sql)
            allResumes=mycursor.fetchall()
            mydb.commit()
            
            sql="""SELECT tbl_resume.User_Id,tbl_user_master.User_Id,tbl_user_master.User_First_Name,tbl_user_master.User_Last_Name,tbl_user_master.User_Type,TIMESTAMPDIFF(hour,tbl_resume.Assigned_Date_Time,CURDATE())
                    From tbl_user_master
                    JOIN tbl_resume ON tbl_resume.Assign_to=tbl_user_master.User_Id AND tbl_user_master.User_Type='editor'"""
            mycursor.execute(sql)
            statistics=mycursor.fetchall()
            mydb.commit()
            context={
                'userId':userId,
                'resumes':resumes,
                'status':0,
                'editors':editors,
                'summary':summary,
                'allResumes':allResumes,
                'statistics':statistics
            }
            return render(request,'superEditor.html',context)

        #admin login
        if(userRole==4):
            sql="SELECT cv_service_id,cv_service_name,service_amount FROM cview_services_master"
            mycursor.execute(sql)
            packages= mycursor.fetchall()
            context={
                'userId':userId,
                'packages':packages,
            }
            return render(request,'admin.html',context)

            
    return render(request,'authentication.html')


def saved(request):
    #checking if user coming from login page or not
    userID = request.POST.get('userID')
    if userID==None:
        return render(request,'authentication.html')
    if(userID.isnumeric()):
            sql = "SELECT * FROM tbl_user_master WHERE User_Id=%s"
            mycursor.execute(sql,(userID,))
            ifExists=mycursor.fetchone()
            if(ifExists==None):
                return render(request,"authentication.html")
    else:
        return render(request,'authentication.html')
    
    item= request.POST #getting all form data 
    item = dict(item) #converting all form data to dictionary
    
    print(item)

    #saving form data
    #saving project details


    sql="update tbl_user_master set User_Last_Name=%s,User_First_Name=%s,User_Middle_Name=%s,User_eMail=%s,User_Mobile_Number=%s,User_Alternative_Number=%s,created_date=current_timestamp() WHERE User_Id=%s"
    mycursor.execute(sql,(item['lname'][0],item['fname'][0],item['mname'][0],item['email'][0],item['mobileNumber'][0],item['alternateMobile'][0],item['userID'][0]))
    mydb.commit()

    projectId=item['projectID']
    for x in range(0,len(projectId)):
        if(projectId[x]=='new'):
            sql="insert into tbl_user_projects(User_ID,User_Project_Title, User_Role_Responsibilities, User_Technology_Used, User_Project_Description,User_Project_client,User_Project_Start_Date,User_Project_End_Date,created_by) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql,(item["userID"][0],item['projectTitle'][x],item['projectRolesResp'][x],item['projectTechnology'][x],item['projectDescription'][x],item['projectClient'][x],"2022-01-01","2022-01-01",item['userID'][0]))
            mydb.commit()
        else:
            sql="update tbl_user_projects set User_Project_Title=%s,User_Role_Responsibilities=%s,User_Technology_Used=%s,User_Project_Description=%s,User_Project_client=%s,User_Project_Start_Date=%s,User_Project_End_Date=%s,created_date=current_timestamp() where User_Project_ID=%s"
            mycursor.execute(sql,(item['projectTitle'][x],item['projectRolesResp'][x],item['projectTechnology'][x],item['projectDescription'][x],item['projectClient'][x],"2022-01-01","2022-01-01",item["projectID"][x],))
            mydb.commit()


            
    educationId=item['educationID']
    for x in range(0,len(educationId)):
        if(educationId[x]=='new'):
            sql="insert into tbl_user_education(User_ID,User_Education, User_Education_Inistitute_Name, User_Educatin_Inistitute_City, User_Educatin_Inistitute_Country,User_Education_Grade_Percentage,User_Education_Passout_Start_Date,User_Education_Passout_End_Year,User_Education_Mode,created_by) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql,(item["userID"][0],item['educationName'][x],item['institutionName'][x],item['institutionCity'][x],item['institutionCountry'][x],item['gradePercentage'][x],"2022-01-01","2022-01-01",item['educationMode'][x],item['userID'][0]))
            mydb.commit()
            #print(item["userID"][0],item['educationName'][x],item['institutionName'][x],item['institutionCity'][x],item['institutionCountry'][x],item['gradePercentage'][x],"2022-01-01","2022-01-01",item['educationMode'][x])
            
        else:
            sql="update tbl_user_education set User_Education=%s,User_Education_Inistitute_Name=%s,User_Educatin_Inistitute_City=%s,User_Educatin_Inistitute_Country=%s,User_Education_Grade_Percentage=%s,User_Education_Passout_Start_Date=%s,User_Education_Passout_End_Year=%s,User_Education_Mode=%s,created_date=current_timestamp() where Education_Id=%s"
            mycursor.execute(sql,(item['educationName'][x],item['institutionName'][x],item['institutionCity'][x],item['institutionCountry'][x],item['gradePercentage'][x],"2022-01-01","2022-01-01",item['educationMode'][x],item["educationID"][x],))
            mydb.commit()
            #print(item['educationName'][x],item['institutionName'][x],item['institutionCity'][x],item['institutionCountry'][x],item['gradePercentage'][x],"2022-01-01","2022-01-01",item['educationMode'][x],item["educationID"][0],)

            
    experienceId=item['experienceID']
    for x in range(0,len(experienceId)):
        if(experienceId[x]=='new'):
            sql="insert into tbl_user_experience(User_ID,User_Work_Exp_Company, User_Work_Exp_Disignation, User_Work_Exp_From_Date,User_Work_Exp_To_Date,User_Exp_Type,Created_By) values(%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql,(item["userID"][0],item['experienceCompany'][x],item['experienceDesignation'][x],"2022-01-01","2022-01-01",item['experienceType'][x],item['userID'][0]))
            mydb.commit()
        else:
            sql="update tbl_user_experience set User_Work_Exp_Company=%s,User_Work_Exp_Disignation=%s,User_Work_Exp_From_Date=%s,User_Work_Exp_To_Date=%s,User_Exp_Type=%s,created_date=current_timestamp() where User_Exp_ID=%s"
            mycursor.execute(sql,(item['experienceCompany'][x],item['experienceDesignation'][x],"2022-01-01","2022-01-01",item['experienceType'][x],item["experienceID"][x],))
            mydb.commit()
            #print(item['experienceCompany'][x],item['experienceDesignation'][x],"2022-01-01","2022-01-01",item['experienceType'][x],item["experienceID"][0],)

    activityId=item['activityID']
    for x in range(0,len(activityId)):
        if(activityId[x]=='new'):
            sql="insert into tbl_user_activities(User_ID,User_Activity_name, User_Activity_Description, User_Awards,User_Papers_Submitted,User_AnyOther_Information,User_Languages_Known,User_Known_Tools,User_Known_Computer_Languages,tbl_user_activitiescol,Created_By) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql,(item["userID"][0],item['activityName'][x],item['activityDescription'][x],item['awards'][x],item['papersSubmitted'][x],item['anyOtherInformation'][x],item['languagesKnown'][x],item['knownTools'][x],item['knownComputerLanguages'][x],item['activitiesCol'][x],item['userID'][0]))
            mydb.commit()
        else:
            sql="update tbl_user_activities set User_Activity_name=%s,User_Activity_Description=%s,User_Awards=%s,User_Papers_Submitted=%s,User_AnyOther_Information=%s,User_Languages_Known=%s,User_Known_Tools=%s,User_Known_Computer_Languages=%s,tbl_user_activitiescol=%s,created_date=current_timestamp() where User_Activity_Id=%s"
            mycursor.execute(sql,(item['activityName'][x],item['activityDescription'][x],item['awards'][x],item['papersSubmitted'][x],item['anyOtherInformation'][x],item['languagesKnown'][x],item['knownTools'][x],item['knownComputerLanguages'][x],item['activitiesCol'][x],item["activityID"][x],))
            mydb.commit()

    socailmediaId=item['socialmediaID']
    for x in range(0,len(socailmediaId)):
        if(socailmediaId[x]=='new'):
            sql="insert into tbl_user_scocial_media(User_ID,User_ScMedia_Description, User_ScMedia_link,Created_By,created_date) values(%s,%s,%s,%s,current_timestamp())"
            mycursor.execute(sql,(item["userID"][0],item['socialMediaDescription'][x],item['socialMediaLink'][x],item['userID'][0]))
            mydb.commit()
        else:
            sql="update tbl_user_scocial_media set User_ScMedia_Description=%s,User_ScMedia_link=%s,created_date=current_timestamp() where User_SocMedia_Id=%s"
            mycursor.execute(sql,(item['socialMediaDescription'][x],item['socialMediaLink'][x],item['socialmediaID'][x]))
            mydb.commit()
    

    techskillsId=item['techSkillId']
    for x in range(0,len(techskillsId)):
        if(techskillsId[x]=='new'):
            sql="insert into tbl_user_tech_skills (User_ID,Tech_Skill_Description,Created_By) values(%s,%s,%s)"
            mycursor.execute(sql,(item["userID"][0],item['techSkillDescription'][x],item['userID'][0],))
            mydb.commit()
        else:
            sql="update tbl_user_tech_skills set Tech_Skill_Description=%s,created_date=current_timestamp() where Tech_Skills_ID=%s"
            mycursor.execute(sql,(item['techSkillDescription'][x],item['techSkillId'][x],))
            mydb.commit()

    profsummId=item['profSummId']
    for x in range(0,len(profsummId)):
        if(profsummId[x]=='new'):
            sql="insert into tbl_user_prof(User_ID,User_Prof_summary,Created_By) values(%s,%s,%s)"
            mycursor.execute(sql,(item["userID"][0],item['profSummary'][x],item['userID'][0]))
            mydb.commit()
        else:
            sql="update tbl_user_prof set User_Prof_summary=%s,created_date=current_timestamp() where User_Prof_Id=%s"
            mycursor.execute(sql,(item['profSummary'][x],item['profSummId'][x],))
            mydb.commit()



   

    #for showing personal ionfotmation
    sql = "SELECT * FROM tbl_user_master WHERE User_Id=%s"
    mycursor.execute(sql,(userID,))
    personalInfoRows = mycursor.fetchone()
    mydb.commit()
    #getting projects
    sql = "SELECT * FROM tbl_user_projects WHERE User_Id=%s"
    mycursor.execute(sql,(userID,))
    projects = mycursor.fetchall()
    mydb.commit()
    #getting experience
    sql = "SELECT * FROM tbl_user_experience WHERE User_Id=%s"
    mycursor.execute(sql,(userID,))
    experienceRows = mycursor.fetchall()
    mydb.commit()
    #getting skills
    sql = "SELECT * FROM tbl_user_tech_skills WHERE User_Id=%s"
    mycursor.execute(sql,(userID,))
    skillRows = mycursor.fetchall()
    mydb.commit()
    #getting activities
    sql = "SELECT * FROM tbl_user_activities WHERE User_Id=%s"
    mycursor.execute(sql,(userID,))
    activitiesRows = mycursor.fetchall()
    mydb.commit()
    #getting scmedia details
    sql = "SELECT * FROM tbl_user_scocial_media WHERE User_Id=%s"
    mycursor.execute(sql,(userID,))
    socialmediaRows = mycursor.fetchall()
    mydb.commit()
    #getting education details
    sql = "SELECT * FROM tbl_user_education WHERE User_Id=%s"
    mycursor.execute(sql,(userID,))
    educationRows = mycursor.fetchall()
    #getting user prof summary
    sql = "SELECT * FROM tbl_user_prof WHERE User_Id=%s"
    mycursor.execute(sql,(userID,))
    profsumRows = mycursor.fetchall()
    mydb.commit()

    #updating status of form
    #print(item['typeOfSave'][0])

    if(item['typeOfSave'][0]=="savedByEditor"):
        sql="UPDATE tbl_resume SET Status_ID=5,Assigned_Date_Time=CURRENT_TIMESTAMP() WHERE resume_id=%s"
        mycursor.execute(sql,(item['resumeId'][0],))
        mydb.commit()

    if(item['typeOfSave'][0]=="submitedByEditor"):
        sql="UPDATE tbl_resume SET Status_ID=6,Assigned_Date_Time=CURRENT_TIMESTAMP() WHERE resume_id=%s"
        mycursor.execute(sql,(item['resumeId'][0],))
        mydb.commit()

        


    if(item['typeOfSave'][0]=="submitedByUser"):
        sql="UPDATE tbl_resume SET Status_ID=2, Assign_to=200,Assigned_Date_Time=CURRENT_TIMESTAMP() WHERE resume_id=%s"
        mycursor.execute(sql,(item['resumeId'][0],))
        mydb.commit()
        # print("status changed")
        # print(item['resumeId'][0])

    


    context={
            'userID':userID,
            'personalInfo':personalInfoRows,
            'projects':projects,
            'experiences':experienceRows,
            'skills':skillRows,
            'educations':educationRows,
            'activities':activitiesRows,
            'socialmedias':socialmediaRows,
            'technicalskills':skillRows,
            'professionalsummaries':profsumRows
    }
    return render(request,'saved.html',context)


def form(request):
    if request.method == 'POST':
        post=dict(request.POST)
        userID=post['userId'][0]

        sql = "SELECT * FROM tbl_user_master WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        personalInfoRows = mycursor.fetchone()
        mydb.commit()
        #getting projects
        sql = "SELECT * FROM tbl_user_projects WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        projects = mycursor.fetchall()
        mydb.commit()
        #getting experience
        sql = "SELECT * FROM tbl_user_experience WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        experienceRows = mycursor.fetchall()
        mydb.commit()
        #getting skills
        sql = "SELECT * FROM tbl_user_tech_skills WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        skillRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_activities WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        activitiesRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_scocial_media WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        socialmediaRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_education WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        educationRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_prof WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        profsumRows = mycursor.fetchall()
        mydb.commit()

        context={
            'userID':userID,
            'resumeId':post['resumeId'][0],
            'personalInfo':personalInfoRows,
            'projects':projects,
            'experiences':experienceRows,
            'skills':skillRows,
            'sampledate':"5",
            'educations':educationRows,
            'activities':activitiesRows,
            'socialmedias':socialmediaRows,
            'technicalskills':skillRows,
            'professionalsummaries':profsumRows,
            'setdate':"4"
        }
        return render(request,'form.html',context)


    else:
        return render(request, 'authentication.html')
    

def form1(request):
    if request.method == 'POST':
        post=dict(request.POST)
        userID=post['userId'][0]

        sql = "SELECT * FROM tbl_user_master WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        personalInfoRows = mycursor.fetchone()
        mydb.commit()
        #getting projects
        sql = "SELECT * FROM tbl_user_projects WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        projects = mycursor.fetchall()
        mydb.commit()
        #getting experience
        sql = "SELECT * FROM tbl_user_experience WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        experienceRows = mycursor.fetchall()
        mydb.commit()
        #getting skills
        sql = "SELECT * FROM tbl_user_tech_skills WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        skillRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_activities WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        activitiesRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_scocial_media WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        socialmediaRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_education WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        educationRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_prof WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        profsumRows = mycursor.fetchall()
        mydb.commit()

        context={
            'userID':userID,
            'resumeId':post['resumeId'][0],
            'personalInfo':personalInfoRows,
            'projects':projects,
            'experiences':experienceRows,
            'skills':skillRows,
            'educations':educationRows,
            'activities':activitiesRows,
            'socialmedias':socialmediaRows,
            'technicalskills':skillRows,
            'professionalsummaries':profsumRows,
            'setdate':"4"
        }
        return render(request,'form1.html',context)


    else:
        return render(request, 'authentication.html')
    



def editingscreen(request):
    if request.method == 'POST':
        post=dict(request.POST)
        userID=post['userId'][0]

        sql = "SELECT * FROM tbl_user_master WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        personalInfoRows = mycursor.fetchone()
        mydb.commit()
        #getting projects
        sql = "SELECT * FROM tbl_user_projects WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        projects = mycursor.fetchall()
        mydb.commit()
        #getting experience
        sql = "SELECT * FROM tbl_user_experience WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        experienceRows = mycursor.fetchall()
        mydb.commit()
        #getting skills
        sql = "SELECT * FROM tbl_user_tech_skills WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        skillRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_activities WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        activitiesRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_scocial_media WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        socialmediaRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_education WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        educationRows = mycursor.fetchall()
        mydb.commit()
        sql = "SELECT * FROM tbl_user_prof WHERE User_Id=%s"
        mycursor.execute(sql,(userID,))
        profsumRows = mycursor.fetchall()
        mydb.commit()

        context={
            'userID':userID,
            'resumeId':post['resumeId'][0],
            'personalInfo':personalInfoRows,
            'projects':projects,
            'experiences':experienceRows,
            'skills':skillRows,
            'sampledate':"5",
            'educations':educationRows,
            'activities':activitiesRows,
            'socialmedias':socialmediaRows,
            'technicalskills':skillRows,
            'professionalsummaries':profsumRows,
            'setdate':"4"
        }
        return render(request,'editingscreen.html',context)
    else:
        return render(request,'home.html')



def test(request):
    return render(request,'test.html')


def ajax(request):
    if request.method == 'POST':
        data= dict(request.POST)
        def deleteQuery(tableName,columnName,Id):
            sql="DELETE FROM %s WHERE %s=%s" % (tableName,columnName,Id)
            mycursor.execute(sql)
            mydb.commit()
        deleteQuery(data['tableName'][0],data['columnName'][0],data['Id'][0])
        return JsonResponse({'status':'deleted'})

    else:
        return JsonResponse({'status':'error'})

    return JsonResponse({'status':'error'})

def assign(request):
    if request.method == 'POST':
        data= dict(request.POST)
        resumeId=data['resumeId'][0]
        userId=data['userId'][0]
        assignToId=data['assignToId'][0]
        sql="UPDATE tbl_resume SET Status_Id=3, Assign_to=%s,Assigned_By=%s WHERE Resume_Id=%s"
        mycursor.execute(sql,(assignToId,userId,resumeId))
        return JsonResponse({'status':'assigned'})

    else:
        return JsonResponse({'status':'error'})
    
def accept(request):
    if request.method == 'POST':
        data= dict(request.POST)
        resumeId=data['resumeId'][0]
        status=data['status'][0]
        userId=data['userId'][0]
        if(status=="decline"):
            sql="UPDATE tbl_resume SET Status_Id=2,assign_to=%s,assigned_by=%s,previous_status=%s WHERE Resume_Id=%s"
            mycursor.execute(sql,("200",userId,"3",resumeId))
            return JsonResponse({'status':'changed'})
        
        if(status=="accept"):
            sql="UPDATE tbl_resume SET Status_Id=4,previous_status=3 WHERE Resume_Id=%s"
            mycursor.execute(sql,(resumeId,))
            return JsonResponse({'status':'changed'})

    else:
        return JsonResponse({'status':'error'})

def package(request):
    if request.method == 'POST':
        data= dict(request.POST)
        userId=data["userId"][0]
        packageId = data['packageId'][0]
        sql="INSERT INTO tbl_resume (user_id,status_id,assign_to,assigned_by,previous_status,package_id) VALUES(%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql,(userId,"1","200","300","11",packageId))
        return JsonResponse({'status':'purchased'})

    else:
        return JsonResponse({'status':'error'})

def uploadcv(request):
    if request.method == 'POST':
        userId=request.POST["userId"][0]
        resumeId=request.POST["resumeId"][0]
        resume = request.FILES['UserCV']
        handle_uploaded_file(resume)
        return JsonResponse({'status':' thank you resume uploaded succesfully'})
    else:
        return JsonResponse({'status':'error'})

def handle_uploaded_file(f):
    with open('static/resumes/cv.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def acceptresume(request):
    if request.method == 'POST':
        data= dict(request.POST)
        resumeId=data["resumeId"][0]
        sql="UPDATE tbl_resume SET status_id=%s, assigned_date_time=current_timestamp() WHERE resume_id= %s"
        mycursor.execute(sql,("7",resumeId))
        return JsonResponse({'status':'accepted'})
    else:
        return JsonResponse({'status':'error'})

def addcomments(request):
    if request.method == 'POST':
        data= dict(request.POST)
        resumeId=data["resumeId"][0]
        comments= data["comments"][0]
        sql="UPDATE tbl_resume SET status_id=%s,comments=%s, assigned_date_time=current_timestamp() WHERE resume_id= %s"
        mycursor.execute(sql,("5",comments,resumeId))
        return JsonResponse({'status':'commented'})
    else:
        return JsonResponse({'status':'error'})

def updatepackages(request):
    if request.method == 'POST':
        data= dict(request.POST)
        packageId = data['packageId']
        for x in range(0,len(packageId)):
            sql="UPDATE cview_services_master SET service_amount = %s, created_date = current_timestamp() WHERE cv_service_id=%s"
            mycursor.execute(sql,(data['packagePrice'][x],data['packageId'][x],))
        return JsonResponse({'status':'updated'})
    else:
        return JsonResponse({'status':'error'})
    
def feedback(request):
    if request.method=='POST':
        hear = request.POST.get("hear")
        visit= request.POST.get("visit")
        email= request.POST.get("email")
        rate = request.POST.get("rate")
        editor = request.POST.get("editor")
        website = request.POST.get("website")
        sql = """ INSERT INTO feedback (platform, visit_again,email,rating,feedback_editor,feedback_website) VALUES (%s,%s,%s,%s,%s,%s)"""
        mycursor.execute(sql,(hear,visit,email,rate,editor,website,))
        mydb.commit()
        
        return JsonResponse({'status':'thank you for your feedback'})
    return JsonResponse({'status':'error'})
    
def createUpdateEmployee(request):
    if request.method == 'POST':
        data = dict(request.POST)
        if(data['createOrUpdate'][0]=="create"):
            query= "INSERT INTO tbl_user_master (User_Last_Name,User_First_Name,User_Middle_Name,User_eMail,User_Mobile_Number,User_Alternative_Number,user_password) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,(data["lname"][0],data["fname"][0],data["mname"][0],data["email"][0],data["mobile"][0],data["almobile"][0],data["password"][0],))
            mydb.commit()
            return JsonResponse({'status':'created'})
        
        if(data['createOrUpdate'][0]=="update"):
            query="UPDATE tbl_user_master SET user_last_name=%s,User_First_Name=%s,User_Middle_Name=%s,User_eMail=%s,User_Mobile_Number=%s,User_Alternative_Number=%s,user_password=%s,created_date=current_timestamp() WHERE user_id=%s"
            mycursor.execute(query,(data["lname"][0],data["fname"][0],data["mname"][0],data["email"][0],data["mobile"][0],data["almobile"][0],data['password'][0],data["employeeId"][0]))
            mydb.commit()
            return JsonResponse({'status':'updated'})
        
    return JsonResponse({'status':'error'})


from django.core.files.storage import FileSystemStorage
from pypdf import PdfReader
import re
import pdfplumber
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from urlextract import URLExtract


def ats(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['UserCV']
        email=request.POST['email']
        
        fs = FileSystemStorage("static/resumes")
        name = fs.save(email+".pdf" , uploaded_file)
        File_url = fs.url(name)
        CV_Report=""
        reader = PdfReader(uploaded_file)
        wordList={ ' i ': 0,' am ': 0,' you ': 0,' our ': 0,' a ': 0,' an ': 0,' the ' : 0}
        SPLChrList = []
        
        Doc_word_count=0
        URL_count=0
        URL_Page_count=0
        IMG_count=0
        SPLCHR_count=0
        for page in reader.pages:
                page_data   = page.extract_text()
                regex = re.compile('[_!#$%^&*<>?\|}{~]')          
                
                x=regex.findall(page_data)
                SPLChrList= SPLChrList + x
                SPLCHR_count=SPLCHR_count+len(x)
 
                for word in wordList :
                    word_count = page_data.lower().count(word)
                    Doc_word_count=Doc_word_count+ word_count
                    wordList[word] = word_count + wordList[word] 
                   
                URL_count =find_url(page_data)
                URL_Page_count=URL_count+URL_Page_count
                try:
                    image_list =  page.images
                    IMG_count=IMG_count + len(image_list)
                except ValueError: 
                    print ("not enough image data")
                
        
        fontList=[] 
        verb_count=0
        Num_count=0
        pdf_file = pdfplumber.open(uploaded_file)
        for p, char in zip(pdf_file.pages, pdf_file.chars):
            words = p.extract_words(keep_blank_chars=True)
            texts = p.extract_text()
            fontList.append(char['fontname'])
            verb_count =verb_count+ count_verbs(texts)
            array = getNumbers(texts)
            Num_count=Num_count+ len(array)
 
        fontList = list(dict.fromkeys(fontList))
 
        fonts_allowed=""
        fonts_not_allowed=""
        for font in fontList:
            left = '+'
            right = ','
            # font= font[font.index(left)+len(left):font.index(right)]
            if font.find("Arial") >= 0 or font.find("Calibri") >= 0 :
                 fonts_allowed="  " + fonts_allowed +" "+font 
            else:
                   fonts_not_allowed=" "  + fonts_not_allowed +" "  +font 
     
        CV_Report=   CV_Report + 'Number of Images     :  ' + str(IMG_count) +'\n'
        CV_Report=   CV_Report + 'Number of urls       :  ' + str(URL_Page_count) +'\n'
        CV_Report=   CV_Report + 'special char count   :  ' + str(SPLCHR_count)+'\n'
        CV_Report=   CV_Report + 'Special words count  :  ' +str(Doc_word_count)+'\n'
        CV_Report=   CV_Report + "Number of verbs      :  "+str(verb_count)+'\n' 
        CV_Report=   CV_Report + "Number of Numbers    :  " +str(Num_count)+'\n' 
        CV_Report=   CV_Report + "fonts allowed        :  " + fonts_allowed    +'\n' 
        CV_Report=   CV_Report + "fonts not allowed    :  " + fonts_not_allowed    +'\n'  

        ATS_Score= 100 - (IMG_count+URL_Page_count+SPLCHR_count+Doc_word_count)*0.5
        CV_Report=   CV_Report + '\n'+ "ATS Score :  " +   str(ATS_Score)   +'\n'  
        
        context={
            'ats':ATS_Score
        }
        sql="INSERT INTO tbl_un_registered_user (ur_email,Created_By)  VALUES(%s,%s)"
        mycursor.execute(sql,(email,email))
        mydb.commit()
        return render(request,'ats.html',context)
    else:
        return render(request,'ats.html')


def find_url(string):
    extractor = URLExtract()
    urls = extractor.find_urls(string)
    return len(urls)





def count_verbs(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    # POS tag the tokens
    tagged_tokens = pos_tag(tokens)
    # # Initialize a counter
    verb_count = 0
    # # Iterate through the tagged tokens
    # print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
    for token in tagged_tokens:
    #     # Check if the token is a verb (POS tag "VB")
     if token[1].startswith("VB"):
          verb_count += 1
    return verb_count
# Function to extract all the numbers from the given string
def getNumbers(str):
    array = re.findall(r'[0-9]+', str)
    return array


