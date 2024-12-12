```mermaid
graph LR
  Start --> A["Register<br>ES: 0<br>EF: 5<br>Slack: 0"]
  A --> B["Login<br>ES: 5<br>EF: 10<br>Slack: 0"]
  
  B --> C["Create Products<br>ES: 10<br>EF: 15<br>Slack: 0"]
  C --> D["Edit Products Information<br>ES: 15<br>EF: 20<br>Slack: 0"]
  C --> E["Delete Product<br>ES: 20<br>EF: 25<br>Slack: 0"]
  C --> F["Search Product By Name<br>ES: 20<br>EF: 25<br>Slack: 0"]
  D --> G["Edit Profile<br>ES: 25<br>EF: 30<br>Slack: 0"]
  
  E --> Finish
  F --> Finish
  G --> Finish

