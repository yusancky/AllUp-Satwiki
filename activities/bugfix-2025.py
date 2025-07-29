# Copyright (c) yusancky. All rights reserved.
# Licensed under the Apache License 2.0. See License in the project root for license information.

import AllUp_utils.wiki
from collections import defaultdict
from re import findall
from time import localtime, strftime

if __name__ == "__main__":
    leaderboard = '{| class="wikitable" style="background: #EEE;font-family: formula1-black;text-align:center;"\n! 排名 !! 用户名 !! 总评分\n'
    pattern = r"\{\{天热站破公示\|1\|([^|]+)\|(\d{1,2}\.\d{1,2})\|[^|]+\|[^|]+\|[^|]+\|(\d{1,2})\}\}"
    pulled_content = AllUp_utils.wiki.pull("博客:天热了，让你站破产吧")
    revid = AllUp_utils.wiki.get_last_revid("博客:天热了，让你站破产吧")
    matches = findall(pattern, pulled_content)
    user_scores = defaultdict(int)
    for match in matches:
        username = match[0]
        score = int(match[2])
        user_scores[username] += score
    if sorted_users := sorted(user_scores.items(), key=lambda x: x[1], reverse=True):
        current_rank, same_score_count = 1, 1
        leaderboard += f'|-\n| 🥇 || [[用户:{sorted_users[0][0]}]] || <font color="#D6E">{sorted_users[0][1]}</font>\n'
        for i in range(1, len(sorted_users)):
            if sorted_users[i][1] == sorted_users[i - 1][1]:
                same_score_count += 1
            else:
                current_rank += same_score_count
                same_score_count = 1
            if current_rank <= 3:
                leaderboard += f'|-\n| {["🥈", "🥉"][current_rank - 2]} || [[User:{sorted_users[i][0]}]] || <font color="#4E4">{sorted_users[i][1]}</font>\n'
            elif same_score_count == 1:
                leaderboard += f'|-\n| {current_rank} || [[User:{sorted_users[i][0]}]] || {f"""<font color="#FB2">{sorted_users[i][1]}</font>""" if sorted_users[i][1] >= 100 else sorted_users[i][1]}\n'
            else:
                leaderboard += f'|-\n| <font color="#9CA3AF">{current_rank}</font> || [[User:{sorted_users[i][0]}]] || {f"""<font color="#FB2">{sorted_users[i][1]}</font>""" if sorted_users[i][1] >= 100 else sorted_users[i][1]}\n'
    leaderboard += f'|-\n| colspan="3" style="text-align:left;" | 排行榜由[https://github.com/yusancky/AllUp-Satwiki AllUp]定期自动更新。<small>（上次更新：[https://github.com/yusancky/AllUp-Satwiki/actions/workflows/activities-bugfix-2025.yml?query=branch%3Amain+is%3Asuccess {strftime("%Y年%m月%d日%H时", localtime())}]）</small>\n|}}'
    AllUp_utils.wiki.push("Template:天热站破公示/leaderboard", leaderboard)
