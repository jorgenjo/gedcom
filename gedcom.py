
# --------------------------------------------------

import tables
import io
import os
from datetime import datetime
from datetime import date
import date_lib

class IndividualClass():

  tbl = tables.TablesClass()

  tbl_person_list = tbl.tbl_person_list
  index_person_list_id = {item[0]: item for item in tbl_person_list}

  tbl_birth_list = tbl.tbl_birth_list
  index_birth_list_id = {item[0]: item for item in tbl_birth_list}

#  tbl_birth_asso_list = tbl.tbl_events_related_list
#  print(tbl_birth_asso_list)

  tbl_birth_asso_list = tbl.get_birth_asso_list()


  tbl_confirmation_list = tbl.tbl_confirmation_list
  index_confirmation_list_id = {item[0]: item for item in tbl_confirmation_list}

  def __init__(self, person_id):
    self.ID = self.get_ID(person_id)
    self.REFN = self.get_REFN(person_id)
    self.EVEN_FAMILYSEARCH = self.get_EVEN_FAMILYSEARCH(person_id)
    self.EVEN_DANISHFAMILYSEARCH = self.get_EVEN_DANISHFAMILYSEARCH(person_id)
    self.GIVN = self.get_GIVN(person_id)
    self.NICK = self.get_NICK(person_id)
    self.SURN = self.get_SURN(person_id)
    self.SEX = self.get_SEX(person_id)
    self.BIRT_DATE = date_lib.iso_to_us(self.get_BIRT_DATE(person_id))
    self.BIRT_PLAC = self.get_BIRT_PLAC(person_id)
    self.BIRT_ASSO = self.get_BIRT_ASSO(person_id)


    self.CONF_DATE = date_lib.iso_to_us(self.get_CONF_DATE(person_id))
    self.CONF_PLAC = self.get_CONF_PLAC(person_id)
    self.CONF_CHURCH = self.get_CONF_CHURCH(person_id)


  def get_ID(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][0]
    except:
      return None       

  def get_REFN(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][0]
    except:
      return None       

  def get_EVEN_FAMILYSEARCH(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][14]
    except:
      return None       

  def get_EVEN_DANISHFAMILYSEARCH(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][1]
    except:
      return None       


  def get_GIVN(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][3]
    except:
      return None       

  def get_NICK(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][4]
    except:
      return None      


  def get_SURN(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][5]
    except:
      return None       

  def get_SEX(self,v_person_id):
    try:
      v_return = self.index_person_list_id[str(v_person_id)][7]
      if ((v_return != 'M') and (v_return != 'F')):
       v_return = 'U'
      return v_return
    except:
      return None       

  def get_BIRT_DATE(self,v_person_id):
    try:
      return self.index_birth_list_id[v_person_id][1]
    except:
      return None

  def get_BIRT_PLAC(self,v_person_id):
    try:
      return self.index_birth_list_id[v_person_id][2]
    except:
      return None

  def get_BIRT_CHURCH(self,v_person_id):
    try:
      return self.index_birth_list_id[v_person_id][4]
    except:
      return None


  def get_BIRT_ASSO(self,v_person_id):

    v_return = None
 
    arr_return = []

    for row in self.tbl_birth_asso_list:
      if (row[0] == int(v_person_id)):
        arr_return.append(row)

    if (arr_return == []):
      return None
    else:
      return arr_return


  def get_CONF_DATE(self,v_person_id):
    try:
      return self.index_confirmation_list_id[v_person_id][1]
    except:
      return None

  def get_CONF_PLAC(self,v_person_id):
    try:
      return self.index_confirmation_list_id[v_person_id][2]
    except:
      return None

  def get_CONF_CHURCH(self,v_person_id):
    try:
      return self.index_confirmation_list_id[v_person_id][4]
    except:
      return None


# -----------------------------------------------------

