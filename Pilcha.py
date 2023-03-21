#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[30]:


df = pd.read_csv("C:/Users/federico.asensio/Downloads/bq-results-20220825-201632-1661458607435.csv")
df.head()
df.city.value_counts()


# In[31]:


df['user_type'] = np.where(df['q_order'] < 3, 'Light', np.where(df['q_order'] >= 8 ,'Super Heavy', np.where(df['q_order'] >= 5 ,'Heavy', 'Medium')))
# mayor igual a 3, 5 y 8


# In[32]:


dfsh = df[(df['user_type'] == 'Super Heavy')]
dfh = df[(df['user_type'] == 'Heavy')]
dfm =  df[(df['user_type'] == 'Medium')]
dfl =  df[(df['user_type'] == 'Light')]
dfalmagro = df[(df['city'] == 'Almagro')]
dfpalermo = df[(df['city'] == 'Palermo')]
dfrosario = df[(df['city'] == 'Rosario')]
dflaplata = df[(df['city'] == 'La Plata')]
dfneuquen = df[(df['city'] == 'Neuquén')]
dfurquiza = df[(df['city'] == 'Villa Urquiza')]
dfgodoycruz = df[(df['city'] == 'Ciudad de Godoy Cruz')]
dfriocuarto = df[(df['city'] == 'Río Cuarto')]
dfmdq = df[(df['city'] == 'Mar del Plata')]
dftrescerrito = df[(df['city'] == 'Tres Cerritos')]


# In[33]:


Total = df['user_type'].value_counts()/df['user_type'].value_counts().sum()
Total = Total.values.tolist()
A = Total[0]
B = Total[1]
C = Total[2]
D = Total[3]
data = [A, B, C, D]
labels = ['Light', 'Medium', 'Heavy','Super Heavy']
colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels = labels, colors = colors, autopct='%.1f%%', startangle = 140)
plt.title('Porcentaje de usuarios por tipo')
plt.show()


# In[34]:


Total = dfalmagro['user_type'].value_counts()/dfalmagro['user_type'].value_counts().sum()
Total = Total.values.tolist()
A = Total[0]
B = Total[1]
C = Total[2]
D = Total[3]
data = [A, B, C, D]
labels = ['Light', 'Medium', 'Heavy','Super Heavy']
colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels = labels, colors = colors, autopct='%.1f%%', startangle = 140)
plt.title('Porcentaje de usuarios en Almagro por tipo')
plt.show()


# In[35]:


Total = dfpalermo['user_type'].value_counts()/dfpalermo['user_type'].value_counts().sum()
Total = Total.values.tolist()
A = Total[0]
B = Total[1]
C = Total[2]
D = Total[3]
data = [A, B, C, D]
labels = ['Light', 'Medium', 'Heavy','Super Heavy']
colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels = labels, colors = colors, autopct='%.1f%%', startangle = 140)
plt.title('Porcentaje de usuarios en Palermo por tipo')
plt.show()


# In[36]:


Total = dfmdq['user_type'].value_counts()/dfmdq['user_type'].value_counts().sum()
Total = Total.values.tolist()
A = Total[0]
B = Total[1]
C = Total[2]
D = Total[3]
data = [A, B, C, D]
labels = ['Light', 'Medium', 'Heavy','Super Heavy']
colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels = labels, colors = colors, autopct='%.1f%%', startangle = 140)
plt.title('Porcentaje de usuarios en Mar del Plata por tipo')
plt.show()


# In[37]:


Total = dfneuquen['user_type'].value_counts()/dfneuquen['user_type'].value_counts().sum()
Total = Total.values.tolist()
A = Total[0]
B = Total[1]
C = Total[2]
D = Total[3]
data = [A, B, C, D]
labels = ['Light', 'Medium', 'Heavy','Super Heavy']
colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels = labels, colors = colors, autopct='%.1f%%', startangle = 140)
plt.title('Porcentaje de usuarios en Neuquén por tipo')
plt.show()


# In[38]:


Total = dfrosario['user_type'].value_counts()/dfrosario['user_type'].value_counts().sum()
Total = Total.values.tolist()
A = Total[0]
B = Total[1]
C = Total[2]
D = Total[3]
data = [A, B, C, D]
labels = ['Light', 'Medium', 'Heavy','Super Heavy']
colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels = labels, colors = colors, autopct='%.1f%%', startangle = 140)
plt.title('Porcentaje de usuarios en Rosario por tipo')
plt.show()


