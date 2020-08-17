import pandas as pd
 model_df = pd.read_json('data/mag_papers_0/mag_subset20K.txt', lines=True)
 model_df.shape
(20000, 19)
 model_df.columns
Index(['abstract', 'authors', 'doc_type', 'doi', 'fos', 'id', 'issue',
 'keywords', 'lang', 'n_citation', 'page_end', 'page_start', 'publisher',
 'references', 'title', 'url', 'venue', 'volume', 'year'],
dtype='object')
# filter out non-English articles and focus on a few variables
model_df = model_df[model_df.lang == 'en']
drop_duplicates(subset='title', keep='first')
drop(['doc_type', 'doi', 'id', 'issue', 'lang', 'n_citation',
 'page_end', 'page_start', 'publisher', 'references', 'url', 'venue', 'volume'],
 axis=1)
 model_df.shape


 #Collaborative filtering stage 1: Build item feature matrix
 unique_fos = sorted(list({feature
 for paper_row in model_df.fos.fillna('0')
 for feature in paper_row }))
 unique_year = sorted(model_df['year'].astype('str').unique())
 def feature_array(x, var, unique_array):
      row_dict = {}
 for i in x.index:
     var_dict = {}
 for j in range(len(unique_array)):
    if type(x[i]) is list:
        if unique_array[j] in x[i]:
           var_dict.update({var + '_' + unique_array[j]: 1})
             else:
              var_dict.update({var + '_' + unique_array[j]: 0})
             else:
           if unique_array[j] == str(x[i]):
                var_dict.update({var + '_' + unique_array[j]: 1})
                     else:
                         var_dict.update({var + '_' + unique_array[j]: 0})
                 row_dict.update({i : var_dict})
 feature_df = pd.DataFrame.from_dict(row_dict, dtype='str').T
 return feature_df
# Back to the Feature: Building an Academic Paper Recommender
 year_features = feature_array(model_df['year'], unique_year)
 fos_features = feature_array(model_df['fos'], unique_fos)
 first_features = fos_features.join(year_features).T
 from sys import getsizeof
 print('Size of first feature array: ', getsizeof(first_features))