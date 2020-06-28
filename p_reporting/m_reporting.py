import time


def export_final_results(path_to,df_all_countries_agegroup,df_by_country_age_group,df_answer_for,df_answer_against,option_country,df_all):
    path_to = '/home/usuario/Documentos/Ironhack/Project_1_0420_JuanMunoz/data/results'
    df_all_countries_agegroup.to_csv(f'{path_to}/results_all_countries.csv', index=True, header=True, sep=';')
    df_by_country_age_group.to_csv(f'{path_to}/results_{option_country}.csv', index=True, header=True, sep=';')
    df_answer_for.to_csv(f'{path_to}/df_answer_for.csv', index=False, header=True, sep=';')
    df_answer_against.to_csv(f'{path_to}/df_answer_against.csv', index=False, header=True, sep=';')
    df_all.to_csv(f'{path_to}/df_all.csv', index=False, header=True, sep=';')
    time.sleep(3)
    print('CSV exporting process has finished successfully!')
    time.sleep(2)
    print('-----------------------------------------------------------------------------------------------------------')

def sending_email(to_address,option_user,option_country):
    # libraries to be imported
    print('Sending email...')
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    fromaddr = "juancamilomunoz498@gmail.com" # <--------------------------------------  Cuenta envío
    toaddr = to_address # <----------------------------------------  Email receptor
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = fromaddr
    # storing the receivers email address
    msg['To'] = toaddr
    # storing the subject
    msg['Subject'] = "Project Report Ironhack - Juan Munoz"
    # string to store the body of the mail
    body = '''Hola!,
    Atthached you will find the age report!
    Regards,
    Juan Muñoz'''
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    # open the file to be sent
    if option_user == 1:
        filename = "results_all_countries.csv"
        attachment = open("/home/usuario/Documentos/Ironhack/Project_1_0420_JuanMunoz/data/results/results_all_countries.csv", "rb")  # <--------------------------------------  Attachements
    else:
        filename = f'results_{option_country}.csv'
        attachment = open(
            f"/home/usuario/Documentos/Ironhack/Project_1_0420_JuanMunoz/data/results/results_{option_country}.csv",
            "rb")  # <--------------------------------------  Attachements
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    # encode into base64
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    s.starttls()
    # Authentication
    s.login(fromaddr, "__________________") # <----------------------------------------  Contraseña de aplicación
    # Converts the Multipart msg into a string
    text = msg.as_string()
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    # terminating the session
    s.quit()
    print('Email sent!')
