| TU  | Player | Role        | Action                 | Target    | Player1 | Role1       | Action1 | Target1   | TU2 | Action2 | Target2   |
| :---| :------| :-----------| :----------------------| :---------| :-------| :-----------| :-------| :---------| :---| :-------| :-------- |
| 1   | Ann    | Executioner | None                   | None      | Ann     | Executioner | None    | None      | 1   | None    | None      |
| 1   | Ben    | Judge       | "True"                 | Inspector | Ann     | Executioner | None    | None      |     |         |           |
| 1   | Cal    | Inspector   | True                   | Ann       | Ann     | Executioner | None    | None      | 1   | True    | Ann       |
| 1   | Dan    | Thief       | "False"                | Ann       | Ann     | Executioner | None    | None      | 1   | "False" | Ann       |
| 1   | Ed     | Reporter    | False                  | Cal       | Ann     | Executioner | None    | None      | 1   | False   | Cal       |
| 1   | Fin    | Trader      | Class                  | Cal, Ed   | Ann     | Executioner | None    | None      | 1   | Class   | Cal, Ed   |
| 2   | Ed     | Inspector   | Class                  | Dan       | Ed      | Inspector   | Class   | Dan       | 2   | Class   | Dan       |
| 2   | Cal    | Reporter    | Class                  | Dan       | Ed      | Inspector   | Class   | Dan       | 2   | Class   | Dan       |
| 2   | Dan    | Executioner | Class                  | Ed        | Ed      | Inspector   | Class   | Dan       | 2   | Class   | Ed        |
| 2   | Ann    | Thief       | Class                  | Dan       | Ed      | Inspector   | Class   | Dan       | 2   | Class   | Dan       |
| 2   | Fin    | Trader      | "3"                    | Dan       | Ed      | Inspector   | Class   | Dan       | 1   | Class   | Cal, Ed   |
| 2   | Ben    | Judge       | ฉันต้องคิดถึงเธอแบบไหน | Inspector | Ed      | Inspector   | Class   | Dan       |     |         |           |
| +NA | Cal    | Reporter    | Claim                  | Inspector | Cal     | Reporter    | Claim   | Inspector | 2   | Class   | Dan       |
| 3   | Dan    | Trader      | =+NA                   | Ben, Cal  | Dan     | Trader      | =+NA    | Ben, Cal  | 3   | =+NA    | Ben, Cal  |
| 4   | Ben    | Inspector   | Class                  | Dan       | Ben     | Inspector   | Class   | Dan       | 4   | Class   | Dan       |
| 4   | Fin    | Executioner | Class                  | Dan       | Ben     | Inspector   | Class   | Dan       | 4   | Class   | Dan       |
| 4   | Cal    | Judge       | Class                  | Trader    | Ben     | Inspector   | Class   | Dan       | 4   | Class   | Trader    |