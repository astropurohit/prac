from fileinput import filename
from kivymd.uix.list import TwoLineAvatarListItem , ImageLeftWidget
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from uuid import uuid4
from kivymd.theming import ThemableBehavior
from kivy.properties import StringProperty
from plyer import filechooser
from kivymd.uix.label import MDLabel
import datetime
import numpy as np
import firebase_admin
from firebase_admin import credentials, storage
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineAvatarListItem, MDList
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import requests
import random
from kivy.utils import platform

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE,
        Permission.INTERNET,
    ])



class LoginPage(Screen):
	pass

class CustomerLoginPage(Screen):
	pass

class AdminLoginPage(Screen):
	pass

class AdminPage(Screen):
	pass

class AddCustomerPage(Screen):
    pass

class GenerateIDPage(Screen):
    pass

class CustomerProfilePage(Screen):
    pass

class ContentNavigationDrawer(BoxLayout):
    pass

class NavigationPageButtons(OneLineAvatarListItem):
    source = StringProperty()

class DrawerList(ThemableBehavior, MDList):
        pass

class CustomerAccountingPage(Screen):
    pass

class CustomerReportsPage(Screen):
    pass

class CustomerAccountingSalesPage(Screen):
    pass

class CustomerAccountingPurcasePage(Screen):
    pass

class CustomerAccountingBankPage(Screen):
    pass

class CustomerAccountingCashPage(Screen):
    pass

class CustomerAccountingExpPage(Screen):
    pass

class CustomerAccountingJounralPage(Screen):
    pass

class CustomerReportsAccountPage(Screen):
    pass

class CustomerReportsP_LPage(Screen):
    pass

class CustomerReportsBLSPage(Screen):
    pass

class CustomerReportsGSTReportsPage(Screen):
    pass

class UploadFhotosPage(Screen):
    pass

class ViewCustomerInfoPage(Screen):
    pass

class UploadFhotosFiles(Screen):
    pass

class EditCustomerProfile(Screen):
    pass

class EditCustomerProfileByAdmin(Screen):
    pass

class ViewEditCustomerProfileByAdmin(Screen):
    pass

sm = ScreenManager()
sm.add_widget(LoginPage(name='loginpage'))
sm.add_widget(CustomerLoginPage(name='customerloginpage'))
sm.add_widget(AdminLoginPage(name='adminloginpage'))
sm.add_widget(AdminPage(name='adminpage'))
sm.add_widget(AddCustomerPage(name='addcustomerpage'))
sm.add_widget(GenerateIDPage(name='generateidpage'))
sm.add_widget(CustomerProfilePage(name='customerprofilepage'))
sm.add_widget(CustomerAccountingPage(name='customeraccountingpage'))
sm.add_widget(CustomerReportsPage(name='customerreportspage'))
sm.add_widget(CustomerAccountingSalesPage(name='CustomerAccountingSalesPage'))
sm.add_widget(CustomerAccountingPurcasePage(name='CustomerAccountingPurcasePage'))
sm.add_widget(CustomerAccountingBankPage(name='CustomerAccountingBankPage'))
sm.add_widget(CustomerAccountingCashPage(name='CustomerAccountingCashPage'))
sm.add_widget(CustomerAccountingExpPage(name='CustomerAccountingExpPage'))
sm.add_widget(CustomerAccountingJounralPage(name='CustomerAccountingJounralPage'))
sm.add_widget(CustomerReportsAccountPage(name='CustomerReportsAccountPage'))
sm.add_widget(CustomerReportsP_LPage(name='CustomerReportsP_LPage'))
sm.add_widget(CustomerReportsBLSPage(name='CustomerReportsBLSPage'))
sm.add_widget(CustomerReportsGSTReportsPage(name='CustomerReportsGSTReportsPage'))
sm.add_widget(UploadFhotosPage(name='UploadFhotosPage'))
sm.add_widget(ViewCustomerInfoPage(name='ViewCustomerInfoPage'))
sm.add_widget(UploadFhotosFiles(name="UploadFhotosFiles"))
sm.add_widget(EditCustomerProfile(name="EditCustomerProfile"))
sm.add_widget(EditCustomerProfileByAdmin(name="EditCustomerProfileByAdmin"))
sm.add_widget(ViewEditCustomerProfileByAdmin(name="ViewEditCustomerProfileByAdmin"))

class CusAdminApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url7 = "https://my-app-aae0f-default-rtdb.firebaseio.com/.json"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        self.str = Builder.load_file('try.kv')
        return self.str

    def handle_selection(self, selection):
        if selection:
            self.root.get_screen('UploadFhotosFiles').ids.upload_Image.text = selection[0]
            cred = credentials.Certificate({
                            "type": "service_account",
                            "project_id": "my-app-aae0f",
                            "private_key_id": "944365e17e0e73061b51f4938cb89071307dd70b",
                            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC0DU9m4gBrlM8G\nhckjy92YW0bUjOkAjnujeGX0FE7zNZmNEbGTW4GCxCHwZeYzIsx/M8r9LH8+ZIfP\nt8Ca0j17AyfUqyV1QgZPR4ttMn/j2xR4qw4eI2fRtMi0dF2k3VrpUG8vFdSLhTag\nFVc2WFvWVj1DWzFsRmzwq5l0W9ae8wWVyM4tliiBsb0z8SXEId3SVp95B9jdgPTA\nujjNDSC4wUHLwdwh8rOn1x+Ib8Vjt2DAfotj49F1T7ilXNozyyAsDf2pP5SPDHE9\nxpKVTHGaxrxI59vaRC8YTc8iDVuQFK/RvPV/6SyvB0kvRcGZClwpTuNmaW1vLC/V\nDnjgu6hVAgMBAAECggEASsDp8fusE/5s87bQ+0E1h/+BiVbVmEsPzx96KNvTqYtb\n7KNneBg6TZnzw1TzPdDZWYid4v45+CQR9O5EE6NtLijxvQyvmR7n8rtwCk64pVf8\niFrwmhe2D22BFNbpWD0k9RBVkRV9sM2Gj/E8S85klrkoZ1Ix01PsAAImzJYipcvo\nugE3WA5CiewshkIzi8p8TYXJ6G9R+Hevkiq0nMSr7/yIWrj/eooSRqmobo7+KJCv\nE4QBP6DeTUKoTEg7kGtqaQ5nUfeZYIDttlorMKaR0kcxe0MjANkPtta7caxTj7jg\n7rQV4NXNvpQO7vor7aHSmcaIvo2wwpkL6XjoByVWEwKBgQD79jhZyJCkCTtr5+Fj\nonxYp/s375Wn26/5IvwIx8L1+DUdRq8GdwgaToASEkNv8fW+tzHykpxh3rYwJiUg\n3CcK0RKt+xIJusw7SPFNIDznwjktBCWgbySisi47Qly1yvynqk8Xe+jWrFJPOKu9\nn/+vfDCc0JjSDSGwLuizU9RQcwKBgQC28Ay1i7e3xfUzaDILbtaPnQ4RQRyNOLo6\nZUjk51Nj3DCYTrx9ux89vu70zzJo27O4n8vlWEVTCEcvV7+yX7pMZmQmrfBRboTO\nUvTlw+zBbYzaACQ+D/f0/AiqUsRtOXfJAhw6pvpcYGOWmGXzK863f/EzE27LINeS\nCHL0QiBaFwKBgQDCQjNwBZJ+5h9KMp0zlDMKp3iox686m8Yw7ygiHOHTgmpxB+4p\nrdwxbBSR2kLkLEirodKAk0i+rFcLCF3X1+TCEi+0s75UghC0JKjmLdTHWpd6fZgE\n+avlRDsgtSmFf9sL6eLQ2FfMK0/KhIbkzFb1lWplfO5WBInUrFX87MTkwQKBgBo3\nbJrX2wxLIkirtgBNchJCv7FZU24powabXUbwn9K/y3cIUZrzJhcDNdt/lgnQ8oCS\n5fWIIOc1WH5AZQh7D4fDZLbmVnpVDFNFMDN9UICn4nebbZY3U6GYPOWr1tqQUcpM\nsx70rwxuA9ehH3sp3AYQH9DiCA60NjCHZXH7yAchAoGAQHcOpEwdj7EdQ/TPkXkE\nEG61BibTVnSuku+XCfr79XxwqZQ4kNUza0A2HaqGMajwAlR/+jo8JhD/r9M/Aj78\nG7Ph8RgqB99uxuFrADloOwIA+52irf3g68Gw3sxiThuYJjkEDusuBMjoVexnUtcz\n55d9LjOx1cUyYlWhuhz3KIg=\n-----END PRIVATE KEY-----\n",
                            "client_email": "firebase-adminsdk-8vsrw@my-app-aae0f.iam.gserviceaccount.com",
                            "client_id": "112518266211723451511",
                            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                            "token_uri": "https://oauth2.googleapis.com/token",
                            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8vsrw%40my-app-aae0f.iam.gserviceaccount.com"
                    })
            app = firebase_admin.initialize_app(cred, {"storageBucket": "my-app-aae0f.appspot.com"})
            self.bucket = storage.bucket()
            fileName = selection[0]
            self.blob = self.bucket.blob(fileName)
            new_token = uuid4()
            metadata  = {"firebaseStorageDownloadTokens": new_token}
            self.blob.metadata = metadata
            self.blob.upload_from_filename(fileName)
            self.blob.make_public()
            print("your file url", self.blob.public_url)
            print(selection[0])

    def AdminLogin(self):
        Admin_Id = self.str.get_screen('adminloginpage').ids.user_id.text
        Admin_password = self.str.get_screen('adminloginpage').ids.user_password.text
        if Admin_Id == "888" and Admin_password == "123":
            self.str.get_screen('adminloginpage').manager.current = 'adminpage'
            print("45")
            r = requests.get(self.url7)
            self.data = r.json()
            self.students = set()
            for key, value in self.data.items():
                self.students.add(key)
            for self.i in self.students:
                # self.i = self.i.replace('.','-')
                print(self.data[self.i]["Name"])
                # self.str.get_screen('adminpage').ids.AdminPageContainer.add_widget(
                #     TwoLineAvatarListItem(text= str(self.data[self.i]["Name"]),
                #     secondary_text=self.data[self.i]["Mobile Number"], on_release=self.prit_Name) ,
                #     ImageLeftWidget(source=str(self.data[self.i]["URL"]))
                # )
                user_imag = ImageLeftWidget(source= self.data[self.i]["URL"])
                user_list = TwoLineAvatarListItem(text= str(self.data[self.i]["Name"]),
                        secondary_text=self.data[self.i]["Mobile Number"], on_release=self.prit_Name)
                user_list.add_widget(user_imag)
                self.str.get_screen('adminpage').ids.AdminPageContainer.add_widget(user_list)
        else:
            cancel_btn_username_dialogue = MDFlatButton(text = 'Retry',on_release=self.close_Customer_login_dialog)
            self.str.get_screen('adminloginpage').manager.current = 'adminloginpage'
            self.dialog = MDDialog(title = "Invalid Username Password",text = "Please check usename or password", size_hint = (0.7,0.2), buttons = [cancel_btn_username_dialogue])
            self.dialog.open()

    def add_customer(self):
        print("ADD Customer")
        self.str.get_screen('adminpage').manager.current = 'addcustomerpage'

    def Generate_Id(self):
        self.customer_name = self.str.get_screen('addcustomerpage').ids.customer_name.text
        self.customer_number = self.str.get_screen('addcustomerpage').ids.user_mobile_number.text
        self.customer_bio = self.str.get_screen('addcustomerpage').ids.customer_bio.text
        self.id = self.customer_name[0:3] + self.customer_bio[2:5] + str(random.randint(1000,9999))
        print(self.id)
        self.password = str(random.randint(100000,999999))
        print(self.password)
        cancel_btn_username_dialogue = MDFlatButton(text = 'OK', on_release=self.close_username_dialog)
        self.dialog = MDDialog(title = "Customer Id and Password",text = f"Customer-ID = {self.id}\nPassword = {self.password}", size_hint = (0.7,0.2), buttons = [cancel_btn_username_dialogue])
        self.dialog.open()

    def close_username_dialog(self, obj):
        self.url2 = "https://www.fast2sms.com/dev/bulk"
        json_data = str(
            {f'\"{self.id}\":{{"Name":\"{self.customer_name}\","Bio":\"{self.customer_bio}\","Mobile Number":\"{self.customer_number}\","Password":\"{self.password}\", "URL":\"{self.blob.public_url}\"}}'}
			)
        # json_data = json_data.replace(".", "-")
        json_data = json_data.replace("\'", "")
        res = requests.patch(url=self.url7, json=json.loads(json_data))
        print(res, "id :" + self.id, "password: " + self.password)
        my_data = {
	        # Your default Sender ID
	        'sender_id': 'FastSM',
	
	        # Put your message here!
	        'message': f'Dear {self.customer_name} you succesfully joined. /n Your Id: {self.id} /n {self.password}',
	
	        'language': 'english',
	        'route': 'p',
	
	        # You can send sms to multiple numbers
	        # separated by comma.
	        'numbers': self.customer_number
            }

            # create a dictionary
        headers = {
	            'authorization': 'zjHFWBvib8KXtNVTqhRP9Yl7np1rJ4fUuxdMC5QDGLS2c0geI6ScyqaW8Rrh4NFYez71xjnDQkboHUig',
	            'Content-Type': "application/x-www-form-urlencoded",
	            'Cache-Control': "no-cache"
            }
            # make a post request
        response = requests.request("POST",
							    self.url2,
							    data = my_data,
							    headers = headers)

            # load json data from source
        returned_msg = json.loads(response.text)

            # print the send message
        print(returned_msg['message'])
        if returned_msg['message'] == "Invalid Numbers":
                cancel_btn_username_dialogue = MDFlatButton(text = 'Retry', on_release=self.close_username_dialog)
                self.dialog = MDDialog(title = "Invalid Number",text = "Please enter valid mobile number", size_hint = (0.7,0.2), buttons = [cancel_btn_username_dialogue])
                self.str.get_screen('addcustomerpage').manager.current = 'addcustomerpage'
                self.dialog.open()
        else:
                self.str.get_screen('addcustomerpage').manager.current = 'adminpage'
        self.dialog.dismiss()
    
    def prit_Name(self, onelinelistitem):
        print('play:', onelinelistitem.text)
        self.str.get_screen('ViewCustomerInfoPage').ids.customer_view_id.text = self.i
        self.str.get_screen('ViewCustomerInfoPage').ids.user_view_image.source = self.data[self.i]["URL"]
        self.str.get_screen('ViewCustomerInfoPage').ids.customer_view_Pass.text = str(self.data[self.i]["Password"])
        self.str.get_screen('ViewCustomerInfoPage').ids.customer_view_name.text = str(self.data[self.i]["Name"])
        self.str.get_screen('ViewCustomerInfoPage').ids.customer_view_mobile.text = str(self.data[self.i]["Mobile Number"])
        self.str.get_screen('ViewCustomerInfoPage').ids.customer_view_bio.text = str(self.data[self.i]["Bio"])
        self.str.get_screen('adminpage').manager.current = 'ViewCustomerInfoPage'

    def open_search_page(self):
        self.str.get_screen('adminpage').manager.current = 'searchiconpage'

    def CustomerLogin(self):
        self.Customer_id = self.str.get_screen('customerloginpage').ids.customer_id.text
        Customer_password = self.str.get_screen('customerloginpage').ids.customer_password.text
        self.login_check = False
        self.Customer_id = self.Customer_id.replace('.','-')
        self.Customer_password = Customer_password.replace('.', '-')
        # request = requests.get(self.url+'?auth='+self.auth)
        request = requests.get(self.url7)
        self.data = request.json()
        emails = set()
        for key,value in self.data.items():
            emails.add(key)

        if self.Customer_id in emails and self.Customer_password == self.data[self.Customer_id]['Password']:
            self.login_check= True
            self.str.get_screen('customerloginpage').manager.current = 'customerprofilepage'
            self.str.get_screen('customerprofilepage').ids.customer_id.text = self.Customer_id
            self.str.get_screen('customerprofilepage').ids.user_image.source = self.data[self.Customer_id]["URL"]
            self.str.get_screen('customerprofilepage').ids.customer_name.text = str(self.data[self.Customer_id]["Name"])
            self.str.get_screen('customerprofilepage').ids.customer_mobile.text = str(self.data[self.Customer_id]["Mobile Number"])
            self.str.get_screen('customerprofilepage').ids.customer_bio.text = str(self.data[self.Customer_id]["Bio"])
            print("r")
        else:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_Customer_login_dialog)
            self.dialog = MDDialog(title="Invalid Username", text="please check your ID or Password",
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
            print("user no longer exists")

    def close_Customer_login_dialog(self, obg):
        self.dialog.dismiss()

    def edit_customer_profile(self):
        self.str.get_screen('customerprofilepage').manager.current = 'EditCustomerProfile'
        self.str.get_screen('EditCustomerProfile').ids.user_image.source = self.data[self.Customer_id]["URL"]
        self.str.get_screen('EditCustomerProfile').ids.customer_name.text = str(self.data[self.Customer_id]["Name"])
        self.str.get_screen('EditCustomerProfile').ids.user_mobile_number.text = str(self.data[self.Customer_id]["Mobile Number"])
        self.str.get_screen('EditCustomerProfile').ids.customer_bio.text = str(self.data[self.Customer_id]["Bio"])
        print("m")

    def Update_Profile(self):
        customer_name = self.str.get_screen('EditCustomerProfile').ids.customer_name.text
        customer_number = self.str.get_screen('EditCustomerProfile').ids.user_mobile_number.text
        customer_bio = self.str.get_screen('EditCustomerProfile').ids.customer_bio.text
        datetime_object = datetime.datetime.now()
        print(datetime_object)
        password = self.Customer_password
        json_data = str(
            {f'\"{self.Customer_id}\":{{"Name":\"{customer_name}\","Bio":\"{customer_bio}\","Mobile Number":\"{customer_number}\","Password":\"{password}\", "URL":\"{self.blob.public_url}\"}}'}
			)
        # json_data = json_data.replace(".", "-")
        json_data = json_data.replace("\'", "")
        res = requests.patch(url=self.url7, json=json.loads(json_data))
        self.str.get_screen('EditCustomerProfile').manager.current = 'customerloginpage'
        print("Profile Updated")

    def edit_customer_profile_by_admin(self):
        self.str.get_screen('EditCustomerProfileByAdmin').ids.customer_id.text = self.i
        self.str.get_screen('EditCustomerProfileByAdmin').ids.user_image.source = self.data[self.i]["URL"]
        self.str.get_screen('EditCustomerProfileByAdmin').ids.customer_password.text = str(self.data[self.i]["Password"])
        self.str.get_screen('EditCustomerProfileByAdmin').ids.customer_name.text = str(self.data[self.i]["Name"])
        self.str.get_screen('EditCustomerProfileByAdmin').ids.user_mobile_number.text = str(self.data[self.i]["Mobile Number"])
        self.str.get_screen('EditCustomerProfileByAdmin').ids.customer_bio.text = str(self.data[self.i]["Bio"])
        self.str.get_screen('ViewCustomerInfoPage').manager.current = 'EditCustomerProfileByAdmin'
        print("edit_customer_profile_by_admin")

    def Update_Profile_By_Admin(self):
        Customer_id = self.str.get_screen('EditCustomerProfileByAdmin').ids.customer_id.text
        customer_name = self.str.get_screen('EditCustomerProfileByAdmin').ids.customer_name.text
        customer_bio = self.str.get_screen('EditCustomerProfileByAdmin').ids.customer_bio.text
        customer_number = self.str.get_screen('EditCustomerProfileByAdmin').ids.user_mobile_number.text
        password = self.str.get_screen('EditCustomerProfileByAdmin').ids.customer_password.text
        json_data = str(
            {f'\"{Customer_id}\":{{"Name":\"{customer_name}\","Bio":\"{customer_bio}\","Mobile Number":\"{customer_number}\","Password":\"{password}\", "URL":\"{self.blob.public_url}\"}}'}
			)
        # json_data = json_data.replace(".", "-")
        json_data = json_data.replace("\'", "")
        res = requests.patch(url=self.url7, json=json.loads(json_data))
        self.str.get_screen('EditCustomerProfile').manager.current = 'customerloginpage'
        print("Profile Updated")

    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection)

    def view_Profile(self):
        self.str.get_screen('ViewCustomerInfoPage').manager.current = 'ViewEditCustomerProfileByAdmin'

    

CusAdminApp().run()