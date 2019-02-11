DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS seat;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  user_type TEXT NOT NULL, 
  ad_id TEXT NULL,
  email TEXT NOT NULL,
  rnk TEXT NOT NULL,
  phone_no TEXT NULL  
);

INSERT INTO user ( username, password, email, user_type, ad_id, rnk, phone_no)
values( '김석현',
'pbkdf2:sha256:50000$m2fOCp7N$6303fd2de9879670bd4318f3355ccd5677f6611519e8fb6b50ababff40641f71',
'sukhyun.kim@doosan.com', '2','','과장','0721' );

INSERT INTO user ( username, password, email, user_type, ad_id, rnk, phone_no)
values( '박두산',
'pbkdf2:sha256:50000$m2fOCp7N$6303fd2de9879670bd4318f3355ccd5677f6611519e8fb6b50ababff40641f71',
'doosan.park@doosan.com', '2','','과장','0721' );


CREATE TABLE seat ( 
  seat_no TEXT PRIMARY KEY,
  floor TEXT NOT NULL,
  occu_id INTEGER NULL,
  occu_date TEXT NULL DEFAULT CURRENT_DATE,
  occu_time TEXT NULL DEFAULT CURRENT_TIME,
  xpos INT NOT NULL,
  ypos INT NOT NULL
);

INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('1', '6', '', 396, 93);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('2', '6', '', 396, 181);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('3', '6', '', 396, 261);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('4', '6', '', 396, 344);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('5', '6', '', 467, 68);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('6', '6', '', 507, 68);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('7', '6', '', 467, 114);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('8', '6', '', 507, 114);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('9', '6', '', 587, 63);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('10', '6', '', 632, 63);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('11', '6', '', 587, 106);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('12', '6', '', 632, 106);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('13', '6', '', 722, 67);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('14', '6', '', 722, 115);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('15', '6', '', 766, 67);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('16', '6', '', 766, 115);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('17', '6', '', 848, 80);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('18', '6', '', 848, 117);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('19', '6', '', 878, 80);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('20', '6', '', 878, 117);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('21', '6', '', 627, 181);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('22', '6', '', 627, 220);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('23', '6', '', 668, 181);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('24', '6', '', 668, 220);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('25', '6', '', 598, 293);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('26', '6', '', 598, 344);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('27', '6', '', 643, 293);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('28', '6', '', 643, 344);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('29', '6', '', 679, 444);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('30', '6', '', 679, 500);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('31', '6', '', 726, 444);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('32', '6', '', 726, 500);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('33', '6', '', 767, 174);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('34', '6', '', 767, 224);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('35', '6', '', 816, 174);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('36', '6', '', 816, 224);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('37', '6', '', 857, 174);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('38', '6', '', 857, 224);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('39', '6', '', 729, 296);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('40', '6', '', 729, 343);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('41', '6', '', 771, 296);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('42', '6', '', 771, 343);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('43', '6', '', 841, 444);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('44', '6', '', 841, 500);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('45', '6', '', 884, 444);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('46', '6', '', 884, 500);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('47', '6', '', 1011, 530);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('48', '6', '', 1011, 624);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('49', '6', '', 1011, 676);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('50', '6', '', 1011, 720);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('51', '6', '', 1011, 761);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('52', '6', '', 1052, 530);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('53', '6', '', 1052, 576);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('54', '6', '', 1052, 624);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('55', '6', '', 1052, 676);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('56', '6', '', 1052, 720);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('57', '6', '', 1052, 761);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('58', '6', '', 1099, 530);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('59', '6', '', 1099, 576);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('60', '6', '', 1099, 624);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('61', '6', '', 1099, 676);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('62', '6', '', 1099, 720);
INSERT INTO seat ( seat_no, floor, occu_id, xpos, ypos) VALUES ('63', '6', '', 1099, 761);


CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);