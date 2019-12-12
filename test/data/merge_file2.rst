===  ======  ===========  ======================  ==========
TU2  Player  Role         Action2                  Target2
===  ======  ===========  ======================  ==========
1    Ann     Executioner  None                    None
1    Cal     Inspector    True                    Ann
1    Dan     Thief        "False"                 Ann
1    Ed      Reporter     False                   Cal
1    Fin     Trader       Class                   "Cal, Ed"
2    Ed      Inspector    Class                   Dan
2    Cal     Reporter     Class                   Dan
2    Dan     Executioner  Class                   Ed
2    Ann     Thief        Class                   Dan
2    Fin     Trader       "3"                     Dan
+NA  Cal     Reporter     Claim                   Inspector
3    Dan     Trader       =+NA                    "Ben, Cal"
4    Ben     Inspector    Class                   Dan
4    Fin     Executioner  Class                   Dan
4    Cal     Judge        Class                   Trader
===  ======  ===========  ======================  ==========