'''
Created on Aug 7, 2017

@author: thelunararmy
'''

skills = [  
         "Acrobatics",
         "Animal Handling",
         "Arcana",
         "Athletics",
         "Deception",
         "History",
         "Insight",
         "Intimidation",
         "Investigation",
         "Medicine",
         "Nature",
         "Perception",
         "Performance",
         "Persuasion",
         "Religion",
         "Sleight of Hand",
         "Stealth",
         "Survival"
         ]

saving = [
         "Strength Save",
         "Dexterity Save",
         "Constitution Save",
         "Intelligence Save",
         "Wisdom Save",
         "Charisma Save"
         ]

atrib = [
         "Strength",
         "Dexterity",
         "Constitution",
         "Intelligence",
         "Wisdom",
         "Charisma"
        ]


bar = "&#124;" # |
com = "&#44;"  # ,
cbk = "&#125;" # }
osb = "[["
csb = "]]"
pls = "+"
ata = "@{"

def GenerateMacro (attrbs,meta,apex):
    final_buf = "/me rolls ?{Roll Type|"
    for idx,(label,fluff,dice) in enumerate([("Standard","a standard","1d20"),("Advantage","an advantaged","2d20kh1"),("Disadvantage","a disadvantaged","2d20kl1")]):
        skill_buf = fluff + " "+ meta + com +" resulting in a " + "?{" + meta.split(" ")[0].title()
        for att in attrbs:
            bn = att.lower().replace(" ","_")+apex
            skill_buf = skill_buf + bar + att + com + osb + dice + pls + osb + ata + bn + "}" + csb + csb + " for " + att
        skill_buf = skill_buf + cbk
        final_buf = final_buf + "|" if idx != 0 else final_buf
        final_buf = final_buf + label + "," + skill_buf 
    final_buf = final_buf + "}"
    print final_buf


if __name__ == '__main__':
    # ''Simply'' generate our macro :)    
#     GenerateMacro(skills,"skill check","_bonus")
#     GenerateMacro(saving,"saving throw","_bonus")
    GenerateMacro(atrib,"attribute check","_mod")
