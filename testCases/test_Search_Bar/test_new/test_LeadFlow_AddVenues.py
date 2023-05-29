from utilites.readProperties_newLeadFlow import ReadConfig_new_lead_flow_venue_add
from utilites.customeLogger import LogGen
from pageObject.Search_Bar.New_Lead_flow_In_Add_venue import NewLeadflowInAddvenue

class Test_001_FlowLead:

    base_URL = ReadConfig_new_lead_flow_venue_add.getApplicationURL()
    vendor_id = ReadConfig_new_lead_flow_venue_add.getVendor_MailID()
    vendor_password = ReadConfig_new_lead_flow_venue_add.getVendor_Pass()
    cust_name = ReadConfig_new_lead_flow_venue_add.getCustname()
    cust_mail_id = ReadConfig_new_lead_flow_venue_add.getCustmail()
    phone_no = ReadConfig_new_lead_flow_venue_add.getPhoneNo()
    event_date = ReadConfig_new_lead_flow_venue_add.getEventDate()
    event_time = ReadConfig_new_lead_flow_venue_add.getEventTime()
    no_of_people = ReadConfig_new_lead_flow_venue_add.getNoOfPeople()
    Budget = ReadConfig_new_lead_flow_venue_add.getBudget()
    Additional_info = ReadConfig_new_lead_flow_venue_add.getAdditional_Info()
    Add_menu = ReadConfig_new_lead_flow_venue_add.getAdd_menu()
    Note = ReadConfig_new_lead_flow_venue_add.getNote()

    def test_008_BusinessHubs(self,setup):
        self.driver= setup
        self.driver.get(self.base_URL)
        self.lp = NewLeadflowInAddvenue(self.driver)
