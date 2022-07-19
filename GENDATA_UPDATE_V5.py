#!/usr/bin/env python
# coding: utf-8

#happy thoughts v4


#from IPython import get_ipython
#get_ipython().system('pip install geonamescache')
#get_ipython().system('pip install pandas')
#get_ipython().system('pip install openpyxl')
#get_ipython().system('pip install pandas')
#get_ipython().system('pip install lxml')
# In[1]:



val = input("Enter your value: ")
x=int(val)
print('Wait while transanction is completed')



import sys
import string
import numpy as np
import pandas as pd
import random
import re
import geonamescache as gn


# In[2]:


gc = gn.GeonamesCache()


# In[3]:


base_url='https://docs.google.com/spreadsheets/d/1CYRpcLXAmw9_XEQLIEGuyny273lRGUK1/edit?usp=sharing&ouid=107259259153241740368&rtpof=true&sd=true'
url='https://drive.google.com/uc?id=' + base_url.split('/')[-2]
df = pd.read_excel(url)


# In[4]:


states = gc.get_us_states_by_names()
state={}
for i in states:
    state[f"{states[i]['name']}"]=f"{states[i]['code']}"


# In[5]:


male_middle_name=list(pd.read_html('https://github.com/aliakbar-sh1991/misc/blob/main/middle_name_male.csv',header=None)[0]['0'])
female_middle_name=list(pd.read_html('https://github.com/aliakbar-sh1991/misc/blob/main/middle_name_female.csv',header=None)[0]['0'])
list(pd.read_html('https://github.com/aliakbar-sh1991/misc/blob/main/middle_name_male.csv',header=None)[0]['0'])
ss_wiki=pd.read_html('https://en.wikipedia.org/wiki/Social_Security_number#:~:text=report%20is%20required.-,Structure,AAA%2DGG%2DSSSS%22.')[0]
profs=pd.read_html('https://github.com/aliakbar-sh1991/misc/blob/main/professions.csv',header=None)
profs = profs[0][['profession','salary']]
profs['salary'] = profs['salary'].apply(lambda x:x.split()[0])


# In[6]:


first_name = list(df['name'])
female_first_name = list(df[df['gender']=='F']['name'])
male_first_name = list(df[df['gender']=='M']['name'])
lastnameexl = pd.read_html('https://github.com/aliakbar-sh1991/misc/blob/main/lastnames.csv',header=None)
last_name = list(lastnameexl[0][1])


# In[7]:


q=[]
def get_x_first_names(x):
    for i in range(0,x):
        a= random.choice(first_name)
        q.append(a)


# In[8]:


get_x_first_names(x)
base_df = pd.DataFrame(q)
base_df.columns=['first_name']


# In[9]:


def get_last_names():
    return random.choice(last_name)


# In[10]:


base_df['last_name']=base_df['first_name'].apply(lambda x:get_last_names())


# In[11]:


def check_gender(name):
    y = name.split()[0]
    if y in female_first_name:
        return 'F'
    else:
        return 'M'
base_df['gender']=base_df['first_name'].apply(lambda x:check_gender(x))


# In[12]:


def get_mid_name(x):
    if x=='M':
        return random.choice(male_middle_name)
    if x=='F':
        return random.choice(female_middle_name)


# In[13]:


base_df['middle_name'] = base_df['gender'].apply(lambda zz:get_mid_name(zz))
base_df=base_df[['first_name','middle_name','last_name','gender']]

# In[14]:


def get_emails(y,z):
    y=y.lower()
    z=z.lower()
    email_providers = ['gmail', 'yahoo', 'outlook', 'aol', 'zoho', 'mail', 'protonMail']
    filler_gmail=['.']
    filler = ['.','_']
    num = np.arange(0,100)
    email_prov_choice = random.choice(email_providers)
    if email_prov_choice=='gmail':
        return y+random.choice(filler_gmail)+z+str(random.choice(num))+'@'+email_prov_choice+'.com'
    else:
        return y+random.choice(filler)+z+str(random.choice(num))+'@'+email_prov_choice+'.com'


# In[15]:


