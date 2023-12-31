# judgment-scrapy


#### 流程：
1. 使用Scrapy框架開發。 
2. 在送出request時夾帶隱藏參數，讓程式自動進入搜索結果頁面。
3. 依案件內容篩選符合申貸人的司法案件，並比對父母姓名、地址等資訊，將資料整理成結構化資料儲存至資料庫。
4. 用Airflow搭建定時自動執行爬蟲的排程，每十分鐘會到資料庫撈取新案件內容，並執行爬蟲。
5. 以Django開發網頁，提供徵審部門查詢，這項服務節省徵審部人工查詢與比對的作業時間，提升20%審件速度。
﻿

#### 工具：Airflow, Django, Scrapy, MySQL

#### 結果示意圖
![image](https://github.com/Stayinmymagic/judgment-scrapy/blob/master/result-example.png)

