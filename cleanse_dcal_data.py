import pandas as pd

dcal = pd.read_csv("dcal_data.csv")
dcal["Airline_Name"] = dcal["url"].str.split('/').apply(lambda x: x[4])
dcal.rename(columns={"Text Header":"Review_Title", "User Status":"User_Nb_Reviews", "User Status_link":"Review_Link", "Text Sub":"User_Name", "Text Subtitle":"User_Country", "Text Sub Time":"Review_Date", "Text Content Block":"Review_Text", "Text Content Link":"Trip_Verified", "Text Content Link_link":"Content_Link", "Review":"Review_Data"}, inplace=True)
dcal["Review_Text_Clean"] = dcal["Review_Text"].str.split("|").apply(lambda x: x[1] if len(x)>1 else x[0])
dcal_clean = dcal.drop(['Review_Link', 'Content_Link', 'Thumbnail Image', 'Thumbnail Image_alt', 'Thumbnail Image_link', 'Large Review', 'Large Review_alt'], axis=1)
dcal_clean["User_Country"]=dcal_clean["User_Country"].str.slice(1,-1)


dcal_clean["Type_Of_Traveller"] = dcal_clean["Review_Data"].str.split(";").apply(lambda x: list(filter(lambda z: "Type Of Traveller" in z, x))[0].split("\n")[1] if len(list(filter(lambda y: "Type Of Traveller" in y, x)))>0 else "")
dcal_clean["Cabin_Flown"] = dcal_clean["Review_Data"].str.split(";").apply(lambda x: list(filter(lambda z: "Cabin Flown" in z, x))[0].split("\n")[1] if len(list(filter(lambda y: "Cabin Flown" in y, x)))>0 else "")
dcal_clean["Aircraft"] = dcal_clean["Review_Data"].str.split(";").apply(lambda x: list(filter(lambda z: "Aircraft" in z, x))[0].split("\n")[1] if len(list(filter(lambda y: "Aircraft" in y, x)))>0 else "")
dcal_clean["Date Flown"] = dcal_clean["Review_Data"].str.split(";").apply(lambda x: list(filter(lambda z: "Date Flown" in z, x))[0].split("\n")[1] if len(list(filter(lambda y: "Date Flown" in y, x)))>0 else "")
dcal_clean["Recommended"] = dcal_clean["Review_Data"].str.split(";").apply(lambda x: list(filter(lambda z: "Recommended" in z, x))[0].split("\n")[1] if len(list(filter(lambda y: "Recommended" in y, x)))>0 else "")
dcal_clean = dcal_clean.drop(["Review_Text", "Review_Data"], axis=1)
dcal_clean.to_csv("cleansed_dcal_data.csv")