base_df['email'] = np.vectorize(get_emails)(base_df['first_name'],base_df['last_name'])


# In[16]:


def do_age(name):
    y = name.split()[0]
    if y in female_first_name:
        a = np.arange(18,35)
        b = random.choice(a)
        return b
    else:
        c = np.arange(18,64)
        d = random.choice(c)
        return d
base_df['age'] = np.vectorize(do_age)(base_df['first_name'])


# In[17]:


cc_comp= ['Visa','MasterCard','American Express']
base_df['cc_comp'] = base_df['first_name'].apply(lambda x:random.choice(cc_comp))


# In[ ]:





# In[ ]:





# In[18]:


base_df['State']=base_df['first_name'].apply(lambda x:random.choice(list(state.keys())))


# In[19]:


base_df['state_abbv'] = base_df['State'].map(state)


# In[36]:


relationship_status= ['Married','Single','Divorced','Commited','Civil Partnership','Engaged']
base_df['relationship_status'] = base_df['first_name'].apply(lambda x:random.choice(relationship_status))
counties = pd.DataFrame(gc.get_us_counties())
def get_county(county):
    x = list(counties[counties['state']==county]['name'])
    return random.choice(x)
base_df['County']=np.vectorize(get_county)(base_df['state_abbv'])
def get_partner_name(x,y):
    if x not in ['Single','Civil Partnership']:
        if y=='M':
            return random.choice(female_first_name)+ ' ' + random.choice(last_name)
        if y=='F':
            return random.choice(male_first_name)+ ' ' + random.choice(last_name)
    if x=='Civil Partnership':
        return random.choice(male_first_name)+ ' ' + random.choice(last_name)
    else:
        return None
base_df["Partner/Ex-Partner's_name"]=np.vectorize(get_partner_name)(base_df['relationship_status'],base_df['gender'])


# In[21]:


def get_phonenum():
    x=np.arange(250,750)
    y=np.arange(250,750)
    z=np.arange(2500,9850)
    return  '+1'+ '-'+ str(random.choice(x))+'-'+str(random.choice(y))+'-'+str(random.choice(z))


# In[22]:


profes1819f=['Student','Waitress','Actress','Voice Artist']
profes1819m=['Student','Waiter']
def get_prof(gen,age):
    if (gen=='M') and age>19:
        return random.choice(list(profs['profession']))
    elif (gen=='M') and age<=19:
        return random.choice(profes1819m)
    elif (gen=='F') and age>19:
        return random.choice(list(profs['profession']))
    elif (gen=='F') and age<=19:
        return random.choice(profes1819f)
base_df['Profession']=np.vectorize(get_prof)(base_df['gender'],base_df['age'])


# In[23]:


dic1819={'Student':'$0','Waitress':'$25,000','Waiter':'$15,000','Actress':'$70,000','Voice Artist':'$35,000'}
def get_salary(prof):
    if prof in list(profs['profession']):
        z = list(profs[profs['profession']==prof]['salary'])
        return f"${z[0]}"
    else:
        return dic1819[prof]
base_df['Salary']=base_df['Profession'].apply(lambda x:get_salary(x))


# In[ ]:





# In[25]:


def own_realestate():
    return random.choice(['Yes','No'])
def own_car():
    return random.choice(['Yes','No'])
def cc_num(x):
    if x == 'Visa':
        return (str(random.choice(np.arange(4000,4999)))+'-'+str(random.choice(np.arange(1000,9999)))+'-'+str(random.choice(np.arange(1000,9999)))+'-'+str(random.choice(np.arange(1000,9999))))
    elif x == 'MasterCard':
        return (str(random.choice(np.arange(5000,5999)))+'-'+str(random.choice(np.arange(1000,9999)))+'-'+str(random.choice(np.arange(1000,9999)))+'-'+str(random.choice(np.arange(1000,9999))))
    else:
        return (str(random.choice(np.arange(3400,5999)))+'-'+str(random.choice(np.arange(1000,9999)))+'-'+str(random.choice(np.arange(1000,9999)))+'-'+str(random.choice(np.arange(100,999))))
