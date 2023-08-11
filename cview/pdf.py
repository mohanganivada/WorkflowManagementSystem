from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.platypus.flowables import Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfdoc
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_RIGHT
import mysql.connector
from pdf2docx import Converter

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="vista1"
)
mycursor = mydb.cursor()



def generateResume(userID):
    # Import our font
    registerFont(TTFont('Inconsolata', 'static/fonts/Inconsolata-Regular.ttf'))
    registerFont(TTFont('InconsolataBold', 'static/fonts/Inconsolata-Bold.ttf'))
    registerFontFamily('Inconsolata', normal='Inconsolata', bold='InconsolataBold')

    # Set the page height and width
    HEIGHT = 11 * inch
    WIDTH = 8.5 * inch

    # Set our styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Content',
                            fontFamily='Inconsolata',
                            fontSize=8,
                            spaceAfter=.1*inch))
                                


    def generate_print_pdf(data, contact):

        # sql = "SELECT * FROM tbl_user_master WHERE User_Id=3"
        # mycursor.execute(sql)
        # result= mycursor.fetchone()
        # mydb.commit()
        # print(result)
        # print(len(result))
        
        pdfname = 'static/resumes/%s.pdf' % (userID)
        doc = SimpleDocTemplate(
            pdfname,
            pagesize=letter,
            bottomMargin=.5 * inch,
            topMargin=.7 * inch,
            rightMargin=.4 * inch,
            leftMargin=.4 * inch)  # set the doc template
        style = styles["Normal"]  # set the style to normal
        story = []  # create a blank story to tell
        contentTable = Table(
            data,
            colWidths=[
                0.8 * inch,
                6.9 * inch])
        tblStyle = TableStyle([
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('FONT', (0, 0), (-1, -1), 'Inconsolata'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT')])
        contentTable.setStyle(tblStyle)
        story.append(contentTable)
        doc.build(
            story,
            onFirstPage=myPageWrapper(
                contact)
            )
        return pdfname


    """
        Draw the framework for the first page,
        pass in contact info as a dictionary
    """
    def myPageWrapper(contact):
        # template for static, non-flowables, on the first page
        # draws all of the contact information at the top of the page
        def myPage(canvas, doc):
            canvas.saveState()  # save the current state
            canvas.setFont('InconsolataBold', 16)  # set the font for the name
            canvas.drawString(
                .4 * inch,
                HEIGHT - (.4 * inch),
                contact['name'])  # draw the name on top left page 1
            canvas.setFont('Inconsolata', 8)  # sets the font for contact
            canvas.drawRightString(
                WIDTH - (.4 * inch),
                HEIGHT - (.4 * inch),
                contact['website'])  
            canvas.line(.4 * inch, HEIGHT - (.47 * inch), 
                WIDTH - (.4 * inch), HEIGHT - (.47 * inch))
            canvas.drawString(
                .4 * inch,
                HEIGHT - (.6 * inch),
                contact['phone'])
            canvas.drawCentredString(
                WIDTH / 2.0,
                HEIGHT - (.6 * inch),
                contact['address'])
            canvas.drawRightString(
                WIDTH - (.4 * inch),
                HEIGHT - (.6 * inch),
                contact['email'])
            # restore the state to what it was when saved
            canvas.restoreState()
        return myPage

    if __name__ == "__main__":
        sql_qry1 = "SELECT * FROM tbl_user_master WHERE User_Id=%s" % (userID)
        sql_qry2 = "SELECT * FROM tbl_user_education WHERE User_Id=%s" % (userID)
        sql_qry3 = "SELECT * FROM tbl_user_experience WHERE User_Id=%s" % (userID)
        sql_qry4 = "SELECT * FROM tbl_user_projects WHERE User_Id=%s" % (userID)
        sql_qry5 = "SELECT * FROM tbl_user_prof WHERE User_Id=%s" % (userID)
        sql_qry6 = "SELECT * FROM tbl_user_tech_skills WHERE User_Id=%s" % (userID)
        sql_qry7 = "SELECT * FROM tbl_user_activities WHERE User_Id=%s" % (userID)
        sql_qry8 = "SELECT * FROM tbl_user_scocial_media WHERE User_Id=%s" % (userID)

        mycursor.execute(sql_qry1)
        result= mycursor.fetchall()
        #mydb.commit()
        #print(result)
        info_list=[]
        info_main=[]
        for i in range(len(result)):
            info_list.append(result[i])
            print(info_list)
            for j in range(2,len(info_list[i])):
                info_main.append(info_list[i][j])
            info_main.append('<br></br>')
        print(info_main)

        
        mycursor.execute(sql_qry2)
        result1= mycursor.fetchall()
        #mydb.commit()
        edu_list=[]
        edu_main=[]
        for i in range(len(result1)):
            edu_list.append(result1[i])
            for j in range(2,len(edu_list[i])):
                edu_main.append(edu_list[i][j])
                edu_main.append(' ')
            
            edu_main.append('<br></br>')
    


        
        mycursor.execute(sql_qry3)
        result2= mycursor.fetchall()
        exp_list=[]
        exp_main=[]
        for i in range(len(result2)):
            exp_list.append(result2[i])
            for j in range(2,len(exp_list[i])):
                exp_main.append(exp_list[i][j])
                exp_main.append(' ')
            exp_main.append('<br></br>')
        


        mycursor.execute(sql_qry4)
        result3= mycursor.fetchall()
        #mydb.commit()
        proj_list=[]
        proj_main=[]
        for i in range(len(result3)):
            proj_list.append(result3[i])
            for j in range(2,len(proj_list[i])):
                proj_main.append(proj_list[i][j])
                proj_main.append(' ')
            proj_main.append('<br></br>')
        


    
        mycursor.execute(sql_qry5)
        result4= mycursor.fetchall()
        #mydb.commit()
        profs_list=[]
        profs_main=[]
        for i in range(len(result4)):
            profs_list.append(result4[i])
            for j in range(2,len(profs_list[i])):
                profs_main.append(profs_list[i][j])
                profs_main.append(' ')
        



        mycursor.execute(sql_qry6)
        result5= mycursor.fetchall()
        #mydb.commit()
        skills_list=[]
        skills_main=[]
        for i in range(len(result5)):
            skills_list.append(result5[i])
            for j in range(2,len(skills_list[i])):
                skills_main.append(skills_list[i][j])
                skills_main.append(',')



        mycursor.execute(sql_qry7)
        result6= mycursor.fetchall()
        #mydb.commit()
        activ_list=[]
        activ_main=[]
        for i in range(len(result6)):
            activ_list.append(result6[i])
            for j in range(2,len(activ_list[i])):
                activ_main.append(activ_list[i][j])
                activ_main.append(' ')


        mycursor.execute(sql_qry8)
        result7= mycursor.fetchall()
        #mydb.commit()
        soc_list=[]
        soc_main=[]
        for i in range(len(result7)):
            soc_list.append(result7[i])
            for j in range(2,len(soc_list[i])):
                soc_main.append(soc_list[i][j])
                soc_main.append(',')
            soc_main.append('<br></br>')

            
        contact = {
            'name': ' '.join(info_main[1:4]),
            'website':' '.join(soc_main[3]) ,
            'email': str(info_main[6]),
            'address': 'Andhra Pradesh ,Vizianagaram, 535221',
            'phone': str(info_main[7])
            }
        data = {
            
            'education':
                        [(' '.join(str(v) for v in edu_main))],

            'experience':[(' '.join(str(v) for v in exp_main))],

            'summary': [(' '.join(str(v) for v in profs_main))],

            'projects':[(' '.join(str(v) for v in proj_main))],

            'skills':[(' '.join(str(v) for v in skills_main))],

            'activities':[(' '.join(str(v) for v in activ_main))],

            'socailmedia':[(' '.join(str(v) for v in soc_main))],
        }
            
        #print(data['education'])
        tblData = [
            ['EDUCATION', [Paragraph(x, styles['Content']) for x in data['education']]],
            ['EXPERINCE',[Paragraph(x, styles['Content']) for x in data['experience']]],
            ['SUMMARY',[Paragraph(x, styles['Content']) for x in data['summary']]],
            ['PROJECTS',[Paragraph(x, styles['Content']) for x in data['projects']]] ,
            ['ACTIVITIES', [Paragraph(x, styles['Content']) for x in data['activities']]],
            ['SOCAIL MEDIA',[Paragraph(x, styles['Content']) for x in data['socailmedia']]],
            ['SKILLS', [Paragraph(x, styles['Content']) for x in data['skills']]],
        ]
        generate_print_pdf(tblData, contact)




    try:
        # Converting PDF to Docx
        cv_obj = Converter('static/resumes/%s.pdf' % (userID))
        cv_obj.convert('static/resumes/%s.docx' % (userID) )
        cv_obj.close()

    except:
        print('Conversion Failed')
        
    else:
        print('File Converted Successfully')