# In[39]:


Total = dflaplata['user_type'].value_counts()/dflaplata['user_type'].value_counts().sum()
Total = Total.values.tolist()
A = Total[0]
B = Total[1]
C = Total[2]
D = Total[3]
data = [A, B, C, D]
labels = ['Light', 'Medium', 'Heavy','Super Heavy']
colors = sns.color_palette('pastel')[0:5]

plt.pie(data, labels = labels, colors = colors, autopct='%.1f%%', startangle = 140)
plt.title('Porcentaje de usuarios por tipo')
plt.show()


# In[ ]:





# In[40]:


fig = sns.kdeplot(dfsh['q_order'], shade=True, color="r")
plt.show()
print(dfsh['q_order'].describe())
print(dfsh['q_order'].mode())


# In[41]:


fig = sns.kdeplot(dfm['q_order'], shade=True, color="r")
plt.show()
dfm['q_order'].describe()


# In[42]:


df.sort_values(['q_order'], ascending=False).head(20)


# In[43]:


qsh= dfsh['q_order'].count()
qh= dfh['q_order'].count()
qm=dfm['q_order'].count()
ql=dfl['q_order'].count()
print('cantidad de usuarios según el tipo SH: ', qsh, 'H: ', qh, 'M: ', qm, 'L: ', ql)


# In[44]:


ax = df['q_order'].value_counts().plot(kind = 'bar')
plt.xlim([0, 10])
ax


# pct = lambda x: 100 * x / x.sum()
# 
# 
# out = df.groupby(['city', 'user_type']).count().groupby('q_user').apply(pct)
# out

# In[45]:


df.groupby(['city', 'user_type'])['q_order'].aggregate('count').unstack()

pd.pivot_table(df, index = ['city','user_type'], aggfunc='count')
# In[ ]:


with pd.ExcelWriter('C:/Users/federico.asensio/Downloads/pilcha.xlsx') as writer:
    dfalmagro.to_excel(writer, sheet_name='almagro')
    dfmdq.to_excel(writer, sheet_name = 'mdq', index = False)
    dfpalermo.to_excel(writer, sheet_name = 'palermo')
    dfrosario.to_excel(writer, sheet_name = 'rosario')
    dfriocuarto.to_excel(writer, sheet_name = 'rio cuarto')
    dflaplata.to_excel(writer, sheet_name = 'la plata')
    dfneuquen.to_excel(writer, sheet_name = 'neuquen')
    dfgodoycruz.to_excel(writer, sheet_name = 'godoy cruz')
    dftrescerrito.to_excel(writer, sheet_name = 'tres cerritos')
    dfurquiza.to_excel(writer, sheet_name = 'villa urquiza')



    



# In[46]:


df.groupby(['city']).count()


# with pd.ExcelWriter('C:/Users/federico.asensio/Downloads/pilchacomplete.xlsx') as writer:
#     df.to_excel(writer, sheet_name='usuarios')

# In[47]:


Light = pd.DataFrame()
Light = Light.append([
                        dfalmagro[(dfalmagro.user_type.str.contains('Light'))].head(1974),dfgodoycruz[(dfgodoycruz.user_type.str.contains('Light'))].head(1267),
                        dflaplata[(dflaplata.user_type.str.contains('Light'))].head(3493),  dfmdq[(dfmdq.user_type.str.contains('Light'))].head(679),
                        dfneuquen[(dfneuquen.user_type.str.contains('Light'))].head(2377), dfpalermo[(dfpalermo.user_type.str.contains('Light'))].head(4825),
                        dfrosario[(dfrosario.user_type.str.contains('Light'))].head(4004), dfriocuarto[(dfriocuarto.user_type.str.contains('Light'))].head(1168),
                        dftrescerrito[(dftrescerrito.user_type.str.contains('Light'))].head(189), dfurquiza[(dfurquiza.user_type.str.contains('Light'))].head(1845)
                      ])
Light.city.value_counts()


# In[48]:


