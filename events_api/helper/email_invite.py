import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import os,datetime

def email_invite(details):
    CRLF = "\r\n"
    #gmail_uid = "oliverbrylle@gmail.com"
    #gmail_password = "Johann@2014"
    attendees = details["email"] #["oliversoh@gmail.com"]
    start_timestamp = details["start_timestamp"]
    end_timestamp = details["end_timestamp"]
    event_name = details["name"]

    organizer = "ORGANIZER;CN=organiser:mailto:first"+CRLF+" @gmail.com"
    fro = "Events_API <events_api@gmail.com>"

    ddtstart = datetime.datetime.strptime(details.get("start_timestamp"), '%Y-%m-%d %H:%M:%S')
    dtoff = datetime.timedelta(days = 1)
    dur = datetime.timedelta(hours = 1)
    dtend = datetime.datetime.strptime(details.get("end_timestamp"), '%Y-%m-%d %H:%M:%S')
    dtstamp = ddtstart.strftime("%Y%m%dT%H%M%SZ")
    dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
    dtend = dtend.strftime("%Y%m%dT%H%M%SZ")

    description = "DESCRIPTION: EVENTS_API invitation: " + details.get("name") + CRLF
    attendee = ""
    for att in attendees:
        attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+CRLF+" ;CN="+att+";X-NUM-GUESTS=0:"+CRLF+" mailto:"+att+CRLF
    ical = "BEGIN:VCALENDAR"+CRLF+"PRODID:pyICSParser"+CRLF+"VERSION:2.0"+CRLF+"CALSCALE:GREGORIAN"+CRLF
    ical+="METHOD:REQUEST"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTART:"+dtstart+CRLF+"DTEND:"+dtend+CRLF+"DTSTAMP:"+dtstamp+CRLF+organizer+CRLF
    ical+= "UID:FIXMEUID"+dtstamp+CRLF
    ical+= attendee+"CREATED:"+dtstamp+CRLF+description+"LAST-MODIFIED:"+dtstamp+CRLF+"LOCATION:"+CRLF+"SEQUENCE:0"+CRLF+"STATUS:CONFIRMED"+CRLF
    ical+= "SUMMARY:" + details.get("name") + " " +ddtstart.strftime("%Y%m%d @ %H:%M")+CRLF+"TRANSP:OPAQUE"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF

    eml_body = "Email body visible in the invite of outlook and outlook.com but not google calendar"
    eml_body_bin = "This is the email body in binary - two steps"
    msg = MIMEMultipart('mixed')
    msg['Reply-To']=fro
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "Events_API invite " + details.get("name")
    msg['From'] = fro
    msg['To'] = ",".join(attendees)

    part_email = MIMEText(eml_body,"html")
    part_cal = MIMEText(ical,'calendar;method=REQUEST')

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    ical_atch = MIMEBase('application/ics',' ;name="%s"'%("invite.ics"))
    ical_atch.set_payload(ical)
    #encoders.encode_base64(ical_atch)
    ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"'%("invite.ics"))

    eml_atch = MIMEBase('text/plain','')
    #encoders.encode_base64(eml_atch)
    eml_atch.add_header('Content-Transfer-Encoding', "")

    msgAlternative.attach(part_email)
    msgAlternative.attach(part_cal)

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(os.environ.get('gmail_uid'), os.environ.get('gmail_password'))
    #mailServer.login(gmail_uid, gmail_password)
    mailServer.sendmail(fro, attendees, msg.as_string())
    mailServer.close()
