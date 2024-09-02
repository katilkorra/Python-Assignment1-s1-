#Find birthdays in a month using dictionary.

month = (input("Enter your Date of Birth in syntex = date/month/year:  "))
date = {"23/01/2002":["kush", "Sita"] ,
        "01/02/2012":["mohan", "tanu", "Sivansh"], 
        "12/03/2003":"nandan", 
        "23/04/2005":"puja",
        "03/05/2001":"bhola", 
        "13/06/1998":"suja",
        "07/07/1998":"dhoni" , 
        "03/08/2009":["geeta" ,"Babita"],
        "04/09/2000" :"amar" , 
        "01/10/2001":"anjali",
        "23/11/1998":"tanvi",
        "02/12/12":"Sanvi"}

if len(month)==10:
  for mDate,name in date.items():
    if month[3:5] == mDate[3:5]:
      print(name) 

    