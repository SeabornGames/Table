===  ======  ===========  ======================  ==========
TU   Player  Role         Action                  Target    
===  ======  ===========  ======================  ==========
1    Ann     Executioner  None                    None      
1    Ben     Judge        "True"                  Inspector 
1    Cal     Inspector    True                    Ann       
1    Dan     Thief        "False"                 Ann       
1    Ed      Reporter     False                   Cal       
1    Fin     Trader       Class                   "Cal, Ed" 
2    Ed      Inspector    Class                   Dan       
2    Cal     Reporter     Class                   Dan       
2    Dan     Executioner  Class                   Ed        
2    Ann     Thief        Class                   Dan       
2    Fin     Trader       Steal                   Dan       
2    Ben     Judge        ฉันต้องคิดถึงเธอแบบไหน  Inspector 
+NA  Cal     Reporter     Claim                   Inspector 
3    Dan     Trader       =+NA                    "Ben, Cal"
4    Ben     Inspector    Class                   Dan       
4    Fin     Executioner  Class                   Dan       
4    Cal     Judge        Class                   Trader    
===  ======  ===========  ======================  ==========