Medium = pd.DataFrame()
Medium = Medium.append([
                        dfalmagro[(dfalmagro.user_type.str.contains('Medium'))].head(478) ,dfgodoycruz[(dfgodoycruz.user_type.str.contains('Medium'))].head(355),
                        dflaplata[(dflaplata.user_type.str.contains('Medium'))].head(1058),  dfmdq[(dfmdq.user_type.str.contains('Medium'))].head(165),
                        dfneuquen[(dfneuquen.user_type.str.contains('Medium'))].head(845), dfpalermo[(dfpalermo.user_type.str.contains('Medium'))].head(1172),
                        dfrosario[(dfrosario.user_type.str.contains('Medium'))].head(1333), dfriocuarto[(dfriocuarto.user_type.str.contains('Medium'))].head(365),
                        dftrescerrito[(dftrescerrito.user_type.str.contains('Medium'))].head(52), dfurquiza[(dfurquiza.user_type.str.contains('Medium'))].head(528)
                      ])
Medium.city.value_counts()


# In[49]:


Heavy = pd.DataFrame()
Heavy = Heavy.append([
                        dfalmagro[(dfalmagro.user_type.str.contains('Heavy'))].head(272),dfgodoycruz[(dfgodoycruz.user_type.str.contains('Heavy'))].head(213),
                        dflaplata[(dflaplata.user_type.str.contains('Heavy'))].head(613),  dfmdq[(dfmdq.user_type.str.contains('Heavy'))].head(94),
                        dfneuquen[(dfneuquen.user_type.str.contains('Heavy'))].head(532), dfpalermo[(dfpalermo.user_type.str.contains('Heavy'))].head(661),
                        dfrosario[(dfrosario.user_type.str.contains('Heavy'))].head(808), dfriocuarto[(dfriocuarto.user_type.str.contains('Heavy'))].head(228),
                        dftrescerrito[(dftrescerrito.user_type.str.contains('Heavy'))].head(30), dfurquiza[(dfurquiza.user_type.str.contains('Heavy'))].head(324)
                      ])
Heavy.city.value_counts()


# In[50]:


Super_Heavy = pd.DataFrame()
Super_Heavy = Super_Heavy.append([
                        dfalmagro[(dfalmagro.user_type.str.contains('Super Heavy'))].head(207),dfgodoycruz[(dfgodoycruz.user_type.str.contains('Super Heavy'))].head(186),
                        dflaplata[(dflaplata.user_type.str.contains('Super Heavy'))].head(540),  dfmdq[(dfmdq.user_type.str.contains('Super Heavy'))].head(60),
                        dfneuquen[(dfneuquen.user_type.str.contains('Super Heavy'))].head(474), dfpalermo[(dfpalermo.user_type.str.contains('Super Heavy'))].head(533),
                        dfrosario[(dfrosario.user_type.str.contains('Super Heavy'))].head(633), dfriocuarto[(dfriocuarto.user_type.str.contains('Super Heavy'))].head(184),
                        dftrescerrito[(dftrescerrito.user_type.str.contains('Super Heavy'))].head(31), dfurquiza[(dfurquiza.user_type.str.contains('Super Heavy'))].head(257)
                      ])
Super_Heavy.city.value_counts()


# In[72]:


with pd.ExcelWriter('C:/Users/federico.asensio/Downloads/pilcha_usertype.xlsx') as writer:
    Light.to_excel(writer, sheet_name='Light')
    Medium.to_excel(writer, sheet_name = 'Medium', index = False)
    Heavy.to_excel(writer, sheet_name = 'Heavy')
    Super_Heavy.to_excel(writer, sheet_name = 'Super Heavy')
  


# In[55]:


x= dfalmagro[(dfalmagro.user_type.str.contains('Medium'))].head(478)
with pd.ExcelWriter('C:/Users/federico.asensio/Downloads/xee.xlsx') as writer:
    x.to_excel(writer, sheet_name='Light')


# In[51]:


no_participants = pd.DataFrame()
no_participants = no_participants.append([
                                        Light, 
                                        Medium, 
                                        Heavy, 
                                        Super_Heavy
                                        ])
no_participants.head()


# In[52]:


df1=pd.merge(df,no_participants,on=['id','id'],how="outer",indicator=True)
df1=df1[df1['_merge']=='left_only']
df1.city_x.value_counts()


# In[53]:


df1


# In[54]:


df1 = df1.drop(columns = ['q_user_y','city_y','q_order_y','user_type_y','_merge'])
df1
#dataframe con los usuarios que participan


# In[55]:


with pd.ExcelWriter('C:/Users/federico.asensio/Downloads/participantes_pilcha.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Participantes')


# In[ ]:




