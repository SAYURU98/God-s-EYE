import pandas as pd
import features as fe

data_limit = 10

#loading the phishing URLs data to dataframe
urls = pd.read_csv("datasets/online-valid.csv")
phishurl = urls.sample(n = data_limit, random_state = 12).copy()
phishurl = phishurl.reset_index(drop=True)
phish_features = []
label = 1
for i in range(0, data_limit):
  url = phishurl['url'][i]
  phish_features.append(fe.featureExtraction(url,label))
  

#Loading legitimate files 
urls = pd.read_csv("datasets/benign_list_big_final.csv")
legiurl = urls.sample(n = data_limit, random_state = 12).copy()
legiurl = legiurl.reset_index(drop=True)
legi_features = []
label = 0
for i in range(0, data_limit):
  url = legiurl['url'][i]
  legi_features.append(fe.featureExtraction(url,label))
  

  
feature_names = ['Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth','Redirection', 
                      'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record',
                      'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over','Right_Click', 'Web_Forwards', 'Label']

legitimate = pd.DataFrame(legi_features, columns= feature_names)
phishing = pd.DataFrame(phish_features, columns= feature_names)

urldata = pd.concat([legitimate, phishing]).reset_index(drop=True)
urldata.to_csv('datasets/urldata.csv', index=False)


# /find a way to speedup this