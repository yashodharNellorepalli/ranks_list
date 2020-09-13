from ..utils.query import get_mysql_results, insert_mysql_rows


def get_rank(mysql_conn, user_id):
    query = f""" select * from userss where id={user_id}"""
    data = get_mysql_results(mysql_conn, query)

    if len(data) != 1:
        return False, None

    return True, data[0].get('rank')


def get_ranks_list(mysql_conn, n):
    query = f"""select * from score_users_list order by score desc"""
    data = get_mysql_results(mysql_conn, query)
    print(data)
    response_data = []
    rank = 1

    for row in data:
        users_list = row.get('users_list')
        if len(users_list) == 0:
            continue
        else:
            response_data.append({
                'rank': rank,
                'score': row.get('score'),
                'users_list': users_list
            })
            rank += 1

        if n == 0:
            break

    return response_data


def update_new_score(mysql_conn, user_id, new_score):
    query = f""" select * from userss where id={user_id}"""
    user_info = get_mysql_results(mysql_conn, query)
    user_info = user_info[0]
    old_score = user_info.get('score')
    # remove user_id from oldScore
    remove_user_id_from_list(mysql_conn, user_id, old_score)
    # add user_id for newScore
    add_user_id_for_new_score(mysql_conn, user_id, new_score)
    # update Rank of user
    new_rank = get_new_rank_by_score(mysql_conn, new_score)
    update_user_info(mysql_conn, user_id, new_score, new_rank)

    return new_rank


def update_user_info(mysql_conn, user_id, score, rank):
    query=f"""update userss set score={score}, rank={rank} where id={user_id}"""
    insert_mysql_rows(mysql_conn, query)


def remove_user_id_from_list(mysql_conn, user_id, old_score):
    print('remove_user_id_from_list', user_id, old_score)
    query = f"""select * from score_users_list where score={old_score}"""
    old_score_info = get_mysql_results(mysql_conn, query)
    users_list = old_score_info[0].get('users_list', '').strip()
    users_list = set(users_list.split(','))
    users_list.remove(str(user_id))
    users_list = ','.join(map(str, users_list))
    query = "update score_users_list set users_list=\"" + users_list + f"\" where score={old_score}"
    insert_mysql_rows(mysql_conn, query)


def add_user_id_for_new_score(mysql_conn, user_id, new_score):
    user_id = str(user_id)
    query = f"""select * from score_users_list where score={new_score}"""
    new_score_info = get_mysql_results(mysql_conn, query)

    if len(new_score_info) == 0:
        query = f"""insert into `score_users_list` (`score`, `users_list`) values({new_score}, {user_id})"""
    else:
        users_list = new_score_info[0].get('users_list', '').strip()
        if users_list == '':
            users_list = user_id
        else:
            users_list += ',' + user_id

        query = f"update score_users_list set users_list=\"" + users_list + f"\" where score={new_score}"
        print(query)

    insert_mysql_rows(mysql_conn, query)


def get_new_rank_by_score(mysql_conn, new_score):
    query = f"""select * from score_users_list order by score desc"""
    data = get_mysql_results(mysql_conn, query)
    rank = 1

    for row in data:
        score = row.get('score')
        users_list = row.get('users_list')
        if len(users_list) == 0:
            continue

        if score == new_score:
            return rank

        rank += 1