def cc_exp_date():
    return (str(random.choice(np.arange(1,13)))+'/'+ str(random.choice(np.arange(22,28))))
def cvv():
    return (str(random.choice(np.arange(100,749))))
def out_country():
    return random.choice(['Yes','No'])
def out_country_name():
    pp = gn.GeonamesCache()
    keys = list(pp.get_countries().keys())
    ipso = []
    for i in keys:
        koko = pp.get_countries()[i]['name']
        ipso.append(koko)
    return random.choice(ipso)
red_flag_country=['Afghanistan', 'Belarus', 'Cuba', 'Iran', 'Nicaragua', 'North Korea', 'Russia', 'Syria', 'Venezuela']
def red_country(x):
    if x in red_flag_country:
        return 'Flag'
    else:
        return 'No Flag'


# In[26]:


base_df['own_realestate']=base_df['first_name'].apply(lambda x:own_realestate())
base_df['own_car']=base_df['first_name'].apply(lambda x:own_car())
base_df['Out country travel']=base_df['first_name'].apply(lambda x:out_country())
base_df['CC num']=np.vectorize(cc_num)(base_df['cc_comp'])
base_df['CC exp']=base_df['first_name'].apply(lambda x:cc_exp_date())
base_df['CVV']=base_df['first_name'].apply(lambda x:cvv())
def out_country_name(x):
    pp = gn.GeonamesCache()
    keys = list(pp.get_countries().keys())
    ipso = []
    if x =='Yes':
        for i in keys:
            koko = pp.get_countries()[i]['name']
            ipso.append(koko)
        return random.choice(ipso)
    else:
        return 'Null'
base_df['out_country_name']=base_df['Out country travel'].apply(lambda x:out_country_name(x))
base_df['Vist_flag']=base_df['out_country_name'].apply(lambda x:red_country(x))


# In[27]:


cars = ["Abarth","Alfa Romeo","Aston Martin","Audi","Bentley","BMW","Bugatti","Cadillac","Chevrolet","Chrysler","Citroën","Dacia","Daewoo","Daihatsu","Dodge","Donkervoort","DS","Ferrari","Fiat","Fisker","Ford","Honda","Hummer","Hyundai","Infiniti","Iveco","Jaguar","Jeep","Kia","KTM","Lada","Lamborghini","Lancia","Land Rover","Landwind","Lexus",
         "Lotus","Maserati","Maybach","Mazda","McLaren","Mercedes-Benz","MG","Mini","Mitsubishi","Morgan","Nissan","Opel","Peugeot","Porsche","Renault","Rolls-Royce","Rover","Saab","Seat","Skoda","Smart","SsangYong","Subaru","Suzuki","Tesla","Toyota","Volkswagen","Volvo"]
base_df['car_brand']=base_df['first_name'].apply(lambda x:random.choice(cars))


# In[28]:


def yesno_chil(age):
    if age<30:
        return random.choice(['Yes','No'])
    else:
        return 'Yes'
base_df['Children_yes_no'] = base_df['age'].apply(lambda age:yesno_chil(age))
def gen_child(ans,age):
    ch_d={}
    if ans=='No':
        ch_d['Male']=0
        ch_d['Female']=0
        return ch_d
    elif ans=='Yes' and age<20:
        male_num = random.choice([0,1])
        female_num = random.choice([0,1])
        if male_num==0:
            x=1
            ch_d['Male']=male_num
            ch_d['Female']=x
            return ch_d
        elif female_num==0:
            y=1
            ch_d['Male']=y
            ch_d['Female']=female_num
            return ch_d
        else:
            ch_d['Male']=1
            ch_d['Female']=0
            return ch_d
    elif ans=='Yes' and 20<=age<=25:
        male_num = random.choice([1,2])
        female_num = random.choice([1,2])
        ch_d['Male']=male_num
        ch_d['Female']=female_num
        return ch_d
    elif ans=='Yes' and 25<age<=35:
        male_num = random.choice([1,2])
        female_num = random.choice([1,2])
        ch_d['Male']=male_num
        ch_d['Female']=female_num
        return ch_d
    elif ans=='Yes' and age>35:
        male_num = random.choice([1,2,3])
        female_num = random.choice([1,2,3])
        ch_d['Male']=male_num
        ch_d['Female']=female_num
        return ch_d
