# import the necessary components first
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(order):
  port = 2525 
  smtp_server = "smtp.mailtrap.io"

  sender_email = "mailtrap@example.com"
  receiver_email = "dkediaphone@icloud.com"
  message = MIMEMultipart("alternative")
  message["Subject"] = "multipart test"
  message["From"] = sender_email
  message["To"] = receiver_email

  html = """\
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
                <a href="#" target="_blank" style="display: inline-block;">
                  <img src="gifshion.png" alt="Logo" border="0" width="150"
                    style="display: block; width: 150px; max-width: 150px; min-width: 150px;">
                </a>
              </td>
              <td align="right" valign="top" style="padding:15px;">
                <p style="margin:0;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif;">
                  <b>Order ID:</b> 32145698745 <br>
                  <b>Date:</b> 05-06-23 <br>
                  <b>Payment Status: :</b> Paid Online
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
                  Hi <b>Name</b>,<br>
                  Here is a summary of your recent order. If you have any questions or concerns about your order, please
                  <a href="#">contact us</a>.
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
                        <p>1234 S. Broadway Ave<br>Unit 2<br>Denver, CO 80211</p>
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
                    <tr>
                      <td align="left" valign="top"
                        style="padding-bottom: 36px; padding-left: 36px; font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                        <p><strong>Billing Address</strong></p>
                        <p>1234 S. Broadway Ave<br>Unit 2<br>Denver, CO 80211</p>
                      </td>
                    </tr>
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
                    html += """
                  <tr>
                    <td align="left" width="75%"
                      style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                      Item</td>
                    <td align="left" width="75%"
                      style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                      3</td>
                    <td align="left" width="25%"
                      style="padding: 6px 25px;font-family: 'Source Sans Pro', Helvetica, Arial, sans-serif; font-size: 16px; line-height: 24px;">
                      $24.00</td>
                  </tr>
                 """
  html += """
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

  # convert both parts to MIMEText objects and add them to the MIMEMultipart message
  part2 = MIMEText(html, "html")
  message.attach(part2)

  # send your email
  with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
      server.login("37b854dadb9bcf", "a6a22f91ed1216")
      server.sendmail(
          sender_email, receiver_email, message.as_string()
      )

  print('Sent')