class PersonClass():

  familyid = None

  person_id = None  
  name = None
  firstname = None
  nick = None
  lastname = None
  birthdate = None
  fatherid = None
  motherid = None

  children_array = None

  print("In person Lib Import tables")

  proband_id = 1 # Default

  tbl = tables.TablesClass()

  tbl_person_list = tbl.tbl_person_list
  index_person_list_id = {item[0]: item for item in tbl_person_list}


  tbl_family_list = tbl.tbl_family_list

  tbl_birth_list = tbl.tbl_birth_list
  index_birth_list_id = {item[0]: item for item in tbl_birth_list}

  tbl_confirmation_list = tbl.tbl_confirmation_list

  tbl_death_list = tbl.tbl_death_list

#  index_death_list_id = {item[0]: item for item in tbl_death_list}
#  print(index_death_list_id)

  def __init__(self, person_id):
    self.v_family_child_id = None
    self.person_id = person_id
    self.firstname = self.get_person_firstname(person_id)
#    self.nickname = self.get_person_nickname(person_id)
#    self.lastname = self.get_person_lastname(person_id)
    self.name = self.get_person_name(person_id)
    self.birthdate = self.get_birthdate(person_id)
    self.birthdateyear = self.get_birthdate_year()
    self.birthplace = self.get_birthplace(person_id)
    self.birthplaceid = self.get_birthplaceid(person_id)
    self.confirmationdate = self.get_confirmationdate(person_id)
    self.confirmationplace = self.get_confirmationplace(person_id)
    self.confirmationplaceid = self.get_confirmationplaceid(person_id)
    self.deathdate = self.get_deathdate(person_id)
    self.deathdateyear = self.get_deathdate_year()
    self.deathplace = self.get_deathplace(person_id)
    self.deathplaceid = self.get_deathplaceid(person_id)
    self.familyid = self.get_familyid(person_id)
    self.fatherid = self.get_fatherid()
    self.motherid = self.get_motherid()

#    self.family_parrents_array = self.get_family_parrents_array()
#    self.children_array = self.get_children_array()


  # ------------------------------------------

  def set_proband(self,v_proband_id):
    self.proband_id = v_proband_id

  # ------------------------------------------

  def get_proband(self):
    return self.proband_id

  # ------------------------------------------

  def get_person_firstname(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][3]
    except:
      return "ERROR: Unknown firstname PersonId"       

  # --------------------------------------------

  def get_person_nickname(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][4]
    except:
      return "ERROR: Unknown nickname PersonId"       

  # --------------------------------------------

  def get_person_lastname(self,v_person_id):
    try:
      return self.index_person_list_id[str(v_person_id)][5]
    except:
      return "ERROR: Unknown lastname PersonId"       

  # --------------------------------------------

  def get_person_name(self,v_person_id):

    try:
      row = self.index_person_list_id[str(v_person_id)]

      v_firstname = row[3] 
      v_nickname = row[4] 
      v_lastname = row[5] 

      if (v_nickname != ''):
        return v_firstname + " '" + v_nickname + "' " + v_lastname
      else:
        return v_firstname + " " + v_lastname
    except:  
      return "ERROR: Unknown name PersonId"       

  # --------------------------------------------

  def get_birthdate(self,v_person_id):
    try:
      return self.index_birth_list_id[v_person_id][1]
    except:
      return None


  # --------------------------------------------

  def get_birthplace(self,v_person_id):
    try:
      return self.index_birth_list_id[v_person_id][2].split(',')[0]
    except:
      return None
  # --------------------------------------------

  def get_birthplaceid(self,v_person_id):
    try:
      return self.index_birth_list_id[v_person_id][3]
    except:
      return None

  # --------------------------------------------

  def get_deathdate(self,v_person_id):
