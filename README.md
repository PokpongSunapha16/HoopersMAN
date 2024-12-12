```mermaid
graph LR
  Start --> A["A<br>ES: 0<br>EF: 7<br>Slack: 2"]
  Start --> B["B<br>ES: 0<br>EF: 9<br>Slack: 0"]
  A --> C["C<br>ES: 7<br>EF: 19<br>Slack: 7"]
  B --> D["D<br>ES: 9<br>EF: 17<br>Slack: 0"]
  D --> E["E<br>ES: 17<br>EF: 26<br>Slack: 0"]
  C --> F["F<br>ES: 26<br>EF: 32<br>Slack: 0"]
  E --> G["G<br>ES: 26<br>EF: 31<br>Slack: 1"]
  F --> Finish
  G --> Finish

** นาย ปกป้อง สู่นภา 65114540345 **
