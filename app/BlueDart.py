import requests
from threading import Thread
from datetime import date
from ecom.models import Tracking


class BlueDart(Thread):
   def __init__(self,order,checkout,customer):
      self.order = order
      self.customer = customer
      self.checkout=checkout
      Thread.__init__(self)
   
   def send_request(self,url,payload,action):
      print("Sending request to bluedart")
      headers = {
         'Content-Type': f'application/soap+xml;charset=utf-8;action="{action}";',
         'SOAPAction': action,
         'Cookie': 'BIGipServerpl_netconnect-bluedart.dhl.com_443=!kU78Vv6AKlcmuNTzvvsIVYa1K6PKfQONoP3fd7ugBNDofGW5IEXvuR2hujFvCB6TqctxMDm8MbQfIqA=; TS01808994=01914b743dc8f3e589af84601c412c624b061911c4128b78d78cc9b35ae074f3ae4f02f30836aaab7da930cb73ce9dbe88687e510338356356da14094ef3f03883f6ed15f9'
      }
      print(headers)
      response = requests.request("POST", url, headers=headers, data=payload)
      response = response.text.encode('utf8')
      response =str(response)
      tracking = Tracking.objects.create(tracking_number=response[response.find('<b:AWBNo>')+9:response.find('</b:AWBNo>')],data=response)
      tracking .tracking_number=response[response.find('<b:AWBNo>')+9:response.find('</b:AWBNo>')]
      self.order.tracking = tracking
      self.order.save()
      try:
         self.order.tracking=response[response.find('<b:AWBNo>')+9:response.find('</b:AWBNo>')]
         self.order.save()
         return [True,int(response[response.find('<b:AWBNo>')+9:response.find('</b:AWBNo>')])]
      except:
         return [False]
      
      
   def create_waybill(self):
      weight = 0.0
      count = 0 
      for item in self.order.items.all():
         if (item.product.sub_category.hand_delivery):
            continue
         weight += float(item.size.weight)*int(item.quantity)
         count += int(item.quantity) 
         # total =
      weight = round(weight,1)
      if weight == 0.0: 
         return 
      print("creating waybill")
      today = date.today()
      today = today.strftime("%Y-%m-%dT00:00:00.000+05:00")
      ACTION="http://tempuri.org/IWayBillGeneration/GenerateWayBill"
      url = "https://netconnect.bluedart.com/Ver1.10/ShippingAPI/WayBill/WayBillGeneration.svc?SOAPAction=http://tempuri.org/IWayBillGeneration/GenerateWayBill"
      payload=f"""
         <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/" xmlns:sapi="http://schemas.datacontract.org/2004/07/SAPI.Entities.WayBillGeneration" xmlns:sapi1="http://schemas.datacontract.org/2004/07/SAPI.Entities.Admin">
         <soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing"><wsa:Action>http://tempuri.org/IWayBillGeneration/GenerateWayBill</wsa:Action></soap:Header>
         <soap:Body>
            <tem:GenerateWayBill>
               <tem:Request>
                  <sapi:Consignee>
                     <sapi:ConsigneeAddress1>{self.checkout.address}</sapi:ConsigneeAddress1>
                     <sapi:ConsigneeAddress2>{self.checkout.city}</sapi:ConsigneeAddress2>
                     <sapi:ConsigneeAddress3>{self.checkout.state}</sapi:ConsigneeAddress3>
                     <sapi:ConsigneeAttention>{self.checkout.fname} {self.checkout.lname}</sapi:ConsigneeAttention>
                     <sapi:ConsigneeMobile>{self.checkout.mobile_number}</sapi:ConsigneeMobile>
                     <sapi:ConsigneeName>{self.customer.username}</sapi:ConsigneeName>
                     <sapi:ConsigneePincode>{self.checkout.zip}</sapi:ConsigneePincode>
                  </sapi:Consignee>
                  <sapi:Services>
                     <sapi:ActualWeight>{weight}</sapi:ActualWeight>
                     <sapi:CollectableAmount>500</sapi:CollectableAmount>
                     <sapi:CommodityDetail1>rose</sapi:CommodityDetail1>
                     <sapi:CreditReferenceNo>{self.order.id}</sapi:CreditReferenceNo>
                     <sapi:DeclaredValue>{self.order.total_amount}</sapi:DeclaredValue>
                     <sapi:Dimensions>
                  """
      for order_item in self.order.items.all():
         print(order_item)
         if (order_item.product.sub_category.hand_delivery):
            continue
         payload+=f"""
                     <sapi:Dimension>
                        <sapi:Breadth>{order_item.size.width}</sapi:Breadth>
                        <sapi:Count>{order_item.quantity}</sapi:Count>
                        <sapi:Height>{order_item.size.height}</sapi:Height>
                        <sapi:Length>{order_item.size.length}</sapi:Length>
                     </sapi:Dimension>
                  """
      payload+=f"""  
            </sapi:Dimensions>
            <sapi:PDFOutputNotRequired>false</sapi:PDFOutputNotRequired>
            <sapi:PickupDate>{today}</sapi:PickupDate>
            <sapi:PickupTime>1600</sapi:PickupTime>
            <sapi:PieceCount>{count}</sapi:PieceCount>
            <sapi:ProductCode>A</sapi:ProductCode>
            <sapi:SubProductCode>C</sapi:SubProductCode>
            <sapi:ProductType>Dutiables</sapi:ProductType>
            <sapi:RegisterPickup>true</sapi:RegisterPickup>
         </sapi:Services>
         <sapi:Shipper>
            <sapi:CustomerAddress1>BL GE PLOT 148 PREMISES NO</sapi:CustomerAddress1>
            <sapi:CustomerAddress2>2010 RAJDANGA MAIN ROAD</sapi:CustomerAddress2>
            <sapi:CustomerAddress3>Road, KOLKATA</sapi:CustomerAddress3>
            <sapi:CustomerCode>280033</sapi:CustomerCode>
            <sapi:CustomerMobile>7439835724</sapi:CustomerMobile>
            <sapi:CustomerName>P R JHA SONS:COD-PREPAID</sapi:CustomerName>
            <sapi:CustomerPincode>700107</sapi:CustomerPincode>
            <sapi:CustomerTelephone>7439835724</sapi:CustomerTelephone>
            <sapi:IsToPayCustomer>false</sapi:IsToPayCustomer>
            <sapi:OriginArea>CCU</sapi:OriginArea>
            <sapi:Sender>P R JHA SONS</sapi:Sender>
         </sapi:Shipper>
         </tem:Request>
         <tem:Profile>
            <sapi1:Api_type>S</sapi1:Api_type>
            <sapi1:Area>ALL</sapi1:Area>
            <sapi1:Customercode>280033</sapi1:Customercode>
            <sapi1:LicenceKey>eyrouhvs8rouu8kkiuhlhgftgcqn8qqk</sapi1:LicenceKey>
            <sapi1:LoginID>CCU82883</sapi1:LoginID>
            <sapi1:Version>1.3</sapi1:Version>
            </tem:Profile>
            </tem:GenerateWayBill>
            </soap:Body>
         </soap:Envelope>
      """
      print(payload)
      self.send_request(url,payload,ACTION)