base_df['child_how_many'] = np.vectorize(gen_child)(base_df['Children_yes_no'],base_df['age'])


# In[33]:


def get_blood():
    alpha=['A','B','AB','O']
    rhd=['+','-']
    return random.choice(alpha)+random.choice(rhd)
base_df['blood_type']=base_df['first_name'].apply(lambda x:get_blood())


# In[34]:


base_df["Mother's_maiden_name"]=base_df['first_name'].apply(lambda x:random.choice(last_name))


# In[40]:


def replace_shit(x):
    y = x.split(' ')
    if len(y)>=3:
        for i in y:
            if i.lower()=='guam':
                return 'Guam'
            elif i.lower()=='enumeration':
                return None
            elif i.lower()=='railroad':
                return None
            elif i.lower()=='worldwide':
                return None
            elif i.lower()=='issued':
                return  
    elif x=='Not issued':
        return 
    else:
        return x
ss_wiki.dropna(inplace=True)
ss_wiki['new_col'] = ss_wiki['Location[47]'].apply(lambda x:replace_shit(x))
ss_wiki['sep_col']=ss_wiki['SSN area number'].apply(lambda x:re.split(r'-|,|–',x))
def ss_generator(loc):
    if loc in list(ss_wiki['Location[47]']):
        z1= int(list(ss_wiki[ss_wiki['Location[47]']==loc]['sep_col'])[0][0])
        z2= int(list(ss_wiki[ss_wiki['Location[47]']==loc]['sep_col'])[0][-1])
        if z1!=z2:
            if z1<10 and z2<=10:
                return '00'+str(random.choice(np.arange(z1,z2))) + '-' + str(random.choice(np.arange(10,99)))  + '-' + str(random.choice(np.arange(1000,9999))) 
            if z1<11 and z2>10:
                return '0'+str(random.choice(np.arange(z1,z2))) + '-' + str(random.choice(np.arange(10,99)))  + '-' + str(random.choice(np.arange(1000,9999)))
            if z1<=50 and 100<z2<=134:
                u = random.choice(np.arange(z1,z2))
                if u<100:
                    return '0' + str(u) + '-' + str(random.choice(np.arange(10,99)))  + '-' + str(random.choice(np.arange(1000,9999)))
                else:
                    return str(u) + '-' + str(random.choice(np.arange(10,99)))  + '-' + str(random.choice(np.arange(1000,9999)))
            if z1<=50 and z2<100:
                return '0' + str(random.choice(np.arange(z1,z2))) + '-' + str(random.choice(np.arange(10,99)))  + '-' + str(random.choice(np.arange(1000,9999)))
            if z1>10 and z2<1000:
                return str(random.choice(np.arange(z1,z2))) + '-' + str(random.choice(np.arange(10,99)))  + '-' + str(random.choice(np.arange(1000,9999))) 
        if z1==z2:
            return str(z1) + '-' + str(random.choice(np.arange(10,99)))  + '-' + str(random.choice(np.arange(1000,9999))) 
base_df['Social Security']=base_df['State'].apply(lambda kk:ss_generator(kk))

base_df=base_df[['first_name','middle_name', 'last_name', 'gender', 'age','relationship_status',
       "Partner/Ex-Partner's_name", 'email', 
        'State', 'state_abbv',  'County',
       'Profession', 'Salary', 'own_realestate', 'own_car',
       'cc_comp', 'CC num', 'CC exp', 'CVV','Out country travel', 'out_country_name',
       'Vist_flag', 'car_brand', 'Children_yes_no', 'child_how_many',
       'Social Security', 'blood_type', "Mother's_maiden_name"]]


popopopo = input('Please enter the filename you want to save with  :  ')
filename = popopopo + str(random.choice(np.arange(200,90000)))+'.xlsx'
base_df.to_excel(filename)


