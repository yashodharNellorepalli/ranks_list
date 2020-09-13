Schema

create table `userss`(
  `id` int auto_increment,
  `score` int default 0,
  `rank` int default NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

create table `score_users_list`(
  `score` int default 0,
  `users_list` text default NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  unique key (`score`),
  PRIMARY KEY (`score`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

run the server -> python3 run.py

api:
curl --location --request GET 'http://localhost:8081/ranks/get-rank?user_id=1'
curl --location --request GET 'http://localhost:8081/ranks/ranks-list?n=10'
curl --location --request POST 'http://localhost:8081/ranks/update-score' \
--header 'Content-Type: application/json' \
--data-raw '{
    "user_id": 2,
    "score": 3
}'