#    try:
#      return str(self.index_death_list_id[str(v_person_id)][1])
#    except:
#      return "ERROR: Unknown date"       

    v_return = None
    for row in self.tbl_death_list:
      if (row[0] == str(v_person_id)):
        v_return = row[1]
        break
    return v_return

  # --------------------------------------------

  def get_deathplace(self,v_person_id):
    v_return = None
    for row in self.tbl_death_list:
      if (row[0] == str(v_person_id)):
        v_return = row[2].split(',')[0]
        break
    return v_return

  # --------------------------------------------

  def get_deathplaceid(self,v_person_id):
    v_return = None
    for row in self.tbl_death_list:
      if (row[0] == str(v_person_id)):
        v_return = row[3]
        break
    return v_return

  # --------------------------------------------

  def get_confirmationdate(self,v_person_id):
    v_return = None
    for row in self.tbl_confirmation_list:
      if (row[0] == str(v_person_id)):
        v_return = str(row[1])
        break
    return v_return

  # --------------------------------------------

  def get_confirmationplace(self,v_person_id):
    v_return = None
    for row in self.tbl_confirmation_list:
      if (row[0] == str(v_person_id)):
        v_return = row[2].split(',')[0]
        break
    return v_return

  # --------------------------------------------

  def get_confirmationplaceid(self,v_person_id):
    v_return = None
    for row in self.tbl_confirmation_list:
      if (row[0] == str(v_person_id)):
        v_return = row[3]
        break
    return v_return

  # --------------------------------------------

  def get_birthdate_year(self):
    if (self.birthdate != None):
      return self.birthdate[0:4]
    else:
      return None

  # --------------------------------------------

  def get_deathdate_year(self):
    if (self.deathdate != None):
      return self.deathdate[0:4]
    else:
      return None
 

  # --------------------------------------------
 
  def get_familyid(self, v_person_id = None):

       # Todo Hurtig Opslag

      if (self.familyid == None): 
        v_return = None

        for row in self.tbl_family_list:
          try: 
            # Check if int value in child row
            v_child_id = int(row[4])
            v_family_id = int(row[1])
            
            if(int(v_person_id) == v_child_id):
              self.familyid = row[1]
              v_return = row[1] 
              break
          except:
            pass

      else:
         # Family child id already found
         v_return = self.familyid

      return v_return
 
  # --------------------------------------------
 
  def get_fatherid(self):

    if (self.fatherid == None): 
      for row in self.tbl_family_list:
        if( row[1] == self.familyid):
         if( row[3] == 'None'):
          if( row[4] == 'None'):
#           print("Row Father = ",row)
           try:
             self.fatherid = int(row[2])
           except:
             self.fatherid = None
           break
    return self.fatherid

  # --------------------------------------------
 

  def get_motherid(self):

    if (self.motherid == None): 
      for row in self.tbl_family_list:
        if( row[1] == self.familyid):
         if( row[2] == 'None'):
          if( row[4] == 'None'):
           try:
             self.motherid = int(row[3])
           except:
             self.motherid = None
           break
    return self.motherid


  # --------------------------------------------


  def get_family_parrents_array(self):
        # Todo Hurtig Opslag
 
#       if (self.v_family_parrents_array == None): 
#        print("Person1 Id = ",self.person_id)
        self.v_family_parrents_array = []
        for row in self.tbl_family_list:
          try: 
            # Check if int value in child row
            v_father_id = int(row[2])
            v_family_id = int(row[1])
            if (int(self.person_id == v_father_id)) :
#              print("Far til barn i familie = ",v_family_id)
              self.v_family_parrents_array.append(v_family_id)
          except:
            pass

          try: 
            # Check if int value in child row
            v_mother_id = int(row[3])
            v_family_id = int(row[1])
            if (int(self.person_id == v_mother_id)) :
#              print("Mor til barn i familie = ",v_family_id)
              self.v_family_parrents_array.append(v_family_id)
          except:
            pass

        return self.v_family_parrents_array


  def get_children_array(self):
     if (self.children_array == None):
      self.children_array = []
     
      for family in self.family_parrents_array:
  
       for row in self.tbl_family_list:
        try: 
          # Check if int value in father_id
          v_family_id = int(row[1])
          v_child_id = int(row[4])
          if (family == v_family_id):
            self.children_array.append(v_child_id)
        except:
          pass
     else:
       pass
     return self.children_array
 
# -----------------------------------------------------------------------------
# Gedcom Header
# ------------------------------------------------------------------------------

def header():

  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")

  today = date.today()
  dag = today.strftime("%#d %b %Y")

  f  = "0 HEAD\n"
  f += "1 SOUR aner.jcon.dk\n"
  f += "2 NAME JohannessenTree\n"
  f += "2 CORP jcon.dk and Jørgen Johannessen\n"
  f += "2 VERS 1.0\n"
  f += "1 DATE " + str(dag) + "\n"
  f += "2 TIME " + str(current_time) + "\n"
  f += "1 GEDC\n"
  f += "2 VERS 7.0.13\n"
  f += "1 SUBM @SUBM@\n"
  f += "0 @SUBM@ SUBM\n"
  f += "1 NAME Jørgen Schlüter/Johannessen/\n" 
  return f

# -----------------------------------------------------------------------------
# Gedcom Family_Record
# ------------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Gedcom Individual Record
# ------------------------------------------------------------------------------

def individual_record(v_person_id):

 gedcom = IndividualClass(v_person_id)

 if ((gedcom.ID != None)):
   file =  "0 @I" + gedcom.ID + "@ INDI\n"
   file += "1 NAME "
   if (gedcom.GIVN != None):
     file += gedcom.GIVN + "/"
   if (gedcom.SURN != None):
     file += gedcom.SURN + "/"
   file += "\n"

   if (gedcom.GIVN != None):
     file += "2 GIVN " + gedcom.GIVN + "\n"
   if (gedcom.SURN != None):
     file += "2 SURN " + gedcom.SURN + "\n"
   if (gedcom.SEX != None):
     file += "1 SEX " + gedcom.SEX + "\n"


   # JCON Reference No Person Id
   if (gedcom.REFN != None):
     file += "1 REFN " + gedcom.REFN + "\n"

   # Family Search ID as Event
   if (gedcom.EVEN_FAMILYSEARCH != None):
     file += "1 EVEN " + gedcom.EVEN_FAMILYSEARCH + "\n"
     file += "2 TYPE FamilySearch ID\n"
     file += "2 NOTE TYPE https://www.familysearch.org/tree/person/details/" + gedcom.EVEN_FAMILYSEARCH + "\n"

   # Danish Family Search ID as Event
   if (gedcom.EVEN_DANISHFAMILYSEARCH != None):
    if (gedcom.EVEN_DANISHFAMILYSEARCH != "0"):
     file += "1 EVEN " + gedcom.EVEN_DANISHFAMILYSEARCH + "\n"
     file += "2 TYPE DanishFamilySearch ID\n"
     file += "2 NOTE TYPE https://www.danishfamilysearch.com/danskerbasen/person" + gedcom.EVEN_DANISHFAMILYSEARCH + "\n"


   if (gedcom.BIRT_DATE != None):
     file += "1 BIRT\n"
     file += "2 DATE " + gedcom.BIRT_DATE + "\n"

     if (gedcom.BIRT_PLAC != None):
       file += "2 PLAC " + gedcom.BIRT_PLAC + "\n"
       file += "3 FORM Place, Parish, Commune, Country\n"

     if (gedcom.BIRT_ASSO != None):

       for row in gedcom.BIRT_ASSO:
         if (str(row[1]) != "0"):
           file += "2 ASSO @I" + str(row[1]) + "@\n"
           file += "3 ROLE " + row[2] + "\n"
           file += "4 PHRASE " + row[3] + "\n"
         else:
           file += "2 ASSO @VOID@\n"   # Unknow ID
           file += "3 PHRASE "
           if (row[4] != None):
            if (row[4] != ""):
             file += row[4]
           if (row[5] != None):
            if (row[5] != ""):
             file += " '" + row[5] + "'" 
           if (row[6] != None):
            if (row[6] != ""):
             file += " " + row[6]
           file += "\n"   
           file += "3 ROLE " + row[2] + "\n"
           file += "4 PHRASE " + row[3] + "\n"


#       file += "2 ASSO " + gedcom.BIRT_PLAC + "\n"
#       file += "3 FORM Place, Parish, Commune, Country\n"



   # Source Birth 

   if (gedcom.BIRT_DATE != None):
     pass
#     file +=  "0 @CHURCHBOOK_BIRT_" + str(gedcom.ID) + "@ SOUR" + "\n"
#     file += "1 DATA" + "\n"
#     file += "2 EVEN BIRT" + "\n" 
#     file += "3 DATE FROM " + gedcom.BIRT_DATE + " TO " + gedcom.BIRT_DATE + "\n"
#     file += "3 PLAC " + gedcom.BIRT_CHURCH + "\n"
#     file += "4 FORM Church, Parish, Commune, Country" + "\n"

   # Confirmation
 
   if (gedcom.CONF_DATE != None):
     file += "1 CONF\n"
     file += "2 DATE " + gedcom.CONF_DATE + "\n"
     file += "2 SOUR @CHURCHBOOK_CONF_" + str(gedcom.ID) + "@" + "\n"

     if (gedcom.CONF_PLAC != None):
      if (gedcom.CONF_PLAC != ""):
       file += "2 PLAC " + gedcom.CONF_PLAC + "\n"
       file += "3 FORM Place, Parish, Commune, Country\n"


   # Source Confirmation  

   if (gedcom.CONF_DATE != None):
     file +=  "0 @CHURCHBOOK_CONF_" + str(gedcom.ID) + "@ SOUR" + "\n"
     file += "1 DATA" + "\n"
     file += "2 EVEN CONF" + "\n" 
     file += "3 DATE FROM " + gedcom.CONF_DATE + " TO " + gedcom.CONF_DATE + "\n"
     file += "3 PLAC " + gedcom.CONF_CHURCH + "\n"
     file += "4 FORM Church, Parish, Commune, Country" + "\n"

   # Source Marriage 

   # Source Death 


 else:
   file = ""

 return file



# -----------------------------------------------------------------------------
# Gedcom Multimedia Record
# ------------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Gedcom Repository Record
# ------------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Gedcom Note Record
# ------------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Gedcom Source Record
# ------------------------------------------------------------------------------

def source_record():
   file =  "0 @CONF_1@ SOUR" + "\n"
   file += "1 DATA" + "\n"
   file += "2 EVEN CONF" + "\n"
   file += "3 DATE FROM 18 May 1980 TO 18 May 1980" + "\n"
   file += "3 PLAC Sædding Kirke, Sædden, Esbjerg, Danmark" + "\n"
   file += "4 FORM Church, Parish, Commune, Country" + "\n"
   return file
     

# -----------------------------------------------------------------------------
# Gedcom Submitter Record
# ------------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Gedcom Tail
# ------------------------------------------------------------------------------


def tail():
  f = "0 TRLR"
  return f


# ---- MAIN ------

filename = "jj_test.ged"
try:
  os.remove(filename)
except:
  pass


# Note utf-8-sig ellers kommer æøå ikke rigtig ind i legacy
with io.open(filename,'w',encoding='utf-8-sig') as f:
 f.write(header())

 tbl = tables.TablesClass()
 for row in tbl.tbl_person_list:
   f.write(individual_record(int(row[0])))

# f.write(source_record())


 f.write(tail())

individual = IndividualClass(142)
if ( individual.BIRT_ASSO != None):
  print("DATA")
  print(individual.BIRT_ASSO)









