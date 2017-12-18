
# coding: utf-8

# In[14]:


from zipfile import ZipFile
from urllib import urlretrieve
import urllib
import urllib2
from tempfile import mktemp
import csv
import datetime
import requests
import pandas as pd
data1={}
n = 1
this_day = datetime.datetime.now().date().weekday()
this_time = datetime.datetime.now().time()
monday_time = this_time.replace(hour=6, minute=40, second=0, microsecond=0)
friday_time = this_time.replace(hour=14, minute=40, second=0, microsecond=0)
print( monday_time)
print(friday_time)
while n>0:
    this_time = datetime.datetime.now().time()
    if(this_time == friday_time and this_day == 4):
        print("CFTC")
        filename = mktemp('.zip')
        # destDir = "c:\Users\ulysses\Documents\Project 1"
        theurl = 'http://www.cftc.gov/files/dea/history/fut_disagg_xls_2017.zip'
        theurl2 = 'http://www.cftc.gov/files/dea/history/com_disagg_xls_2017.zip'
        name, hdrs = urlretrieve(theurl2, filename)
#         name, hdrs = urlretrieve(theurl, filename)
        thefile=ZipFile(filename)
        thefile.extractall(destDir)
        name, hdrs = urlretrieve(theurl, filename)
        thefile=ZipFile(filename)
        thefile.extractall()
        thefile.close()


        data_xls = pd.read_excel('f_year.xls', index_col=None)
        data_xls.to_csv('f_year.csv', encoding='utf-8')
        df = pd.read_csv('f_year.csv', error_bad_lines=False,index_col=False,usecols=[1,2,8,9,10,11,12,14,15,17,18])
        df.to_csv('f_year.csv')
        
        data_xls1 = pd.read_excel('c_year.xls', index_col=None)
        data_xls1.to_csv('c_year.csv', encoding='utf-8')
        df1 = pd.read_csv('c_year.csv', error_bad_lines=False,index_col=False,usecols=[1,2,8,9,10,11,12,14,15,17,18])
        df1.to_csv('c_year.csv')
                    
        df_f=pd.DataFrame.from_csv("f_year.csv")
        df_f['Swap_net']=df_f['Swap_Positions_Long_All']- df_f['Swap__Positions_Short_All']
        df_f['Managed_net']=df_f['M_Money_Positions_Long_ALL']- df_f['M_Money_Positions_Short_ALL']
        df_f['other_net']=df_f['Other_Rept_Positions_Long_ALL']- df_f['Other_Rept_Positions_Short_ALL']
        df_f['Prod_net']=df_f['Prod_Merc_Positions_Long_ALL']- df_f['Prod_Merc_Positions_Short_ALL']
        df_f['Swap_ratio']=df_f['Swap_net']/ df_f['Open_Interest_All']
        df_f['Managed_ratio']=df_f['Managed_net']/ df_f['Open_Interest_All']
        df_f['other_ratio']=df_f['other_net']/ df_f['Open_Interest_All']
        df_f['Prod_ratio']=df_f['Prod_net']/ df_f['Open_Interest_All']
        df_f.to_csv('cftc_f.csv',index=False)
        
        df_c=pd.DataFrame.from_csv("c_year.csv")
        df_c['Swap_net']=df_c['Swap_Positions_Long_All']- df_c['Swap__Positions_Short_All']
        df_c['Managed_net']=df_c['M_Money_Positions_Long_ALL']- df_c['M_Money_Positions_Short_ALL']
        df_c['other_net']=df_c['Other_Rept_Positions_Long_ALL']- df_c['Other_Rept_Positions_Short_ALL']
        df_c['Prod_net']=df_c['Prod_Merc_Positions_Long_ALL']- df_c['Prod_Merc_Positions_Short_ALL']
        df_c['Swap_ratio']=df_c['Swap_net']/ df_c['Open_Interest_All']
        df_c['Managed_ratio']=df_c['Managed_net']/ df_c['Open_Interest_All']
        df_c['other_ratio']=df_c['other_net']/ df_c['Open_Interest_All']
        df_c['Prod_ratio']=df_c['Prod_net']/ df_c['Open_Interest_All']
        df_c.to_csv('cftc_c.csv',index=False)
        
        reader = csv.reader(open("cftc_f.csv", "r"), delimiter=',')

        f = csv.writer(open("final_cftc_f.csv", "w"))
        for line in reader:
            if  ("Market_and_Exchange_Names") in line:
                            f.writerow(line)
                    #         print line
            if  ("CRUDE OIL, LIGHT SWEET - NEW YORK MERCANTILE EXCHANGE") in line:
                            f.writerow(line)
                    #         print line   
            if  ("CRUDE OIL, LIGHT SWEET-WTI - ICE FUTURES EUROPE") in line:
                            f.writerow(line)
        reader = csv.reader(open("cftc_c.csv", "r"), delimiter=',')

        f = csv.writer(open("final_cftc_c.csv", "w"))
        for line in reader:
            if  ("Market_and_Exchange_Names") in line:
                            f.writerow(line)
                    #         print line
            if  ("CRUDE OIL, LIGHT SWEET - NEW YORK MERCANTILE EXCHANGE") in line:
                            f.writerow(line)
                    #         print line   
            if  ("CRUDE OIL, LIGHT SWEET-WTI - ICE FUTURES EUROPE") in line:
                            f.writerow(line)
       
        df = pd.read_csv("final_cftc_f.csv")
        date=df['As_of_Date_In_Form_YYMMDD']
        data1 = {}
        for i in range(0,len(date)):
            x = date[i]
            print(x)
            data = pd.read_csv("http://apps.ulysses.biz/get_report?date=20"+str(x)+"&table=wti&type=csv",header=None,error_bad_lines=False,delimiter=";")
        #     print data[0]; 
            data1[i] = data[0];
        with open('mycsvfile.csv', 'wb') as f: 
            w = csv.DictWriter(f, data1)
            w.writeheader()
            w.writerow(data1)
        mycsv=pd.read_csv('mycsvfile.csv')
        mycsv1=mycsv.apply(lambda x : str(x).split('|')[-1])
        mycsv1.to_csv("mycsv.csv",index=False)
        mycsv2=pd.read_csv("mycsv.csv",header=None)
        df["spot_price"]=mycsv2
        df["spot_price"]
        # df['spot_price'] = df['spot_price'].apply(lambda x : str(x).split('|')[-1])
        df['spot_price'] = df['spot_price'].map(lambda x: str(x)[0:5])
        df.to_csv("final_cftc_f.csv",index=False)
        
        
        df = pd.read_csv("final_cftc_c.csv")
        date=df['As_of_Date_In_Form_YYMMDD']
        data1 = {}
        for i in range(0,len(date)):
            x = date[i]
            print(x)
            data = pd.read_csv("http://apps.ulysses.biz/get_report?date=20"+str(x)+"&table=wti&type=csv",header=None,error_bad_lines=False,delimiter=";")
        #     print data[0]; 
            data1[i] = data[0];
        with open('mycsvfile.csv', 'wb') as f: 
            w = csv.DictWriter(f, data1)
            w.writeheader()
            w.writerow(data1)
        mycsv=pd.read_csv('mycsvfile.csv')
        mycsv1=mycsv.apply(lambda x : str(x).split('|')[-1])
        mycsv1.to_csv("mycsv.csv",index=False)
        mycsv2=pd.read_csv("mycsv.csv",header=None)
        df["spot_price"]=mycsv2
        df["spot_price"]
        # df['spot_price'] = df['spot_price'].apply(lambda x : str(x).split('|')[-1])
        df['spot_price'] = df['spot_price'].map(lambda x: str(x)[0:5])
        df.to_csv("final_cftc_c.csv",index=False)
        break
        
    elif(this_day==0 and this_time == monday_time):
        print("ICE Data")
        
        ice_df=pd.read_csv("https://www.theice.com/publicdocs/futures/COTHist2017.csv", error_bad_lines=False,index_col=False,usecols=[0,1,7,8,9,10,11,13,14,16,17])
        ice_df["Swap_net"]=ice_df["Swap_Positions_Long_All"]- ice_df["Swap__Positions_Short_All"]
        ice_df["Managed_net"]=ice_df["M_Money_Positions_Long_All"]- ice_df["M_Money_Positions_Short_All"]
        ice_df["other_net"]=ice_df["Other_Rept_Positions_Long_All"]- ice_df["Other_Rept_Positions_Short_All"]
        ice_df["Prod_net"]=ice_df["Prod_Merc_Positions_Long_All"]- ice_df["Prod_Merc_Positions_Short_All"]
        ice_df['Swap_ratio']=ice_df['Swap_net']/ ice_df['Open_Interest_All']
        ice_df['Managed_ratio']=ice_df['Managed_net']/ ice_df['Open_Interest_All']
        ice_df['other_ratio']=ice_df['other_net']/ ice_df['Open_Interest_All']
        ice_df['Prod_ratio']=ice_df['Prod_net']/ ice_df['Open_Interest_All']
        ice_df.to_csv("ice_parsed.csv",index=False)
        
        with open("ice_parsed.csv", "r") as  reader:
        
            with open("final_ice.csv", "w") as f:
                for line in reader:
                    if  ("Market_and_Exchange_Names") in line:
                        f.write(line)
                #         print line
                    if  ("ICE Brent Crude Futures - ICE Futures Europe") in line:
                        f.write(line)
                #         print line   
                    if  ("ICE Brent Crude Futures and Options - ICE Futures Europe") in line:
                        f.write(line)
            
        df = pd.read_csv("final_ice.csv")
        date=df['As_of_Date_In_Form_YYMMDD']
        data1 = {}
        for i in range(0,len(date)):
            x = date[i]
            print(x)
            try:
                data = pd.read_csv("http://apps.ulysses.biz/get_report?date=20"+str(x)+"&table=b&type=csv",header=None,error_bad_lines=False,delimiter=";")
                print data[0]
                data1[i] = data[0]

            except urllib2.HTTPError, e:
                print "error"
                print e.code
                print e.msg
                data1[i] = data1[i-1]
        with open('mycsvfile.csv', 'wb') as f: 
            w = csv.DictWriter(f, data1)
            w.writeheader()
            w.writerow(data1)
        mycsv=pd.read_csv('mycsvfile.csv')
        mycsv1=mycsv.apply(lambda x : str(x).split('|')[-1])
        mycsv1.to_csv("mycsv.csv",index=False)
        mycsv2=pd.read_csv("mycsv.csv",header=None)
        df["spot_price"]=mycsv2
        df["spot_price"]
        # df['spot_price'] = df['spot_price'].apply(lambda x : str(x).split('|')[-1])
        df['spot_price'] = df['spot_price'].map(lambda x: str(x)[0:5])
        df.to_csv("final_brent_ice.csv",index=False)
                        

        break


# In[ ]:




