# import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from threading import Thread

PORT = 2525
HOST = "sandbox.smtp.mailtrap.io"
USERNAME = "44b56349d5df35"
PASSWORD = "5703b0a77fc4d1"

class OtpThread(Thread):
  def __init__(self, user,otp):
    print("Sending Email")
    self.otp = otp
    self.user = user
    Thread.__init__(self)
    
  def run(self):
    send_otp(self.otp,self.user)
    
def send_otp(otp,user):
  print("Sending Email")
  otp = str(otp) 
  html = """<section>
  <div class="title">GIFSHION</div>
  <svg width="250" height="200" viewBox="0 0 292 208" fill="none" xmlns="http://www.w3.org/2000/svg">
    <g clip-path="url(#clip0_1_45)">
      <path d="M152.106 208C201.536 208 241.606 167.93 241.606 118.5C241.606 69.0706 201.536 29 152.106 29C102.676 29 62.6058 69.0706 62.6058 118.5C62.6058 167.93 102.676 208 152.106 208Z" fill="#C5FFFF" />
      <path d="M117.144 64.4241C113.81 64.4241 111.108 67.1261 111.108 70.46V167.057C111.108 170.391 113.81 173.093 117.144 173.093H186.572C189.906 173.093 192.608 170.391 192.608 167.057V92.382L163.507 64.4241H117.144Z" fill="#91E4FF" />
      <path d="M192.608 92.382H169.544C166.21 92.382 163.508 89.68 163.508 86.3461V64.4241L192.608 92.382Z" fill="#0CB4EA" />
      <path d="M162.304 131.646C162.304 135.494 159.185 138.613 155.339 138.613H104.483C100.635 138.613 97.5186 135.494 97.5186 131.646V110.363C97.5186 106.515 100.635 103.397 104.483 103.397H155.339C159.185 103.397 162.304 106.515 162.304 110.363V131.646Z" fill="#0CB4EA" />
      <path d="M117.094 114.409C118.563 114.409 119.825 114.707 120.876 115.302C121.93 115.897 122.728 116.745 123.267 117.843C123.807 118.941 124.079 120.23 124.079 121.712C124.079 122.808 123.932 123.803 123.635 124.697C123.338 125.592 122.894 126.369 122.302 127.025C121.71 127.681 120.981 128.184 120.119 128.532C119.257 128.879 118.266 129.053 117.153 129.053C116.044 129.053 115.054 128.875 114.178 128.518C113.302 128.16 112.571 127.657 111.985 127.005C111.398 126.354 110.956 125.572 110.656 124.658C110.358 123.744 110.208 122.755 110.208 121.692C110.208 120.604 110.364 119.604 110.676 118.697C110.99 117.788 111.442 117.017 112.034 116.378C112.627 115.739 113.349 115.253 114.198 114.914C115.047 114.574 116.012 114.409 117.094 114.409ZM121.17 121.692C121.17 120.655 121.003 119.756 120.669 118.997C120.334 118.238 119.856 117.663 119.233 117.273C118.612 116.883 117.899 116.688 117.093 116.688C116.521 116.688 115.991 116.795 115.504 117.012C115.017 117.228 114.599 117.542 114.247 117.954C113.897 118.367 113.621 118.893 113.416 119.534C113.214 120.176 113.113 120.895 113.113 121.694C113.113 122.499 113.214 123.226 113.416 123.877C113.621 124.527 113.907 125.067 114.277 125.495C114.647 125.923 115.073 126.244 115.552 126.456C116.031 126.668 116.558 126.775 117.131 126.775C117.866 126.775 118.54 126.592 119.154 126.224C119.77 125.857 120.259 125.29 120.623 124.524C120.988 123.757 121.17 122.813 121.17 121.692Z" fill="white" />
      <path d="M134.976 117.018H131.846V127.306C131.846 127.898 131.713 128.338 131.45 128.625C131.187 128.912 130.844 129.054 130.425 129.054C130 129.054 129.654 128.909 129.388 128.619C129.121 128.33 128.987 127.892 128.987 127.305V117.017H125.856C125.366 117.017 125.003 116.909 124.765 116.693C124.528 116.477 124.408 116.192 124.408 115.838C124.408 115.47 124.532 115.181 124.779 114.969C125.028 114.757 125.387 114.649 125.858 114.649H134.977C135.473 114.649 135.842 114.76 136.082 114.977C136.326 115.196 136.446 115.483 136.446 115.836C136.446 116.189 136.323 116.475 136.078 116.691C135.834 116.907 135.466 117.018 134.976 117.018Z" fill="white" />
      <path d="M143.642 123.297H141.015V127.306C141.015 127.879 140.879 128.313 140.609 128.61C140.339 128.907 139.997 129.054 139.584 129.054C139.152 129.054 138.804 128.907 138.542 128.614C138.279 128.322 138.146 127.891 138.146 127.324V116.409C138.146 115.777 138.291 115.326 138.581 115.056C138.871 114.786 139.331 114.65 139.963 114.65H143.643C144.733 114.65 145.568 114.734 146.154 114.902C146.734 115.063 147.235 115.33 147.657 115.703C148.079 116.077 148.399 116.534 148.619 117.076C148.84 117.617 148.947 118.224 148.947 118.901C148.947 120.344 148.503 121.437 147.615 122.182C146.726 122.926 145.4 123.297 143.642 123.297ZM142.945 116.804H141.014V121.133H142.945C143.622 121.133 144.188 121.062 144.64 120.921C145.095 120.78 145.44 120.548 145.678 120.226C145.917 119.904 146.036 119.483 146.036 118.959C146.036 118.335 145.853 117.826 145.485 117.433C145.074 117.013 144.228 116.804 142.945 116.804Z" fill="white" />
      <rect x="233.582" y="79" width="10" height="10" rx="1" transform="rotate(27.2727 233.582 79)" fill="#91A3FF" />
      <circle cx="74" cy="139" r="5" fill="#FF91B9" />
      <circle cx="79" cy="43" r="5" fill="#91E5FF" />
      <circle cx="188" cy="203" r="5" fill="#FF9191" />
    </g>
    <circle cx="220" cy="15" r="5" fill="#FFC691" />
    <circle cx="119.606" cy="5" r="5" fill="#91FFAF" />
    <rect x="250.606" y="163" width="10" height="10" rx="1" fill="#E991FF" />
    <rect x="274" y="47.0925" width="10" height="10" rx="1" transform="rotate(-24.1576 274 47.0925)" fill="#FF9191" />
    <rect y="68.5666" width="10" height="10" rx="1" transform="rotate(-27.1716 0 68.5666)" fill="#91A3FF" />
    <path d="M33.0121 175.265L40.7499 180.821L32.0689 184.744L33.0121 175.265Z" fill="#FF9191" />
    <path d="M15.077 128.971L16.567 138.38L7.67356 134.966L15.077 128.971Z" fill="#FD91FF" />
    <path d="M286.447 120.204L287.505 129.672L278.777 125.854L286.447 120.204Z" fill="#FF91BF" />
    <defs>
      <clipPath id="clip0_1_45">
        <rect width="179" height="179" fill="white" transform="translate(62.6058 29)" />
      </clipPath>
    </defs>
  </svg>
  <div class="title">Verification Code</div>
  <p>Dear, **USERNAME**,
  <br/>
  Use this otp to confirm the cash order
  </p>
  <div id='inputs'>
    <input id='input1' type='text' maxLength="1" value="**1**"/>
    <input id='input2' type='text' maxLength="1" value="**2**"/>
    <input id='input3' type='text' maxLength="1" value="**3**"/>
    <input id='input4' type='text' maxLength="1" value="**4**"/>
    <input id='input4' type='text' maxLength="1" value="**5**"/>
    <input id='input4' type='text' maxLength="1" value="**6**"/>
  </div>
</section>
<style>
@import url("https://fonts.googleapis.com/css2?family=Lato:wght@100;300;400;700&display=swap");

html {
  background-color: deepskyblue;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
  font-family: "Lato", sans-serif;
}

section {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-around;
  width: 40vw;
  min-width: 350px;
  height: 80vh;
  background-color: white;
  border-radius: 12px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px,
    rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
  padding: 24px 0px;
}
svg {
  margin: 16px 0;
}
title {
  font-size: 20px;
  font-weight: bold;
}

p {
  color: #a3a3a3;
  font-size: 14px;
  width: 200px;
  margin-top: 4px;
}
input {
  width: 32px;
  height: 32px;
  text-align: center;
  border: none;
  border-bottom: 1.5px solid #d2d2d2;
  margin: 0 10px;
}

input:focus {
  border-bottom: 1.5px solid deepskyblue;
  outline: none;
}

button {
  width: 250px;
  letter-spacing: 2px;
  margin-top: 24px;
  padding: 12px 16px;
  border-radius: 8px;
  border: none;
  background-color: #33cdff;
  color: white;
  cursor: pointer;
}
</style>
"""
  html = html.replace("**1**",otp[0])
  html = html.replace("**2**",otp[1])
  html = html.replace("**3**",otp[2])
  html = html.replace("**4**",otp[3])
  html = html.replace("**5**",otp[4])
  html = html.replace("**6**",otp[5])
  html = html.replace("**USERNAME**",user.username)
  sender_email = "mailtrap@example.com"
  receiver_email = user.email
  message = MIMEMultipart("alternative")
  message["Subject"] = f"Team Gifshion"
  message["From"] = sender_email
  message["To"] = receiver_email
  message.attach(MIMEText(html, "html"))
  with smtplib.SMTP(HOST,PORT) as server:
    print("Sending")
    server.login(USERNAME, PASSWORD)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
      )
  print("Sent")
    

