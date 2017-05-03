from custfactory import CustFactory

factory = CustFactory()

def main():
    cust_types = ['SMBCust', 'ENTCust', 'GOVCust', 'ALIENCust']
    for cust_type in cust_types:
        cust = factory.create_instance(cust_type)
        cust.name = cust_type
        cust.send_invoice()

if __name__ == '__main__':
    main()
