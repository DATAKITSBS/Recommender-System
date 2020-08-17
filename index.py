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