class WelcomeThread(Thread):
  def __init__(self, user):
    self.user = user
    Thread.__init__(self)
  def run (self):
    send_welcome_mail(self.user)
    
def send_welcome_mail(user):
  html = """<!-- Change values in [brackets] in the template and pass { {variables} } with API call -->
<!-- Feel free to adjust it to your needs and delete all these comments-->
<!-- Also adapt TXT version of this email -->
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <title></title>
  <!--[if !mso]><!-- -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!--<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style type="text/css">
    #outlook a {
      padding: 0;
    }

    .ReadMsgBody {
      width: 100%;
    }

    .ExternalClass {
      width: 100%;
    }

    .ExternalClass * {
      line-height: 100%;
    }

    body {
      margin: 0;
      padding: 0;
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }

    table,
    td {
      border-collapse: collapse;
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }

  </style>
  <!--[if !mso]><!-->
  <style type="text/css">
    @media only screen and (max-width:480px) {
      @-ms-viewport {
        width: 320px;
      }
      @viewport {
        width: 320px;
      }
    }
  </style>
  <!--<![endif]-->
  <!--[if mso]><xml>  <o:OfficeDocumentSettings>    <o:AllowPNG/>    <o:PixelsPerInch>96</o:PixelsPerInch>  </o:OfficeDocumentSettings></xml><![endif]-->
  <!--[if lte mso 11]><style type="text/css">  .outlook-group-fix {    width:100% !important;  }</style><![endif]-->
  <!--[if !mso]><!-->
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet" type="text/css">
  <style type="text/css">
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap');
  </style>
  <!--<![endif]-->
  <style type="text/css">
    @media only screen and (max-width:595px) {
      .container {
        width: 100% !important;
      }
      .button {
        display: block !important;
        width: auto !important;
      }
    }
  </style>
</head>

<body style="font-family: 'Inter', sans-serif; background: #E5E5E5;">
  <table width="100%" cellspacing="0" cellpadding="0" border="0" align="center" bgcolor="#F6FAFB">
    <tbody>
      <tr>
        <td valign="top" align="center">
          <table class="container" width="600" cellspacing="0" cellpadding="0" border="0">
            <tbody>
              <tr>
                <td style="padding:48px 0 30px 0; text-align: center; font-size: 14px; color: #4C83EE;">
                 <a href="https://ebe2-49-37-33-255.ngrok-free.app/media/logo.png" target="_blank" style="display: inline-block;">
                  <img src="https://ebe2-49-37-33-255.ngrok-free.app/media/logo.png" alt="Logo" border="0" width="150"
                    style="display: block; width: 150px; max-width: 150px; min-width: 150px;">
                </a>
                </td>
              </tr>
              <tr>
                <td class="main-content" style="padding: 48px 30px 40px; color: #000000;" bgcolor="#ffffff">
                  <table width="100%" cellspacing="0" cellpadding="0" border="0">
                    <tbody>
                      <tr>
                        <td style="padding: 0 0 24px 0; font-size: 18px; line-height: 150%; font-weight: bold; color: #000000; letter-spacing: 0.01em;">
                          Welcome, {{user_name}}!
                        </td>
                      </tr>
                      <tr>
                        <td style="padding: 0 0 10px 0; font-size: 14px; line-height: 150%; font-weight: 400; color: #000000; letter-spacing: 0.01em;">
                          Thanks for choosing Gifshion! We are happy to see you on board.
                        </td>
                      </tr>
                      <tr>
                        <td style="padding: 0 0 16px 0; font-size: 14px; line-height: 150%; font-weight: 400; color: #000000; letter-spacing: 0.01em;">
                          To get started, do this next step:
                        </td>
                      </tr>
                      <tr>
                        <td style="padding: 0 0 24px 0;">
                          <a class="button" href="http://localhost:8000" title="Reset Password" style="width: 100%; background: #4C83EE; text-decoration: none; display: inline-block; padding: 10px 0; color: #fff; font-size: 14px; line-height: 21px; text-align: center; font-weight: bold; border-radius: 7px;">Go To Website</a>
                        </td>
                      </tr>
                      <tr>
                        <td style="padding: 0 0 16px;">
                          <span style="display: block; width: 117px; border-bottom: 1px solid #8B949F;"></span>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size: 14px; line-height: 170%; font-weight: 400; color: #000000; letter-spacing: 0.01em;">
                          Best regards, <br><strong>Gishion</strong>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
              </tr>
              <tr>
                <td style="padding: 24px 0 48px; font-size: 0px;">
                  <!--[if mso | IE]>      <table role="presentation" border="0" cellpadding="0" cellspacing="0">        <tr>          <td style="vertical-align:top;width:300px;">      <![endif]-->
                  <div class="outlook-group-fix" style="padding: 0 0 20px 0; vertical-align: top; display: inline-block; text-align: center; width:100%;">
                    <span style="padding: 0; font-size: 11px; line-height: 15px; font-weight: normal; color: #8B949F;">2023 Gifshion, Inc. All rights reserved
                    </div>
                  </div>
                  <!--[if mso | IE]>      </td></tr></table>      <![endif]-->
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
</body>
</html>"""
  html = html.replace("{{user_name}}",user.username)
  sender_email = "mailtrap@example.com"
  receiver_email = user.email
  message = MIMEMultipart("alternative")
  message["Subject"] = f"Welcome to Gifshion, {user.username}!"
  message["From"] = sender_email
  message["To"] = receiver_email
  message.attach(MIMEText(html, "html"))
  with smtplib.SMTP(HOST,PORT) as server:
      server.login(USERNAME, PASSWORD)
      server.sendmail(
          sender_email, receiver_email, message.as_string()
        )

