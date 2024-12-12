```mermaid
graph TD
    Start[Start] --> A[Activity A<br>ออกแบบหน้าจอสมัครสมาชิก<br>ES: 0, EF: 2, Slack: 0]
    Start --> B[Activity B<br>ออกแบบหน้าจอเข้าสู่ระบบ<br>ES: 0, EF: 2, Slack: 0]
    A --> C[Activity C<br>พัฒนา API และฐานข้อมูลสมาชิก<br>ES: 2, EF: 5, Slack: 0]
    B --> C
    C --> D[Activity D<br>พัฒนา API และฐานข้อมูลสินค้า<br>ES: 5, EF: 9, Slack: 0]
    D --> E[Activity E<br>พัฒนา UI/UX สำหรับจัดการสินค้า<br>ES: 9, EF: 12, Slack: 0]
    D --> G[Activity G<br>ทดสอบระบบจัดการสินค้า<br>ES: 12, EF: 14, Slack: 0]
    E --> G
    A --> F[Activity F<br>ทดสอบระบบสมัครสมาชิกและเข้าสู่ระบบ<br>ES: 2, EF: 3, Slack: 9]
    B --> F
    G --> Finish[Finish]
    F --> Finish

