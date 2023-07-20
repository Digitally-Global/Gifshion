# import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from threading import Thread

PORT = 587
HOST = "smtp-relay.sendinblue.com"
USERNAME = "ccegifshion24x7@gmail.com"
PASSWORD = "KQ0xEVwPsfFgdqI9"

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
  print(otp)
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
                 <a href="https://gifshion.com/static/assets/images/Asset%201%40300x%20(1).png" target="_blank" style="display: inline-block;">
                  <img src="https://gifshion.com/static/assets/images/Asset%201%40300x%20(1).png" alt="Logo" border="0" width="150"
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
                          Dear, {{user_name}},
                        </td>
                      </tr>
                      <tr>
                        <td style="padding: 0 0 10px 0; font-size: 14px; line-height: 150%; font-weight: 400; color: #000000; letter-spacing: 0.01em;">
                          Use <b>{{otp}}</b> to confirm your cash order.
                        </td>
                      </tr>
                      <tr>
                        <td style="padding: 0 0 16px 0; font-size: 14px; line-height: 150%; font-weight: 400; color: #000000; letter-spacing: 0.01em;">
                        Please do not share this OTP with anyone.
                        </td>
                      </tr>
                       <tr>
                        <td style="padding: 0 0 16px 0; font-size: 14px; line-height: 150%; font-weight: 400; color: #000000; letter-spacing: 0.01em;">
                        Ignore this email if you did not request for OTP.
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
  html = html.replace("{{otp}}",otp)
  html = html.replace("{{user_name}}",user.username)
  sender_email = "ccegifshion24x7@gmail.com"
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
                 <a href="https://gifshion.com/static/assets/images/Asset%201%40300x%20(1).png" target="_blank" style="display: inline-block;">
                  <img src="https://gifshion.com/static/assets/images/Asset%201%40300x%20(1).png" alt="Logo" border="0" width="150"
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
                          <a class="button" href="http://gifshion.com" title="Reset Password" style="width: 100%; background: #4C83EE; text-decoration: none; display: inline-block; padding: 10px 0; color: #fff; font-size: 14px; line-height: 21px; text-align: center; font-weight: bold; border-radius: 7px;">Go To Website</a>
                        </td>
                      </tr>
                      <tr>
                        <td style="padding: 0 0 16px;">
                          <span style="display: block; width: 117px; border-bottom: 1px solid #8B949F;"></span>
                        </td>
                      </tr>
                      <tr>
                        <td style="font-size: 14px; line-height: 170%; font-weight: 400; color: #000000; letter-spacing: 0.01em;">
                          Best regards, <br><strong>Gifshion</strong>
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
  sender_email = "ccegifshion24x7@gmail.com"
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
  sender_email = "ccegifshion24x7@gmail.com"
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
                <a href="https://gifshion.com/media/logo.png" target="_blank" style="display: inline-block;">
                  <img src="https://gifshion.com/media/logo.png" alt="Logo" border="0" width="150"
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
                <a href="https://gifshion.com">  ©2023 Gifshion, Inc. All rights reserved</a>
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