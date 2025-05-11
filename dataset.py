from simple_image_download  import simple_image_download as simp 

# It is a variable which contains download functionality
response = simp.Downloader

# Enter the list which content all data attributes which you require.
keywords = ['AloeVera',' Ginseng','Echinacea','Turmeric','Lavender','Peppermint','Chamomile','St. Johns Wort','Garlic','Ginger']

# Enter the amount of data you rquire.
for kw in keywords:
    response().download(kw, 50)

#If you are using this then you have to manually seprate the data into train and test.