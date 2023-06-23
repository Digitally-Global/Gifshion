import requests

url = "https://netconnect.bluedart.com/Ver1.10/ShippingAPI/WayBill/WayBillGeneration.svc?SOAPAction=http://tempuri.org/IWayBillGeneration/GenerateWayBill"

payload = """
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/" xmlns:sapi="http://schemas.datacontract.org/2004/07/SAPI.Entities.WayBillGeneration" xmlns:sapi1="http://schemas.datacontract.org/2004/07/SAPI.Entities.Admin">
   <soap:Header xmlns:wsa="http://www.w3.org/2005/08/addressing"><wsa:Action>http://tempuri.org/IWayBillGeneration/GenerateWayBill</wsa:Action></soap:Header>
   <soap:Body>
      <tem:GenerateWayBill>
         <tem:Request>
            <sapi:Consignee>
               <sapi:ConsigneeAddress1>binodini avenue</sapi:ConsigneeAddress1>
               <sapi:ConsigneeAddress2>baguiati</sapi:ConsigneeAddress2>
               <sapi:ConsigneeAddress3>kolkata</sapi:ConsigneeAddress3>
               <sapi:ConsigneeAttention>tanmoy majumder</sapi:ConsigneeAttention>
               <sapi:ConsigneeMobile>8017555762</sapi:ConsigneeMobile>
               <sapi:ConsigneeName>Tanmoy Majumder</sapi:ConsigneeName>
               <sapi:ConsigneePincode>700107</sapi:ConsigneePincode>
            </sapi:Consignee>
            <sapi:Services>
               <sapi:ActualWeight>0.5</sapi:ActualWeight>
               <sapi:CollectableAmount>500</sapi:CollectableAmount>
               <sapi:CommodityDetail1>rose</sapi:CommodityDetail1>
               <sapi:CreditReferenceNo>tes458755</sapi:CreditReferenceNo>
               <sapi:DeclaredValue>500.0</sapi:DeclaredValue>
               <sapi:Dimensions>
                  <sapi:Dimension>
                     <sapi:Breadth>10.0</sapi:Breadth>
                     <sapi:Count>1</sapi:Count>
                     <sapi:Height>10.0</sapi:Height>
                     <sapi:Length>10.0</sapi:Length>
                  </sapi:Dimension>
               </sapi:Dimensions>
               <sapi:PDFOutputNotRequired>false</sapi:PDFOutputNotRequired>
               <sapi:PickupDate>2023-03-04T00:00:00.000+05:00</sapi:PickupDate>
               <sapi:PickupTime>1600</sapi:PickupTime>
               <sapi:PieceCount>1</sapi:PieceCount>
               <sapi:ProductCode>A</sapi:ProductCode>
               <sapi:SubProductCode>C</sapi:SubProductCode>
               <sapi:ProductType>Dutiables</sapi:ProductType>
               <sapi:RegisterPickup>false</sapi:RegisterPickup>
            </sapi:Services>
            <sapi:Shipper>
               <sapi:CustomerAddress1>4D Annapurna Apartments</sapi:CustomerAddress1>
               <sapi:CustomerAddress2>68/A, Ballygunge Circular</sapi:CustomerAddress2>
               <sapi:CustomerAddress3>Road, KOLKATA</sapi:CustomerAddress3>
               <sapi:CustomerCode>276010</sapi:CustomerCode>
               <sapi:CustomerMobile>9831309444</sapi:CustomerMobile>
               <sapi:CustomerName>GJ LIFESTYLE MANAGEMENT:COD</sapi:CustomerName>
               <sapi:CustomerPincode>700107</sapi:CustomerPincode>
               <sapi:CustomerTelephone>9831309444</sapi:CustomerTelephone>
               <sapi:IsToPayCustomer>false</sapi:IsToPayCustomer>
               <sapi:OriginArea>CCU</sapi:OriginArea>
               <sapi:Sender>Flourish</sapi:Sender>
            </sapi:Shipper>
         </tem:Request>
         <tem:Profile>
            <sapi1:Api_type>S</sapi1:Api_type>
            <sapi1:Customercode>CCU280033</sapi1:Customercode>
            <sapi1:LicenceKey>eyrouhvs8rouu8kkiuhlhgftgcqn8qqk</sapi1:LicenceKey>
            <sapi1:LoginID>CCU82883</sapi1:LoginID>
            <sapi1:Version>1.3</sapi1:Version>
         </tem:Profile>
      </tem:GenerateWayBill>
   </soap:Body>
</soap:Envelope>
"""
headers = {
  'Content-Type': 'application/soap+xml;charset=utf-8;action="http://tempuri.org/IWayBillGeneration/GenerateWayBill";',
  'SOAPAction': 'http://tempuri.org/IWayBillGeneration/GenerateWayBill',
  'Cookie': 'BIGipServerpl_netconnect-bluedart.dhl.com_443=!kU78Vv6AKlcmuNTzvvsIVYa1K6PKfQONoP3fd7ugBNDofGW5IEXvuR2hujFvCB6TqctxMDm8MbQfIqA=; TS01808994=01914b743dc8f3e589af84601c412c624b061911c4128b78d78cc9b35ae074f3ae4f02f30836aaab7da930cb73ce9dbe88687e510338356356da14094ef3f03883f6ed15f9'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