class EmailThread(Thread):
    def __init__(self, order,icon):
        self.order = order 
        self.icon = icon
        Thread.__init__(self)

    def run (self):
      send_mail(self.order,self.icon)

def send_mail(order,icon):
  sender_email = "mailtrap@example.com"
  receiver_email = order.checkout.email
  message = MIMEMultipart("alternative")
  message["Subject"] = "Gifshion Payment Receipt"
  message["From"] = sender_email
  message["To"] = receiver_email

  html = """
  <!DOCTYPE html>
  <html>

  <head>

    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Email Receipt</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style type="text/css">
      /**
    * Google webfonts. Recommended to include the .woff version for cross-client compatibility.
    */
      @media screen {
        @font-face {
          font-family: 'Source Sans Pro';
          font-style: normal;
          font-weight: 400;
          src: local('Source Sans Pro Regular'), local('SourceSansPro-Regular'), url(https://fonts.gstatic.com/s/sourcesanspro/v10/ODelI1aHBYDBqgeIAH2zlBM0YzuT7MdOe03otPbuUS0.woff) format('woff');
        }

        @font-face {
          font-family: 'Source Sans Pro';
          font-style: normal;
          font-weight: 700;
          src: local('Source Sans Pro Bold'), local('SourceSansPro-Bold'), url(https://fonts.gstatic.com/s/sourcesanspro/v10/toadOcfmlt9b38dHJxOBGFkQc6VGVFSmCnC_l7QZG60.woff) format('woff');
        }
      }

      /**
    * Avoid browser level font resizing.
    * 1. Windows Mobile
    * 2. iOS / OSX
    */
      body,
      table,
      td,
      a {
        -ms-text-size-adjust: 100%;
        /* 1 */
        -webkit-text-size-adjust: 100%;
        /* 2 */
      }

      /**
    * Remove extra space added to tables and cells in Outlook.
    */
      table,
      td {
        mso-table-rspace: 0pt;
        mso-table-lspace: 0pt;
      }

      /**
    * Better fluid images in Internet Explorer.
    */
      img {
        -ms-interpolation-mode: bicubic;
      }

      /**
    * Remove blue links for iOS devices.
    */
      a[x-apple-data-detectors] {
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        color: inherit !important;
        text-decoration: none !important;
      }

      /**
    * Fix centering issues in Android 4.4.
    */
      div[style*="margin: 16px 0;"] {
        margin: 0 !important;
      }

      body {
        width: 100% !important;
        height: 100% !important;
        padding: 0 !important;
        margin: 0 !important;
      }

      /**
    * Collapse table borders to avoid space between cells.
    */
      table {
        border-collapse: collapse !important;
      }

      a {
        color: #1a82e2;
      }

      img {
        height: auto;
        line-height: 100%;
        text-decoration: none;
        border: 0;
        outline: none;
      }

      .receipt-clmn td {
        border: 1px solid #222;
      }
    </style>

  </head>

  <body style="background-color: #f1f1f1;">

    <!-- start preheader -->
    <div class="preheader"
      style="display: none; max-width: 0; max-height: 0; overflow: hidden; font-size: 1px; line-height: 1px; color: #fff; opacity: 0;">
      A preheader is the short summary text that follows the subject line when an email is viewed in the inbox.
    </div>
    <!-- end preheader -->

    <!-- start body -->
    <table border="0" cellpadding="0" cellspacing="0" width="100%">

      <!-- start logo -->
      <tr>
        <td align="center" bgcolor="#f1f1f1">
          <!--[if (gte mso 9)|(IE)]>
          <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
          <tr>
          <td align="center" valign="top" width="600">
          <![endif]-->
          <table bgcolor="#fff" border="0" cellpadding="0" cellspacing="0" width="100%"
            style="max-width: 600px;border: 1px solid #222;border-bottom: 0;">
            <tr>
              <td align="left" valign="top" style="padding:15px;">
                <a href="https://ebe2-49-37-33-255.ngrok-free.app/media/logo.png" target="_blank" style="display: inline-block;">
                  <img src="https://ebe2-49-37-33-255.ngrok-free.app/media/logo.png" alt="Logo" border="0" width="150"
                    style="display: block; width: 150px; max-width: 150px; min-width: 150px;">
                </a>
              </td>
              <td align="right" valign="top" style="padding:15px;">
                <p style="margin:0;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif;">
                  <b>Order ID:</b> **ORDER ID** <br>
                  <b>Date:</b> **ORDER DATE** <br>
                  <b>Payment Status: :</b> **ORDER STATUS**
                </p>
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
          </td>
          </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <!-- end logo -->

      <!-- start hero -->
      <tr>
        <td align="center" bgcolor="#f1f1f1">
          <!--[if (gte mso 9)|(IE)]>
          <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
          <tr>
          <td align="center" valign="top" width="600">
          <![endif]-->
          <table bgcolor="#fff" border="0" cellpadding="0" cellspacing="0" width="100%"
            style="max-width: 600px;border-left: 1px solid;border-right: 1px solid;">
            <tr>
              <td align="left" bgcolor="#db6d09"
                style="padding:24px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; border-top: 2px solid #db6d09;">
                <h1
                  style="margin: 0; font-size: 32px; font-weight: 700; letter-spacing: -1px; line-height: 48px;color: #fff;">
                  Thank you for your order!</h1>
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
          </td>
          </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <!-- end hero -->
      <tr>
        <td align="center" bgcolor="#f1f1f1">
          <!--[if (gte mso 9)|(IE)]>
            <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
            <tr>
            <td align="center" valign="top" width="600">
            <![endif]-->
          <table bgcolor="#fff" border="0" cellpadding="0" cellspacing="0" width="100%"
            style="max-width: 600px;border-left: 1px solid;border-right: 1px solid;">
            <!-- start copy -->
            <tr>
              <td align="left" bgcolor="#ffffff"
                style="padding: 24px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                <p style="margin: 0;">
                  Hi <b>**NAME**</b>,<br>
                  Here is a summary of your recent order. If you have any questions or concerns about your order, please contact us
                </p>
              </td>
            </tr>
            <!-- end copy -->
          </table>
        </td>
      </tr>
      <!-- start receipt address block -->
      <tr>
        <td align="center" bgcolor="#f1f1f1" valign="top" width="100%">
          <!--[if (gte mso 9)|(IE)]>
          <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
          <tr>
          <td align="center" valign="top" width="600">
          <![endif]-->
          <table align="center" bgcolor="#f1f1f1" border="0" cellpadding="0" cellspacing="0" width="100%"
            style="max-width: 600px;border-left: 1px solid;border-right: 1px solid;">
            <tr>
              <td align="center" valign="top" style="font-size: 0;">
                <!--[if (gte mso 9)|(IE)]>
                <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
                <tr>
                <td align="left" valign="top" width="300">
                <![endif]-->
                <div style="display: inline-block; width: 100%; max-width: 50%; min-width: 240px; vertical-align: top;">
                  <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 300px;">
                    <tr>
                      <td align="left" valign="top"
                        style="padding-bottom: 36px; padding-left: 36px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                        <p><strong>Delivery Address</strong></p>
                        <p>**ADDRESS**</p>
                        <p>**CITY**</p>
                        <p>**STATE**</p>
                        <p>**COUNTRY**</p>
                      </td>
                    </tr>
                  </table>
                </div>
                <!--[if (gte mso 9)|(IE)]>
                </td>
                <td align="left" valign="top" width="300">
                <![endif]-->
                <div style="display: inline-block; width: 100%; max-width: 50%; min-width: 240px; vertical-align: top;">
                  <table align="left" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 300px;">
                  </table>
                </div>
                <!--[if (gte mso 9)|(IE)]>
                </td>
                </tr>
                </table>
                <![endif]-->
              </td>
            </tr>
          </table>
          <!--[if (gte mso 9)|(IE)]>
          </td>
          </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <!-- end receipt address block -->

      <!-- start copy block -->
      <tr>
        <td align="center" bgcolor="#f1f1f1">
          <!--[if (gte mso 9)|(IE)]>
          <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
          <tr>
          <td align="center" valign="top" width="600">
          <![endif]-->
          <table bgcolor="#fff" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px;">



            <!-- start receipt table -->
            <tr>
              <td align="left" bgcolor="#ffffff"
                style="font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                <table class="receipt-clmn" border="0" cellpadding="0" cellspacing="0" width="100%">
                  <tr>
                    <td align="left" bgcolor="#fff" width="75%"
                      style="padding: 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;padding-left: 25px;">
                      <span style=""><strong>Order #</strong></span>
                    </td>
                    <td align="left" bgcolor="#fff" width="25%"
                      style="padding: 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;padding-left: 25px;">
                      <span style=""><strong>Qty</strong></span>
                    </td>
                    <td align="left" bgcolor="#fff" width="25%"
                      style="padding: 12px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;padding-left: 25px;">
                      <span style=""><strong>Price</strong></span>
                    </td>
                  </tr>"""
  for item in order.items.all():
                    html += f"""
                  <tr>
                    <td align="left" width="75%"
                      style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                      {item.product.name}</td>
                    <td align="left" width="75%"
                      style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                      {item.quantity}</td>
                    <td align="left" width="25%"
                      style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                      {icon}{item.price}</td>
                  </tr>
                 """

                
  html += f"""
                <tr>
                  <td colspan="2" align="left" width="75%" style="padding: 25px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;"><strong>Total</strong></td>
                  
                  <td align="left" width="30%" style="padding: 25px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;"><strong>{f"{icon}{order.total_amount}"}</strong></td>
                </table>
              </td>
            </tr>
            <!-- end reeipt table -->

          </table>
          <!--[if (gte mso 9)|(IE)]>
          </td>
          </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <!-- end copy block -->

      <!-- start footer -->
      <tr>
        <td align="center" bgcolor="#f1f1f1" style="padding:0 24px;">
          <!--[if (gte mso 9)|(IE)]>
          <table align="center" border="0" cellpadding="0" cellspacing="0" width="600">
          <tr>
          <td align="center" valign="top" width="600">
          <![endif]-->
          <table bgcolor="#fff" border="0" cellpadding="0" cellspacing="0" width="100%"
            style="max-width: 600px;border-left: 1px solid;border-right: 1px solid;">


            <!-- start unsubscribe -->
            <tr>
              <td align="center" bgcolor="#fff"
                style="padding:24px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 20px; color: #666;">
                <p style="margin: 0;">If you have any questions about your bill, please get in touch with us by replying
                  to this email!
                </p>
                <a href="http://localhost:8000">  ©2023 Gifshion, Inc. All rights reserved</a>
              </td>
            </tr>
            <!-- end unsubscribe -->

          </table>
          <!--[if (gte mso 9)|(IE)]>
          </td>
          </tr>
          </table>
          <![endif]-->
        </td>
      </tr>
      <!-- end footer -->

    </table>
    <!-- end body -->

  </body>

  </html>
  """
  html = html.replace('**ORDER ID**',order.id)
  html = html.replace('**ORDER DATE**',order.order_date.strftime('%d %B %Y'))
  if order.paid:
    html = html.replace('**ORDER STATUS**','PAID ONLINE')
  else:
    html = html.replace('**ORDER STATUS**','CASH ON DELIVERY')
  html = html.replace('**NAME**',order.user.username)
  html = html.replace('**CITY**',order.checkout.city)
  html = html.replace('**STATE**',order.checkout.state)
  html = html.replace('**COUNTRY**',order.checkout.country)
  html = html.replace('**ADDRESS**',order.checkout.address)
  # convert both parts to MIMEText objects and add them to the MIMEMultipart message
  part2 = MIMEText(html, "html")
  message.attach(part2)

  # send your email
  with smtplib.SMTP(HOST,PORT) as server:
    server.login(USERNAME,PASSWORD)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )

  print('Sent')
  
  
  """
</tr>
  
  <td colspan="2" align="left" width="75%" style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">Shipping</td>
  
  <td align="left" width="25%" style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">$6.00</td>
  
     <tr>
                  <td colspan="2" align="left" width="75%" style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">Sales Tax</td>
                  
                  <td align="left" width="25%" style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">$0.00</td>
                </tr>
  """