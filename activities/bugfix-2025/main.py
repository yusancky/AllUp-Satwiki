# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

import AllUp_utils.wiki
from collections import defaultdict
from re import findall

if __name__ == "__main__":
    leaderboard = '{| class="wikitable"\n! 排名 !! 用户名 !! 总评分\n'
    pattern = r"\{\{天热站破公示\|1\|([^|]+)\|(\d{1,2}\.\d{1,2})\|[^|]+\|[^|]+\|[^|]+\|(\d{1,2})\}\}"
    pulled_content = AllUp_utils.wiki.pull("博客:天热了，让你站破产吧")
    matches = findall(pattern, pulled_content)
    user_scores = defaultdict(int)
    for match in matches:
        username = match[0]
        score = int(match[2])
        user_scores[username] += score
    if sorted_users := sorted(user_scores.items(), key=lambda x: x[1], reverse=True):
        current_rank, same_score_count = 1, 1
        leaderboard += f'|-\n| <center><b>1</b></center> || [[用户:{sorted_users[0][0]}]] || <font color="#D6E"><center><b>{sorted_users[0][1]}</b></center></font>\n'
        for i in range(1, len(sorted_users)):
            if sorted_users[i][1] == sorted_users[i - 1][1]:
                same_score_count += 1
            else:
                current_rank += same_score_count
                same_score_count = 1
            leaderboard += f"""|-\n| <center><b>{current_rank}</b></center> || [[用户:{sorted_users[i][0]}]] || {'<font color="#4E4">' if current_rank <= 3 else ''}<center>{'<b>' if current_rank <= 5 else ''}{sorted_users[i][1]}{'</b>' if current_rank <= 5 else ''}</center>{'</font>' if current_rank <= 3 else ''}\n"""
    leaderboard += "|-\n| colspan=\"3\" | 统计图表基于[https://github.com/yusancky/AllUp-Satwiki '''AllUp-Satwiki''']生成，于<small>（北京时间）</small>每天13时、22时<small>（可能有一定延迟）</small>自动更新。\n|}"
    AllUp_utils.wiki.push("Template:天热站破公示/leaderboard", leaderboard)
