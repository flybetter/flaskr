drop TABLE if EXISTS entries;
create table entries(
  id INTEGER PRIMARY key autoincrement,
  title string not NULL ,
  text string not NULL 
)